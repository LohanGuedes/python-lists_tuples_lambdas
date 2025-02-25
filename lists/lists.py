def main():
    inventory = [
        {"id": 1, "car_make": "Lincoln", "car_model": "Navigator", "car_year": 2009},
        {"id": 2, "car_make": "Mazda", "car_model": "Miata MX-5", "car_year": 2001},
        {
            "id": 3,
            "car_make": "Land Rover",
            "car_model": "Defender Ice Edition",
            "car_year": 2010,
        },
        {"id": 4, "car_make": "Honda", "car_model": "Accord", "car_year": 1983},
        {"id": 5, "car_make": "Mitsubishi", "car_model": "Galant", "car_year": 1990},
        {"id": 6, "car_make": "Honda", "car_model": "Accord", "car_year": 1995},
        {"id": 7, "car_make": "Smart", "car_model": "Fortwo", "car_year": 2009},
        {"id": 8, "car_make": "Audi", "car_model": "4000CS Quattro", "car_year": 1987},
        {"id": 9, "car_make": "Ford", "car_model": "Windstar", "car_year": 1996},
        {
            "id": 10,
            "car_make": "Mercedes-Benz",
            "car_model": "E-Class",
            "car_year": 2000,
        },
        {"id": 11, "car_make": "Infiniti", "car_model": "G35", "car_year": 2004},
        {"id": 12, "car_make": "Lotus", "car_model": "Esprit", "car_year": 2004},
        {"id": 13, "car_make": "Chevro", "car_model": "Cavalier", "car_year": 1997},
        {"id": 14, "car_make": "Dodge", "car_model": "Ram Van 1500", "car_year": 1999},
        {"id": 15, "car_make": "Dodge", "car_model": "Intrepid", "car_year": 2000},
        {
            "id": 16,
            "car_make": "Mitsubishi",
            "car_model": "Montero Sport",
            "car_year": 2001,
        },
        {"id": 17, "car_make": "Buick", "car_model": "Skylark", "car_year": 1987},
        {"id": 18, "car_make": "Geo", "car_model": "Prizm", "car_year": 1995},
        {"id": 19, "car_make": "Oldsmobile", "car_model": "Bravada", "car_year": 1994},
        {"id": 20, "car_make": "Mazda", "car_model": "Familia", "car_year": 1985},
        {"id": 21, "car_make": "Chevro", "car_model": "Express 1500", "car_year": 2003},
        {"id": 22, "car_make": "Jeep", "car_model": "Wrangler", "car_year": 1997},
        {"id": 23, "car_make": "Eagle", "car_model": "Talon", "car_year": 1992},
        {"id": 24, "car_make": "Toyota", "car_model": "MR2", "car_year": 2003},
        {"id": 25, "car_make": "BMW", "car_model": "525", "car_year": 2005},
        {"id": 26, "car_make": "Cadillac", "car_model": "Escalade", "car_year": 2005},
        {"id": 27, "car_make": "Infiniti", "car_model": "Q", "car_year": 2000},
        {"id": 28, "car_make": "Suzuki", "car_model": "Aerio", "car_year": 2005},
        {"id": 29, "car_make": "Mercury", "car_model": "Topaz", "car_year": 1993},
        {"id": 30, "car_make": "BMW", "car_model": "6 Series", "car_year": 2010},
        {"id": 31, "car_make": "Pontiac", "car_model": "GTO", "car_year": 1964},
        {"id": 32, "car_make": "Dodge", "car_model": "Ram Van 3500", "car_year": 1999},
        {"id": 33, "car_make": "Jeep", "car_model": "Wrangler", "car_year": 2011},
        {"id": 34, "car_make": "Ford", "car_model": "Escort", "car_year": 1991},
        {"id": 35, "car_make": "Chrysler", "car_model": "300M", "car_year": 2000},
        {"id": 36, "car_make": "Volvo", "car_model": "XC70", "car_year": 2003},
        {"id": 37, "car_make": "Oldsmobile", "car_model": "LSS", "car_year": 1997},
        {"id": 38, "car_make": "Toyota", "car_model": "Camry", "car_year": 1992},
        {"id": 39, "car_make": "Ford", "car_model": "Econoline E250", "car_year": 1998},
        {"id": 40, "car_make": "Lotus", "car_model": "Evora", "car_year": 2012},
        {"id": 41, "car_make": "Ford", "car_model": "Mustang", "car_year": 1965},
        {"id": 42, "car_make": "GMC", "car_model": "Yukon", "car_year": 1996},
        {
            "id": 43,
            "car_make": "Mercedes-Benz",
            "car_model": "R-Class",
            "car_year": 2009,
        },
        {"id": 44, "car_make": "Audi", "car_model": "Q7", "car_year": 2012},
        {"id": 45, "car_make": "Audi", "car_model": "TT", "car_year": 2008},
        {"id": 46, "car_make": "Oldsmobile", "car_model": "Ciera", "car_year": 1995},
        {"id": 47, "car_make": "Volkswagen", "car_model": "Jetta", "car_year": 2007},
        {"id": 48, "car_make": "Dodge", "car_model": "Magnum", "car_year": 2008},
        {"id": 49, "car_make": "Chrysler", "car_model": "Sebring", "car_year": 1996},
        {"id": 50, "car_make": "Lincoln", "car_model": "Town Car", "car_year": 1999},
    ]

    print("=== Challenge 1 ===")
    found_car = find_car_by_id(33, inventory)
    print(found_car)

    print("\n=== Challenge 2 ===")
    last_car = get_last_car(inventory)
    print(last_car)

    print("\n=== Challenge 3 ===")
    sorted_cars = sort_cars(inventory)
    for car in sorted_cars:
        print(car["car_model"])

    print("\n=== Challenge 4 ===")
    car_years = get_car_years(inventory)
    for year in car_years:
        print(f"Car Year: {year}")

    print("\n=== Challenege 5 ===")
    old_cars = get_old_cars(inventory)
    print(f"Number of cars maded before 2000: {len(old_cars)}")

    print("\n=== Challenge 6 ===")
    cars = find_bmw_and_audi(inventory)
    for car in cars:
        print("Car Make: {}, Car Model: {}".format(car["car_make"], car["car_model"]))


