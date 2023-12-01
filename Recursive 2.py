#SECOND FUNCTION
# Returns number of pennies if pennies are doubled num_days times
def double_pennies(num_pennies, num_days):

    if num_days == 0:
        return num_pennies

    else:
        total_pennies = double_pennies((num_pennies * 2), (num_days - 1))

    return total_pennies

# Program computes pennies if you have 1 penny today,
# 2 pennies after one day, 4 after two days, and so on
starting_pennies = int(input())
user_days = int(input())

print(f'Number of pennies after {user_days} days: ', end="")
print(double_pennies(starting_pennies, user_days))
