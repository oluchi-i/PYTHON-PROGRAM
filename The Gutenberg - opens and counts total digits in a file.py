file_name = "1404.txt"
file = open(file_name, "r")

total_numbers = 0

for line in file:
    words = line.split()
    
    for word in words:
        if any(char.isdigit() for char in word):
            print(word)
            total_numbers += 1

print(f"Total numbers found in the file: {total_numbers}")

file.close()