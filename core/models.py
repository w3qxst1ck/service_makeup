from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('services_with_category', args=[self.slug])


class Service(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return f'{self.title} - {self.title}'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
