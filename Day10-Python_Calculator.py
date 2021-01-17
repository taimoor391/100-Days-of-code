import Calculator_logo as lg

def add(n1,n2):
    """Adds up two number"""
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={"+":add,"-":subtract,"*":multiply,"/":divide}
def my_calculator():
    print(lg.logo)
    first_number=float(input("whats the first number?\n"))

    calculate_again="y"
    while calculate_again=="y":
        for i in operations:
            print(i)
        operation_choice=input("What operation do you want to perform?\n")
        second_number=float(input("whats the next number?\n"))
        choose_function=operations[operation_choice]
        result=choose_function(first_number,second_number)
        print("{} {} {} ={}".format(first_number,operation_choice,second_number,result))
        calculate_again=input("Type 'y' to contine calculating with {}, or type 'n to exit: \n".format(result)).lower()
        if calculate_again=='y':
            first_number=result
            print(first_number)
        else:
            start_again=input("Do you want to restart the calulator?y or n\n").lower()
            if start_again=="y":
                my_calculator()


my_calculator()

