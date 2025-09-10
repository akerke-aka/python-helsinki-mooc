"""
Filtering the contents of a file
--------------------------------
- Reads the contents of the file solutions.csv
- writes those lines which have a correct result into the file correct.csv
- writes those lines which have an incorrect result into the file incorrect.csv
"""

def filter_solutions():
    correct_list = []
    incorrect_list = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            parts = line.strip().split(";")
            calculation = parts[1]
            result = int(parts[2])
          # two possible operators "+" or "-"
            if "+" in calculation:
                operands = calculation.split("+")
              # compare computed sum with claimed result
                if int(operands[0]) + int(operands[1]) == int(result):
                    correct_list.append(line)
                else:
                    incorrect_list.append(line)
            elif "-" in calculation:
                operands = calculation.split("-")
              # compare computed difference with claimed result
                if int(operands[0]) - int(operands[1]) == int(result):
                    correct_list.append(line)
                else:
                    incorrect_list.append(line)
      # add lists content to their target SCV files
        with open("correct.csv", "w") as crr:
            for correct in correct_list:
                crr.write(correct + "\n")
        with open("incorrect.csv", "w") as incr:
            for incorrect in incorrect_list:
                incr.write(incorrect + "\n")
