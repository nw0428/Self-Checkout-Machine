# What to work on
## As a group:
Answer the following questions and email David:
* What is happening in `while input("Is there another customer? yes/no ").find("n") == -1:`? Explain fully
* What is `inp.lower()` doing? Does it change inp in any way?
* What do the following three code snippets return and how are they different?
  * `"Hello my name is Elmo".split(" ")`
  * `"Hello my name is Elmo".split(" ", maxsplit=3)`
  * `"Hello my name is Elmo".rsplit(" ", maxsplit=2)`


## For homework add the following features:
1. Annotate the code
1. After there are no more customers print the total revenue (combination of the amount spent by each customer)
1. In the add item loop add an option "Delete", which allows you to remove all of an item from the receipt. i.e. Remove all the Banana
1. Fix the issue where this code recognizes "Banana" and "banana" as two different items.
1. Fix the issue where you cannot buy the "Statue of Ferdinand..."
1. If an unknown item is added, ask for its price and add the item and its price to the for_sale dictionary. To do this, you need to know that you can ask if an item is in a dictionary
1. When printing a receipt give the option to do at least one of the following:
    - sort the items by item price
    - sort the items by number of items bought
    - When printing a receipt use turtle to draw a picture of the each item bought
1. Fix the bug where if you by 3 firetruck(s) and then 1 firetruck the receipt only shows 1 firetruck. Note: *This will require redesigning the code and is therefore VERY difficult*

