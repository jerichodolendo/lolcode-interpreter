import re
from regex import *

# function that checks if a token has any regex matches


def identifier(lexemeTups, tokens):
    global comm_lit, BTW_flag, OBTW_flag
    j = 0

    if (BTW_flag == 1):
        if (tokens[j] == "\n"):
            BTW_flag = 0
            if (re.search(comment_lit, comm_lit)):
                print(comm_lit, "\t == Comment Literal")
                lexemeTups.append((comm_lit, "Comment Literal"))

            comm_lit = ""
            return(tokens)
        else:
            comm_lit = comm_lit + tokens[j]
            if (tokens[j+1] != "\n"):
                comm_lit = comm_lit + " "

            tokens.pop(0)
            return(tokens)

    elif (OBTW_flag == 1 and tokens[j] != "\n"):
        if (tokens[j] == "TLDR"):
            OBTW_flag = 0

            comm_lit = ""
            return(tokens)
        else:
            comm_lit = comm_lit + tokens[j]
            if (tokens[j+1] != "\n"):
                comm_lit = comm_lit + " "

            tokens.pop(0)
            return(tokens)

    elif (type(tokens) == str):
        tokens = tokens.strip()

        if (re.search(declaration, tokens)):
            print(tokens, "\t == Variable Declaration")
            lexemeTups.append((tokens, "Variable Declaration"))

        elif (re.search(plus, tokens)):
            print(tokens, "\t == Addition Operator")
            lexemeTups.append((tokens, "Addition Operator"))

        elif (re.search(difference, tokens)):
            print(tokens, "\t == Subtraction Operator")
            lexemeTups.append((tokens, "Subtraction Operator"))

        elif (re.search(multiply, tokens)):
            print(tokens, "\t == Multiplication Operator")
            lexemeTups.append((tokens, "Multiplication Operator"))

        elif (re.search(divide, tokens)):
            print(tokens, "\t == Division Operator")
            lexemeTups.append((tokens, "Division Operator"))

        elif (re.search(modulo, tokens)):
            print(tokens, "\t == Modulo Operator")
            lexemeTups.append((tokens, "Modulo Operator"))

        elif (re.search(xor_operator, tokens)):
            print(tokens, "\t == XOR Operator")
            lexemeTups.append((tokens, "XOR Operator"))

        elif (re.search(arity_and, tokens)):
            print(tokens, "\t == Infinite Arity AND Keyword")
            lexemeTups.append((tokens, "Infinite Arity AND Keyword"))

        elif (re.search(arity_or, tokens)):
            print(tokens, "\t == Infinite Arity OR Keyword")
            lexemeTups.append((tokens, "Infinite Arity OR Keyword"))

        elif (re.search(equal, tokens)):
            print(tokens, "\t == Equal Operator")
            lexemeTups.append((tokens, "Equal Operator"))

        elif (re.search(recast, tokens)):
            print(tokens, "\t == Recast Keyword")
            lexemeTups.append((tokens, "Recast Keyword"))

        elif (re.search(if_start, tokens)):
            print(tokens, "\t == If Start Keyword")
            lexemeTups.append((tokens, "If Start Keyword"))

        elif (re.search(if_cond, tokens)):
            print(tokens, "\t == If Condition Keyword")
            lexemeTups.append((tokens, "If Condition Keyword"))

        elif (re.search(else_cond, tokens)):
            print(tokens, "\t == Else Condition Keyword")
            lexemeTups.append((tokens, "Else Condition Keyword"))

        elif (re.search(loop_start, tokens)):
            print(tokens, "\t == Loop Start Keyword")
            lexemeTups.append((tokens, "Loop Start Keyword"))

        elif (re.search(loop_end, tokens)):
            print(tokens, "\t == Loop End Keyword")
            lexemeTups.append((tokens, "Loop End Keyword"))

        elif (re.search(max, tokens)):
            print(tokens, "\t == Max Operator")
            lexemeTups.append((tokens, "Max Operator"))

        elif (re.search(minimum, tokens)):
            print(tokens, "\t == Minimum Operator")
            lexemeTups.append((tokens, "Minimum Operator"))

        elif (re.search(or_operator, tokens)):
            print(tokens, "\t == OR Operator")
            lexemeTups.append((tokens, "OR Operator"))

        elif (re.search(and_operator, tokens)):
            print(tokens, "\t == AND Operator")
            lexemeTups.append((tokens, "AND Operator"))

        return(tokens)

    elif (type(tokens) == list):
        if (re.search(start, tokens[j])):
            print(tokens[j], "\t == Program Start Keyword")
            lexemeTups.append((tokens[j], "Program Start Keyword"))

        elif (re.search(end, tokens[j])):
            print(tokens[j], "\t == Program End Keyword")
            lexemeTups.append((tokens[j], "Program End Keyword"))

        elif (re.search(single_line, tokens[j])):
            print(tokens[j], "\t == Single line comment")
            lexemeTups.append((tokens[j], "Single line comment"))
            BTW_flag = 1

        elif (re.search(multiple_start, tokens[j])):
            print(tokens[j], "\t == Multiple line comment starts")
            lexemeTups.append((tokens[j], "Multiple line comment starts"))
            OBTW_flag = 1

        elif (re.search(multiple_end, tokens[j])):
            print(tokens[j], "\t == Multiple line comment ends")
            lexemeTups.append((tokens[j], "Multiple line comment ends"))
            OBTW_flag = 0

        elif (re.search(assignment_var, tokens[j])):
            print(tokens[j], "\t == Assignment Initialize Keyword")
            lexemeTups.append((tokens[j], "Assignment Initialize Keyword"))

        elif (re.search(assignment_op, tokens[j])):
            print(tokens[j], "\t == Assignment Operator Keyword")
            lexemeTups.append((tokens[j], "Assignment Operator Keyword"))

        elif (re.search(not_operator, tokens[j])):
            print(tokens[j], "\t == Not Operator")
            lexemeTups.append((tokens[j], "Not Operator"))

        elif (re.search(operand_sep, tokens[j])):
            print(tokens[j], "\t == Operand Separator Keyword")
            lexemeTups.append((tokens[j], "Operand Separator Keyword"))

        elif (re.search(not_equal, tokens[j])):
            print(tokens[j], "\t == Not Equal Operator")
            lexemeTups.append((tokens[j], "Not Equal Operator"))

        elif (re.search(str_concat, tokens[j])):
            print(tokens[j], "\t == String Concatenator Keyword")
            lexemeTups.append((tokens[j], "String Concatenator Keyword"))

        elif (re.search(typecast, tokens[j])):
            print(tokens[j], "\t == Typecast Keyword")
            lexemeTups.append((tokens[j], "Typecast Keyword"))

        elif (re.search(typecast_assign, tokens[j])):
            print(tokens[j], "\t == Typecast Assign Keyword")
            lexemeTups.append((tokens[j], "Typecast Assign Keyword"))

        elif (re.search(printing, tokens[j])):
            print(tokens[j], "\t == Output/Printing Keyword")
            lexemeTups.append((tokens[j], "Output/Printing Keyword"))

        elif (re.search(inputting, tokens[j])):
            print(tokens[j], "\t == Inputting Keyword")
            lexemeTups.append((tokens[j], "Inputting Keyword"))

        elif (re.search(if_end, tokens[j])):
            print(tokens[j], "\t == If End Keyword")
            lexemeTups.append((tokens[j], "If End Keyword"))

        elif (re.search(elif_cond, tokens[j])):
            print(tokens[j], "\t == Elif Condition Keyword")
            lexemeTups.append((tokens[j], "Elif Condition Keyword"))

        elif (re.search(switch_case, tokens[j])):
            print(tokens[j], "\t == Switch Case Start Keyword")
            lexemeTups.append((tokens[j], "Switch Case Start Keyword"))

        elif (re.search(case, tokens[j])):
            print(tokens[j], "\t == Case Condition Keyword")
            lexemeTups.append((tokens[j], "Case Condition Keyword"))

        elif (re.search(default, tokens[j])):
            print(tokens[j], "\t == Default Condition Keyword")
            lexemeTups.append((tokens[j], "Default Condition Keyword"))

        elif (re.search(break_key, tokens[j])):
            print(tokens[j], "\t == Break Keyword")
            lexemeTups.append((tokens[j], "Break Keyword"))

        elif (re.search(increment, tokens[j])):
            print(tokens[j], "\t == Loop Increment Keyword")
            lexemeTups.append((tokens[j], "Loop Increment Keyword"))

        elif (re.search(decrement, tokens[j])):
            print(tokens[j], "\t == Loop Decrement Keyword")
            lexemeTups.append((tokens[j], "Loop Decrement Keyword"))

        elif (re.search(loop_cond, tokens[j])):
            print(tokens[j], "\t == Loop Condition Keyword")
            lexemeTups.append((tokens[j], "Loop Condition Keyword"))

        elif (re.search(til, tokens[j])):
            print(tokens[j], "\t == Loop Until Keyword")
            lexemeTups.append((tokens[j], "Loop Until Keyword"))

        elif (re.search(wile, tokens[j])):
            print(tokens[j], "\t == Loop While Keyword")
            lexemeTups.append((tokens[j], "Loop While Keyword"))

        elif (re.search(NUMBR, tokens[j])):
            print(tokens[j], "\t == NUMBR")
            lexemeTups.append((tokens[j], "NUMBR"))

        elif (re.search(NUMBAR, tokens[j])):
            print(tokens[j], "\t == NUMBAR")
            lexemeTups.append((tokens[j], "NUMBAR"))

        elif (re.search(YARN, tokens[j])):
            print(tokens[j], "\t == YARN")
            strLtrl = tokens[j][1:-1]
            lexemeTups.append((tokens[j], "YARN"))
            lexemeTups.append(("\"", "String Delimiter"))
            lexemeTups.append((strLtrl, "String Literal"))
            lexemeTups.append(("\"", "String Delimiter"))

        elif (re.search(TROOF, tokens[j])):
            print(tokens[j], "\t == TROOF")
            lexemeTups.append((tokens[j], "TROOF"))

        elif (re.search(TYPE, tokens[j])):
            print(tokens[j], "\t == TYPE literal")
            lexemeTups.append((tokens[j], "TYPE literal"))

        elif (re.search(variable, tokens[j])):
            print(tokens[j], "\t == Variable Identifier")
            lexemeTups.append((tokens[j], "Variable Identifier"))

        elif (re.search(new_line, tokens[j])):
            if (comm_lit != "" and re.search(comment_lit, comm_lit)):
                print(comm_lit, "\t == Part of Comment Block")
                lexemeTups.append((comm_lit, "Part of Comment Block"))
                comm_lit = ""

            print("\\n \t == New Line")
            lexemeTups.append(("\\n", "New Line"))

        else:
            print(tokens[j], "\t == Unknown")
            lexemeTups.append((tokens[j], "Unknown"))

        tokens.pop(0)
        return (tokens)


