from lexical_analyzer import *
from regex import *

index = 0

'''	PROGRAM:
    <program> ::= <comment> HAI <linebreak> <code_block> <linebreak> KTHXBYE <comment>
'''


def program(tokens):
    global index
    print(type(tokens[index][1]))

    index = 0

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

    linebreak(tokens)

    tokens_length = len(tokens)

    if index < tokens_length:
        if tokens[index][1] == "Single line comment":
            print("Single Line Comment found: " + tokens[index][0])
            index += 1

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

    if operator1 is not None:
        block_code_list.append(operator1)

    while tokens[index][1] != "Program End Keyword":
        block_code(tokens, block_code_list)

    if len(block_code_list) > 1:
        return tuple(block_code_list)
    else:
        return block_code_list[0]


def block_code_2(tokens):
    global index
    print("Entered block_code " + tokens[index][0])

    if tokens[index][1] == "Output/Printing Keyword":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = prints(tokens)
        return keyword1, operator1

    elif tokens[index][1] == "Variable Declaration":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = declarations(tokens)
        return keyword1, (operator1)
    elif tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
        comment(tokens)
    elif tokens[index][1] == "String Concatenator Keyword":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = concat(tokens)
        return keyword1, (operator1)
    elif tokens[index][1] == "Inputting Keyword":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = input_(tokens)
        return keyword1, operator1
    elif tokens[index][1] == "":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = if_(tokens)
        return keyword1, (operator1)

    elif tokens[index][1] == "Switch Case Start Keyword":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = switch(tokens)
        return keyword1, (operator1)

    elif tokens[index][1] == "Variable Identifier":
        op = assignment(tokens)
        return op

    elif (tokens[index][1] == "Variable Identifier"
          or tokens[index][1] == "NUMBR"
          or tokens[index][1] == "NUMBAR"
          or tokens[index][1] == "YARN"
          or tokens[index][1] == "TROOF"
          or tokens[index][1] == "TYPE literal"
          or ((tokens[index][1] == "AND Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "OR Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "XOR Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Not Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Infinite Arity OR Keyword" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Infinite Arity AND Keyword" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Addition Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Subtraction Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Multiplication Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Division Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Modulo Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Max Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Minimum Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Equal Operator" and tokens[index-1][1] != "New Line")
              or (tokens[index][1] == "Not Equal Operator" and tokens[index-1][1] != "New Line"))):
        operator1 = expr(tokens)
        return operator1

    elif tokens[index][1] == "New Line":
        index += 1

    else:
        print(tokens[index][0], tokens[index][1])
        prompt_error()


def switch(tokens):
    pass


def assignment(tokens):
    pass


def if_(tokens):
    pass


def else_if(tokens):
    pass


def code_block3(token):
    pass


def input_(tokens):
    global index
    if tokens[index][1] == "Variable Identifier":
        print("Entered variable identifier " + tokens[index][0])
        var = tokens[index][1]
    else:
        prompt_error()
    index += 1
    return var


def concat(tokens):
    global index

    operator1 = strconcat(tokens)
    return operator1


def strconcat(token):
    global index

    op1 = func_str(token)
    if token[index][1] == "Operand Separator Keyword":
        print("Entered operator separator " + token[index][0])
        kw1 = token[index][0]
        index += 1
        op2 = strconcat(token)
        return op1, kw1, op2
    else:
        if token[index-2][1] == "Operand Separator Keyword":
            return op1
        else:
            prompt_error()


def func_str(token):
    global index

    if token[index][1] == "YARN":
        print("Entered literal " + token[index][0])
        operator1 = token[index][0].strip('"')

    elif token[index][1] == "Variable Identifier":
        print("Entered variable identifier " + token[index][0])
        operator1 = token[index][0]

    else:
        operator1 = str(token[index][0])

    index += 1
    return operator1


