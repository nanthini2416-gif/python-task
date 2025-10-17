
cities = []


num_cities = int(input("How many cities do you want to enter? "))


for i in range(num_cities):
    city = input(f"Enter city #{i + 1}: ")
    cities.append(city)

print("\nYou entered the following cities:")
for city in cities:
    print(city)
