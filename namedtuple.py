from collections import namedtuple

Product = namedtuple('Product', ['name', 'price', 'quantity'])

product_list = [
    Product('iphone 16pro', 1100, 10),
    Product('iphone 18pro', 1300, 5),
    Product('iphone 12pro', 800, 7),
    Product('Samsung s24', 900, 6),
]

for products in product_list:
    print(f"productni nomi-{products.name}, productni narxi-{products.price}, productni qiymati-{products.quantity}")



class User(namedtuple('User', ['name', 'age', 'gender'])):
    def age_check(self):
        return self.age >= 18

user_list = [
    User('Alex', 21, 'male'),
    User('Ann', 20, 'female'),
    User('Mike', 23, 'male'),
    User('John', 17, 'female'),
]

for user in user_list:
    if user.age_check():
        print(f'user ismi-{user.name}, user yoshi-{user.age}, user genderi-{user.gender}')
    else:
        print(f"User {user.name} 18 yoshdan kichik")

