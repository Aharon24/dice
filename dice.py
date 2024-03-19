import random 
 
i = 0
j = 1
while i  < j :

    a  =  random.randrange(0,6)
    b  =  random.randrange(0,6)
    if a + b == 7 or a + b == 11:
        print("you won", a + b)
    elif i == 0 and (a + b == 4 or a + b == 5 or a + b == 6 or a + b  == 7 or a + b == 8 or a + b == 9 or a + b == 10):
        print("Now your  gobal number is " , a + b)
        j = a+b
        w = 0
       # if i == 0 :
        while  w < j:
            # avelacnel stugumner tveri hamar 
            a  =  random.randrange(0,6)
            b  =  random.randrange(0,6)
            if a + b == 7 or a + b == 11 :
                 print ("you won",a + b)
                 w += 1
                 j = 1
            elif a + b == 2 or a + b == 3 or a + b == 12:
                print("craps ! Casino wins ",a + b)
                w += 1
                j = 1 # (?)
          
    elif a + b == 2 or a + b == 3 or a + b == 12:
        print ("Craps ! Casino wins " , a + b)           
        i += 1
    
  #  else:
  #      print ("The sum of dice is" ,a + b das)
#     i == 5 #(?)
    i += 1