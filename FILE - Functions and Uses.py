def main():
    sportsList = open('sport.txt')
    sp = sportsList.read() 
    print(sp)

############ Call to main() ############ 
main()
#print(call)
sportsList = open('sport.txt')
for index in range(1, 11) : 
    sp = sportsList.readline () 
    print( str ( index ) + ". ", sp)

sportsList = open('sport.txt')
for index in range(1, 11) :
    sp = sportsList.readline ()
    print( str ( index ) + ". ", sp.rstrip () )

sportsList = open('sport.txt')
for index in range(1, 11):
    sp = sportsList.readline()
    if len(sp) >= 8:
        print(sp.rstrip())

def main():
    lastName = input("Enter last name: ")
    firstName = input("Enter first name: ")
    studentID = input("Enter ID: ")
    
    inFile = open("studentInfo.txt", "a")
    inFile.write ("Name: " + firstName + " " + lastName)
    inFile.write ("\nStudentID: " + studentID ) 
    inFile.write ("\n") 
    inFile.close ()
    print("Done! Data is saved in file: studentInfo.txt")

  ############ Call to main() ############
main()

def main():
    lastName = input("Enter last name: ")
    firstName = input("Enter first name: ")
    studentID = input("Enter ID: ")
    
    inFile = open("studentInfo.txt", "w")
    inFile.write ("Name: " + firstName + " " + lastName)
    inFile.write ("\nStudentID: " + studentID ) 
    inFile.write ("\n") 
    inFile.close ()
    print("Done! Data is saved in file: studentInfo.txt")

  ############ Call to main() ############
main()

def main():
    lastName = input("Enter last name: ")
    firstName = input("Enter first name: ")
    studentID = input("Enter ID: ")
    credit_earned = input("Enter the number of credits earned: ")
    
    inFile = open("studentInfo.txt", "w")
    inFile.write ("Name: " + firstName + " " + lastName)
    inFile.write ("\nStudentID: " + studentID )
    inFile.write("\nCredits Earned: " + credit_earned)
    inFile.write ("\n") 
    inFile.close ()
    print("Done! Data is saved in file: studentInfo.txt")

  ############ Call to main() ############
main()



