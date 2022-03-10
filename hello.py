# print("Hello world")
print(5.2)
print('hello world')

print(type(5))
print(type(5.2))
print(type("bla"))
print(type(True))

pet = "Kutya"
print(pet)
pet = "Macska"
print(pet)

#print(type(pet))

wheel_of_car = 4
print(type(wheel_of_car))
wheel_of_car = "asd"
print(type(wheel_of_car))

#type hint
number_of_cars: int = 16

number_of_cars_in_parking = number_of_cars

print(number_of_cars_in_parking)
number_of_cars_in_parking = 20

print(number_of_cars)
print(number_of_cars_in_parking)

print(len("alma"))
length_of_apple = len("alma")
print(length_of_apple)

print(10*10)
print(10.0*1.5)
print(10/6)
print(10.6-10)

name = "John Doe"
age = 40

print(name +" "+ str(age))

print(name,age, "eves", sep="*****")

print(f"A {name} emberke {age} eves")
print(f"A 3+5 kifejezés értéke {3+5}")