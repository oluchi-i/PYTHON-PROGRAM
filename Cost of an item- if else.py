cost1 = int(input("Enter cost of first item: $"))
cost2 = int(input("Enter cost of second item: $"))
pay = int(input('Payment value: $'))
total = cost1 + cost2
if pay < total:
    print("Balance: $", (total - pay), sep="")
else:
    print("Thank you!, your change will be $", (pay-total), sep="")
