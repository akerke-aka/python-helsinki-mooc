"""
Store personal data
-------------------
- appends one person's record to CSV file from tuple
"""
def store_personal_data(person: tuple):
    with open("people.csv", "a") as new_file:
      # unpack input tuple
        name = person[0]
        age = person[1]
        height = person[2]
        line = f"{name};{age};{height}"
        new_file.write(line + "\n")
