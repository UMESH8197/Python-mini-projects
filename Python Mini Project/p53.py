# Countryinfo in Python (Tutorial)
from countryinfo import CountryInfo
country = CountryInfo("India")
# print(country.alt_spellings())
# print(country.capital())
# print(country.currencies())
# print(country.languages())
# print(country.borders())
data = country.info()
for i, j in data.items():
  print(f"{i}:>>{j}")