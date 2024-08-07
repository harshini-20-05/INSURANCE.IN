# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgentLogin(models.Model):
    agent_id = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_login'


class Agents(models.Model):
    agent_name = models.CharField(max_length=20, blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    aemail = models.CharField(max_length=40, blank=True, null=True)
    aphone = models.BigIntegerField(blank=True, null=True)
    aage = models.IntegerField(blank=True, null=True)
    agender = models.CharField(max_length=6, blank=True, null=True)
    astate = models.CharField(max_length=20, blank=True, null=True)
    acity = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agents'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Claims(models.Model):
    claim_id = models.IntegerField(blank=True, null=True)
    policy_no = models.IntegerField(blank=True, null=True)
    claim_type = models.CharField(max_length=20, blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claims'


class CustomerLogin(models.Model):
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_login'


class Customers(models.Model):
    cust_name = models.CharField(max_length=20, blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)
    cemail = models.CharField(max_length=40, blank=True, null=True)
    cphone = models.CharField(max_length=20, blank=True, null=True)
    cage = models.IntegerField(blank=True, null=True)
    cgender = models.CharField(max_length=10, blank=True, null=True)
    cstate = models.CharField(max_length=50, blank=True, null=True)
    ccity = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hospitals(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospitals'


class LoginCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    cust_name = models.CharField(max_length=20)
    cust_id = models.IntegerField()
    cemail = models.CharField(max_length=254)
    cphone = models.CharField(max_length=20)
    cage = models.IntegerField()
    cgender = models.CharField(max_length=10)
    cstate = models.CharField(max_length=50)
    ccity = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login_customer'


class LoginUser(models.Model):
    login_id = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'login_user'


class Policy(models.Model):
    cust_id = models.IntegerField(blank=True, null=True)
    policy_type = models.CharField(max_length=20, blank=True, null=True)
    policy_no = models.IntegerField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'policy'


class PolicyType(models.Model):
    policy_no = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'policy_type'


class Transactions(models.Model):
    transaction_id = models.BigIntegerField(blank=True, null=True)
    policy_no = models.IntegerField(blank=True, null=True)
    cust_id = models.IntegerField(blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserLogin(models.Model):
    login_id = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_login'
