from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    sub_category = models.CharField(max_length=50,default="")
    price = models.IntegerField()
    disc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

# # prod_category = models.ForeignKey(Category, on_delete=models.CASCADE)
# product_code = models.CharField(max_length=20, blank=True)
# product_name = models.CharField(max_length=255)
# product_price = models.FloatField(null=True, blank=True)
# product_desc = models.TextField()

# class Meta:
#     verbose_name_plural = "Product"
#
# def __str__(self):
#     return self.product_name
#
# def save(self, *args, **kwargs):
#     if not len(self.product_code):
#         self.product_code = 'prod-' + random_string_generator(5)
#     super(Product, self).save(*args, **kwargs)

# product_image = models.ImageField(upload_to='image/productImage',
# default='image/productImage/default_prod_image.jpg', blank=True)
