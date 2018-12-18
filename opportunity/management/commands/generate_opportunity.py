import random
from datetime import datetime, timedelta
from random import *
from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import Account
from cases.models import Case
from common.models import User, Address
from common.utils import LEAD_STATUS, LEAD_SOURCE, CURRENCY_CODES, STAGES
from contacts.models import Contact
from leads.models import Lead
from opportunity.models import Opportunity

fake = Faker('sk_SK')
end = datetime.now()
start = end - timedelta(days=21900)
random_date = end + (end - start) * random()
user = User.objects.all()
accounts = Account.objects.all()
addres = Address.objects.all()
contacts = Contact.objects.all()

class Command(BaseCommand):
    for i in range(10 ** 4):
        name = fake.job()
        fist_name = fake.first_name()
        last_name = fake.last_name()
        account = choice(accounts)
        email = fake.email()
        phone = fake.phone_number()
        stage = choice(STAGES[1])
        currency = choice(CURRENCY_CODES[1])
        lead_source = choice(LEAD_SOURCE[1])
        amount = round(random(), 2)
        probability = fake.pyint()
        contact =choice(contacts)
        closed_by =choice(user)
        closed_on = random_date
        description = fake.text()
        created_by = choice(user)
        created_on = random_date

        new_opportuniti = Opportunity.objects.create(
            name=name,
            account=account,
            stage=stage,
            # currency=currency,
            amount=amount,
            probability=probability,
            closed_by=closed_by,
            closed_on=closed_on,
            lead_source=lead_source,
            description=description,
            created_by=created_by,
            created_on=created_on
        )

        new_opportuniti.save()
        print(new_opportuniti)
