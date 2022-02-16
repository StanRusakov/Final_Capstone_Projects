import sys

print(sys.version)
print(sys.executable)

# user input width
def user_width():
    num_w = 0
    while num_w < 0.1:
        try:
            num_w = float(input('\nEnter width:\n'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return num_w

# user input height
def user_height():
    num_h = 0
    while num_h < 0.1:
        try:
            num_h = float(input('\nEnter height:\n'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return num_h

# user input price
def user_price():
    num_p = 0
    while num_p < 0.1:
        try:
            num_p = float(input('\nEnter price:\n'))
        except:
            print('\nWrong input. Please, enter NUMBER!\n')
            continue
    else:
        return num_p

# user input validation
class Calcul:
    def __init__(self, width, height, price):
        self.width = width
        self.height = height
        self.price = price
        self.total_price = width * height * price

    def param_return(self):
        print("\nParameters:")
        print(f"\tWidth: {self.width}m")
        print(f"\tHeight: {self.height}m")
        print(f"\tTotal area: {self.width * self.height}sq.m.")
        print(f"\tPrice: {self.price}$/sq.m.")

    def __str__(self) -> str:
        return f"\nTotal price for {self.width * self.height}sq.m. of tile with {self.price}$ cost per sq.m.: {self.total_price:.2f}$"

# main function
def main():
    us_width = user_width()
    us_height = user_height()
    us_price = user_price()

    param = Calcul(us_width, us_height, us_price)

    param.param_return()
    print(param)

print(main())