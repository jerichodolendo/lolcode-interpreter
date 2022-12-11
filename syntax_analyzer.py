from lexical_analyzer import *
from regex import *

index = 0

'''	PROGRAM:
    <program> ::= <comment> HAI <linebreak> <code_block> <linebreak> KTHXBYE <comment>
'''


def program(tokens):
    global index
    index = 0
    if tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
        while tokens[index][1] == "Single line comment" or tokens[index][1] == "Multiple line comment starts":
            comment(tokens)

    if tokens[index][1] == "Program Start Keyword" and (tokens[index-1][1] != None and tokens[index-1][1] == "New Line"):
        print('{0:30}  {1}'.format("Start of Program ", tokens[index][0]))
        keyword1 = tokens[index][0]
        index += 1
        code_block_list = []
        operator1 = code_block(tokens, code_block_list)

        if tokens[index][1] == "Program End Keyword" and tokens[index+1][1] == "New Line":
            print('{0:30}  {1}'.format("End of Program ", tokens[index][0]))
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
            print('{0:30}  {1}'.format(
                "Single Line Comment Found ", tokens[index][0]))
            index += 1

            if tokens[index][1] == "Comment Literal":
                print('{0:30}  {1}'.format(
                    "Comment Literal Found ", tokens[index][0]))
                index += 1
                linebreak(tokens)

        elif tokens[index][1] == "Multiple line comment starts":
            print('{0:30}  {1}'.format(
                "Multiple Line Comment Found ", tokens[index][0]))
            index += 1
            linebreak(tokens)

            if tokens[index][1] == "Part of Comment Block":
                while index < tokens_length and tokens[index][1] == "Part of Comment Block":
                    print('{0:30}  {1}'.format(
                        "Part of Comment Block Found ", tokens[index][0]))
                    index += 1
                    linebreak(tokens)

                if tokens[index][1] == "Multiple line comment ends":
                    print('{0:30}  {1}'.format(
                        "Multiple Line Comment ends", tokens[index][0]))
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


'''
    CODE BLOCK:
    <code_block>	::= <code_block_2> <code_block>
    <code_block_2>	::= <print> | <declaration> | <comment> | <concat> | <input> |
                        <exp_it> | <assignment> | <if> | <switch>
'''


def code_block(tokens, code_block_list):
    operator1 = code_block_2(tokens)

    if operator1 is not None:
        code_block_list.append(operator1)

    while tokens[index][1] != "Program End Keyword":
        code_block(tokens, code_block_list)

    if len(code_block_list) > 1:
        return tuple(code_block_list)
    else:
        print(code_block_list)
        return code_block_list


def code_block_2(tokens):
    global index
    print('{0:30}  {1}'.format("Entered code_block ", tokens[index][0]))

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
    elif tokens[index][1] == "Keyword Operand Separator":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = concat(tokens)
        return keyword1, (operator1)
    elif tokens[index][1] == "Inputting Keyword":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = input_(tokens)
        return keyword1, operator1
    elif tokens[index][1] == "If End Keyword":
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

    elif tokens[index][1] == "New Line":
        index += 1

    else:
        print(tokens[index][0], tokens[index][1])
        prompt_error()


def case(tokens):
    global index

    if tokens[index][1] == "Case Condition Keyword":
        print('{0:30}  {1}'.format("Entered code_block", tokens[index][0]))
        keyword1 = tokens[index][0]
        index += 1

        if (tokens[index][1] == "NUMBR"
            or tokens[index][1] == "NUMBAR"
            or tokens[index][1] == "YARN literal"
            or tokens[index][1] == "TROOF"
            or tokens[index][1] == "NUMBR"
                or tokens[index][1] == "TYPE Literal"):

            print("Entered literal: " + tokens[index][0])

            literal = tokens[index][0]
            index += 1
            statements = code_block_4(tokens)

            lines = [keyword1, literal, (statements)]

            if tokens[index][1] == "Break Keyword":
                brk = tokens[index][0]
                print("Entered break")
                index += 1
                lines.append(brk)

            operator2 = case(tokens)

            if operator2 is not None:
                lines.append(operator2)
            return tuple(lines)

        else:
            prompt_error()
    elif tokens[index][1] == "Default Condition Keyword":
        pass
    else:
        prompt_error()


