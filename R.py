print("                                                        github: azzam008    ")

flag =True


while(flag):

    print("                                                    Azzam Salim Al-harbi                                                  ")
    print("-----------------------------------------------------------------------------------------------------------------------")
    a=int(input("Enter Num 1 : "))
    b=int(input("Enter Num 2 : "))
    print(" Select your choice") 
    print("1- +  " )
    print("2- ×   ")
    print("3- ÷   " ) 
    print("4- -   " )
    print("5- ××  " )
    print("6-  >   ")
    print("7-  <  ")
    print("8-  >= ")
    print("9-  <=")
    print("0- to EXIT ")
    z = int(input(" your choice "))

    if (z==1 ):
        print(a+b)
    elif(z==2):
        print(a*b)
    elif(z==3):
        print(a/b)
    elif(z==4):
        print(a-b)
    elif(z==5):
        print(a**b)
    elif(z==6):
        print(a>b)
    elif(z==7):
        print(a<b)
    elif(z==8):
        print(a>=b)
    elif(z==9):
        print(a<=b)
    elif(z==0):
        flag=False
    else:
        print("PLEASE SELECT THE CORRECT VALUE")   
    print("-----------------------------------------------------------------------------------------------------------------------")
    print("                                                    Azzam Salim Al-harbi                                                  ")
