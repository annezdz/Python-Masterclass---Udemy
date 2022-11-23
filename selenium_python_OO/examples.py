from selenium_python_OO.access_modifiers import Car

car = Car()

print(car.public_var)
print(car._protected_ar)
# print(car.__private_var)

car.public_method()
car._protected_method()