'''	SWITCH CASE	
    <switch> ::= <exp_it> WTF? <case> OMGWTF? <code_block> OIC
    <case> ::= OMG <literal> |
            OMG <literal> <case>
'''


def switch(tokens):
    global index

    operator1 = case(tokens)

    if tokens[index][1] == "Default Condition Keyword":
        default_statement = tokens[index][0]
        index += 1

        statements = code_block_4(tokens)

        if tokens[index][1] == "If End Keyword":
            keyword_end = tokens[index][0]
            index += 1

            print("Entered end of SWITCH/CASE")

            return (operator1), (default_statement, (statements)), (keyword_end)
        else:
            prompt_error()
    else:
        prompt_error()


def code_block_4(tokens):
    global index

    code_block_list = []

    while (tokens[index][1] != "Else Condition Keyword"
           and tokens[index][1] != "Elif Condition Keyword"
           and tokens[index][1] != "If End Keyword"):

        if tokens[index][1] == "New Line":
            index += 1
            continue

        code_block_list.append(code_block_3(tokens))

    return tuple(code_block_list)


def assignment(tokens):
    global index

    if tokens[index][1] == "Variable Identifier":
        varident = tokens[index][0]
        print('{0:30}  {1}'.format(
            "Entered Variable Identifier", tokens[index][0]))
        index += 1

        if tokens[index][1] == "Assignment Operator Keyword":
            keyword_assign = tokens[index][0]
            print("Entered Assignment Operator: " + tokens[index][0])
            index += 1

            if (tokens[index][1] == "AND Operator"
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

                ex = expr(tokens)

                return keyword_assign, (varident, ex)

            elif tokens[index][1] == "Variable Identifier":
                varident2 = tokens[index][0]
                print('{0:30}  {1}'.format(
                    "Entered Variable Identifier", tokens[index][0]))
                index += 1

                return keyword_assign, (varident, varident2)

            elif (tokens[index][1] == tokens[index][1] == "NUMBR"
                  or tokens[index][1] == "NUMBAR"
                  or tokens[index][1] == "YARN literal"
                  or tokens[index][1] == "TROOF"
                  or tokens[index][1] == "NUMBR"
                  or tokens[index][1] == "TYPE Literal"):

                lit = literal(tokens)

                return keyword_assign, (varident, lit)
            else:
                prompt_error()
        else:
            prompt_error()
    else:
        prompt_error()


''' IF ELSE
    <if> ::= <exp_it> O RLY? <line_break> YA RLY <code_block> <else_if> OIC
    <else_if> ::= MEBBE <expr> <code_block> <else_if> |
                NO WAI <code_block>
'''


def if_(tokens):
    global index

    if tokens[index][1] == "If Condition Keyword":
        keyword1 = tokens[index][0]
        index += 1

        statements = code_block_3(tokens)
        keyword2 = else_if(tokens)

        if keyword2 == None:
            prompt_error()

        if tokens[index][1] == "If End Keyword":
            keyword3 = tokens[index][0]
            index += 1
            print("Entered If/If-else statement")

            return(keyword1, (statements)), keyword2, (keyword3)
        else:
            prompt_error()


def else_if(tokens):
    global index

    if tokens[index][1] == "Elif Condition Keyword":
        keyword1 = tokens[index][0]
        print('{0:30}  {1}'.format("Entered code_block", tokens[index][0]))

        index += 1

        if (tokens[index][1] == "AND Operator"
            or tokens[index][1] == "OR Operator"
            or tokens[index][1] == "XOR Operator"
            or tokens[index][1] == "Not Operator"
            or tokens[index][1] == "TROOF"
                or tokens[index][1] == "Variable Identifier"):
            condition = expr(tokens)

        statements = code_block_3(tokens)
        keyword2 = else_if(tokens)

        if keyword2 != None:
            return keyword1, condition, (statements), keyword2
        else:
            return keyword1, condition, (statements)

    elif tokens[index][1] == "Else Condition Keyword":
        keyword1 = tokens[index][0]
        print('{0:30}  {1}'.format("Entered code_block", tokens[index][0]))
        index += 1

        statements = code_block_3(tokens)
        return keyword1, (statements)

    elif tokens[index][1] == "If End Keyword":
        pass
    else:
        prompt_error()


def code_block_3(tokens):
    global index

    code_block_list = []
    while (tokens[index][1] != "Else Condition Keyword"
           and tokens[index][1] != "Elif Condition Keyword"
           and tokens[index][1] != "If End Keyword"):

        if tokens[index][1] == "New Line":
            index += 1
            continue

        code_block_list.append(code_block_2(tokens))

    return tuple(code_block_list)


def input_(tokens):
    global index
    if tokens[index][1] == "Variable Identifier":
        print('{0:30}  {1}'.format(
            "Entered Variable Identifier", tokens[index][0]))
        var = tokens[index][0]
    else:
        prompt_error()
    index += 1
    return var


def concat(tokens):
    global index

    operator1 = strconcat(tokens)
    return operator1


def strconcat(tokens):
    global index

    op1 = func_str(tokens)
    if tokens[index][1] == "Operand Separator Keyword":
        # print("Entered operator separator " + tokens[index][0])
        print('{0:30}  {1}'.format(
            "Entered operator separator ", tokens[index][0]))
        kw1 = tokens[index][0]
        index += 1
        op2 = strconcat(tokens)
        return op1, kw1, op2
    else:
        if tokens[index-2][1] == "Operand Separator Keyword":
            return op1
        else:
            prompt_error()


def func_str(tokens):
    global index

    if tokens[index][1] == "YARN literal":
        # print("Entered literal " + tokens[index][0])
        print('{0:30}  {1}'.format("Entered literal ", tokens[index][0]))
        operator1 = tokens[index][0].strip('"')

    elif tokens[index][1] == "Variable Identifier":
        # print("Entered variable identifier " + tokens[index][0])
        print('{0:30}  {1}'.format(
            "Entered variable identifier ", tokens[index][0]))
        operator1 = tokens[index][0]

    else:
        operator1 = str(tokens[index][0])

    index += 1
    return operator1


def declarations(tokens):
    global index
    # print("Entered declaration " + tokens[index][0])
    print('{0:30}  {1}'.format("Entered declaration ", tokens[index][0]))
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
                or tokens[index][1] == "YARN literal"
                or tokens[index][1] == "TROOF"
                or tokens[index][1] == "NUMBR"
                    or tokens[index][1] == "TYPE Literal"):
                lit = literal(tokens)
                return var1, kw1, lit

            elif tokens[index][1] == "Variable Identifier":
                var2 = tokens[index][0]
                index += 1
                return var1, kw1, var2

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
    print('{0:30}  {1}'.format("Entered prints ", tokens[index][0]))

    printsList = []
    operator1 = inf_print(tokens)
    operator = str(operator1) if type(operator1) != tuple else operator1
    printsList.append(operator)

    while (tokens[index][1] == "Variable Identifier"
           or tokens[index][1] == "NUMBR"
           or tokens[index][1] == "NUMBAR"
           or tokens[index][1] == "YARN literal"
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
    print('{0:30}  {1}'.format("Entered inf_prints ", tokens[index][0]))

    if (tokens[index][1] == "Variable Identifier"):
        print('{0:30}  {1}'.format(
            "Variable Identifier found ", tokens[index][0]))
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
          or tokens[index][1] == "YARN literal"
          or tokens[index][1] == "TROOF"
          or tokens[index][1] == "TYPE literal"):
        operator1 = literal(tokens)
        return operator1

    else:
        prompt_error()


