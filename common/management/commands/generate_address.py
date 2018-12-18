from django.core.management.base import BaseCommand
from faker import Faker

from common.models import Address

fake = Faker('sk_SK')

class Command(BaseCommand):
    for i in range(10 ** 4):
        address_line = fake.address()
        street = fake.address()
        city = fake.city()
        state = fake.country()
        postcode = fake.postcode()
        country = fake.country_code(representation="alpha-2")

        new_address = Address.objects.create(
            address_line=address_line,
            street=street,
            city=city,
            state=state,
            postcode=postcode,
            country=country
        )

        new_address.save()
        print(new_address)
