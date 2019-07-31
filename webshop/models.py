from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField('отчество', max_length=100)
    company = models.CharField('компания', max_length=100)
    position = models.CharField('должность', max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Shop(models.Model):
    name = models.CharField('название', max_length=100)
    url = models.URLField('адрес', max_length=100)
    filename = models.CharField('файл', max_length=100)


class Category(models.Model):
    name = models.CharField('название', max_length=100)
    shops = models.ManyToManyField(Shop, related_name='categories')


class Product(models.Model):
    name = models.CharField('название', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def get_info(self):
        return 'Продукт %s из категории %s' % (self.name, self.category) # TODO: доработать, чтобы выдавало информацию продукта


class ProductInfo(models.Model):
    name = models.CharField('название', max_length=100)
    quantity = models.PositiveIntegerField('остаток', default=0)
    price = models.PositiveIntegerField('цена', default=0)
    price_rrc = models.PositiveIntegerField('рекомендуемая розничная цена', default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Parameter(models.Model):
    name = models.CharField('название', max_length=100)


class ProductParameter(models.Model):
    value = models.CharField('значение', max_length=100)
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)


class Order(models.Model):
    dt = models.DateTimeField(auto_now=True)
    status = models.CharField('статус', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField('количество', default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def price(self):
        return self.product # TODO: доделать метод, чтобы выдавал цену продукта

    def sum(property)
        return None # self.quantity * self.product.price # TODO: доделать метод, чтобы выдавал сумму

class Contact(models.Model):
    type = models.CharField('вид пользователя', max_length=100)
    value = models.CharField('значение', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_user_contacts(self):
        return self.user # TODO: дописать метод, чтобы возвращал контакты пользователя


