from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('lakshadweep', 'lakshadweep'),
    ('ladakh', 'ladakh'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
)

ORDER_STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
    ('Returned', 'Returned'),
    ('Refunded', 'Refunded'),
    ('Failed', 'Failed'),
)

CATEGORY_CHOICES = (
        ('Electronics', 'Electronics'),
        ('Mobile' , 'Mobile'),
        ('Laptop' , 'Laptop'),
        ('Clothing', 'Clothing'),
        ('Home & Garden', 'Home & Garden'),
        ('Books', 'Books'),
        ('Toys', 'Toys'),
        ('Sports & Outdoors', 'Sports & Outdoors'),
        ('Beauty & Personal Care', 'Beauty & Personal Care'),
        ('Grocery & Health ', 'Health & Household'),
        ('Jewelry', 'Jewelry'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Music', 'Music'),
        ('Movies & TV', 'Movies & TV'),
        ('Software', 'Software'),
        ('Tools & Home Improvement', 'Tools & Home Improvement'),
        ('Baby Products', 'Baby Products'),
        ('Industrial & Scientific', 'Industrial & Scientific'),
        ('luggage & Travel Gear', 'luggage & Travel Gear'),
        ('Arts, Crafts & Sewing', 'Arts, Crafts & Sewing'),
        ('Other', 'Other'),
    )

#l:l4
class Customer(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    name = models. CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models. CharField(max_length=50)
    zipcode = models. IntegerField()
    state = models. CharField(choices=STATE_CHOICES,max_length= 50)

    def str (self) :
        return str(self.id ,max_length=50)    

class Product(models.Model):
    title =models.CharField( max_length=100)
    MRP = models. FloatField()
    list_price = models. FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField( choices=CATEGORY_CHOICES, max_length=50)
    product_image = models.ImageField( upload_to='product_images')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models. ForeignKey(User, on_delete=models.CASCADE)
    product = models. ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__ (self) :
        return str(self.id)
    
class OrderPlaced(models.Model):
    user = models. ForeignKey(User, on_delete=models.CASCADE)
    customer = models. ForeignKey(Customer, on_delete=models.CASCADE)
    product = models. ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=ORDER_STATUS_CHOICES, default='Pending' )

