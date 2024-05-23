from django.shortcuts import render,HttpResponse
from django.shortcuts import  redirect
from django.contrib.auth import authenticate, login
from .models import Agent, Customer,Claim,Policy,PolicyDetails,Transaction,Claim, ClaimDetails
from django.utils import timezone
from django.db import IntegrityError
from datetime import timedelta,datetime
import logging
# Create your views here.
def index(request):
    return render(request,'home.html')
def agent_login(request):
    if request.method == 'POST':
        agent_id = request.POST.get('userid')
        password = request.POST.get('password')
        print("Received Agent ID:", agent_id)
        print("Received Password:", password)
        try:
            agent = Agent.objects.get(agent_id=agent_id)
        except Agent.DoesNotExist:
            agent = None

        if agent is not None:
            # Agent with the provided agent_id exists
            if password == agent.password:
                request.session['agent_id'] = agent.agent_id
                return render(request, 'agent_dashboard.html', {'agent': agent})
            else:
                # Password does not match
                pass
        else:
            # Agent with the provided agent_id does not exist
            pass
    
    return render(request, 'agent_login.html')

def customer_login(request):
    if request.method == 'POST':
        cust_id = request.POST['userid']
        password = request.POST['password']
        
        try:
            customer = Customer.objects.get(cust_id=cust_id)
        except Customer.DoesNotExist:
            # Customer with the provided cust_id does not exist
            customer = None
        print(cust_id)
        if customer is not None:
            # Customer with the provided cust_id exists
            if password == customer.password:
                 request.session['cust_id'] = customer.cust_id
                 return redirect('customer_dashboard')
            else:
                pass
        else:
            # Customer with the provided cust_id does not exist
            pass
    
    return render(request, 'customer_login.html')
 
def agent_dashboard(request):
    agent=Agent.objects.get(agent_id=request.session.get('agent_id'))
    
    # Pass the customer details to the template
    context = {'agent': agent}
    return render(request,'agent_dashboard.html',context)


def customer_dashboard(request):
    customer = None
    claim_count = 0
    policy_count = 0

    try:
        customer = Customer.objects.get(cust_id=request.session.get('cust_id'))
    except Customer.DoesNotExist:
        return HttpResponse("Customer not found")

    if customer:
        claim_count = Claim.objects.filter(cust_id=customer).count()
        policy_count = Policy.objects.filter(cust_id=customer).count()
    print(claim_count)
    print(policy_count)
    context = {
        'claim_count': claim_count,
        'policy_count': policy_count,
        'customer':customer
        
    }

    return render(request, 'customer_dashboard.html', context)


def buy_a_policy(request):
    if request.method == 'POST':
        policy_no = int(request.POST.get('policy_no'))  # Convert to integer
        policy_type = request.POST.get('policy_type')
        agent_no = int(request.POST.get('agent_no'))  # Convert to integer
        cust_id = request.session.get('cust_id')
        print(cust_id)
        customer = Customer.objects.get(cust_id=cust_id)
        print(customer)
        
        start_date = datetime.now().date()  # Start date is today's date
          # Calculate end date
        
        print(customer)
        # Retrieve the Agent instance corresponding to agent_no
        try:
            policy_details = PolicyDetails.objects.get(policy_no=policy_no)
            validity_period_years = PolicyDetails.objects.get(policy_no=policy_no).validity_period_years  # Convert to integer
            payment_period = PolicyDetails.objects.get(policy_no=policy_no).payment_period
            end_date = start_date + timedelta(days=validity_period_years * 365)
            policy_ty=policy_details.policy_type
        except PolicyDetails.DoesNotExist:
            policy_details=None
        try:
            agent = Agent.objects.get(agent_id=agent_no)
            print(agent.agent_name)
        except Agent.DoesNotExist:
            agent = None
        if policy_details:
            if agent and policy_ty==policy_type:
                # Create a new Policy object and save it to the database
                policy = Policy.objects.create(
                    cust_id=customer,
                    policy_type=policy_type,
                    policy_no=policy_details,
                    agent_id=agent,  # Assign the Agent instance to agent_id
                    start_date=start_date,
                    end_date=end_date,
                )
                context={
                    'agent_id':agent.agent_id,
                    'policy_no':policy.policy_no.policy_no,
                    'policy_type':policy.policy_type
                }
                # Redirect to a success page or wherever appropriate
                return render(request,'policy_success.html',context)  # Replace 'success_page' with your URL name
            else:
                content={
                    'content':"Agent or policy type doesnt match."
                }
                return render(request,'failure.html',content)
        else:
            content={
                    'content':"Policy Not found."
                }
            return render(request,'failure.html',content)
    
    return render(request, 'buy_a_policy.html')
