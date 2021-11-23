def Equation(op, num1, num2):
    param1 = int(num1)
    param2 = int(num2)

    match op:
        case '+':
            return param1 + param2
        case '-':
            return param1 - param2
        case 'x':
            return param1 * param2
        case '/':
            return param1 / param2
        case _:
            return "You must enter a valid operator. Please only enter '+', '-', 'x', or '/'."

def EnterCalc():
    operator = input("Please input an operator using '+', '-', 'x', or '/' ")
    param1 = float(input('Please input the first number of the equation '))
    param2 = float(input('Please enter the second number of the equation '))
    print(Equation(operator, param1, param2))

def ReadFileForCalcs():
    fileName = "C:\TestOutputFiles\Workshop Module 1\step_2.txt"
    file = open(fileName, mode="r")
    linesToCalculate = file.read().splitlines()
    endResult = 0

    for line in linesToCalculate:
        splitLine = line.split()
        endResult += Equation(splitLine[1], splitLine[2], splitLine[3])

    print(endResult)
        
def ReadFileInstructions():
    instructFileName = "C:\TestOutputFiles\Workshop Module 1\step_3.txt"
    instructFile = open(instructFileName, mode="r")
    linesOfInstructions = instructFile.read().splitlines()

    printedInstructions = []

    for line in linesOfInstructions:
        splitLine = line.split()
        if(len(splitLine) > 2):
            lineNo = round(Equation(splitLine[2], splitLine[3], splitLine[4]),0)
        else:
            lineNo = round(float(splitLine[1]), 0)
        result = linesOfInstructions[int(lineNo) - 1]

        if(printedInstructions.__contains__(result)):
            print("Ended here! \nThe line that was about to be repeated was {0} with the result of {1}".format(lineNo - 1, result))
            print("The last line number was {0} with the result {1}".format(lineNo - 2, result))
            print(printedInstructions.index(result))
            break
        else:
            printedInstructions.append(result)
            print(result)



if(input("Select type in the number of the operation to use \n1) Enter a Calculation \n2) Read from file\n") == "1"):
    EnterCalc()
else:
    ReadFileInstructions()