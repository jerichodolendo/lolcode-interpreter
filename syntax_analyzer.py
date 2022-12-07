from lexical_analyzer import *
from regex import *

index = 0

'''	PROGRAM:
    <program> ::= <comment> HAI <linebreak> <code_block> <linebreak> KTHXBYE <comment>
'''
def program(tokens):
    global index

    if tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
        while tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
            comment(tokens)
    
    if tokens[index][1] == "Program Start Keyword" and (tokens[index-1][1] != None and tokens[index-1][1] == "New Line"):
        print("Start of Program: " + tokens[index][0])
        keyword1 = tokens[index][0]
        index += 1

        block_code_list = []
        operator1 = block_code(tokens, block_code_list)

        if tokens[index][1] == "Program End Keyword" and tokens[index+1][1] == "New Line":
            print("End of Program: " + tokens[index][0])
            keyword2 = tokens[index][0]

            index += 2

            while index < len(tokens):
                if tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
                    comment(tokens)
                else:
                    prompt_error()

            return keyword1, operator1, keyword2
        
        else:
            prompt_error()
    else:
        prompt_error()

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

'''	CODE BLOCK:
    <code_block>	::= <code_block2> <code_block>
    <code_block2>	::= <print> | <declaration> | <comment> | <concat> | <input> |
                        <exp_it> | <assignment> | <if> | <switch>
'''
def block_code(tokens, block_code_list):
    operator1 = block_code_2(tokens)

    if operator1 is not None: block_code_list.append(operator1)

    while tokens[index][1] != "Program End Keyword":
        block_code(tokens, block_code_list)

    if len(block_code_list):
        pass

def block_code_2(tokens):
    pass

# prints an error message
def prompt_error():
    print("Error!")
    quit()