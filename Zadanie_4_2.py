def Is_palindrom(string):
    '''
        Checking whether the string is palidrome
        Argument: string
    '''
    string_reversed = string[-1::-1]
    if string == string_reversed:
        return True
    else:
        return False
    
print(Is_palindrom('kajak'))
print(Is_palindrom('kajaki'))




