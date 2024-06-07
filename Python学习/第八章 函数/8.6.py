def city_country(city,country):
   full_city=f"{city.title()},{country.title()}"
   return full_city


print(city_country('wuhan', 'China'))
print(city_country('Santiago', 'Chile'))
print(city_country('beijing', 'China'))

