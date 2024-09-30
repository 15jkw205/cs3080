import car

dd_car = car.Car('white')
dd_car.report()
print(dd_car)

print(dd_car.__color)

dd_car._Car__color = 'pink'
print(dd_car)