def agent_customer_details(request):
    agent_id = request.session.get('agent_id')  # Assuming agent_id is stored in session
    agent = Agent.objects.get(agent_id=agent_id)  # Retrieve the agent object
    
    # Retrieve all policies associated with the agent
    policies = Policy.objects.filter(agent_id=agent)
    
    # Initialize an empty list to store customer details
    customers = []
    
    # Iterate over each policy and retrieve customer details
    for policy in policies :
        if policy.status=='running':
            customer = policy.cust_id    # Retrieve customer associated with the policy
            customers.append(customer)
            print(customer)

    # Pass the list of customer details to the template
    context = {'customers': customers}
    
    return render(request, 'agent_customer_details.html', context)
def agent_customer_policies(request):
    agent_id = request.session.get('agent_id')  # Assuming agent_id is stored in session
    agent = Agent.objects.get(agent_id=agent_id)
    policies = Policy.objects.filter(agent_id=agent)
    policy_details = []
    for policy in policies :
        # Retrieve customer details for the current policy
        if policy.status=='running':
            customer = Customer.objects.get(cust_id=policy.cust_id.cust_id)

            # Retrieve policy details for the current policy
            policy_detail = PolicyDetails.objects.get(policy_no=policy.policy_no.policy_no)

            # Append policy and customer details to the list
            policy_details.append({
                'policy_no': policy.policy_no.policy_no,
                'cust_id': policy.cust_id.cust_id,
                'cust_name': customer.cust_name,
                'policy_type': policy.policy_type,
                'start_date': policy.start_date,
                'payment_period': policy_detail.payment_period,
                'end_date': policy.end_date,
            })

    # Pass the list of policy details to the templates
    context = {'policy_details': policy_details}
    
    return render(request, 'agent_customer_policies.html', context)
def customer_policies(request):
    cust_id = request.session.get('cust_id')  # Assuming cust_id is stored in session
    customer = Customer.objects.get(cust_id=cust_id)  # Retrieve the customer object
    
    # Retrieve all policies associated with the customer
    policies = Policy.objects.filter(cust_id=customer)

    # Initialize an empty list to store policy details along with associated agent information
    policy_details = []
    
    # Iterate through each policy to fetch associated agent details
    for policy in policies:
        # Retrieve agent details for the current policy
        if policy.status=='running':
            agent = policy.agent_id

            # Retrieve policy details for the current policy
            policy_detail = PolicyDetails.objects.get(policy_no=policy.policy_no.policy_no)

            # Append policy and agent details to the list
            policy_details.append({
                'policy_no': policy.policy_no.policy_no,
                'agent_id': policy.agent_id.agent_id,
                'agent_name': agent.agent_name,
                'policy_type': policy.policy_type,
                'start_date': policy.start_date,
                'payment_period': policy_detail.payment_period,
                'end_date': policy.end_date,
                'status':policy.status
            })

    # Pass the list of policy details to the template
    context = {'policy_details': policy_details}
    
    return render(request, 'customer_policies.html', context)

def customer_claims(request):
    cust_id=request.session.get('cust_id')
    customer=Customer.objects.get(cust_id=cust_id)
    claim=Claim.objects.filter(cust_id=customer)
    claims=[]
    for c in claim:
        claims.append(c)
    context={'claims':claims}
    return render(request,'customer_claims.html',context)

def agent_claims(request):
    agent_id=request.session.get('agent_id')
    agent=Agent.objects.get(agent_id=agent_id)
    policy=Policy.objects.filter(agent_id=agent)
    details=[]
    for policies in policy:
        claims=Claim.objects.filter(policy_no=policies)
        for claim in claims:
            details.append(claim)
    context={'details':details}
    return render(request,'agent_claims.html',context)


def customer_agent_details(request):
    cust_id = request.session.get('cust_id')  # Assuming cust_id is stored in session
    customer = Customer.objects.get(cust_id=cust_id)  # Retrieve the customer object
    
    # Retrieve all policies associated with the agent
    policies = Policy.objects.filter(cust_id=customer)
    
    # Initialize an empty list to store customer details
    agents = []
    
    # Iterate over each policy and retrieve customer details
    for policy in policies :
        if policy.status=='running':
            agent = policy.agent_id    # Retrieve customer associated with the policy
            agents.append(agent)
    
    # Pass the list of customer details to the template
    context = {'agents': agents}
    
    return render(request, 'customer_agent_details.html', context)
def transactions(request):
    if request.method == 'POST':
        transaction_id = int(request.POST.get('transaction_id'))
        transaction_date = request.POST.get('transaction_date')
        policy_number = int(request.POST.get('policy_number'))
        amount = int(request.POST.get('amount'))

        try:
            

            # Check if the transaction ID is unique
            if Transaction.objects.filter(transaction_id=transaction_id).exists():
                content={
                    'content':"Invalid transaction ID: Transaction ID must be unique."
                }
                return render(request,'failure.html',content)

            # Retrieve policy details
            try:
                policy = Policy.objects.get(policy_no=policy_number)
                policy_details = PolicyDetails.objects.get(policy_no=policy_number)
            except Policy.DoesNotExist and policy.status=='expired':
                content={
                    'content':"Policy number does not exist"
                }
                return render(request,'failure.html',content)

            # Check if the policy is associated with the customer
            customer = Customer.objects.get(cust_id=request.session.get('cust_id'))
            if policy.cust_id != customer:
                content={
                    'content':"You have not taken this policy."
                }
                return render(request,'failure.html',content)

            # Validate the amount
            if amount == policy_details.amount_to_be_paid:
                # Create a new transaction record
                transaction = Transaction.objects.create(
                    transaction_id=transaction_id,
                    policy_no=policy,
                    cust_id=customer,
                    amount=amount,
                    transaction_date=transaction_date
                )

                # Process the transaction (if needed)
                # (You can add your transaction processing logic here)
                content={
                    'content':"Transaction successful"
                }
                return render(request,'failure.html',content)
                
            else:
                content={
                    'content':"Amount does not match the policy details"
                }
                return render(request,'failure.html',content)
        except ValueError:
            content={
                    'content':"Invalid input"
                }
            return render(request,'failure.html',content)
    return render(request, 'transaction_form.html')

