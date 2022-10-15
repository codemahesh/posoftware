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
    customer_po_number = models.ForeignKey(CustomerPo, on_delete=models.CASCADE, db_column = 'customer_po_number')
    customer_item_code = models.CharField(max_length=255)
    customer_item_description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    
    def __str__(self) -> str:
        return self.customer_po_number
    class Meta:
        ordering =['customer_po_number']
        
        
        
class Dispatch(models.Model):
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
    
    MAIL_STATUS_CHOICES=(
        ('EM','Emailed'),
        ('NM','Not Emailed')
    )
    SENDER_CHOICES =(
        ('01','ARUSH'), 
        ('02','ARUSH LLP'), 
        ('03','ARNAV')
    )
    INVOICE_STATUS_CHOICES = (
        ('IN','Invoiced'), 
        ('NI','Not Invoiced'), 
    )
    INSURANCE_CHOICES = (
        ('YES','YES'),
        ('NO','NO')
    )
    DELIVERY_STATUS =(
        ('DL','DELIVERED'),
        ('ND','NOT DELIVERED'),
        ('RE','RETURNED')
    )
    PARCEL_CHOICES = (
        ('PAR','PARCEL'),
        ('CHA','CHALLAN'),
        ('CHQ','CHEQUE'),
        ('DEN','DEBIT NOTE'),
        ('DOC','DOCUMENTS'),
        ('FBL','FREIGHT BILL'),
        ('NDC','NDC'),
        ('OBL','ORIGINAL BILL'),
        ('VFM','VENDOR FORM'),
        ('CFM','C-FORM'),
    )
    CURIOR_COMPANY_CHOICES = (
        ('1','DTDC'),
('2','By Hand'),
('3','Gati'),
('4','Gaurav Transport'),
('5','Blue Dart'),
('6','Delhi Sonipat'),
('7','FedEx'),
('8','HKS Transport'),
('9','Inland'),
('10','Professional'),
('11','Shree Maruti'),
('12','TCI Express'),
('13','Tempo'),
('14','Trackon'),
('15','VRL'),
('16','DAKSH LOGISTICS'),
('17','The Bharat Motor Transport'),
('18','By Metro'),
('19','Samay Shatabdi Travels'),
('20','Satellitte cargo'),
('21','Aash Logistics'),
('22','Speed Post'),
('23','Delhi Rudarpur sitarganj Goods'),
('24','Bombay Barelly Goods Carriers'),
('25','Delhi Modi Transport'),
('26','Associat Road Carrier'),
('27','Spoton logistics'),
('28','Pooja Transport'),
('29','Dexters Logistics pvt ltd'),
('30','Om logistics'),
('31','RSC LOGISTICS'),
('32','Bom gim Courier'),
('33','Delivery'),
('34','ECOM Express'),
('35','XpressBee'),
('36','Sugam Parivahan'),
('37','TCI FREIGHT'),
('38','HELLO Courier'),
('39','Khullar tempo'),
('40','Surjit Singh Tempo Service'),
('41','SAFEEXPRESS'),
('42','Tirupati Courier'),
('43','Accurate freight carriers'),
('44','The Bharat Motor Transport'),
('45','Porter'))
    
    customer_po_number=models.CharField(max_length=255)
    date = models.DateField(verbose_name='P.O. Date (yyyy-mm-dd)')
    invoice_number = models.CharField(max_length = 255, unique=True)
    dispatch_mail_status = models.CharField(max_length=10, choices=MAIL_STATUS_CHOICES)
    docket = models.CharField(max_length=255)
    parcel =  models.CharField(max_length=10, choices=PARCEL_CHOICES)
    dimension = models.CharField(max_length = 255)
    charged_weight = models.FloatField(null=True,blank=True)
    weight = models.FloatField()
    unit =  models.CharField(max_length=10, choices=UNIT_CHOICES)
    curior_company = models.CharField(max_length=10, choices= CURIOR_COMPANY_CHOICES)
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES, null=True,blank=True)
    delivery_status = models.CharField(max_length=10, choices=DELIVERY_STATUS)
    delivery_date=models.DateField(verbose_name='P.O. Date (yyyy-mm-dd)', null=True,blank=True)
    invoice_status = models.CharField(max_length=10, choices= INVOICE_STATUS_CHOICES)
    insurance = models.CharField(max_length=10, choices=INSURANCE_CHOICES)
    remark =models.CharField(max_length=255, null=True,blank=True)
    asn_number = models.CharField(max_length=255, null=True,blank=True)
    def __str__(self) -> str:
        return self.invoice_number
    class Meta:
        ordering =['date']
    
    
class VendorPo(models.Model):
    customer_po_number = models.CharField(max_length=100)
    our_po_number = models.CharField(max_length=100, unique=True)
    vendor_name = models.CharField(max_length=100)
    po_date = models.DateField(verbose_name='P.O. Date (yyyy-mm-dd)')
    acknowledgement_date = models.DateField(verbose_name='Acknowledgement Date (yyyy-mm-dd)',null=True,blank=True)
    
    def __str__(self) -> str:
        return self.our_po_number
    class Meta:
        ordering =['po_date']
    
    
    
    


    