
input1 = int(input("Enter number1: "))
input2 = int(input("Enter number2: "))


choice = int(input ("Enter your choice 1-Add,2-Subtract,3-Multiply,4-Divide; "))

def calc_dict(choice,input1,input2):
    return {
            1: lambda: input1 + input2,
            2: lambda: input1 - input2,
            3: lambda: input1 * input2,
            4: lambda: input1 / input2
        }.get(choice,lambda:None)()

print('The result for inp is : ',choice, calc_dict(choice, input1,input2))

