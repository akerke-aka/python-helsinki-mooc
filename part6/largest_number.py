"""
Largest number
--------------
Reads 'numbers.txt' file and finds the largest number.
"""
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for number in new_file:
            number = int(number)
            if number > largest:
                largest = number
    return largest

