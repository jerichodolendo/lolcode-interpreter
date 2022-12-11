def evaluate(validSyntax):
    symbolTable = {}

    print(validSyntax)
    for x in validSyntax[1]:
        if (x[0] == 'I HAS A'):
            # print("Variable Declaration")
            if (type(x[1]) == tuple):
                # print("Variable Initialization")
                symbolTable[x[1][0]] = x[1][2]
            elif (type(x[1]) == str):
                # print("Variable Uninitialized")
                symbolTable[x[1]] = "NOOB"

    print("SymbolTable (keys = variables; values = value of variable):", symbolTable)
