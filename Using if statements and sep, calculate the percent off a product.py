originalPrice = float (input ("Enter the original cost of the time: ")) 
salePrice = float (input ("Enter the sale price: "))
percentOff = int (( originalPrice - salePrice )/ originalPrice * 100)
print ("Original Price: $" ,format( originalPrice , ".2f") , sep ="")
print ("Sale Price: $" ,format( salePrice , ".2f") , sep ="") 
print ("Percent Off: " ,format( percentOff , "d") ,"%" , sep ="")
if ( percentOff >= 50):
    print ("You got a great sale!")
    print("Congratulations!")
 

