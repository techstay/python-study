# %%
import random
from pprint import pprint

from faker import Faker
from faker.providers import BaseProvider

fake = Faker("zh_CN")


# custom providers
class Provider(BaseProvider):
    def random_hello(self):
        return random.choice(["hello", "hi"])


fake.add_provider(Provider)
# %%
fake.random_hello()


# %%
def generate_user():
    return dict(
        name=fake.name(),
        password=fake.password(length=10),
        company=fake.company(),
        job=fake.job(),
        birthday=fake.date_of_birth(minimum_age=0, maximum_age=120),
        telephone=fake.phone_number(),
        address=fake.address(),
    )


users = []
for _ in range(5):
    users.append(generate_user())

pprint(users)

# %%
