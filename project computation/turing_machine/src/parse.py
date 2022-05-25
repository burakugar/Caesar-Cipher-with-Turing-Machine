def parse_string_add(letter):
    number_of_line=0
    final_str=""
    if letter == 'A':
        number_of_line= 1
    elif letter == 'B':
        number_of_line= 2
    elif letter == 'C':
        number_of_line= 3
    elif letter == 'D':
        number_of_line= 4
    elif letter == 'E':
        number_of_line= 5
    elif letter == 'F':
        number_of_line= 6
    elif letter == 'G':
        number_of_line= 7
    elif letter == 'H':
        number_of_line= 8
    elif letter == 'I':
        number_of_line= 9
    elif letter == 'J':
        number_of_line= 10
    elif letter == 'K':
        number_of_line= 11
    elif letter == 'L':
        number_of_line= 12
    elif letter == 'M':
        number_of_line= 13
    elif letter == 'N':
        number_of_line= 14
    elif letter == 'O':
        number_of_line= 15
    elif letter == 'P':
        number_of_line= 16
    elif letter == 'Q':
        number_of_line= 17
    elif letter == 'R':
        number_of_line= 18
    elif letter == 'S':
        number_of_line= 19
    elif letter == 'T':
        number_of_line= 20
    elif letter == 'U':
        number_of_line= 21
    elif letter == 'V':
        number_of_line= 22
    elif letter == 'W':
        number_of_line= 23
    for i in range (0,number_of_line):
        final_str=final_str+'|'
    return final_str
def parse_string_substract(letter):
    number_of_line=0
    final_str=""
    if letter == 'A':
        number_of_line= 1
    elif letter == 'B':
        number_of_line= 2
    elif letter == 'C':
        number_of_line= 3
    elif letter == 'D':
        number_of_line= 4
    elif letter == 'E':
        number_of_line= 5
    elif letter == 'F':
        number_of_line= 6
    elif letter == 'G':
        number_of_line= 7
    elif letter == 'H':
        number_of_line= 8
    elif letter == 'I':
        number_of_line= 9
    elif letter == 'J':
        number_of_line= 10
    elif letter == 'K':
        number_of_line= 11
    elif letter == 'L':
        number_of_line= 12
    elif letter == 'M':
        number_of_line= 13
    elif letter == 'N':
        number_of_line= 14
    elif letter == 'O':
        number_of_line= 15
    elif letter == 'P':
        number_of_line= 16
    elif letter == 'Q':
        number_of_line= 17
    elif letter == 'R':
        number_of_line= 18
    elif letter == 'S':
        number_of_line= 19
    elif letter == 'T':
        number_of_line= 20
    elif letter == 'U':
        number_of_line= 21
    elif letter == 'V':
        number_of_line= 22
    elif letter == 'W':
        number_of_line= 23
    elif letter == 'X':
        number_of_line= 24
    elif letter == 'Y':
        number_of_line= 25
    elif letter == 'Z':
        number_of_line= 26
    elif letter == '#':
        number_of_line= 27
    elif letter == '%':
        number_of_line= 28
    elif letter == '/':
        number_of_line= 29
        
    for i in range (0,number_of_line):
        final_str=final_str+'|'
    return final_str    
        
def count_lines(string):
    number_of_line=0
    letter= ""
    for char in string:
       if char == '|':
           number_of_line= number_of_line+1
    if number_of_line == 1:
        letter = 'A'
    elif number_of_line == 2:
        letter = 'B'
    elif number_of_line == 3:
        letter = 'C'
    elif number_of_line == 4:
        letter = 'D'
    elif number_of_line == 5:
        letter = 'E'  
    elif number_of_line == 6:
        letter = 'F'
    elif number_of_line == 7:
        letter = 'G'
    elif number_of_line == 8:
        letter = 'H'  
    elif number_of_line == 9:
        letter = 'I'
    elif number_of_line == 10:
        letter = 'J'
    elif number_of_line == 11:
        letter = 'K'
    elif number_of_line == 12:
        letter = 'L'
    elif number_of_line == 13:
        letter = 'M'  
    elif number_of_line == 14:
        letter = 'N'
    elif number_of_line == 15:
        letter = 'O'
    elif number_of_line == 16:
        letter = 'P'  
    elif number_of_line == 17:
        letter = 'Q'
    elif number_of_line == 18:
        letter = 'R'
    elif number_of_line == 19:
        letter = 'S'
    elif number_of_line == 20:
        letter = 'T'
    elif number_of_line == 21:
        letter = 'U'  
    elif number_of_line == 22:
        letter = 'V'
    elif number_of_line == 23:
        letter = 'W'
    elif number_of_line == 24:
        letter = 'X'  
    elif number_of_line == 25:
        letter = 'Y'
    elif number_of_line == 26:
        letter = 'Z'
    return letter


def substract_letter(letter):
    if letter == 'A':
        letter= 'X'
    elif letter == 'B':
        letter= 'Y'
    elif letter == 'C':
        letter= 'Z'
    elif letter == 'D':
        letter == 'A'
    elif letter == 'E':
        letter= 'B'
    elif letter == 'F':
        letter= 'C'
    elif letter == 'G':
       letter= 'D'
    elif letter == 'H':
        letter= 'E'
    elif letter == 'I':
        letter= 'F'
    elif letter == 'J':
        letter= 'G'
    elif letter == 'K':
       letter= 'H'
    elif letter == 'L':
       letter= 'I'
    elif letter == 'M':
       letter= 'J'
    elif letter == 'N':
       letter= 'K'
    elif letter == 'O':
        letter= 'L'
    elif letter == 'P':
        letter= 'M'
    elif letter == 'Q':
        letter= 'N'
    elif letter == 'R':
        letter= 'O'
    elif letter == 'S':
        letter= 'P'
    elif letter == 'T':
        letter= 'Q'
    elif letter == 'U':
        letter= 'R'
    elif letter == 'V':
        letter= 'S'
    elif letter == 'W':
       letter= 'T'
    elif letter == 'X':
        letter= 'U'
    elif letter == 'Y':
        letter= 'V'
    elif letter == 'Z':
        letter= 'W'
    return letter    