'''
EXPRESSION:
    <expr> ::= <sumdiff> | <and> | <or> | <xor> | <not> | <inf_and> | <inf_or> |
<comparison>
'''


def expr(tokens):
    global index
    print('{0:30}  {1}'.format("Entered expression ", tokens[index][0]))

    if tokens[index][1] == "Addition Operator" or tokens[index][1] == "Subtraction Operator" or tokens[index][1] == "Multiplication Operator" or tokens[index][1] == "Division Operator" or tokens[index][1] == "Modulo Operator":
        return sumdiff(tokens)

    elif tokens[index][1] == "AND Operator":
        keyword1 = tokens[index][0]
        index += 1
        operator1 = and_(tokens)
        return keyword1, operator1
    elif tokens[index][1] == "OR Operator":
        kw1 = tokens[index][0]
        index += 1
        op1 = or_(tokens)
        return kw1, (op1)

    elif tokens[index][1] == "XOR Operator":
        kw1 = tokens[index][0]
        index += 1
        op1 = xor(tokens)
        return kw1, (op1)

    elif tokens[index][1] == "Not Operator":
        kw1 = tokens[index][0]
        index += 1
        op1 = not_(tokens)
        return kw1, (op1)

    elif tokens[index][1] == "Infinite Arity AND Keyword":
        kw1 = tokens[index][0]
        index += 1
        op1 = inf_and(tokens)
        return kw1, (op1)

    elif tokens[index][1] == "Infinite Arity OR Keyword":
        kw1 = tokens[index][0]
        index += 1
        op1 = inf_or(tokens)
        return kw1, (op1)

    elif tokens[index][1] == "Equal Operator" or tokens[index][1] == "Not Equal Operator":
        op = comparison(tokens)
        return op
    index += 1


