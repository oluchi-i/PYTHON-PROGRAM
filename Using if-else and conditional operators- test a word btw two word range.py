word = input("Enter a word: ")
lower_range = "apple"
upper_range = "pear"
if lower_range < word < upper_range:
    print("The word is valid.")
else:
    print("The word is out of range.")