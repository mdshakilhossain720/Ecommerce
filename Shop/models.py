from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIVICTION_CHOOSE=(
    ('DHAKA','DHAKA'),
    ('Rangpur','Rangpur'),
    ('Sylhet','Sylhet'),
    ('Barisal','Barisal'),
    ('Khulna','Khulna'),
    ('Tangail','Tangail'),
    ('Gazipur','Gazipur'),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    division=models.CharField(max_length=100)
    dis=models.CharField(max_length=50)
    thana=models.CharField(max_length=100)
    village=models.CharField(max_length=80)
    zipcode=models.IntegerField()

    def __str__(self):
        return self.id



CATEGORTY_CHOOSE=(
    ('L','Lehenga'),
    ('S','Sare'),
    ('Gp','Gents Pant'),
    ('Bc','Borkha'),
    ('BF','Baby Fashion'),

)


class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_prices=models.FloatField()
    discount=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(max_length=200)
    brand=models.CharField(max_length=100)
    categroy=models.CharField(choices=CATEGORTY_CHOOSE,max_length=2)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    


    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.id
    


STATIC_CHOOSE=(
    ('Accepted','Accepted'),
    ('packed','packed'),
    ('on the way','on the way'),
    ('Deliveried','Deliveried'),
    ('Cancell','Cancell'),

)


class OrderPlace(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATIC_CHOOSE,default='Pending')


    

   

