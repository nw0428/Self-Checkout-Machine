from math import *
#from draw_items import *


# for_sale is a type of thing in Python called a dictionary.
# Why do you think it is called that?
for_sale = {
  "Banana": 0.20,
  "Apple": 0.30,
  "Firetruck": 480000,
  "Statue of Ferdinand, some trees and flowers": inf,
  "Shirt": 15,
  "Electron": 9.10938356E-31,
}

def print_receipt(bas, tot):
  for pair in bas.items():
    print(pair[0] + "   " + pair[1])
  print("Your total before taxes is $" + str(tot))

basket = {}
revenue = 0
while input("Is there another customer? yes/no ").find("n") == -1:
  total = 0
  while True:
    inp = input("Enter an item name and quantity,\n or PAY if you have scanned all items ")
    if inp.lower() == "pay":
      break
    item = inp.rsplit(sep=" ", maxsplit=1)[0]
    quantity = int(inp.split(sep=" ")[1])

    basket[item] = str(quantity) + \
                    " * " + str(for_sale[item]) + \
                    " = $" + str(quantity * for_sale[item])
    total += quantity * for_sale[item]
    revenue += quantity * for_sale[item]

  print_receipt(basket, total)
print("Total revenue = " , revenue)