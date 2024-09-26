class Test():
    def Elegible():
        Gender=input("Enter Your Gender:")
        Age=int(input("Enter Your Age:"))
        if (Gender=="Male") and (Age >=21):
            print("ELIGIBLE")
        elif (Gender=="Female") and (Age >=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
    def OddorEven():
        num=int(input("Enter number:"))
        if((num)%2)==0:
            print(num,"is Even number")
        else:
            print(num,"is Odd number")