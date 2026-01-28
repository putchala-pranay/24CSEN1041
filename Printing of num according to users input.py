first_num = int(input("Enter the first number:"))
last_num = int(input("Enter the last number:"))
break_num = int(input("Enter the valid number:"))
if first_num > last_num or break_num > last_num:
    print("Invalid input")
    exit()
    
for i in range(first_num,last_num):
    if i % 2 != 0:
        continue  
    elif i == break_num:
        print(i)
        break    
    else:
        pass    

    print(i)
Output:
Enter the first number:0
Enter the last number:12
Enter the valid number:10
0
2
4
6
8
