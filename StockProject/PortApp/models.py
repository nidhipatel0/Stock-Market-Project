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

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'countries'


class Currencies(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'currencies'




class Exchanges(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'exchanges'


class Photos(models.Model):
    photo =  models.ImageField(null=False,blank=False)
    photo_date = models.DateField()
    photo_comment = models.CharField(max_length=1000, blank=True, null=True)
    trade = models.ForeignKey('Trades', models.DO_NOTHING)
    photo_response = models.CharField(max_length=500, blank=True, null=True)

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
    
    def __str__(self):
        return self.symbol
    
    class Meta:
        managed = False
        db_table = 'stocks'

position_choices = (
    ('buy', 'Buy'),
    ('sell', 'Sell'),
)
outcome_choices = (('success','Success'),('failed','Failed'),('neutral','Neutral'))

trade_choices = (('normal','Normal'),('options','Options'),('futures','Futures'))


class Trades(models.Model):
    
    trade_comment = models.CharField(max_length=1000, blank=True, null=True)
    trade_date = models.DateField()
    position = models.CharField(max_length=45,choices=position_choices, blank=True, null=True)
    outcome = models.CharField(max_length=45,choices=outcome_choices, blank=True, null=True)
    trade_type = models.CharField(max_length=45,choices=trade_choices, blank=True, null=True)
    stock = models.ForeignKey(Stocks, models.DO_NOTHING)
    #stock = models.ForeignKey('Stock',  on_delete=models.SET_NULL, null=True, blank=True)
    expiry = models.DateField(blank=True, null=True)
    
    portfolio = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'trades'
'''
<div class="form-group m-3">
                            <label>Trade comment</label>
                            <input name="trade_comment" type="text" placeholder="Enter a comment" class="form-control">
                            </div>
                        
                        <nav class="navbar navbar-expand-lg navbar-light ">
                            <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                                <form class="form-inline my-2 my-lg-0">
                                    <input class="form-control mr-sm-2" type="date " name="trade_date" placeholder="Date of trade" aria-label="Search">
                                    
                                </form>
                            </div>
                        </nav>
                    
                        <div class="form-group m-3">
                            <label class="mr-sm-2" for="inlineFormCustomSelect">position</label>
                            <select class="custom-select mr-sm-2" type="text" name="position" id="inlineFormCustomSelect">
                                <option selected>Choose</option>
                                <option value="buy">Buy</option>
                                <option value="sell">Sell</option>
                            </select>
                        </div>

                        <div class="form-group m-3">
                            <label class="mr-sm-2" for="inlineFormCustomSelect">Outcome</label>
                            <select class="custom-select mr-sm-2" type="text" name="outcome" id="inlineFormCustomSelect">
                                <option selected>Choose</option>
                                <option value="neutral">Neutral</option>
                                <option value="success">Success</option>
                                <option value="failed">Failed</option>
                            </select>
                        </div>

                        <div class="form-group m-3">
                            <label class="mr-sm-2" for="inlineFormCustomSelect">Trade_type</label>
                            <select class="custom-select mr-sm-2" type="text" name="trade_type" id="inlineFormCustomSelect">
                                <option selected>Choose</option>
                                <option value="normal">Normal</option>
                                <option value="options">Options</option>
                                <option value="futures">Futures</option>
                            </select>
                        </div>

                        <div class="form-group m-3">
                            <label>Stock</label>
                            <input name="stock" type="text" placeholder="Enter a stock" class="form-control">
                            </div>

                        <nav class="navbar navbar-expand-lg navbar-light ">
                            <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                                <form class="form-inline my-2 my-lg-0">
                                    <input class="form-control mr-sm-2" type="date " name="expiry" placeholder="Date of trade" aria-label="Search">
                                    
                                </form>
                            </div>
                        </nav>

                        <div class="form-group m-3">
                            <label>Upload photo</label>
                            <input name="photo" type="file" multiple class="form-control-file">
                            </div>

                            
                        <nav class="navbar navbar-expand-lg navbar-light ">
                            <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
                                <form class="form-inline my-2 my-lg-0">
                                    <input class="form-control mr-sm-2" type="date " name="photo_date" placeholder="Date of trade" aria-label="Search">
                                    
                                </form>
                            </div>
                        </nav>
                        
                        '''