def not_(tokens):
    global index
    print('{0:30}  {1}'.format("Entered not_ ", tokens[index][0]))
    if (tokens[index][1] == "AND Operator"
            or tokens[index][1] == "OR Operator"
            or tokens[index][1] == "XOR Operator"
            or tokens[index][1] == "Not Operator"
            or tokens[index][1] == "TROOF"
            or tokens[index][1] == "Variable Identifier"):
        op1 = bool_exp(tokens)
        return op1
    else:
        prompt_error()


def or_(tokens):
    global index
    print('{0:30}  {1}'.format("Entered or_ ", tokens[index][0]))
    if (tokens[index][1] == "AND Operator"
            or tokens[index][1] == "OR Operator"
            or tokens[index][1] == "XOR Operator"
            or tokens[index][1] == "Not Operator"
            or tokens[index][1] == "TROOF"
            or tokens[index][1] == "Variable Identifier"):
        op1 = bool_exp(tokens)
        if tokens[index][1] == "Operand Separator Keyword":
            kw1 = tokens[index][0]
            # print("Entered operator separator " + kw1)

            index += 1
            if (tokens[index][1] == "AND Operator"
                    or tokens[index][1] == "OR Operator"
                    or tokens[index][1] == "XOR Operator"
                    or tokens[index][1] == "Not Operator"
                    or tokens[index][1] == "TROOF"
                    or tokens[index][1] == "Variable Identifier"):
                op2 = bool_exp(tokens)
                return op1, kw1, op2
            else:
                prompt_error()
        else:
            prompt_error()
    else:
        prompt_error()


