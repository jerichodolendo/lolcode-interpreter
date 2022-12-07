from lexical_analyzer import *
from regex import *

index = 0

'''	PROGRAM:
    <program> ::= <comment> HAI <linebreak> <code_block> <linebreak> KTHXBYE <comment>
'''
def program(tokens):
    global index

    tokens_length = len(tokens)
    if index < tokens_length:
        if tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
            while tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
                comment(tokens)
    
        if tokens[index][1] == "Program Start Keyword":
            pass

def comment(tokens):
    global index

    tokens_length = len(tokens)

    if index < tokens_length:
        if tokens[index][1] == "Single line comment":
            print("Single Line Comment found: " + tokens[index][0])
            index += 1
            linebreak(tokens)

            if tokens[index][1] == "Comment Literal":
                print("Comment Literal Found: " + tokens[index][0])
                index += 1
                linebreak(tokens)

        elif tokens[index][1] == "Multiple line comment starts":
            print("Multiple Line Comment found: " + tokens[index][0])
            index += 1
            linebreak(tokens)

            if tokens[index][1] == "Part of Comment Block":
                while index < tokens_length and tokens[index][1] == "Part of Comment Block":
                    print("Part of Comment Block Found: " + tokens[index][0])
                    index += 1
                    linebreak(tokens)

                if tokens[index][1] == "Multiple line comment ends":
                    print("Multiple Line Comment ends: " + tokens[index][0])
                    index += 1
                    linebreak(tokens)

            else:
                prompt_error()
        else:
            prompt_error()  
    else:
        prompt_error()

'''	LINE BREAK:
    <linebreak> ::= \n
'''
def linebreak(tokens):
    global index
    print("Linebreak found")

    tokens_length = len(tokens)

    if index < tokens_length:
        if tokens[index][1] == "New Line":
            index += 1

            if index < tokens_length:
                while tokens[index][1] == "New Line":
                    index += 1

            return True
        return False


# prints an error message
def prompt_error():
    print("Error!")
    quit()