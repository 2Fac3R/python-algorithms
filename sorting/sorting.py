if __name__ == '__main__':
    countries_population = [
        {"country": "China", "population": 1444216107},
        {"country": "India", "population": 1393409038},
        {"country": "United States", "population": 332915073},
        {"country": "Indonesia", "population": 276361783},
        {"country": "Pakistan", "population": 225199937},
        {"country": "Brazil", "population": 213993437},
        {"country": "Nigeria", "population": 211400708},
        {"country": "Bangladesh", "population": 166303498},
        {"country": "Russia", "population": 145912025},
        {"country": "Mexico", "population": 130262216},
    ]
    animals = ["Dog", "Cat", "Elephant", "Lion", "Giraffe",
               "Monkey", "Penguin", "Kangaroo", "Dolphin", "Tiger"]

    animals_sorted_by_name_len = sorted(animals, key=len)
    countries_sorted_by_population_desc = sorted(
        countries_population, key=lambda x: x['population'], reverse=True)
    countries_sorted_by_country_name_len = sorted(
        countries_population, key=lambda x: len(x['country']))

    print(animals_sorted_by_name_len)
    # print(countries_sorted_by_population_desc)
    # print(countries_sorted_by_country_name_len)