def declarations(tokens):
    global index
    print("Entered declaration " + tokens[index][0])

    if tokens[index][1] == "Variable Identifier":
        var1 = tokens[index][0]
        index += 1
        if tokens[index][1] == "New Line":
            linebreak(tokens)
            return var1

        if tokens[index][1] == "Assignment Initialize Keyword":
            kw1 = tokens[index][0]
            index += 1

            if (tokens[index][1] == "NUMBR"
                or tokens[index][1] == "NUMBAR"
                or tokens[index][1] == "YARN"
                or tokens[index][1] == "TROOF"
                or tokens[index][1] == "NUMBR"
                    or tokens[index][1] == "TYPE Literal"):
                lit = literal(tokens)
                return var1, kw1, lit

            elif tokens[index][1] == "Variable Identifier":
                var2 = tokens[index][0]
                index += 1
                return var1, kw1, var2

            elif (tokens[index][1] == "Variable Identifier"
                  or tokens[index][1] == "NUMBR"
                  or tokens[index][1] == "NUMBAR"
                  or tokens[index][1] == "YARN"
                  or tokens[index][1] == "TROOF"
                  or tokens[index][1] == "TYPE literal"
                  or ((tokens[index][1] == "AND Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "OR Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "XOR Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Not Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Infinite Arity OR Keyword" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Infinite Arity AND Keyword" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Addition Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Subtraction Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Multiplication Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Division Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Modulo Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Max Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Minimum Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Equal Operator" and tokens[index-1][1] != "New Line")
                      or (tokens[index][1] == "Not Equal Operator" and tokens[index-1][1] != "New Line"))):
                var2 = expr(tokens)
                return var1, kw1, var2

            else:
                prompt_error()

        linebreak(tokens)


'''	PRINT:
    <start_print> ::= VISIBLE <inf_print>
    <print> ::= <inf_print> <print>
    <inf_print> ::= varident | <expr> | <literal>
'''


def prints(tokens):
    global index
    print("Entered prints " + tokens[index][0])

    printsList = []
    operator1 = inf_print(tokens)
    operator = str(operator1) if type(operator1) != tuple else operator1
    printsList.append(operator)

    while (tokens[index][1] == "Variable Identifier"
           or tokens[index][1] == "NUMBR"
           or tokens[index][1] == "NUMBAR"
           or tokens[index][1] == "YARN"
           or tokens[index][1] == "TROOF"
           or tokens[index][1] == "TYPE literal"
           or ((tokens[index][1] == "AND Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "OR Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "XOR Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Not Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Infinite Arity OR Keyword" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Infinite Arity AND Keyword" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Addition Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Subtraction Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Multiplication Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Division Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Modulo Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Max Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Minimum Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Equal Operator" and tokens[index-1][1] != "New Line")
           or (tokens[index][1] == "Not Equal Operator" and tokens[index-1][1] != "New Line"))):
        operator1 = inf_print(tokens)
        printsList.append(operator1)
    return printsList[0] if len(printsList) == 1 else tuple(printsList)


def inf_print(tokens):
    global index
    print("Entered inf_print " + tokens[index][0])

    if (tokens[index][1] == "Variable Identifier"):
        print("Variable Identifier found: " + tokens[index][0])
        var = tokens[index][0]
        index += 1
        return var

    elif (tokens[index][1] == "AND Operator"
          or tokens[index][1] == "OR Operator"
          or tokens[index][1] == "XOR Operator"
          or tokens[index][1] == "Not Operator"
          or tokens[index][1] == "Infinite Arity OR Keyword"
          or tokens[index][1] == "Infinite Arity AND Keyword"
          or tokens[index][1] == "Addition Operator"
          or tokens[index][1] == "Subtraction Operator"
          or tokens[index][1] == "Multiplication Operator"
          or tokens[index][1] == "Division Operator"
          or tokens[index][1] == "Modulo Operator"
          or tokens[index][1] == "Max Operator"
          or tokens[index][1] == "Minimum Operator"
          or tokens[index][1] == "Equal Operator"
          or tokens[index][1] == "Not Equal Operator"):
        operator1 = expr(tokens)
        return operator1

    elif (tokens[index][1] == "NUMBR"
          or tokens[index][1] == "NUMBAR"
          or tokens[index][1] == "YARN"
          or tokens[index][1] == "TROOF"
          or tokens[index][1] == "TYPE literal"):
        operator1 = literal(tokens)
        return operator1

    else:
        prompt_error()


'''	EXPRESSION:
    <expr> ::= <sumdiff> | <and> | <or> | <xor> | <not> | <inf_and> | <inf_or> |
<comparison>
'''


