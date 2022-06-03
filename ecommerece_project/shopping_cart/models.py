from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering=('name',)
        verbose_name= 'category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('shopping_cart:product_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Product(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product', blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name= 'product'
        verbose_name_plural='products'

    def get_url(self):
        return reverse('shopping_cart:prodCatdetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)