from django.db import models
from datetime import date

class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=20)
    aemail = models.EmailField(max_length=40)
    aphone = models.BigIntegerField()
    aage = models.IntegerField()
    agender = models.CharField(max_length=6)
    astate = models.CharField(max_length=20)
    acity = models.CharField(max_length=20)
    password = models.CharField(max_length=20)  # Adjust the max_length as needed

    class Meta:
        db_table = 'agents'

class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=20)
    cemail = models.EmailField(max_length=40)
    cphone = models.BigIntegerField()
    cage = models.IntegerField()
    cgender = models.CharField(max_length=6)
    cstate = models.CharField(max_length=20)
    ccity = models.CharField(max_length=20)
    password = models.CharField(max_length=20)  # Adjust the max_length as needed

    class Meta:
        db_table = 'customers'

class Claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    policy_no = models.ForeignKey('Policy', on_delete=models.CASCADE)
    claim_type = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)  # ForeignKey to Customer model

    class Meta:
        db_table = 'claims'

class Transaction(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    policy_no = models.ForeignKey('Policy', on_delete=models.CASCADE)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)  # ForeignKey to Customer model
    amount = models.BigIntegerField()
    transaction_date = models.DateField()

    class Meta:
        db_table = 'transactions'

class PolicyDetails(models.Model):
    policy_no = models.IntegerField(primary_key=True)
    policy_type = models.CharField(max_length=20)
    validity_period_years = models.IntegerField(default=1) 
    payment_period = models.CharField(max_length=20)
    amount_to_be_paid=models.BigIntegerField(default=0)
    class Meta:
        db_table = 'policy_details'


class Policy(models.Model):
    policy_id = models.AutoField(primary_key=True)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=20)
    policy_no = models.ForeignKey('PolicyDetails', on_delete=models.CASCADE, db_column='policy_no')
    agent_id = models.ForeignKey('Agent', on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    status = models.CharField(max_length=20, default='running') 

    class Meta:
        db_table = 'policy'

class ClaimDetails(models.Model):
    claim_details_id = models.AutoField(primary_key=True)
    policy_no = models.ForeignKey('PolicyDetails', on_delete=models.CASCADE,db_column='policy_no')
    end_of_policy_period_claim = models.DecimalField(max_digits=10, decimal_places=2)
    accident_claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delayed_claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_to_claim_delayed_amount = models.IntegerField()  # Time in days after which delayed claim amount can be made

    class Meta:
        db_table = 'claim_details'

