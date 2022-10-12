from django.db import models
from django import forms

class Customer(models.Model):
    CATEGORY_CHOICES = (
        ('A','A'),
        ('B','B'),
        ('C','C'),
        ('D','D'),
    )
    customer_name = models.CharField(max_length = 255, unique=True)
    customer_code = models.CharField(max_length = 255)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    address = models.TextField()
    place = models.CharField(max_length=50, null=True)
    
    def __str__(self) -> str:
        return self.customer_name

    class Meta:
        ordering = ['customer_name']

class Item(models.Model):   
    item_name =  models.CharField(max_length = 255, unique=True)
    our_item_code =  models.CharField(max_length = 255,  unique=True)

    def __str__(self) -> str:
        return self.item_name

    class Meta:
        ordering =['item_name']

class Uom(models.Model):
    unit = models.CharField(max_length=100, unique=True)
    unit_type = models.CharField(max_length=100)
    unit_code    = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.unit_code

    class Meta:
        ordering =['unit_code']


class CustomerPo(models.Model):
    STATUS_CHOICES = (
        ('PE','PO ENTERED'),
        ('W','WORKING'),
        ('PC','PO CREATED'),
        ('E','EMAILED'),
        ('C','CANCELLED'),
        ('F','FILED'),
        ('R','RECEIVED'),
        ('PR','PARTIAL RECEIVED'),
        ('MI','MISC')
    )
    customer_id = models.CharField(max_length=100)
    customer_po_number = models.CharField(max_length = 255, unique=True)
    date = models.DateField(verbose_name='P.O. Date (yyyy-mm-dd)')
    customer_name = models.CharField(max_length = 255, null=True,blank=True)
    customer_code = models.CharField(max_length = 255)
    category = models.CharField(max_length=1)
    address = models.TextField()
    place = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.customer_po_number
    
    def get_po_item(self):
        return self.customerpoitem_set.all()
    class Meta:
        ordering =['customer_po_number']


class CustomerPoItem(models.Model):
    UNIT_CHOICES =(
       ('1' ,'BAG'),
	   ('2' ,'BAL'),
	   ('3' ,'BDL'),
	   ('4' ,'BKL'),
	   ('5' ,'BOU'),
	   ('6' ,'BOX'),
	   ('7' ,'BTL'),
	   ('8' ,'BUN'),
	   ('9' ,'CAN'),
 	   ('10', 'CBM'),
 	   ('11', 'CCM'),
 	   ('12', 'CMS'),
 	   ('13', 'CTN'),
 	   ('14', 'DOZ'),
 	   ('15', 'DRM'),
 	   ('16', 'GGR'),
 	   ('17', 'GMS'),
 	   ('18', 'GRS'),
 	   ('19', 'GYD'),
 	   ('20', 'KGS'),
 	   ('21', 'KLR'),
 	   ('22', 'KME'),
 	   ('23', 'MLT'),
 	   ('24', 'MTR'),
	   ('25', 'MTS'),
 	   ('26', 'NOS'),
 	   ('27', 'PAC'),
 	   ('28', 'PCS'),
 	   ('29', 'PRS'),
 	   ('30', 'QTL'),
 	   ('31', 'ROL'),
 	   ('32', 'SET'),
 	   ('33', 'SQF'),
 	   ('34', 'SQM'),
 	   ('35', 'SQY'),
 	   ('36', 'TBS'),
 	   ('37', 'TGM'),
 	   ('38', 'THD'),
 	   ('39', 'TON'),
 	   ('40', 'TUB'),
 	   ('41', 'UGS'),
 	   ('42', 'UNT'),
 	   ('43', 'YDS'),
 	   ('44', 'OTH')   
    )
    customer_po_number = models.ForeignKey(CustomerPo, on_delete=models.CASCADE)
    customer_item_code = models.CharField(max_length=255)
    customer_item_description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    
    def __str__(self) -> str:
        return self.customer_item_code
    class Meta:
        ordering =['customer_item_code']