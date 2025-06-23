import factory
from django.contrib.auth.models import User
from faker import Faker
from ocelot.bookstore.models import Book

fake = Faker()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    ISBN = factory.LazyAttribute(lambda _: fake.isbn13(separator=""))
    title = factory.LazyAttribute(lambda _: fake.text(20))
    author = factory.LazyAttribute(lambda _: fake.name())
    publish_date = factory.LazyAttribute(lambda _: fake.date())
    price = factory.LazyAttribute(lambda _: fake.random_number())


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: fake.user_name())
    password = factory.LazyAttribute(lambda _: fake.password())