# Example 1 for loop:

# list = ['a', 'b', 'c', 'd']
# for letter in list:
#     print(letter)
# 'a' 'b' 'c' 'd'

# Example 2 for loop:

# nums = [12, 13, 14, 15]
# evens = []
# for num in nums:
#     if num % 2 == 0:
#       evens.append(num)
# print(evens)
# [12, 14]

# ==== Challenge 1 ====
# The dealer can't recall the information for a car with an id of 33 on his lot.
# Help the dealer find out which car has an id of 33 by returning
# a string with the car's year, make, and model in the string
def find_car_by_id(id, cars_list):
    # Loop through each car, inside the car_list 
    for car in cars_list:
        # Check if the id is equal to 33
        if car.get("id") == 33:
            return f"Car {car.get('id')} is a {car.get('car_year')} {car.get('car_make')} {car.get('car_model')}"


# ==== Challenge 2 ====
# The dealer needs the information on the last car in their inventory.
# What is the make and model of the last car in the inventory?
# return a string with the make and model
def get_last_car(cars_list):
    # Get the length of the list, and turn it into a index using -1
    last_index = len(cars_list) - 1
    # Use the index for getting the last pos
    last_car = cars_list[last_index]
    # Format the String
    last_car_formated_string = f"{last_car.get('car_make')} {last_car.get('car_model')}"
    
    return last_car_formated_string


# ==== Challenge 3 ====
# The marketing team wants the car models listed alphabetically on the website.
# Sort all the car model names into alphabetical order and return the result
def sort_cars(cars_list):
    car_models = sorted(cars_list, key=lambda car: car['car_model'])
    return car_models


# ==== Challenge 4 ====
# The accounting team needs all the years from every car on the lot.
# Create a new array from the dealer data containing only the car years and return the result.
def get_car_years(cars_list):
    only_years = [car.get('car_year') for car in cars_list]
    car_years = sorted(only_years)
    return car_years


# ==== Challenge 5 ====
# The car lot manager needs to find out how many cars are older than the year 2000.
# Using the car_years array you just created, find out how many cars were made
# before the year 2000 by populating the list old_cars and return the result
def get_old_cars(cars_list):
    old_cars = []
    for car in cars_list:
        if car.get('car_year') < 2000:
            old_cars.append(car)
    return old_cars

# ==== Challenge 6 ====
# A buyer is interested in seeing only BMW and Audi cars within the inventory.
# Return an array that only contains BMW and Audi cars
def find_bmw_and_audi(cars_list):
    bmw_and_audi = []
    for car in cars_list:
        if car.get('car_make') == 'Audi' or car.get('car_make') == 'BMW':
            bmw_and_audi.append(car)
    return bmw_and_audi


# === STRETCH ====
# see if you can refactor your functions to use the
# **map** function and list comprehension where possible

if __name__ == "__main__":
    main()
