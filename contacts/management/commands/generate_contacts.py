import random
from datetime import datetime, timedelta
from random import choice
from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import Account
from cases.models import Case
from common.models import User, Address
from contacts.models import Contact

fake = Faker('sk_SK')
end = datetime.now()
start = end - timedelta(days=21900)
random_date = end + (end - start) * random.random()
user = User.objects.first()
accounts = Account.objects.all()
address = Address.objects.all()



class Command(BaseCommand):
    for i in range(10 ** 4):
        fist_name = fake.first_name()
        last_name = fake.last_name()
        account = choice(accounts)
        email = fake.email()
        phone = fake.phone_number()
        addres =choice(address)
        description = fake.text()
        created_by = user
        created_on = random_date

        new_contacts = Contact.objects.create(
            first_name=fist_name,
            last_name=last_name,
            email=email,
            phone=phone,
            account=account,
            address=addres,
            description=description,
            created_by=created_by,
            created_on=created_on
        )

        new_contacts.save()
        print(new_contacts)
