"""
URL configuration for dbms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('agent_login',views.agent_login,name='agent_login'),
    path('customer_login',views.customer_login,name='customer_login'),
    path('agent_dashboard',views.agent_dashboard,name='agent_dashboard'),
    path('customer_dashboard',views.customer_dashboard,name='customer_dashboard'),
    path('transactions',views.transactions,name='transactions'),
    path('buy_a_policy',views.buy_a_policy,name='buy_a_policy'),
    path('agent_claims',views.agent_claims,name='agent_claims'),
    path('agent_customer_details',views.agent_customer_details,name='agent_customer_details'),
    path('customer_policies',views.customer_policies,name='customer_policies'),
    path('agent_customer_policies',views.agent_customer_policies,name='agent_customer_policies'),
    path('customer_agent_details',views.customer_agent_details,name='customer_agent_details'),
    path('transaction_details',views.transaction_details,name='transaction_details'),
    path('file_a_claim',views.file_a_claim,name='file_a_claim'),
    path('customer_claims',views.customer_claims,name='customer_claims'),
    path('agent_claims',views.agent_claims,name='agent_claims'),
    path('policy_details',views.policy_details,name='policy_details'),
    path('claim_details',views.claim_details,name='claim_details'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('payment_success/',views.payment_success,name='payment_success'),
    path('razorpay/callback/', views.razorpay_callback, name='razorpay_callback'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
