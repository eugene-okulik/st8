from faker import Faker
fake = Faker('ja_JP')

for _ in range(5):
    print(fake.name())
    print(fake.address())
    print(fake.email())
