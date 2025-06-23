import factory
from faker import Faker

from apps.example.models import SomeModel

fake = Faker()


class SomeModelFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = SomeModel

    name = factory.LazyAttribute(lambda _: fake.name())
