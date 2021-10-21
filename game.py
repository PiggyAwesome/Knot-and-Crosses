import os, getpass



o = "o"
x = "x"

xxx = 0
ooo = 0

for i in range(int(input("Enter Rounds: "))):
    x1 = "1"
    x2 = "2"
    x3 = "3"
    x4 = "4"
    x5 = "5"
    x6 = "6"
    x7 = "7"
    x8 = "8"
    x9 = "9"
    getpass.getpass("\nPress ENTER to continue.")
    finished = False
    while finished == False:
    
        for i in range(2):
            if x7 == x and x8 == x and x9 == x:
                os.system("cls")            
                print("x Won!")
                xxx += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            
            elif x7 == o and x8 == o and x9 == o:
                os.system("cls")            
                print("o Won!")
                ooo += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            
            elif x4 == x and x5 == x and x6 == x:
                os.system("cls")            
                print("x Won!")
                xxx += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            
            elif x4 == o and x5 == o and x6 == o:
                os.system("cls")            
                print("o Won!")
                ooo += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            
            elif x1 == x and x2 == x and x3 == x:
                os.system("cls")            
                print("x Won!")
                xxx += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            elif x1 == o and x2 == o and x3 == o:
                print("o Won!")
                ooo += 1
    
                finished = True
                break
            
            elif x1 == x and x5 == x and x9 == x:
                os.system("cls")            
                print("x Won!")
                xxx += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            
            elif x1 == o and x5 == o and x9 == o:
                os.system("cls")            
                print("o Won!")
                ooo += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            
            elif x3 == x and x5 == x and x7 == x:
                os.system("cls")            
                print("x Won!")
                xxx += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break
            elif x3 == o and x5 == o and x7 == o:
                os.system("cls")            
                print("o Won!")
                ooo += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break

            elif x2 == o and x5 == o and x8 == o:
                os.system("cls")            
                print("o Won!")
                ooo += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break

            elif x2 == x and x5 == x and x8 == x:
                os.system("cls")            
                print("x Won!")
                xxx += 1
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                finished = True
                break            
            os.system("cls")
            if i == 0:
                turn = o
            else:
                turn = x
            tryAgain = True
            print("")
            while tryAgain == True:
                print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                print("",x1,"|",x2,"|",x3)
                print("-----------")
                print("",x4,"|",x5,"|",x6)
                print("-----------")
                print("",x7,"|",x8,"|",x9)  
                inp = input(f":: ")
  

                if inp == "1":
                        if x1 in "123456789":
                            x1 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
                elif inp == "2":
                        if x2 in "123456789":
                            x2 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
                elif inp == "3":
                        if x3 in "123456789":
                            x3 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
    
                elif inp == "4":
                        if x4 in "123456789": 
                            x4 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
    
                elif inp == "5":
                        if x5 in "123456789": 
                            x5 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
    
                elif inp == "6":
                        if x6 in "123456789": 
                            x6 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
    
                elif inp == "7":
                        if x7 in "123456789": 
                            x7 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
    
                elif inp == "8":
                        if x8 in "123456789": 
                            x8 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
    
    
                elif inp == "9":
                        if x9 in "123456789": 
                            x9 = turn
                            tryAgain = False
                        else:
                            tryAgain = True
                            os.system("cls")
                            print(f"Error: block {inp} is already taken!")
    
                elif inp == "epic":
                    x1 = turn
                    x2 = turn
                    x3 = turn
                    x4 = turn
                    x5 = turn
                    x6 = turn
                    x7 = turn
                    x8 = turn
                    x9 = turn
                    tryAgain = False
    
                elif inp == "oink":
                
                    if turn == x:
                        xe = x
                        x = "🐽"
                        for i in range(9):
                            exec(f"""if x{i+1} == xe:
                                x{i+1} = "🐽"
                            """)
                    if turn == o:
                        oe = o
                        o = "🐖"
                        for i in range(9):
                            exec(f"""if x{i+1} == oe:
                                x{i+1} = "🐖"
                            """)
                    tryAgain = False
    
                elif inp == "sus":
                
                    if turn == x:
                        xe = x
                        x = "🍆"
                        for i in range(9):
                            exec(f"""if x{i+1} == "{xe}":
                                x{i+1} = "🍆"
                            """)
                    if turn == o:
                        oe = o
                        o = "🍑"
                        for i in range(9):
                            exec(f"""if x{i+1} == "{oe}":
                                x{i+1} = "🍑"
                            """)
                    tryAgain = False
    
    
                elif inp == "custom":
                
                    if turn == x:
                        xe = x
                        x = input("Enter Custom Marker: ")
                        for i in range(9):
                            exec(f"""if x{i+1} == xe:
                                x{i+1} = x
                            """)
                    if turn == o:
                        oe = o
                        o = input("Enter Custom Marker: ")
                        for i in range(9):
                            exec(f"""if x{i+1} == oe:
                                x{i+1} = o
                            """)
                    tryAgain = False

                else:
                    os.system("cls")
                    print(f"Error: block {inp} is invalid")
    
                opened = 0
                for i in range(9):
                    exec(f"""if x{i+1} in "123456789":
                        opened += 1""")
                if opened == 0:
                    os.system("cls")            
                    print("No-One Won! (You both lose, losers.)")
                    print(f"Knots and Crosses: {turn}  (x: {xxx} o: {ooo})")
                    print("",x1,"|",x2,"|",x3)
                    print("-----------")
                    print("",x4,"|",x5,"|",x6)
                    print("-----------")
                    print("",x7,"|",x8,"|",x9)  
                    finished = True
                    tryAgain = False
                    break        
    
