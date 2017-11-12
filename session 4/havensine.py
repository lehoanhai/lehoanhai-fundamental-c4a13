from haversine import haversine

hanoi = [21,105]
danang = [16,108]

distance = haversine(hanoi,danang)
print (distance)
