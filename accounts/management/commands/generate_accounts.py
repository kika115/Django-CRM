from django.core.management.base import BaseCommand
from faker import Faker
import random
import uuid
from random import seed, choice
from datetime import datetime, timedelta

from accounts.models import Account
from common.models import User, Address
from common.utils import INDCHOICES

fake = Faker('sk_SK')
end = datetime.now()
start = end - timedelta(days=21900)
random_date = end + (end - start) * random.random()
user = User.objects.all()
address = Address.objects.all()


class Command(BaseCommand):
    for i in range(10 ** 4):
        id = str(uuid.uuid4())
        name = fake.company()
        industry = choice(INDCHOICES[1])
        website = fake.uri()
        description = fake.text()
        created_by = choice(user)
        created_on = random_date
        email = fake.email()
        billing_address = choice(address)
        shipping_address = choice(address)

        new_cases = Account.objects.create(
            name=name,
            email=email,
            industry=industry,
            website=website,
            description=description,
            shipping_address=shipping_address,
            billing_address=billing_address,
            created_by=created_by,
            created_on=created_on
        )

        new_cases.save()
        print(new_cases)
