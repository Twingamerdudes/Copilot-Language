#make a main function
from unittest import expectedFailure
import keyboard;
import time;
def main():
    #make so it gets the user input and stores it in a variable
    user_input = input("Please enter a file path: ")
    #open a file using the user input
    #if the input ends in .cpl
    if user_input[-4:] == ".cpl":
        file = open(user_input, "r")
    else:
        try:
            file = open(user_input + ".cpl", "r")
        except:
            print("\nError: This file does not exist or is not a .cpl file")
            exit(1)
    #read the file
    file_read = file.read()
    #put the file into a list called code
    code = file_read.split()
    #close the file
    file.close()
    #if the code is empty
    global globalCode
    globalCode = code
    global temparray
    temparray = []
    global fileTemp
    global fileImport
    global customFunctions
    customFunctions = []
    if code == []:
        #print out an error message
        print("Error: File is empty")
    #if the code is not empty
    else:
        #if the first line of the code has a function named main
        if code[0] == "func" and code[1] == "main(){":
            #run the function
            #make a variable that contains the body of the function and after the } it stops
            body = code[2:code.index("}")]
            RunFunction(body)
        #if the first line of the code does not have a function named main
        else:
            #print out an error message
            print("Error: No start function")
            exit(1)
#make the RunFunction function
def RunFunction(code):
    temp = ""
    #make a varirable called canDoDelay
    #loop through the code
    for i in range(len(code)):
        #if the line is a comment
        if code[i] == "//":
            #skip this line
            continue
        #if the line of code has it's first char .
        if code[i][0] == ".":
            #if there is "array" after the .
            try:
                if code[i][1:6] == "array":
                    #if there are [] after the array
                    if code[i][6:7] == "[":
                        #set temp to the index of temparray
                        temp = temparray[int(code[i][7:code[i].index("]")].strip())]
                        continue
            except:
                temp = ""
            #assign a temp variable to whats infront of the .

            temp = code[i][2:]
            #get rid of any . and " in the temp variable
            temp = temp.replace("\"", "")
            temp = temp.replace("\n", "")
            continue
            
        #if the line of code starts with print
        elif code[i] == "print":
            
            #if a > is infront of the print
            if code[i+1] == "->":
                if code[i+2] == ".":
                    #print out the temp variable
                    print(temp, end="")
                    
                else:
                    #Make a error message saying that you can only print temp
                    print("\nError: You can only print temp")
                    exit(1)
            continue
        #if the line of code starts with spc
        elif code[i] == "spc":
            
            #print out a space
            print(" ", end="")
            continue
            
        #if the line of code starts with nl
        elif code[i] == "nl" and code[i-1] != "file":
            
            #print out a new line
            print("\n", end="")
            continue
            
        #if the line of code starts with a "call"
        elif code[i] == "call":
            #call a fucntion
            CallFunction(code[i+1])
            continue
            
        #if the line of code starts with a "io"
        elif code[i][0] == "i" and code[i][1] == "o":
            #if io has .getInput infront of it
            
            if code[i][2:] == ".getInput":
                #get the user input and store it in a variable
                user_input = input()
                #assign the user input to the temp variable
                temp = user_input
            #if io has .key infront of it
            elif code[i][2:] == ".key":
                #makes the user press a key, then store it in temp
                temp = keyboard.read_key()
            continue
        #if the line of code starts with a "if"
        elif code[i] == "if":
            #if the next line of code is "=="
            try:
                if code[i+2] == "==":
                    #if the temp variable is equal to the next line of code
                    if code[i+1] == code[i+3]:
                    #run the function
                        CallFunction(code[i+4])
                    #else if if code[i+1] is "."
                    elif code[i+1] == ".":
                    #if the temp variable is not equal to the next line of code
                        if temp.strip() == code[i+3]:
                            #run the function
                            CallFunction(code[i+4])
                        elif "else" in code[i+5] and code[i+5] == "else":
                            #run the function
                            CallFunction(code[i+6])
                    elif "else" in code[i+5] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                    #if the next line of code is "!="
                    elif code[i+2] == "!=":
                    #if the temp variable is not equal to the next line of code
                        if code[i+1] != code[i+3]:
                            #run the function
                            CallFunction(code[i+4])
                        #else if code[i+5] is "else"
                        elif code[i+1] == ".":
                            #if the temp variable is equal to the next line of code
                            if temp.strip() != code[i+3]:
                                #run the function
                                CallFunction(code[i+4])
                        elif "else" in code[i+5] and code[i+5] == "else":
                            #run the function
                            CallFunction(code[i+6])
                    elif "else" in code[i+5] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                #if the next line of code is ">"
                elif code[i+2] == ">":
                    #if the temp variable is greater than the next line of code
                    if int(code[i+1]) > int(code[i+3]):
                        #run the function
                        CallFunction(code[i+4])
                    #else if code[i+5] is "else"
                    elif code[i+1] == ".":
                        #if the temp variable is not greater than the next line of code
                        if int(temp) > int(code[i+3]):
                            #run the function
                            CallFunction(code[i+4])
                        elif "else" in code[i+5] and code[i+5] == "else":
                            #run the function
                            CallFunction(code[i+6])
                    elif "else" in code[i+5] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                elif code[i+2] == "<":
                    #if the temp variable is less than the next line of code
                    if int(code[i+1]) < int(code[i+3]):
                        #run the function
                        CallFunction(code[i+4])
                    #else if code[i+5] is "else"
                    elif code[i+1] == ".":
                        #if the temp variable is not less than the next line of code
                        if int(temp) < int(code[i+3]):
                            #run the function
                            CallFunction(code[i+4])
                        elif "else" in code[i+5] and code[i+5] == "else":
                            #run the function
                            CallFunction(code[i+6])
                    elif "else" in code[i+5] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                elif code[i+2] == ">=":
                    #if the temp variable is greater than or equal to the next line of code
                    if int(code[i+1]) >= int(code[i+3]):
                        #run the function
                        CallFunction(code[i+4])
                    #else if code[i+5] is "else"
                    elif code[i+1] == ".":
                        #if the temp variable is not greater than or equal to the next line of code
                        if int(temp) >= int(code[i+3]):
                            #run the function
                            CallFunction(code[i+4])
                        elif "else" in code[i+5] and code[i+5] == "else":
                            #run the function
                            CallFunction(code[i+6])
                    elif "else" in code[i+5] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                elif code[i+2] == "<=":
                    #if the temp variable is less than or equal to the next line of code
                    if int(code[i+1]) <= int(code[i+3]):
                        #run the function
                        CallFunction(code[i+4])
                    #else if code[i+5] is "else"
                    elif code[i+1] == ".":
                        #if the temp variable is not less than or equal to the next line of code
                        if int(temp) <= int(code[i+3]):
                            #run the function
                            CallFunction(code[i+4])
                        elif "else" in code[i+5] and code[i+5] == "else":
                            #run the function
                            CallFunction(code[i+6])
                    elif "else" in code[i+5] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                elif code[i+2] == "in":
                    #if the temp variable is in the next line of code
                    if code[i+1] in code[i+3]:
                        #run the function
                        CallFunction(code[i+4])
                    #else if code[i+5] is "else"
                    elif code[i+1] == ".":
                        #if the temp variable is not in the next line of code
                        if temp in code[i+3]:
                            #run the function
                            CallFunction(code[i+4])
                        elif "else" in code[i+5] and code[i+5] == "else":
                            #run the function
                            CallFunction(code[i+6])
                    elif "else" in code[i+5] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                elif code[i+2] == "!=in":
                    #if the temp variable is not in the next line of code
                    if code[i+1] not in code[i+3]:
                        #run the function
                        CallFunction(code[i+4])
                    #else if code[i+5] is "else"
                    elif code[i+1] == ".":
                        #if the temp variable is in the next line of code
                        if temp not in code[i+3]:
                            #run the function
                            CallFunction(code[i+4])
                    elif "else" in code[i] and code[i+5] == "else":
                        #run the function
                        CallFunction(code[i+6])
                elif "else" in code[i] and code[i+5] == "else":
                    #run the function
                    CallFunction(code[i+6])
            except:
                continue
            continue
        elif code[i] == "array":
            #check if there is a equal sign after array
            if code[i+1] == "=":
                #if there is a [ next to the equal sign
                if code[i+2][0] == "[":
                    temp2 = code[i+2]
                    #loop through temp2 and if there is a [, remove it]
                    for j in range(len(temp2)):
                        if temp2[j] == "[":
                            temp2 = temp2[:j] + temp2[j+1:]
                            break
                    #if there is qoutes inside the [] remove it
                    try:
                        for j in range(len(temp2)):
                            if temp2[j] == "\"":
                                temp2 = temp2[:j] + temp2[j+1:]
                                continue
                    except:
                        temparray = []
                    #split the temparray into a list
                    temparray = temp2.split(",")
            continue
        elif code[i] == "file": 
            #if a .open is next to file
            if code[i+1] == "open":
                #open the file
                #if there is no quotes in code[i+2]
                if code[i+2][0] != "\"":
                    #print a error message
                    print("Error: You must put quotes around the file name")
                    exit(1)
                if code[i+3][0] != "\"":
                    #print a error message
                    print("Error: You must put quotes around the perm type")
                    exit(1)
                #remove "" in code[i+2]
                try:
                    for j in range(len(code[i+2])):
                        if code[i+2][j] == "\"":
                            code[i+2] = code[i+2][:j] + code[i+2][j+1:]
                            continue
                except:
                    asasasasa = 0
                try:
                    for j in range(len(code[i+3])):
                        if code[i+3][j] == "\"":
                            code[i+3] = code[i+3][:j] + code[i+3][j+1:]
                            continue
                except:
                    asasasasa = 0
                fileTemp = open(code[i+2], code[i+3])
            #if a .close is next to file
            elif code[i+1] == "close":
                #close the file
                fileTemp.close()
            #if a .read is next to file
            elif code[i+1] == "read":
                #read the file
                temp2 = fileTemp.read()
                #split the temp into a list
                temparray = temp2.split("\n")
                #if the temp is not empty
            elif code[i+1] == "write":
                try:
                    for j in range(len(code[i+2])):
                        if code[i+2][j] == "\"":
                            code[i+2] = code[i+2][:j] + code[i+2][j+1:]
                            continue
                except:
                    temparray = []
                #write the file
                temp2 = code[i+2]
                fileTemp.write(temp2)
            elif code[i+1] == "nl":
                #write a new line to the file
                fileTemp.write("\n")
            elif code[i+1] == "spc":
                #write a space to the file
                fileTemp.write(" ")
            continue
        elif code[i] == "import":
            #open the file
            fileImport = open(code[i+1], "r")
            #read the file
            temp2 = fileImport.read()
            #split the temp into a list called body
            body = temp2.split()
            #close the file
            fileImport.close()
            #if the body is not empty
            if body != ['']:
                #for each line in the body
                for j in range(len(body)):
                    #add the line to the code
                    customFunctions.append(body[j])
            continue
        elif code[i] == "math":
            #if the next line is a + sign
            if code[i+1] == "+":
                #add the next line to the temp variable
                temp = int(code[i+2]) + int(temp)
            #if the next line is a - sign
            elif code[i+1] == "-":
                #subtract the next line from the temp variable
                temp = int(temp) - int(code[i+2])
            #if the next line is a * sign
            elif code[i+1] == "*":
                #multiply the next line to the temp variable
                temp = int(temp) * int(code[i+2])
            #if the next line is a / sign
            elif code[i+1] == "/":
                #divide the next line from the temp variable
                temp = int(temp) / int(code[i+2])
            #if the next line is a % sign
            elif code[i+1] == "%":
                #mod the next line from the temp variable
                temp = int(temp) % int(code[i+2])
            #if the next line is a ** sign
            elif code[i+1] == "**":
                #exponent the next line from the temp variable
                temp = int(temp) ** int(code[i+2])
            continue
        #if the line of code does not equal any of the above
        
        
def CallFunction(code):
    #check if gobalCode contains code
    if code in globalCode:
        #get the index of the code
        index = 0
        try:
            index = globalCode.index(code + "(){")
        except:
            #if customFunctions contains code
            if code + "(){" in customFunctions:
                #get the index of the code
                try:
                    index = customFunctions.index(code + "(){")
                except:
                    print("\nError: This function does not exist")
                    exit(1)
                body = customFunctions[index+1:customFunctions.index("}", index+1)]
                RunFunction(body)
                return None
            else:
                print("\nError: This function does not exist")
                exit(1)
            #make a error saying that this function does not exist
        #make a variable that contains the body of the function
        body = globalCode[index:globalCode.index("}", index)]
        #run the function
        RunFunction(body)
    elif code + "(){" in customFunctions:
        #get the index of the code
        index = 0
        try:
            index = customFunctions.index(code + "(){")
        except:
            print("\nError: This function does not exist")
            exit(1)
        #make a variable that contains the body of the function
        body = customFunctions[index:customFunctions.index("}", index)]
        #run the function
        RunFunction(body)
    else:
        print("\nError: This function does not exist")
        exit(1)
main()