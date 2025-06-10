def describe_city(city, country="italy"):
    print(f"{city.title()} is in {country.title()}.")
describe_city("rome")
describe_city("milan")
describe_city("paris", "france")