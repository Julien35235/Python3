from faker import Faker

fake = Faker('en_FR')
phone_number = fake.phone_number()

print(phone_number)
