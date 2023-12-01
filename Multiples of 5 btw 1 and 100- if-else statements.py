number = int(input("Enter a value between 1 and 100: "))
if (number % 5 == 0) and (number <= 100):
    print('Valid Entry, well done!')
else:
    print("Invalid number, please try again.")