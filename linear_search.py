#Getting user input for the collection of data
import sys
lst = list([])
n = int(input("Enter the number of data you want to enter:"))
for i in range (0,n):
    data = int(input("Enter the data:"))
    lst.append(data)
while(1):
    option = input("Do you want to search for any data?(y for yes/n for no)")
    if(option=='y'):
        num = int(input("Enter the data value you want to search for:"))
        for i in range (0,n):
            if(num==lst[i]):
                print("Found! the data has been found")
                c=0
                break
            else:
                c=1
        if(c):
            print("Not Found! the data not found")
    else:
        print("Thank you for using this service!!")
        sys.exit(0)