# function that checks content of tokens
def analyze_tokens(lexemeTups, tokens):
    global BTW_flag, OBTW_flag
    # temporary variable initializations
    tokensCop = tokens.copy()
    s = ""
    fin = ""
    i = 0

    # while loop that exhausts list of tokens
    while (i == 0):
        try:
            if (tokensCop == []):
                i = 1
                break

            # checks for the first detected token
            if (tokensCop != [] and (tokensCop[i] == "I" or
                tokensCop[i] == "SUM" or
                tokensCop[i] == "DIFF" or
                tokensCop[i] == "PRODUKT" or
                tokensCop[i] == "QUOSHUNT" or
                tokensCop[i] == "MOD" or
                tokensCop[i] == "BIGGR" or
                tokensCop[i] == "SMALLR" or
                tokensCop[i] == "BOTH" or
                tokensCop[i] == "EITHER" or
                tokensCop[i] == "WON" or
                tokensCop[i] == "ANY" or
                tokensCop[i] == "ALL" or
                tokensCop[i] == "BOTH" or
                tokensCop[i] == "IS" or
                tokensCop[i] == "O" or
                tokensCop[i] == "YA" or
                tokensCop[i] == "NO" or
                    tokensCop[i] == "IM")):
                # if found, concatenate to s and pop the token
                # while loop continues to exhaust the list
                s = s + tokensCop[i]
                tokensCop.pop(0)

            # if s has a partial keyword, proceeds to examine the tokens
            elif (s == "SUM" and tokensCop[i] == "OF" or
                  s == "DIFF" and tokensCop[i] == "OF" or
                  s == "PRODUKT" and tokensCop[i] == "OF" or
                  s == "QUOSHUNT" and tokensCop[i] == "OF" or
                  s == "MOD" and tokensCop[i] == "OF" or
                  s == "BIGGR" and tokensCop[i] == "OF" or
                  s == "SMALLR" and tokensCop[i] == "OF" or
                  s == "BOTH" and tokensCop[i] == "OF" or
                  s == "EITHER" and tokensCop[i] == "OF" or
                  s == "WON" and tokensCop[i] == "OF" or
                  s == "ANY" and tokensCop[i] == "OF" or
                  s == "ALL" and tokensCop[i] == "OF" or
                  s == "BOTH" and tokensCop[i] == "SAEM" or
                  s == "O" and tokensCop[i] == "RLY?" or
                  s == "YA" and tokensCop[i] == "RLY" or
                  s == "NO" and tokensCop[i] == "WAI"):

                # if found, concatenate to s and pop the token
                s = s + " " + tokensCop[i]
                tokensCop.pop(0)

                # at this point, it is sufficient to examine for any keyword regex matches
                # calls re.search function to search final string of any matches
                fin = s
                identifier(lexemeTups, fin)

                # resets temporary variables
                # while loop continues
                s = ""
                fin = ""

            # if there are still tokens, proceed to exhaust the list and examine
            elif (s == "I" and tokensCop[i] == "HAS" or
                  s == "IS" and tokensCop[i] == "NOW" or
                  s == "IM" and tokensCop[i] == "IN" or
                  s == "IM" and tokensCop[i] == "OUTTA"):

                # if found, concatenate to s and pop the token
                # while loop continues
                s = s + " " + tokensCop[i]
                tokensCop.pop(0)

            # checks if current string has partial identifiers, then proceeds to examine next token
            elif (s == "I HAS" and tokensCop[i] == "A" or
                  s == "IS NOW" and tokensCop[i] == "A" or
                  s == "IM IN" and tokensCop[i] == "YR" or
                  s == "IM OUTTA" and tokensCop[i] == "YR"):

                # if found, concatenate to s and pop the token
                s = s + " " + tokensCop[i]
                tokensCop.pop(0)
                fin = s

                # at this point again, enough to search for any keyword regex matches
                identifier(lexemeTups, fin)

                # resets temporary variables
                s = ""
                fin = ""

            # checks if a token has any regex matches other than being a keyword
            elif (tokensCop[i] == ""):
                continue
            elif (BTW_flag == 1):
                tokensCop = identifier(lexemeTups, tokensCop)
            else:
                tokensCop = identifier(lexemeTups, tokensCop)
                # sets i to 1 to break the while loop
        except Exception as e:
            print(repr(e))
            print("Lexical Error")
            break
