import factory
from django.contrib.auth.models import User
from ..models import Train
from faker import Faker
fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    email = fake.email()
    password = fake.password()
    is_staff = False
    is_superuser = False
    is_active = True

class TrainFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Train

    user = factory.SubFactory(UserFactory)
    weight = fake.random_int(min=1, max=500)
    date = fake.date_time_this_year()
    exercise = fake.random_int(min=1, max=10)
    repetitions = fake.random_int(min=1, max=15)




