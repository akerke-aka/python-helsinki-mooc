"""
Fruit market
------------
reads fruit data from 'fruits.csv' and returns a dictionary (fruit_name, price).
"""
def read_fruits():
    with open("fruits.csv") as file:
        fruits = {}
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruits[parts[0]] = float(parts[1])
    return fruits
