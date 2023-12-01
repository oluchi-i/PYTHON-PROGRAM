cities = {
    'Toronto': 958,
    'Nairobi': 982,
    'Chicago': 5259,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)