from django.db import models

# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=122)
    product_img = models.ImageField(upload_to='media/image', default='')
    product_desc = models.CharField(max_length=122)


class Contact(models.Model):
    contact_name = models.CharField(max_length=122)
    contact_email = models.CharField(max_length=122)
    contact_phone = models.CharField(max_length=12)
    contact_comment = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
