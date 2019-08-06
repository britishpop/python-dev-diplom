from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField('отчество', max_length=100, null=True)
    company = models.CharField('компания', max_length=100, null=True)
    position = models.CharField('должность', max_length=100, null=True)

    def __str__(self):
        return 'Информация о пользователе №%s (%s)' % (self.user.pk, self.user.get_full_name())


@receiver(post_save, sender=User) # сигнал для создания админов через консоль (иначе создается без профиля)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) # сигнал для создания админов через консоль (иначе создается без профиля)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_staff:
        instance.profile.save()


class Shop(models.Model):
    name = models.CharField('название', max_length=100)
    url = models.URLField('адрес', max_length=100)
    filename = models.CharField('файл', max_length=100)

    def __str__(self):
        return 'Магазин %s' % (self.name)


class Category(models.Model):
    name = models.CharField('название', max_length=100)
    shops = models.ManyToManyField(Shop, related_name='categories')

    def __str__(self):
        return 'Категория %s' % (self.name)


class Product(models.Model):
    name = models.CharField('название', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_info(self):
        return get_object_or_404(ProductInfo, product=self)


class ProductInfo(models.Model):
    name = models.CharField('название', max_length=100)
    quantity = models.PositiveIntegerField('остаток', default=0)
    price = models.PositiveIntegerField('цена', default=0)
    price_rrc = models.PositiveIntegerField('рекомендуемая розничная цена', default=0)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    shops = models.ManyToManyField(Shop, related_name='products')

    def __str__(self):
        return 'Инфо о продукте %s' % (self.product.name)


class Parameter(models.Model):
    name = models.CharField('название', max_length=100)

    def __str__(self):
        return 'Параметр %s' % (self.name)


class ProductParameter(models.Model):
    value = models.CharField('значение', max_length=100)
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)

    def __str__(self):
        return 'Параметр продукта %s' % (self.product_info.name)


class Order(models.Model):
    dt = models.DateTimeField(auto_now=True)
    status = models.CharField('статус', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Заказ №%s от %s' % (self.pk, self.dt)


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField('количество', default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def price(self):
        return self.product.get_info().price_rrc

    def sum(self):
        return self.price() * self.quantity

    def __str__(self):
        return 'Продукт %s из заказа №%s' % (self.product.name, self.order.pk)


class Contact(models.Model):
    type = models.CharField('тип контакта', max_length=100)
    value = models.CharField('значение', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_user_contacts(self):
        return self.user.contact_set.all()

    def __str__(self):
        return '%s: %s' % (self.type, self.value)


