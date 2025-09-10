"""
Diary
-----
Program first reads old entries if the file exists. Then program appends new entries to the end of the file. 
Menu: 1 - add, 2 - show content, 0 - quit
"""
diary = []
# read old entries at first execution 
with open("diary.txt") as new_file:
    for line in new_file:
        diary.append(line.strip())
# keep file open while working with it 
with open("diary.txt", "a") as new_file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        n = int(input("Function: "))
        if n == 1:
            s = input("Diary entry:")
            new_file.write(s + "\n")
            diary.append(s)
            print("Diary saved")
        elif n == 2:
            print("Entries:")
            for line in diary:
                print(line)
        elif n == 0:
            print("Bye now!")
            break
