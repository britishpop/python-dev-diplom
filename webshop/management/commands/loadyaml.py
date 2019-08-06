import yaml
from django.core.management.base import BaseCommand, CommandError
from webshop.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter

class Command(BaseCommand):
    help = 'Loads the YAML data with the provided structure'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options['filename']

        try:
            with open(filename, 'r') as stream:         
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    raise CommandError(exc)
        except FileNotFoundError:
            raise CommandError('File "%s" does not exist' % filename)

        shop, created = Shop.objects.get_or_create(
            name=data['shop'],
            url='example.com',
            filename=filename,
        )

        for item in data['categories']:
            category, created = Category.objects.get_or_create(
                id=item['id'],
                name=item['name'],
            )
            category.shops.add(shop)

        for item in data['goods']:
            product = Product(
                id=item['id'],
                name=item['name'],
                category=Category.objects.get(pk=item['category']),
            )
            product.save()

            product_info = ProductInfo(
                name=item['name'],
                quantity=item['quantity'],
                price=item['price'],
                price_rrc=item['price_rrc'],
                product=product,
            )
            product_info.save()
            product_info.shops.add(shop)

            for name, value in item['parameters'].items():
                parameter, created = Parameter.objects.get_or_create(
                    name=name,
                )

                product_parameter = ProductParameter(
                    value=value,
                    product_info=product_info,
                    parameter=parameter,
                )
                product_parameter.save()

