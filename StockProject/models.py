# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    country = models.ForeignKey('Countries', models.DO_NOTHING)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=60)
    registration_date = models.DateField()
    last_login = models.DateField()
    phone_number = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'clients'


class Countries(models.Model):
    name = models.CharField(max_length=225)
    country_phone_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Currencies(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'currencies'


class Exchanges(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'exchanges'


class Photos(models.Model):
    id = models.IntegerField(primary_key=True)
    photo = models.TextField()
    photo_date = models.DateField()
    photo_comment = models.CharField(max_length=1000, blank=True, null=True)
    trade = models.ForeignKey('Trades', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photos'


class Prices(models.Model):
    stock = models.ForeignKey('Stocks', models.DO_NOTHING)
    timestamp = models.DateTimeField()
    open = models.PositiveIntegerField()
    low = models.PositiveIntegerField()
    high = models.PositiveIntegerField()
    close = models.PositiveIntegerField()
    volume = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'prices'


class Stocks(models.Model):
    country = models.ForeignKey(Countries, models.DO_NOTHING)
    currency = models.ForeignKey(Currencies, models.DO_NOTHING)
    exchange = models.ForeignKey(Exchanges, models.DO_NOTHING)
    name = models.CharField(max_length=225)
    symbol = models.CharField(max_length=225)

    class Meta:
        managed = False
        db_table = 'stocks'


class Trades(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    trade_comment = models.CharField(max_length=1000, blank=True, null=True)
    trade_date = models.DateField()
    position = models.CharField(max_length=45)
    outcome = models.CharField(max_length=45, blank=True, null=True)
    trade_type = models.CharField(max_length=45)
    stock = models.ForeignKey(Stocks, models.DO_NOTHING)
    expiry = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trades'
