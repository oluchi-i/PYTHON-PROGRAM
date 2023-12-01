# Create a user name using letters of a string, to be done with slicing and dictionary
# NAME: Ikwuegbu Oluchi 
# CLASS: Junior

# define the function below this line
def generateUserName(month, year):
    f = first[0]
    m = mid[0]
    l = last[0:3]
    name = f+m+l
    my_dict = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    month_num = my_dict[month]
    year_num = year[2:]
    user_name = "%s%s%s" %(name, month_num, year_num)
    return user_name

# the main script
if __name__ == "__main__":
    # main script code goes below this line. Keep the same indentation level as this line.
    first = input('Enter your first name: ')
    mid = input('Enter your middle name:')
    last = input('Enter your last name: ')
    month = input('Enter your birth month: ')
    year = input('Enter your birth year: ')
    name_gen = generateUserName(month, year)
    print(name_gen.lower())
    print('Your username is: ', name_gen.lower())