def transaction_details(request):
    # Retrieve the customer ID from the session
    cust_id = request.session.get('cust_id')

    # Filter transactions based on the customer ID and order them by transaction_date in descending order
    transactions = Transaction.objects.filter(cust_id=cust_id).order_by('-transaction_date')

    # Initialize an empty list to store transaction details
    transaction_details = []

    # Iterate over each transaction and extract relevant details
    for transaction in transactions:
        transaction_details.append({
            'transaction_id': transaction.transaction_id,
            'policy_no': transaction.policy_no.policy_no.policy_no,
            'transaction_date': transaction.transaction_date,
            'amount': transaction.amount
        })

    # Pass the list of transaction details to the template
    context = {'transactions': transaction_details}
    return render(request, 'transaction_details.html', context)


def file_a_claim(request):
    print("entered")
    if request.method == 'POST':
        # Get form data
        print("got in")
        policy_no = int(request.POST.get('policy_no'))
        claim_type = request.POST.get('claim_type')
        print(policy_no)
        print(claim_type)
        # Check if the customer has the policy
        cust_id = request.session.get('cust_id')
        policy_detail=PolicyDetails.objects.get(policy_no=policy_no)
        customer = Customer.objects.get(cust_id=cust_id)
        policy = Policy.objects.get(policy_no=policy_detail,cust_id=customer)
        print(policy)
        claim_detail = ClaimDetails.objects.get(policy_no=policy_no)

        # Print statements for debugging
        print(policy_detail)
        print(claim_detail)
        if policy is not None and policy.status=='running':
            if claim_type == 'accident':
                Claim.objects.create(
                    policy_no=policy,
                    claim_type=claim_type,
                    amount=claim_detail.accident_claim_amount,
                    cust_id=customer
                )
                policy.status='expired'
                policy.save()
                context={
                    'policy_no':policy_no,
                    'claim_type':claim_type,
                    'amount':claim_detail.accident_claim_amount
                }
                return render(request,'claim_success.html',context)
            elif claim_type == 'mid_policy_claim':
                # Calculate the time since the policy started
                policy_start_date = policy.start_date
                current_date = datetime.now().date()
                time_since_start = (current_date - policy_start_date).days
                print(time_since_start)
                print(claim_detail.time_to_claim_delayed_amount)
                # Check if the time since start is greater than or equal to the delayed claim time
                if time_since_start >= claim_detail.time_to_claim_delayed_amount:
                    Claim.objects.create(
                        policy_no=policy,
                        claim_type=claim_type,
                        amount=claim_detail.delayed_claim_amount,
                        cust_id=customer
                    )
                    policy.status='expired'
                    policy.save()
                    context={
                        'policy_no':policy_no,
                        'claim_type':claim_type,
                        'amount':claim_detail.delayed_claim_amount
                    }
                    return render(request,'claim_success.html',context)
                else:
                    return HttpResponse("Claim cannot be filed yet. Not enough time has passed.")
            
            elif claim_type == 'term_end_claim':
                # Check if the policy validity period has ended
                policy_end_date = policy.end_date
                current_date = datetime.now().date()
                
                if current_date >= policy_end_date:
                    Claim.objects.create(
                        policy_no=policy,
                        claim_type=claim_type,
                        amount=claim_detail.end_of_policy_period_claim,
                        cust_id=customer
                    )
                    policy.status='expired'
                    policy.save()
                    context={
                        'policy_no':policy_no,
                        'claim_type':claim_type,
                        'amount':claim_detail.end_of_policy_period_claim
                    }
                    return render(request,'claim_success.html',context)
                else:
                    content={
                        'content':"Policy period has not ended yet. Claim cannot be filed."
                    }
                    return render(request,'failure.html',content)
        else:
            content={
                        'content':"Policy not found"
                    }
            return render(request,'failure.html',content)

    return render(request, 'file_claim.html')


def policy_details(request):
    policy_detail=PolicyDetails.objects.all()
    
    return render(request,'policy_details.html',{'policy_details': policy_detail})
def claim_details(request):
    claim_detail=ClaimDetails.objects.all()
    
    return render(request,'claim_details.html',{'claim_details': claim_detail})
