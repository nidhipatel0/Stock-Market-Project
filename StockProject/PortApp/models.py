# from django.contrib.auth.models import User
# from django.urls import reverse

# User for authentication, and reverse from django.urls to give us greater flexibility with creating URLs.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Client(models.Model):
    country = models.ForeignKey('Country', models.DO_NOTHING)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=60)
    registration_date = models.PositiveIntegerField()
    last_login = models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'clients'


class Country(models.Model):
    name = models.CharField(max_length=225)
    country_phone_code = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        verbose_name_plural = 'Countries'
        db_table = 'countries'


class Currency(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        verbose_name_plural = 'Currencies'
        db_table = 'currencies'


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


class Exchange(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'exchanges'
position_choices = (
    ('buy', 'Buy'),
    ('sell', 'Sell'),
)
outcome_choices = (('success','Success'),('failed','Failed'),('neutral','Neutral'))

trade_choices = (('normal','Normal'),('options','Options'),('futures','Futures'))

class Photo(models.Model):   
    photo = models.ImageField(upload_to='photos/')
    comment = models.CharField(max_length=1000, blank=True, null=True)
    trade_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=45,choices=position_choices, blank=True, null=True)
    outcome = models.CharField(max_length=45,choices=outcome_choices, blank=True, null=True)
    trade_type = models.CharField(max_length=45,choices=trade_choices, blank=True, null=True)
    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'photos'

class Price(models.Model):
    stock = models.ForeignKey('Stock', models.DO_NOTHING)
    timestamp = models.DateTimeField()
    open = models.PositiveIntegerField()
    low = models.PositiveIntegerField()
    high = models.PositiveIntegerField()
    close = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'prices'


class Stock(models.Model):
    country = models.ForeignKey(Country, models.DO_NOTHING)
    currency = models.ForeignKey(Currency, models.DO_NOTHING)
    exchange = models.ForeignKey(Exchange, models.DO_NOTHING)
    name = models.CharField(max_length=225)
    symbol = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'stocks'
