from haversine import haversine

hanoi = {
    'name':'ha noi',
    'lat':21,
    'lng':105
}
danang = {
    'name': 'da nang',
    'lat':16,
    'lng':108
}
haiphong = {
    'name': 'hai phong',
    'lat':20,
    'lng':106
}
cities = [hanoi,danang,haiphong]
n = len(cities)
for i in range(0, n-1):
    for j in range(i + 1, n):
        city1 = cities[i]
        city2 = cities[j]
        cord1 = (city1['lat'],city1['lng'])
        cord2 = (city2['lat'],city2['lng'])
        distance = haversine(cord1,cord2)
        print ('Khoang cach tu {0} den {1} la {2} '.format(city1['name'],city2['name'], distance))
