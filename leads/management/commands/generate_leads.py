from datetime import datetime, timedelta
from random import *

from django.core.management.base import BaseCommand
from faker import Faker

from accounts.models import Account
from common.models import User, Address
from common.utils import LEAD_STATUS, LEAD_SOURCE
from leads.models import Lead

fake = Faker('sk_SK')
end = datetime.now()
start = end - timedelta(days=21900)
random_date = end + (end - start) * random()
user = User.objects.all()
accounts = Account.objects.all()
address = Address.objects.all()

class Command(BaseCommand):
    for i in range(10 ** 4):
        name = fake.job()
        fist_name = fake.first_name()
        last_name = fake.last_name()
        account = choice(accounts)
        email = fake.email()
        phone = fake.phone_number()
        status = choice(LEAD_STATUS[1])
        source = choice(LEAD_SOURCE[1])
        addres = choice(address)
        website = fake.uri()
        account_name = fake.company()
        opportunity_amount = round(random(), 2)
        description = fake.text()
        created_by = choice(user)
        created_on = random_date
        enquery_type = fake.text()

        new_leads = Lead.objects.create(
            title=name,
            first_name=fist_name,
            last_name=last_name,
            email=email,
            phone=phone,
            account=account,
            address=addres,
            status =status,
            source=source,
            website=website,
            account_name=account_name,
            opportunity_amount=opportunity_amount,
            description=description,
            enquery_type =enquery_type,
            created_by=created_by,
            created_on=created_on
        )

        new_leads.save()
        print(new_leads)
