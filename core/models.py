from django.contrib.auth.models import User
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
        return reverse('services_list', args=[self.slug])


class Service(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services')

    def __str__(self):
        return f'{self.category.title} - {self.title}'

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.category.slug, self.id, self.slug])

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.service}: {self.date}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'



