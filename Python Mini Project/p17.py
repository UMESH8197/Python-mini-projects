# Create Dummy Data using Python
from faker import Faker
fake = Faker()
print(fake.name())
print(fake.user_name())
print(fake.address())
print(fake.text())

# The Faker().profile() method returns fake data about job profiles containing 13 columns. 
# So below is how you can create a dummy dataset using Python:

from faker import Faker
import pandas as pd
fake = Faker()
data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)
print(data.head())



