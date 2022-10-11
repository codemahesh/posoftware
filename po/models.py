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
    customer_po_number = models.ForeignKey(CustomerPo, on_delete=models.CASCADE)
    customer_item_code = models.CharField(max_length=255)
    customer_item_description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.customer_item_code
    class Meta:
        ordering =['customer_item_code']