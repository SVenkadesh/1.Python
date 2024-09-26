class Assignment():
    
    def Subfield():
        list=["Sub-fields in AI are: ","Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        for SubfieldsInAI in list:
            print(SubfieldsInAI)
            
    def Even():
        num=int(input("Enter number:"))
        if((num)%2)==0:
            print(num,"is Even number")
        else:
            print(num,"is Odd number")
        
    def Elegible():
        Gender=input("Enter Your Gender:")
        Age=int(input("Enter Your Age:"))
        if (Gender=="Male") and (Age >=21):
            print("ELIGIBLE")
        elif (Gender=="Female") and (Age >=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")

    def percentage():
        Subject1=int(input("Subject1:"))
        Subject2=int(input("Subject2:"))
        Subject3=int(input("Subject3:"))
        Subject4=int(input("Subject4:"))
        Subject5=int(input("Subject5:"))
        Total=(Subject1+Subject2+Subject3+Subject4+Subject5)
        Percentage=(Total/5)
        print("Total:",Total)
        print("Percentage:",Percentage)

    def triangle(): 
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area formula:",(Height*Breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth1=int(input("Breadth:"))
        print("Perimeter of Triangle:",Height1+Height2+Breadth1)