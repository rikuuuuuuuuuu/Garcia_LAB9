rows = int(input("Enter the number of rows: "))

current_num = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(current_num, end=" ")
        current_num += 1 

    print()