def xor(tokens):
    global index
    print('{0:30}  {1}'.format("Entered xor_ ", tokens[index][0]))

    if (tokens[index][1] == "AND Operator"
            or tokens[index][1] == "OR Operator"
            or tokens[index][1] == "XOR Operator"
            or tokens[index][1] == "Not Operator"
            or tokens[index][1] == "TROOF"
            or tokens[index][1] == "Variable Identifier"):
        op1 = bool_exp(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            kw1 = tokens[index][0]
            index += 1

            if (tokens[index][1] == "AND Operator"
                    or tokens[index][1] == "OR Operator"
                    or tokens[index][1] == "XOR Operator"
                    or tokens[index][1] == "Not Operator"
                    or tokens[index][1] == "TROOF"
                    or tokens[index][1] == "Variable Identifier"):
                op2 = bool_exp(tokens)
                return op1, kw1, op2
            else:
                prompt_error()
        else:
            prompt_error()
    else:
        prompt_error()


def inf_and(tokens):
    global index

    if (tokens[index][1] == "AND Operator"
                            or tokens[index][1] == "OR Operator"
                            or tokens[index][1] == "XOR Operator"
                            or tokens[index][1] == "Not Operator"
                            or tokens[index][1] == "TROOF"
                            or tokens[index][1] == "Variable Identifier"):
        op1 = bool_exp(tokens)
        if tokens[index][1] == "Operator Separator Keyword":
            kw_sep = tokens[index][0]
            print('{0:30}  {1}'.format(
                "Entered operator separator ", tokens[index][0]))
            index += 1
            op2 = inf_and(tokens)
            return op1, kw_sep, op2
        else:
            return op1
    else:
        prompt_error()


def inf_or(tokens):
    global index

    if (tokens[index][1] == "AND Operator"
                            or tokens[index][1] == "OR Operator"
                            or tokens[index][1] == "XOR Operator"
                            or tokens[index][1] == "Not Operator"
                            or tokens[index][1] == "TROOF"
                            or tokens[index][1] == "Variable Identifier"):
        op1 = bool_exp(tokens)
        if tokens[index][1] == "Operator Separator Keyword":
            kw_sep = tokens[index][0]
            print('{0:30}  {1}'.format(
                "Entered operator separator ", tokens[index][0]))
            index += 1
            op2 = inf_or(tokens)
            return op1, kw_sep, op2
        else:
            return op1
    else:
        prompt_error()


def comparison(tokens):
    global index

    if tokens[index][1] == "Equal Operator" or tokens[index][1] == "Not Equal Operator":
        kw1 = tokens[index][0]
        print('{0:30}  {1}'.format("Entered comparison ", tokens[index][0]))
        index += 1
        op1 = comparison(tokens)
        if tokens[index][1] == "Operand Separator Keyword":
            sep = tokens[index][0]
            print('{0:30}  {1}'.format(
                "Entered operator separator ", tokens[index][0]))
            index += 1
            op2 = comparison(tokens)
            return kw1, (op1, sep, op2)
    else:
        return comparison2(tokens)


def comparison2(tokens):
    global index

    if tokens[index][1] == "Max Operator" or tokens[index][1] == "Minimum Operator":
        kw1 = tokens[index][0]
        print('{0:30}  {1}'.format("Entered comparison ", tokens[index][0]))
        index += 1
        op1 = comparison2(tokens)
        if tokens[index][1] == "Operand Separator Keyword":
            sep = tokens[index][0]
            print('{0:30}  {1}'.format(
                "Entered operator separator ", tokens[index][0]))
            index += 1
            op2 = comparison2(tokens)
            return kw1, (op1, sep, op2)

    else:
        return comp_op(tokens)


def comp_op(tokens):
    global index

    ret = None
    if tokens[index][1] == "Variable Identifier":
        ret = tokens[index][0]
        print('{0:30}  {1}'.format(
            "Entered Variable Identifier ", tokens[index][0]))
        index += 1
    elif tokens[index][1] == "NUMBR":  # Numbr
        ret = tokens[index][0]
        print('{0:30}  {1}'.format("Entered numbr literal ", tokens[index][0]))
        index += 1
    elif tokens[index][1] == "NUMBAR":  # numbar.
        ret = tokens[index][0]
        print('{0:30}  {1}'.format(
            "Entered numbar literal ", tokens[index][0]))
        index += 1
    else:
        prompt_error()
    return ret


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
    <literal> ::= numbr | numbar | YARN literal | troof
'''


def literal(tokens):
    global index
    if tokens[index][1] == "NUMBR":
        print('{0:30}  {1}'.format("Entered int literal ", tokens[index][0]))
    elif tokens[index][1] == "NUMBAR":
        print('{0:30}  {1}'.format("Entered float literal ", tokens[index][0]))
    elif tokens[index][1] == "YARN literal":
        print('{0:30}  {1}'.format(
            "Entered string literal ", tokens[index][0]))
    elif tokens[index][1] == "TROOF":
        print('{0:30}  {1}'.format(
            "Entered boolean literal ", tokens[index][0]))
    elif tokens[index][1] == "TYPE literal":
        print('{0:30}  {1}'.format("Entered type literal ", tokens[index][0]))
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
            index += 1
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
    print('{0:30}  {1}'.format("Entered and_ ", tokens[index][0]))

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
    elif tokens[index][1] == "Division Operator":
        index += 1
        op1 = sumdiff(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            index += 1
            op2 = sumdiff(tokens)

            return 'QUOSHUNT OF', (op1, 'AN', op2)
        else:
            prompt_error()

    elif tokens[index][1] == "Modulo Operator":
        index += 1
        op1 = sumdiff(tokens)

        if tokens[index][1] == "Operand Separator Keyword":
            index += 1
            op2 = sumdiff(tokens)

            return 'MOD OF', (op1, 'AN', op2)
        else:
            prompt_error()

    else:
        op = value(tokens)
        index += 1
        return op


def bool_exp(tokens):
    global index

    if tokens[index][1] == "TROOF":
        print('{0:30}  {1}'.format("Entered BOOL_LIT ", tokens[index][0]))
        keyword1 = tokens[index][0]
        index += 1
        return keyword1

    elif tokens[index][1] == "Variable Identifier":
        print('{0:30}  {1}'.format("Entered VAR_IDENT ", tokens[index][0]))
        var = tokens[index][0]
        index += 1
        return var


def prompt_error():
    print("Error!")
    quit()
