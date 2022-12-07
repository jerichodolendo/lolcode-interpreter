import re
import sys

global printArray
symbolTable = {}
printArray = None
codeLength = None
codeSize = None
operationStack = []
variable = None
ifFlag = None
ifOrElse = None

def assign(code):
        #===========================================================
        # GRAMMAR: I HAS A varident
    if re.match(r'[a-z][A-z_0-9]+', code[0]):
        remember = code[0]
        symbolTable.update({code[0]:None})
        code.pop(0)
        if len(code) == 0:
            print("pass here")
            return printArray, symbolTable, 0
        elif re.match("^R$",code[0]):
            code.pop(0)
            if len(code) == 0:
                print("Error")
            else:
                return baseVariable(code, printArray, symbolTable, remember)
        elif re.match(r'ITZ', code[0]):
            if re.match(r'ITZ', code[0]):
                code.pop(0)
                return baseVariable(code, printArray, symbolTable, remember)
                    
        else:
            print("Error")
        #===========================================================
        # GRAMMAR: I HAS A varident ITZ <literal> 
        # match NUMBAR

def baseVariable(code, printArray, symbolTable, remember):
    printArray = None
    #============================================================
    # catch variables
    if re.match(r'[a-z][A-z_0-9]+', code[0]):
        if code[0] in symbolTable:
            symbolTable[remember] = symbolTable[code[0]]
            return printArray, symbolTable, 0
        else:
            print("Error")# check muna if nasa symbol table, if wala error
        # code.pop(0)
        # if len(code) == 0:
        #     return print("Pass")
    #============================================================   
    elif re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", code[0]):
        symbolTable.update({remember:code[0]})
        return printArray, symbolTable, 0
    # match NUMBR
    elif re.match("(-?[1-9]+[0-9]*|^0$)", code[0]):
        symbolTable.update({remember:code[0]})
        return printArray, symbolTable, 0
    # match TROOF
    elif re.match("^(WIN)$|^(FAIL)$", code[0]):
        symbolTable.update({remember:code[0]})
        return printArray, symbolTable, 0
    # match YARN
    elif re.match(r'\"(.+?)\"', code[0]):   
        symbolTable.update({remember:code[0]})
        return printArray, symbolTable, 0
    # match Data types
    elif re.match("^(NUMBR)$|^(NUMBAR)$|^(YARN)$|^(TROOF)$", code[0]):
        symbolTable.update({remember:code[0]})
        return printArray, symbolTable, 0
    #===========================================================
    # GRAMMAR: I HAS A varident ITZ <expr>
    # <arithmetic>
    elif re.match("^(SUM OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(DIFF OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(PRODUKT OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(QUOSHUNT OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(MOD OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(BIGGR OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(SMALLR OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(BOTH OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(EITHER OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(WON OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    # <comparison>
    elif re.match("^(BOTH SAEM)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(DIFFRINT)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    elif re.match("^(NOT)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        if remember in symbolTable:
            symbolTable.update({remember:symbolTable["IT"]})
        return printArray, symbolTable, flag
    #===========================================================
    else:
        return print("Error3")

def scanVariable(code):
    #============================================================
    # catch variables
    if re.match(r'[a-z][A-z_0-9]', code[0]):
        variable = code[0]
        code.pop(0)
        value = str(input())
        if variable in symbolTable:
            symbolTable[variable] = value
            return printArray, symbolTable, 0
        else:
            symbolTable.update({variable:value})
            return printArray, symbolTable, 0
    else:
        return print("ErrorScan - read statement should be followed by a variable identifier")
#========================================================================================================
# ARITHMETIC OPERATIONS
# Catches all values after operand separator (nested expressions and values)
def literal2(code):
    # if re.match("^(SUM OF)$|^(DIFF OF)$|^(PRODUKT OF)$|^(QUOSHUNT OF)$|^(MOD OF)$|^(BIGGR OF)$|^(SMALLR OF)$", code[0]):
    #     evaluate(code, printArray, symbolTable, codeLength, codeSize)
    if re.match("^(SUM OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(DIFF OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(PRODUKT OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(QUOSHUNT OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(MOD OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(BIGGR OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(SMALLR OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(BOTH SAEM)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(DIFFRINT)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(BOTH OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(EITHER OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(WON OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    # catches second operand in the equation
    elif re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", code[0]):
        code.pop(0)
        if len(code) == 0: 
            return print("Pass Float")
        else:
            print("Pass Float")
            # continue to find second operand
            operandSeparator(code)
    elif re.match("(-?[1-9]+[0-9]*|^0$)", code[0]):
        code.pop(0)
        if len(code) == 0: 
            return print("Pass Integer")
        else:
            print("Pass Integer")
            # continue to find second operand
            operandSeparator(code)
    elif re.match("\"(.+?)\"", code[0]):
        code.pop(0)
        if len(code) == 0: 
            return print("Pass String")
        else:
            print("Pass String")
            # continue to find second operand
            operandSeparator(code)
    elif re.match("^(WIN)$|^(FAIL)$", code[0]):
        code.pop(0)
        if len(code) == 0: 
            return print("Pass Boolean")
        else:
            print("Pass Boolean")
            # continue to find second operand
            operandSeparator(code)

def operandSeparator(code):
    # Finds Operand separator
    if re.match("^AN$", code[0]):
        code.pop(0)
        if len(code) == 0:
            return print("Error5")
        else:
            literal2(code)
    
def literal(code):
    global printArray
    global symbolTable
    # nested Arithmetic operations
    if re.match("^(SUM OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(DIFF OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(PRODUKT OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(QUOSHUNT OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(MOD OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(BIGGR OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(SMALLR OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(BOTH SAEM)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(DIFFRINT)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(BOTH OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(EITHER OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    elif re.match("^(WON OF)$", code[0]):
        printArray, symbolTable, flag = evaluate(code, printArray, symbolTable, codeLength, codeSize)
        printArray = "IT"
        return printArray, symbolTable, flag
    # if re.match("^(SUM OF)$|^(DIFF OF)$|^(PRODUKT OF)$|^(QUOSHUNT OF)$|^(MOD OF)$|^(BIGGR OF)$|^(SMALLR OF)$", code[0]):
    #     evaluate(code, printArray, symbolTable, codeLength, codeSize)
    # cathces first operand in an equation
    elif re.match("[a-z][A-z_0-9]+", code[0]):
        printArray = code[0]
        if printArray in symbolTable:
            return printArray, symbolTable, 0
        else:
            print("Error")
    elif re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", code[0]):
        printArray = "IT"
        if "IT" in symbolTable:
            symbolTable[printArray] = code[0]
        else:
            symbolTable.update({"IT":code[0]})
        return printArray, symbolTable, 0
    elif re.match("(-?[1-9]+[0-9]*|^0$)", code[0]):
        printArray = "IT"
        if "IT" in symbolTable:
            symbolTable[printArray] = code[0]
        else:
            symbolTable.update({"IT":code[0]})
        return printArray, symbolTable, 0
    elif re.match("\"(.+?)\"", code[0]):
        printArray = "IT"
        if "IT" in symbolTable:
            symbolTable[printArray] = code[0]
        else:
            symbolTable.update({"IT":code[0]})
        return printArray, symbolTable, 0
    elif re.match("^(WIN)$|^(FAIL)$", code[0]):
        printArray = "IT"
        if "IT" in symbolTable:
            symbolTable[printArray] = code[0]
        else:
            symbolTable.update({"IT":code[0]})
        return printArray, symbolTable, 0
    elif re.match("IT", code[0]):
        printArray = "IT"
        return printArray, symbolTable, 0

    if len(code) != 0:
        code.pop(0)
        if len(code) == 0:
            print("Error4")
        else:
            operandSeparator(code)

def performStackOp(code,variable):
    variable2 = None
    variable1 = None
    printArray = None

    if re.match(r'[a-z][A-z_0-9]+', operationStack[len(operationStack)-1]):
        if re.match(r'[a-z][A-z_0-9]+', operationStack[len(operationStack)-2]):
            variable2 = operationStack.pop(len(operationStack)-1)
            variable1 = operationStack.pop(len(operationStack)-1)
            if variable1 in symbolTable and variable2 in symbolTable:
                if re.match(r'(^-?[1-9]+[0-9]*$|^0$)', symbolTable[variable1]) and re.match(r'(^-?[1-9]+[0-9]*$|^0$)', symbolTable[variable2]):
                    variable2 = symbolTable[variable2]
                    variable1 = symbolTable[variable1]
                    if re.match(r"SUM OF", operationStack[len(operationStack)-1]):
                        var = str(int(variable1)+int(variable2))
                        
                    elif re.match(r"DIFF OF", operationStack[len(operationStack)-1]):
                        var = str(int(variable1)-int(variable2))
                        
                    elif re.match(r"PRODUKT OF", operationStack[len(operationStack)-1]):
                        var = str(int(variable1)*int(variable2))
                        
                    elif re.match(r"QUOSHUNT OF", operationStack[len(operationStack)-1]):
                        var = str(int(variable1)/int(variable2))
                        
                    elif re.match(r"MOD OF", operationStack[len(operationStack)-1]):
                        var = str(int(variable1)%int(variable2))
                        
                    elif re.match(r"BIGGR OF", operationStack[len(operationStack)-1]):
                        var = str(max(int(variable1),int(variable2)))
                        
                    elif re.match(r"SMALLR OF", operationStack[len(operationStack)-1]):
                        var = str(min(int(variable1),int(variable2)))
                        
                    if variable is not None:
                        if variable in symbolTable:
                            symbolTable[printArray] = var
                        else:
                            symbolTable.update({variable:var})
                    else:
                        symbolTable.update({"IT":var})
                    operationStack.pop(len(operationStack)-1)
                    return printArray, symbolTable, 0
                elif re.match(r'-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)', symbolTable[variable1]) and re.match(r'-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)', symbolTable[variable2]):
                    variable2 = symbolTable[variable2]
                    variable1 = symbolTable[variable1]
                    if re.match(r"SUM OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)+float(variable2))

                    elif re.match(r"DIFF OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)-float(variable2))

                    elif re.match(r"PRODUKT OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)*float(variable2))

                    elif re.match(r"QUOSHUNT OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)/float(variable2))

                    elif re.match(r"MOD OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)%float(variable2))

                    elif re.match(r"BIGGR OF", operationStack[len(operationStack)-1]):
                        var = str(max(float(variable1),float(variable2)))

                    elif re.match(r"SMALLR OF", operationStack[len(operationStack)-1]):
                        var = str(min(float(variable1),float(variable2)))

                    if variable is not None:
                        if variable in symbolTable:
                            symbolTable[printArray] = var
                        else:
                            symbolTable.update({variable:var})
                    else:
                        symbolTable.update({"IT":var})
                    operationStack.pop(len(operationStack)-1)
                    return printArray, symbolTable, 0
                elif (re.match(r'-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)', symbolTable[variable1]) and re.match(r'(^-?[1-9]+[0-9]*$|^0$)', symbolTable[variable2])) or (re.match(r'(^-?[1-9]+[0-9]*$|^0$)', symbolTable[variable1]) and re.match(r'-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)', symbolTable[variable2])):
                    variable2 = symbolTable[variable2]
                    variable1 = symbolTable[variable1]
                    if re.match(r"SUM OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)+float(variable2))

                    elif re.match(r"DIFF OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)-float(variable2))

                    elif re.match(r"PRODUKT OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)*float(variable2))

                    elif re.match(r"QUOSHUNT OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)/float(variable2))

                    elif re.match(r"MOD OF", operationStack[len(operationStack)-1]):
                        var = str(float(variable1)%float(variable2))

                    elif re.match(r"BIGGR OF", operationStack[len(operationStack)-1]):
                        var = str(max(float(variable1),float(variable2)))

                    elif re.match(r"SMALLR OF", operationStack[len(operationStack)-1]):
                        var = str(min(float(variable1),float(variable2)))
                    
                    if variable is not None:
                        if variable in symbolTable:
                            symbolTable[printArray] = var
                        else:
                            symbolTable.update({variable:var})
                    else:
                        symbolTable.update({"IT":var})
                    operationStack.pop(len(operationStack)-1)
                    return printArray, symbolTable, 0
                else:
                    print("error")
            else:
                print("error")
    
    if re.match(r"-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-1]):
        if re.match(r"-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-2]):
            variable2 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match(r"SUM OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)+float(variable2))

            elif re.match(r"DIFF OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)-float(variable2))

            elif re.match(r"PRODUKT OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)*float(variable2))

            elif re.match(r"QUOSHUNT OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)/float(variable2))

            elif re.match(r"MOD OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)%float(variable2))

            elif re.match(r"BIGGR OF", operationStack[len(operationStack)-1]):
                var = str(max(float(variable1),float(variable2)))

            elif re.match(r"SMALLR OF", operationStack[len(operationStack)-1]):
                var = str(min(float(variable1),float(variable2)))

            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            operationStack.pop(len(operationStack)-1)
            return printArray, symbolTable, 0
        else:
            print("pass")
    
    if re.match(r"(^-?[1-9]+[0-9]*$|^0$)", operationStack[len(operationStack)-1]):
        if re.match(r"(^-?[1-9]+[0-9]*$|^0$)", operationStack[len(operationStack)-2]):
            variable2 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match(r"SUM OF", operationStack[len(operationStack)-1]):
                var = str(int(variable1)+int(variable2))

            elif re.match(r"DIFF OF", operationStack[len(operationStack)-1]):
                var = str(int(variable1)-int(variable2))

            elif re.match(r"PRODUKT OF", operationStack[len(operationStack)-1]):
                var = str(int(variable1)*int(variable2))

            elif re.match(r"QUOSHUNT OF", operationStack[len(operationStack)-1]):
                var = str(int(variable1)/int(variable2))

            elif re.match(r"MOD OF", operationStack[len(operationStack)-1]):
                var = str(int(variable1)%int(variable2))

            elif re.match(r"BIGGR OF", operationStack[len(operationStack)-1]):
                var = str(max(int(variable1),int(variable2)))

            elif re.match(r"SMALLR OF", operationStack[len(operationStack)-1]):
                var = str(min(int(variable1),int(variable2)))

            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            operationStack.pop(len(operationStack)-1)
            return printArray, symbolTable, 0
        else:
            print("pass")
        
    if re.match(r"(^-?[1-9]+[0-9]*$|^0$)", operationStack[len(operationStack)-1]) or re.match(r"-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-1]):
        if re.match(r"-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-2]) or re.match(r"(^-?[1-9]+[0-9]*$|^0$)", operationStack[len(operationStack)-2]):
            variable2 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match(r"SUM OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)+float(variable2))

            elif re.match(r"DIFF OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)-float(variable2))

            elif re.match(r"PRODUKT OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)*float(variable2))

            elif re.match(r"QUOSHUNT OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)/float(variable2))

            elif re.match(r"MOD OF", operationStack[len(operationStack)-1]):
                var = str(float(variable1)%float(variable2))

            elif re.match(r"BIGGR OF", operationStack[len(operationStack)-1]):
                var = str(max(float(variable1),float(variable2)))

            elif re.match(r"SMALLR OF", operationStack[len(operationStack)-1]):
                var = str(min(float(variable1),float(variable2)))

            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            operationStack.pop(len(operationStack)-1)
            return printArray, symbolTable, 0
        else:
            print("pass")
            
    else:
        print("error")

def booleanperformStackOp(code, variable):
    variable2 = None
    variable1 = None
    printArray = None

    if re.match("^(WIN)$|^(FAIL)$", operationStack[len(operationStack)-1]):
        if re.match("^(WIN)$|^(FAIL)$", operationStack[len(operationStack)-2]):
            variable2 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match("^(BOTH OF)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "WIN"
                else:
                    var = "FAIL"
            elif re.match("^(EITHER OF)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2 and variable1 == "WIN":
                    var = "WIN"
                elif (variable1 == "WIN" and variable2 == "FAIL") or (variable1 == "FAIL" and variable2 == "WIN"):
                    var = "WIN"
                else:
                    var = "FAIL"
            elif re.match("^(WON OF)$", operationStack[len(operationStack)-1]):
                if variable1 != variable2:
                    var = "WIN"
                else:
                    var = "FAIL"

            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            return printArray, symbolTable, 0
        else:
            print("error")
    elif re.match(r'[a-z][A-z_0-9]+', operationStack[len(operationStack)-1]):
       if re.match(r'[a-z][A-z_0-9]+', operationStack[len(operationStack)-2]): 
            variable2 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if variable2 in symbolTable and variable1 in symbolTable:
                if re.match("^(WIN)$|^(FAIL)$", symbolTable[variable1]) and re.match("^(WIN)$|^(FAIL)$", symbolTable[variable2]):
                    variable1 = symbolTable[variable1]
                    variable2 = symbolTable[variable2]
                    if re.match("^(BOTH OF)$", operationStack[len(operationStack)-1]):
                        if variable1 == variable2:
                            var = "WIN"
                        else:
                            var = "FAIL"
                    elif re.match("^(EITHER OF)$", operationStack[len(operationStack)-1]):
                        if variable1 == variable2 and variable1 == "WIN":
                            var = "WIN"
                        elif (variable1 == "WIN" and variable2 == "FAIL") or (variable1 == "FAIL" and variable2 == "WIN"):
                            var = "WIN"
                        else:
                            var = "FAIL"
                    elif re.match("^(WON OF)$", operationStack[len(operationStack)-1]):
                        if variable1 != variable2:
                            var = "WIN"
                        else:
                            var = "FAIL"

                    if variable is not None:
                        if variable in symbolTable:
                            symbolTable[printArray] = var
                        else:
                            symbolTable.update({variable:var})
                    else:
                        symbolTable.update({"IT":var})
                    operationStack.pop(0)
                    return printArray, symbolTable, 0
                else:
                    printArray = "IT"
                    if "IT" in symbolTable:
                        symbolTable[printArray] = "DED: Invalid literals used for boolean operation."
                    else:
                        symbolTable.update({"IT":"DED: Invalid literals used for boolean operation."})
                    return printArray, symbolTable, 1

    else:
       print("error")

def operandsNest(code,variable):
    printArray = None
    if re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return performStackOp(code, variable)
        else:
            return concatInfar(code,variable)
    elif re.match("(-?[1-9]+[0-9]*|^0$)", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return performStackOp(code, variable)
        else:
            return concatInfar(code,variable)
    elif re.match(r"[a-z][A-z_0-9]+", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return performStackOp(code, variable)
        else:
            return concatInfar(code,variable)

def booleanoperandNest(code,variable):
    printArray = None
    if re.match("^(WIN)$|^(FAIL)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return booleanperformStackOp(code, variable)
        else:
            return booleanconcatInfar(code,variable)

def NotOperandNest(code, variable):
    printArray = None

    if re.match("^(WIN)$|^(FAIL)$", code[0]):
        if code[0] == "WIN":
            var = "FAIL"
        else:    
            var = "WIN"
        code.pop(0)
        if variable is not None:
            if variable in symbolTable:
                symbolTable[printArray] = var
            else:
                symbolTable.update({variable:var})
        else:
            symbolTable.update({"IT":var})
        return printArray, symbolTable, 0
    elif re.match("[a-z][A-z_0-9]+", code[0]):
        if code[0] in symbolTable:
            if re.match("^(WIN)$|^(FAIL)$", symbolTable[code[0]]):
                if symbolTable[code[0]] == "WIN":
                    var = "FAIL"
                else:    
                    var = "WIN"
                code.pop(0)
                if variable is not None:
                    if variable in symbolTable:
                        symbolTable[printArray] = var
                    else:
                        symbolTable.update({variable:var})
                else:
                    symbolTable.update({"IT":var})
                return printArray, symbolTable, 0
        else:
            printArray = "IT"
            if "IT" in symbolTable:
                symbolTable[printArray] = "DED: Invalid literal values used for boolean operation."
            else:
                symbolTable.update({"IT":"DED: Invalid literal values used for boolean operation."})
            return printArray, symbolTable, 1
    else:
        printArray = "IT"
        if "IT" in symbolTable:
            symbolTable[printArray] = "DED: Invalid literal values used for boolean operation."
        else:
            symbolTable.update({"IT":"DED: Invalid literal values used for boolean operation."})
        return printArray, symbolTable, 1

def comparisonOperandNest(code, variable):
    if re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return comparisonperformStackOp(code, variable)
        else:
            return comparisonconcatInfar(code, variable)
    elif re.match("(-?[1-9]+[0-9]*|^0$)", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return comparisonperformStackOp(code, variable)
        else:
            return comparisonconcatInfar(code, variable)
    elif re.match("^(WIN)$|^(FAIL)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return comparisonperformStackOp(code, variable)
        else:
            return comparisonconcatInfar(code, variable)
    elif re.match("[a-z][A-z_0-9]+", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            return comparisonperformStackOp(code, variable)
        else:
            return comparisonconcatInfar(code, variable)

def comparisonperformStackOp(code, variable):
    variable2 = None
    variable1 = None
    printArray = None
    # "FAIL"
    if re.match("(-?[1-9]+[0-9]*|^0$)", operationStack[len(operationStack)-1]) or re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-1]) or re.match("^(WIN)$|^(FAIL)$", operationStack[len(operationStack)-1]) or re.match("\"(.+?)\"", operationStack[len(operationStack)-1]):
        variable2 = operationStack[len(operationStack)-1]
        operationStack.pop(len(operationStack)-1)
        if re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-1]) or re.match("(-?[1-9]+[0-9]*|^0$)", operationStack[len(operationStack)-1]) or re.match("\"(.+?)\"", operationStack[len(operationStack)-1]) or re.match("^(WIN)$|^(FAIL)$", operationStack[len(operationStack)-1]):
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match("^(BOTH SAEM)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "WIN"
                else:
                    var = "FAIL"
            elif re.match("^(DIFFRINT)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "FAIL"
                else:
                    var = "WIN"
            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            return printArray, symbolTable, 0
        else:
            print("error")

    elif re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-1]):
        variable2 = operationStack[len(operationStack)-1]
        operationStack.pop(len(operationStack)-1)
        if re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", operationStack[len(operationStack)-1]):
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match("^(BOTH SAEM)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "WIN"
                else:
                    var = "FAIL"
            elif re.match("^(DIFFRINT)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "FAIL"
                else:
                    var = "WIN"
            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            return printArray, symbolTable, 0
        else:
            print("error")

    elif re.match("(-?[1-9]+[0-9]*|^0$)", operationStack[len(operationStack)-1]):
        variable2 = operationStack[len(operationStack)-1]
        operationStack.pop(len(operationStack)-1)
        if re.match("(-?[1-9]+[0-9]*|^0$)", operationStack[len(operationStack)-1]):
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match("^(BOTH SAEM)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "WIN"
                else:
                    var = "FAIL"
            elif re.match("^(DIFFRINT)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "FAIL"
                else:
                    var = "WIN"
            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            return printArray, symbolTable, 0
        else:
            print("error")

    elif re.match("^(WIN)$|^(FAIL)$", operationStack[len(operationStack)-1]):
        variable2 = operationStack[len(operationStack)-1]
        operationStack.pop(len(operationStack)-1)
        if re.match("^(WIN)$|^(FAIL)$", operationStack[len(operationStack)-1]):
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match("^(BOTH SAEM)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "WIN"
                else:
                    var = "FAIL"
            elif re.match("^(DIFFRINT)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "FAIL"
                else:
                    var = "WIN"
            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            return printArray, symbolTable, 0
        else:
            print("error")

    elif re.match("\"(.+?)\"", operationStack[len(operationStack)-1]):
        variable2 = operationStack[len(operationStack)-1]
        operationStack.pop(len(operationStack)-1)
        if re.match("\"(.+?)\"", operationStack[len(operationStack)-1]):
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if re.match("^(BOTH SAEM)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "WIN"
                else:
                    var = "FAIL"
            elif re.match("^(DIFFRINT)$", operationStack[len(operationStack)-1]):
                if variable1 == variable2:
                    var = "FAIL"
                else:
                    var = "WIN"
            if variable is not None:
                if variable in symbolTable:
                    symbolTable[printArray] = var
                else:
                    symbolTable.update({variable:var})
            else:
                symbolTable.update({"IT":var})
            return printArray, symbolTable, 0
        else:
            print("error")

    elif re.match("[a-z][A-z_0-9]+", operationStack[len(operationStack)-1]):
        print("pass")
        if re.match("[a-z][A-z_0-9]+", operationStack[len(operationStack)-2]):
            variable2 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            variable1 = operationStack[len(operationStack)-1]
            operationStack.pop(len(operationStack)-1)
            if variable1 in symbolTable and variable2 in symbolTable:
                variable1 = symbolTable[variable1]
                variable2 = symbolTable[variable2]
                if re.match("^(BOTH SAEM)$", operationStack[len(operationStack)-1]):
                    if variable1 == variable2:
                        var = "WIN"
                    else:
                        var = "FAIL"
                elif re.match("^(DIFFRINT)$", operationStack[len(operationStack)-1]):
                    if variable1 == variable2:
                        var = "FAIL"
                    else:
                        var = "WIN"
                symbolTable.update({"IT":var})
                return printArray, symbolTable, 0
            else:
                print("error")

    else:
        print("error")

#========================================================================================================
def concatInfar(code, variable):
    if re.match("^AN$", code[0]):
        code.pop(0)
        if len(code) == 0:
            return print("ErrorConcat")
        else:
            return operandsNest(code, variable)
    else:
        return print("ErrorConcat")

def booleanconcatInfar(code, variable):
    if re.match("^AN$", code[0]):
        code.pop(0)
        if len(code) == 0:
            return print("ErrorConcat")
        else:
            return booleanoperandNest(code, variable)
    else:
        return print("ErrorConcat")

def comparisonconcatInfar(code, variable):
    if re.match("^AN$", code[0]):
        code.pop(0)
        if len(code) == 0:
            return print("ErrorConcat")
        else:
            return comparisonOperandNest(code, variable)
    else:
        return print("ErrorConcat")

def concatenate(code):  # pwede ba nested concatenation di ako sure??? di ko muna nilagay wala sa specs e
    # match NUMBAR
    if re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", code[0]):
        print("Pass Float - typecast to String")
    # match NUMBR
    elif re.match("(-?[1-9]+[0-9]*|^0$)", code[0]):
        print("Pass Integer - typecast to String")
    # match TROOF
    elif re.match("^(WIN)$|^(FAIL)$", code[0]):
        print("Pass Boolean - typecast to String")
    # match YARN
    elif re.match(r'\"(.+?)\"', code[0]):   
        print("Pass String")
    else:
        return print("Error")
    code.pop(0)
    if len(code) != 0:
        concatInfar(code, variable)

def booleanNot(code):
    if re.match("^(NOT)$", code[0]):
        code.pop(0)
        booleanNot(code)
    elif re.match("^(WIN)$|^(FAIL)$", code[0]):
        code.pop(0)
        if len(code) == 0: 
            return print("Pass Boolean")
        else:
            return print("Error")
    elif re.match("^(BOTH OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(EITHER OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)
    elif re.match("^(WON OF)$", code[0]):
        evaluate(code, printArray, symbolTable, codeLength, codeSize)

def evaluate(code, printArray, symbolTable, codeLen, codeSiz):
    # check list's first index if matches the respective token 
    global codeLength
    global codeSize

    codeLength = codeLen
    codeSize = codeSiz

    print(code)

    if codeLength == 0:
        if re.match(r'HAI', code[0]):
            return printArray, symbolTable, 0
        else:
            printArray = "IT"
            if "IT" in symbolTable:
                symbolTable[printArray] = "DED: Program does not start with the HAI reserved keyword."
            else:
                symbolTable.update({"IT":"DED: Program does not start with the HAI reserved keyword."})
            return printArray, symbolTable, 1
    elif codeLength == codeSize-1:
        if re.match(r'^KTHXBYE', code[0]) and (codeLength == codeSize-1):
            return printArray, symbolTable, 0
        else:
            printArray = "IT"
            if "IT" in symbolTable:
                symbolTable[printArray] = "DED: Program still has trailing code after the KTHXBYE reserved keyword."
            else:
                symbolTable.update({"IT":"DED: Program still has trailing code after the KTHXBYE reserved keyword."})
            return printArray, symbolTable, 1

    # VARIABLE DECLARATIONS
    if re.match(r'I HAS A', code[0]):
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            return assign(code)

    # PRINT STATEMENTS
    elif re.match("^(VISIBLE)$", code[0]):
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            print(code)
            return literal(code)

    elif re.match("^(GIMMEH)$", code[0]):
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            return scanVariable(code)
    # CONCATENATION 
    elif re.match("^(SMOOSH)$", code[0]):
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            concatenate(code)
    # catches every starting operation
    # ARTIHMETIC OPERATIONS + - * / %% bigger smaller
    elif re.match("^(SUM OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return operandsNest(code,variable)

    elif re.match("^(DIFF OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return operandsNest(code,variable)
    elif re.match("^(PRODUKT OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return operandsNest(code,variable)
    elif re.match("^(QUOSHUNT OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return operandsNest(code,variable)
    elif re.match("^(MOD OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return operandsNest(code,variable)
    elif re.match("^(BIGGR OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return operandsNest(code,variable)
    elif re.match("^(SMALLR OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return operandsNest(code,variable)
    # Comparison operations == !=
    # supports operation nesting therefore catches relational operations
    # Relational operations >= <= > <
    elif re.match("^(BOTH SAEM)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return comparisonOperandNest(code,variable)
    elif re.match("^(DIFFRINT)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return comparisonOperandNest(code,variable)
    # Boolean operations and or xor not
    elif re.match("^(BOTH OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return booleanoperandNest(code,variable)
    elif re.match("^(EITHER OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return booleanoperandNest(code,variable)
    elif re.match("^(WON OF)$", code[0]):
        operationStack.append(code[0])
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return booleanoperandNest(code,variable)
    elif re.match("^(NOT)$", code[0]):
        code.pop(0)
        if len(code) == 0:
            print("Error1")
        else:
            # checks for operand
            return NotOperandNest(code,variable)

    # catches variable assignments
    elif re.match("^([a-z][A-z_0-9]*)$", code[0]):
        if len(code) == 0:
            print("Error1")
        else:
            # looks for assignment operator
            return assign(code)

    elif re.match("^(O RLY\?)", code[0]):
        code.pop(0)
        ifFlag = True
        if "IT" in symbolTable:
            print(symbolTable["IT"])
            ifOrElse = symbolTable["IT"]
            
        else:
            print("Error - No expression to be evaluated")
        return printArray, symbolTable, 0
