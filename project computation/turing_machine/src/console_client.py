import unary_tms
from parse import parse_string_add,parse_string_substract,count_lines,substract_letter
def add_unary():
    print('\nAdd unary:')
    var=input("Enter the string : ")
    last_string=""
    for letter in var:
        return_value= parse_string_add(letter)
        tm_add = unary_tms.add(return_value+'&|||', True)
        print('Tape before processing: ' + tm_add.get_tape())
        tm_add.process()
        print('Tape after processing: ' + tm_add.get_tape())
        last_lines=tm_add.get_tape()
        temp=""
        for i in last_lines[1:len(last_lines)-1]:
            temp= temp+i
        char= count_lines(temp)
        last_string =last_string+char
    print("Last word is : " + last_string)

def substract_unary():
    print('\nSubtract unary:')
    var=input("Enter the string : ")
    last_string=""
    for letter in var:
        return_value= parse_string_substract(letter)
        if letter == 'A':
            return_value= parse_string_substract('#')
        elif letter == 'B':
            return_value= parse_string_substract('%')
        elif letter == 'C':
            return_value= parse_string_substract('/')
        tm_subtract = unary_tms.subtract(return_value+'#|||', True)
        print('Tape before processing: ' + tm_subtract.get_tape())
        tm_subtract.process()
        print('Tape after processing: ' + tm_subtract.get_tape())
        last_lines=tm_subtract.get_tape()
        temp=""
        for i in last_lines[1:len(last_lines)-1]:
            temp= temp+i
        char= count_lines(temp)
        last_string =last_string+char
    print("Last word is : " + last_string)