def expr(tokens):
    global index
    print("Entered expr " + tokens[index][1])

    if tokens[index][1] == "Addition Operator" or tokens[index][1] == "Subtraction Operator" or tokens[index][1] == "Multiplication Operator" or tokens[index][1] == "Division Operator":
        return sumdiff(tokens)

    elif tokens[index][1] == "AND Operator":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = and_(tokens)
        return keyword1, operator1

    elif tokens[index][1] == "Division Operator":
        index += 1
        operator1 = sumdiff(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            index += 1
            operator2 = sumdiff(tokens)

            return 'QUOSHUNT OF', (operator1, 'AN', operator2)
        else:
            prompt_error()
    elif tokens[index][1] == "Modulo Operator":
        index += 1
        operator1 = sumdiff(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            index += 1
            operator2 = sumdiff(tokens)

            return 'MOD OF', (operator1, 'AN', operator2)
        else:
            prompt_error()
    else:
        op = value(tokens)
        index += 1
        return op


def value(tokens):
    global index

    if tokens[index][1] == "NUMBR":
        return tokens[index][0]
    elif tokens[index][1] == "NUMBAR":
        return tokens[index][0]
    elif tokens[index][1] == "Variable Identifier":
        return tokens[index][0]
    else:
        prompt_error()


'''	LITERAL:
    <literal> ::= numbr | numbar | yarn | troof
'''


def literal(tokens):
    global index
    if tokens[index][1] == "NUMBR":
        print("Entered int literal " + tokens[index][0])
    elif tokens[index][1] == "NUMBAR":
        print("Entered float literal " + tokens[index][0])
    elif tokens[index][1] == "YARN":
        print("Entered string literal " + tokens[index][0])
    elif tokens[index][1] == "TROOF":
        print("Entered boolean literal " + tokens[index][0])
    elif tokens[index][1] == "TYPE literal":
        print("Entered type literal " + tokens[index][0])
    else:
        prompt_error()
    literal = tokens[index][0]
    index += 1
    return literal


def sumdiff(tokens):
    global index

    if tokens[index][1] == "Addition Operator":
        index += 1

        operator1 = sumdiff(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            i += 1
            operator2 = sumdiff(tokens)

            return 'SUM OF', (operator1, 'AN', operator2)
        else:
            prompt_error()

    elif tokens[index][1] == "Subtraction Operator":
        index += 1
        operator1 = sumdiff(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            index += 1
            operator2 = sumdiff(tokens)

            return 'DIFF OF', (operator1, 'AN', operator2)
        else:
            prompt_error()

    else:
        op = multdiv(tokens)
        return op


def and_(tokens):
    global index
    print("Entered and_ " + tokens[index][1])

    if tokens[index][1] == "AND Operator" or tokens[index][1] == "OR Operator" or tokens[index][1] == "XOR Operator" or tokens[index][1] == "Not Operator" or tokens[index][1] == "TROOF" or tokens[index][1] == "Variable Identifier":
        operator1 = bool_exp(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            keyword1 = tokens[index][0]
            index += 1

            if tokens[index][1] == "AND Operator" or tokens[index][1] == "OR Operator" or tokens[index][1] == "XOR Operator" or tokens[index][1] == "Not Operator" or tokens[index][1] == "TROOF" or tokens[index][1] == "Variable Identifier":
                operator2 = bool_exp(tokens)
                return operator1, keyword1, operator2

            else:
                prompt_error()

        else:
            prompt_error()
    else:
        prompt_error()


def multdiv(tokens):
    global index
    if tokens[index][1] == "Multiplication Operator":
        index += 1
        operator1 = sumdiff(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            index += 1
            operator2 = sumdiff(tokens)

            return 'PRODUKT OF', (operator1, 'AN', operator2)
        else:
            prompt_error()


def bool_exp(tokens):
    global index

    if tokens[index][1] == "TROOF":
        print("Entered BOOL_LIT: " + tokens[index][0])
        keyword1 = tokens[index][0]
        index += 1
        return keyword1

    elif tokens[index][1] == "Variable Identifier":
        print("Entered VAR_IDENT: " + tokens[index][0])
        var = tokens[index][0]
        index += 1
        return var


def prompt_error():
    print("Error!")
    # quit()
