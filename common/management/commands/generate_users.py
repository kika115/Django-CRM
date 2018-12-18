from random import choice

from django.core.management.base import BaseCommand
from faker import Faker

from common.models import Address, User
from common.utils import ROLES

fake = Faker('sk_SK')
tru = [True,False]

class Command(BaseCommand):
    for i in range(10):
        username = fake.last_name()
        last_name = fake.last_name()
        fist_name = fake.first_name()
        is_active= choice(tru)
        email=fake.email()
        id_admin = choice(tru)
        is_staff = choice(tru)
        date_joined = fake.date(pattern="%Y-%m-%d", end_datetime=None)
        role = choice(ROLES[1])
        password = 'heslo123'

        new_user = User.objects.create(
            username=username,
            last_name=last_name,
            first_name=fist_name,
            email=email,
            is_active=is_active,
            is_admin=id_admin,
            is_staff=is_staff,
            date_joined=date_joined,
            role=role
        )
        new_user.set_password('heslo123')
        new_user.save()
        print(new_user)