import math
valid=False
while not valid:
    try :
       x=int(input("enter your number"))
       y=math.sqrt(x)
       print(y)
       valid=True
    except:
        print("Veuillez saisir un etier positive")
  
