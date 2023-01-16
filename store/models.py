from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# for multiple selection
from multiselectfield import MultiSelectField


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255, db_index=True)
	slug = models.SlugField(max_length=255, unique=True)

	class Meta:
		verbose_name_plural = 'categories'


	def get_absolute_url(self):
		return reverse('store:category_list', args=[self.slug])

	def __str__(self):
		return self.name

class Color(models.Model):
    color = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.color

class Product(models.Model):
    BRENDS = [
        ('1 brend', '1 brend'), 
        ('2 brend', '2 brend'),
        ('3 brend', '3 brend'), 
    ]

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    brends = models.CharField(max_length=200, null=True, choices = BRENDS)
    colors=models.ManyToManyField(Color, null=True)

    def __str__(self):
    	return self.title