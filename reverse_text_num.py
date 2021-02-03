# function for evaluate palidrome or not

def palidrome(input_string):

    # convert to int to string
    input_string=str(input_string)
    
    # intialize empty array's and string

    b =[]
    reversed_string =''
    
    # length of string

    c=len(str(input_string))

    for i in range(c-1,-1,-1):
        b.append(input_string[i])


    for j in b:
        reversed_string+=str(j)

    print(reversed_string)

    if (input_string ==reversed_string):
        print(input_string+" is a palidrome ")
    else:
        print(input_string+" is not a palidrome ")

