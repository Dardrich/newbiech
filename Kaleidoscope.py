# You sell souvenir kaleidoscopes at a gift shop, and if a customer buys more than one, they get a 10% discount on all of them! 
# Given the total number of kaleidoscopes that a customer buys, let them know what their total will be.
# Tax is 7%. All of your kaleidoscopes cost the same amount, 5.00.

# Task: Take the number of kaleidoscopes that a customer buys and output their total cost including task and any discount.
# Input format: An integer value that represents the number of kaleidoscopes that a customers orders.
# Output format: A number that represents the total purchase price to two decimal places.


def pricing():
    barang = int(input("How many kaleidoscopes that you want to buy? "))
    price = barang * 5.00 * 1.07
    if barang == 1:
        print(f"Your total cost is {price:.2f}")
    elif barang > 1:
        print(f"Your total cost is {price * 0.9:.2f}")
    else:
        print("Please enter the right amount, please")
        pricing()

def ask():
    rebuy = input("Wanna buy again? (y/n) ").lower()

    if rebuy == "y":
        pricing()
        ask()
    elif rebuy == "n":
        exit()
    else:
        print("Please only enter y or n! ")
        ask()

pricing()
ask()
       