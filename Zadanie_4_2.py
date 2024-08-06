def is_palindrom(string):
    '''
        Checking whether the string is palidrome
        Argument: string
    '''
    string_isalpha_casefold = ""

    for c in string:
        if c.isalpha():
            string_isalpha_casefold += c.casefold()

    string_reversed = string_isalpha_casefold[-1::-1]
    
    return string_isalpha_casefold == string_reversed
   

print(is_palindrom('ka Jak!!  '))







