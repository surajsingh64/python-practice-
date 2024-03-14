#question -1
print("question -1")
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print('*' * i)

#question -2
print("question -2")
for i in range(rows, 0, -1):
    print('*' * i)
    
#question -3
print("question -3")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)
    
#question -4
print("question -4")   
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * i)
    
#question -5
print("question -5")   
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
    
#question -6
print("question -6")
for i in range(1, rows + 1):
    print(str(i) * i)
    
#question -7
print("question -7")   
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end='')
        num += 1
    print()
#question -8
print("question -8")   
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    increasing_numbers = ''.join(str(j) for j in range(1, i + 1))
    decreasing_numbers = ''.join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + increasing_numbers + decreasing_numbers)

#question -9
print("question -9")
# Printing the top half of the pattern
for i in range(1, rows + 1):
    spaces = ' ' * (rows - i)
    increasing_numbers = ''.join(str(j) for j in range(1, i + 1))
    decreasing_numbers = ''.join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + increasing_numbers + decreasing_numbers)

# Printing the bottom half of the pattern
for i in range(rows - 1, 0, -1):
    spaces = ' ' * (rows - i)
    increasing_numbers = ''.join(str(j) for j in range(1, i + 1))
    decreasing_numbers = ''.join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + increasing_numbers + decreasing_numbers)

#question -10
print("question -10")  
if rows % 2 == 0:
    print("Please enter an odd number of rows.")
else:
    for i in range(1, rows + 1, 2):
        print(' ' * ((rows - i) // 2) + '*' * i)
    for i in range(rows - 2, 0, -2):
        print(' ' * ((rows - i) // 2) + '*' * i)
