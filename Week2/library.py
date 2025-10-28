class libraryClass:
    def Subfields(): 
        print("Sub-fields in AI are:")
        listItems=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for lists in listItems:
            print(lists)

    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is odd number")

    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age>21):
                print("Elgible")
            else:
                print("Not Eligible")
        elif(gender=="Female"):
            if(age>18):
                print("Elgible")
            else:
                print("Not Eligible")

    def percentage():
        Subject1=int(input("Subject1="))
        Subject2=int(input("Subject2="))
        Subject3=int(input("Subject3="))
        Subject4=int(input("Subject4="))
        Subject5=int(input("Subject5="))
        total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total :",total)
        percent=float((total)/500)*100
        print("Percentage :",percent)

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        calcTriangle=(height*breadth)/2
        print("Area of Triangle:",calcTriangle)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        calcPerimeter=Height1+Height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",calcPerimeter)