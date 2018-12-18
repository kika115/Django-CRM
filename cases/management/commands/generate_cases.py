import random
from datetime import datetime, timedelta
from random import choice
from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import Account
from cases.models import Case
from common.models import User
from common.utils import STATUS_CHOICE, PRIORITY_CHOICE, CASE_TYPE

fake = Faker('sk_SK')
end = datetime.now()
start = end - timedelta(days=21900)
random_date = end + (end - start) * random.random()
user = User.objects.all()
accounts = Account.objects.all()


class Command(BaseCommand):
    for i in range(10 ** 4):
        name = fake.company()
        status = choice(STATUS_CHOICE[1])
        priority = choice(PRIORITY_CHOICE[1])
        case_type = choice(CASE_TYPE[1])
        account = choice(accounts)
        closed_on = random_date
        description = fake.text()
        created_by = choice(user)
        created_on = random_date

        new_accounts = Case.objects.create(
            name=name,
            status=status,
            priority=priority,
            case_type=case_type,
            account=account,
            closed_on=closed_on,
            description=description,
            created_by=created_by,
            created_on=created_on
        )

        new_accounts.save()
        print(new_accounts)
