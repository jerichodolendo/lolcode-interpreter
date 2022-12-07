import re
from copy import deepcopy

flag = 0
comment = ""

class Lexer(object):
    def __init__(self, sourceCode):
        self.sourceCode = sourceCode

    def tokenize(self):
        global comment
        global flag
        tokens = []

        # word list of the file contents    
        #sourceCode = self.sourceCode.split("\n")
        fileContent = self.sourceCode

        # create matching regex to tokenize the words
        # matches all lolcode reserved keywords
        keywords = re.compile("HAI|KTHXBYE|BTW|OBTW|TLDR|I HAS A|ITZ|SUM OF|DIFF OF|PRODUKT OF|QUOSHUNT OF|MOD OF|BIGGR OF|SMALLR OF|BOTH OF|EITHER OF|WON OF|NOT|ANY OF|BOTH SAEM|DIFFRINT|SMOOSH|MAEK|IS NOW A|VISIBLE|GIMMEH|O RLY?|YA RLY|MEBBE|NO WAI|OIC|WTF?|OMG|OMGWTF|IM IN YR|UPPIN|NERFIN|YR|TIL|WILE|IM OUTTA YR|HOW IZ I|IF U SAY SO|IT")
        # matches all numbers including negative values and floating point values
        numbers = re.compile("-?(?:\d+?)+")
        # matches all values enclosed in double quotes
        strings = re.compile(r'\"(.+?)\"')
        # matches all other values 
        nonKeywordIdentfiers = re.compile("[a-z][A-z_0-9]*|WIN|FAIL|NUMBR|NUMBAR|YARN|TROOF|\\n")

        # keeps track of the current line number of the input file
        keywords = re.compile(r'^HAI.*|^KTHXBYE.*|^BTW.*|^OBTW.*|^TLDR.*|^I HAS A.*|^ITZ.*|^R.*|^SUM OF.*|^DIFF OF.*|^PRODUKT OF.*|^QUOSHUNT OF.*|^MOD OF.*|^BIGGR OF.*|^SMALLR OF.*|^BOTH OF.*|^EITHER OF.*|^WON OF.*|^NOT.*|^ANY OF.*|^ALL OF.*|^BOTH SAEM.*|^DIFFRINT.*|^SMOOSH.*|^MAEK.*|^A .*|^IS NOW A.*|^VISIBLE.*|^GIMMEH.*|^O RLY\?.*|^YA RLY.*|^MEBBE.*|^NO WAI.*|^OIC.*|^WTF\?.*|^OMG.*|^OMGWTF.*|^IM IN YR.*|^UPPIN.*|^NERFIN.*|^YR.*|^TIL.*|^WILE.*|^IM OUTTA YR.*|^IT.*')
        keywords2 = re.compile(r'^HAI( |\n)|^KTHXBYE( |\n)|^BTW( |\n)|^OBTW( |\n)|^TLDR( |\n)|^I HAS A( |\n)|^ITZ( |\n)|^R( |\n)|^SUM OF( |\n)|^DIFF OF( |\n)|^PRODUKT OF( |\n)|^QUOSHUNT OF( |\n)|^MOD OF( |\n)|^BIGGR OF( |\n)|^SMALLR OF( |\n)|^BOTH OF( |\n)|^EITHER OF( |\n)|^WON OF( |\n)|^NOT( |\n)|^ANY OF( |\n)|^ALL OF( |\n)|^BOTH SAEM( |\n)|^DIFFRINT( |\n)|^SMOOSH( |\n)|^MAEK( |\n)|^A( |\n)|^IS NOW A( |\n)|^VISIBLE( |\n)|^GIMMEH( |\n)|^O RLY\?( |\n)|^YA RLY( |\n)|^MEBBE( |\n)|^NO WAI( |\n)|^OIC( |\n)|^WTF\?( |\n)|^OMG( |\n)|^OMGWTF( |\n)|^IM IN YR( |\n)|^UPPIN( |\n)|^NERFIN( |\n)|^YR( |\n)|^TIL( |\n)|^WILE( |\n)|^IM OUTTA YR( |\n)|^IT( |\n)')
        # matches all numbers including negative values and floating point values
        numbers = re.compile(r"^[-]?\d*[.]?\d+.*")
        numbers2 = re.compile(r"^[-]?\d*[.]?\d+( |\n)")
        # matches all values enclosed in double quotes
        strings = re.compile(r'^\"(.+?)\".*')
        strings2 = re.compile(r'^\"(.+?)\"( |\n)')
        # matches all other values 
        nonKeywordIdentfiers = re.compile(r"^[a-z][A-z_0-9]*.*|WIN|FAIL|NUMBR|NUMBAR|YARN|TROOF|AN")
        nonKeywordIdentfiers2 = re.compile(r"^[a-z][A-z_0-9]*( |\n)|^WIN( |\n)|^FAIL( |\n)|^NUMBR( |\n)|^NUMBAR( |\n)|^YARN( |\n)|^TROOF( |\n)|^AN( |\n)")

        #print(fileContent)

        #OBTW filter

        OBTWs = []
        OBTWflag = 0
        newArray = []

        for i in fileContent:
            i = re.sub(r'^ *', '', i)
            if i == "OBTW\n" or re.match(r"^OBTW.*", i):
                OBTWs.append(i)
                OBTWflag = 1
            elif i == "TLDR\n" or re.match(r".*TLDR$", i):
                OBTWs.append(i)
                OBTWflag = 0
                OBTWs = []
            elif OBTWflag == 1:
                OBTWs.append(i)
            else:
                newArray.append(i)

        #print(newArray)

        #BTW filter

        partitionedCode = []

        for i in newArray:
            if type(i) == list:
                partitionedCode.append(i)
                continue

            if re.match(r"^BTW.*", i):
                pass
            elif re.match(r".*BTW.*", i):
                i = re.sub(r' BTW.*', '', i)
                partitionedCode.append(i)
            else:
                partitionedCode.append(i)

        #print(*partitionedCode)

        # remove newlines

        for i in range(len(partitionedCode)):
            try:
                if partitionedCode[i] == '\n':
                    partitionedCode.pop(i)
            except IndexError:
                break # means tapos na nabura na lahat

        #partition based on keywords
        forSyntax = []
        lexicalErrorFlag = 0
        line = 0
        for i in partitionedCode:
            codeBeingEvaluated = deepcopy(i)
            line += 1
            lineOfCode = []
            while i != "":
                if re.match(keywords, i):
                    match = re.match(keywords2, i)
                    lineOfCode.append(match.group(0))
                    i = re.sub(keywords2, '', i)
                    continue
                
                if re.match(numbers, i):
                    match = re.match(numbers2, i)
                    lineOfCode.append(match.group(0))
                    i = re.sub(numbers2, '', i)
                    continue

                if re.match(strings, i):
                    match = re.match(strings2, i)
                    lineOfCode.append(match.group(0))
                    i = re.sub(strings2, '', i)
                    continue

                if re.match(nonKeywordIdentfiers, i):
                    match = re.match(nonKeywordIdentfiers2, i)
                    lineOfCode.append(match.group(0))
                    i = re.sub(nonKeywordIdentfiers2, '', i)
                    continue

                if re.match(r'\n', i):
                    break

                if re.match(r'.+( |\n)', i): # case for catching unknown keywords
                    lexicalErrorFlag = 1
                    return [], lexicalErrorFlag, codeBeingEvaluated

            forSyntax.append(lineOfCode)
        
        # clean by removing trailing spaces and newlines
        cleanedForSyntax = []
        for i in forSyntax:
            lineOfCode = []
            for j in i:
                if (re.match(r".+ ", j)):
                    lineOfCode.append(j[:len(j)-1])
                elif (re.match(r".+\n", j)):
                    lineOfCode.append(j[:len(j)-1])
                else:
                    lineOfCode.append(j)
            if lineOfCode == []:
                pass
            else:
                cleanedForSyntax.append(lineOfCode)

        print(cleanedForSyntax)

        for lineOfCode in cleanedForSyntax:
            for word in lineOfCode:
                # LITERALS matching
                if re.match("-?[1-9]+[0-9]*\.[0-9]*([1-9]|0)", word):
                    tokens.append(["NUMBAR Literal", word])
                elif re.match("(-?[1-9]+[0-9]*|^0$)", word):
                    tokens.append(["NUMBR Literal", word])
                elif re.match("\"(.+?)\"", word):
                    tokens.append(["YARN Literal", word])
                elif re.match("^(WIN)$|^(FAIL)$", word):
                    tokens.append(["TROOF Literal", word])
                elif re.match("^(NUMBR)$|^(NUMBAR)$|^(YARN)$|^(TROOF)$", word):
                    tokens.append(["TYPE Literal", word])
                # KEYWORDS matching^(WIN)$|^(FAIL)$
                elif re.match("^(HAI)$", word):
                    tokens.append(["PROGRAM START", word])
                elif re.match("^(KTHXBYE)$", word):
                    tokens.append(["PROGRAM END", word])
                elif re.match("^(OBTW|TLDR)$", word):
                    tokens.append(["Multi Line Comment", word])
                    flag = 2
                elif re.match("^(I HAS A|ITZ)$", word):
                    tokens.append(["Variable Declaration", word])
                elif re.match("R", word):
                    tokens.append(["Assignment operator", word])
                # ARITHMETIC operations
                elif re.match("^(SUM OF)$", word):
                    tokens.append(["Addition operation", word])
                elif re.match("^(DIFF OF)$", word):
                    tokens.append(["Subtraction operation", word])
                elif re.match("^(PRODUKT OF)$", word):
                    tokens.append(["Multiplication operation", word])
                elif re.match("^(QUOSHUNT OF)$", word):
                    tokens.append(["Division operation", word])
                elif re.match("^(MOD OF)$", word):
                    tokens.append(["Modulo operation", word])
                elif re.match("^(BIGGR OF)$", word):
                    tokens.append(["Greater than operation", word])
                elif re.match("^(SMALLR OF)$", word):
                    tokens.append(["Less than operation", word])
                elif re.match("^AN$", word):
                    tokens.append(["Operand Separator", word])
                # BOOLEAN operations
                elif re.match("^(BOTH OF)$", word):
                    tokens.append(["And operation", word])
                elif re.match("^(EITHER OF)$", word):
                    tokens.append(["Or operation", word])
                elif re.match("^(WON OF)$", word):
                    tokens.append(["Xor operation", word])
                elif re.match("^(NOT)$", word):
                    tokens.append(["not operation", word])
                elif re.match("^(ANY OF)$", word):
                    tokens.append(["Infinite Arity Or", word])
                elif re.match("^(ALL OF)$", word):
                    tokens.append(["Infinite Arity And", word])
                # COMPARISON operations
                elif re.match("^(BOTH SAEM)$", word):
                    tokens.append(["Equal operation", word])
                elif re.match("^(DIFFRINT)$", word):
                    tokens.append(["Not equal operation", word])
                elif re.match("^(SMOOSH)$", word):
                    tokens.append(["Concatenation operation", word])
                elif re.match("^(MAEK|IS NOW A)$", word):
                    tokens.append(["Cast operation", word])
                # elif re.match("A", word):
                    # tokens.append(["Value operation", word])
                elif re.match("^(VISIBLE)$", word):
                    tokens.append(["Print Statement", word])
                elif re.match("^(GIMMEH)$", word):
                    tokens.append(["Read input stream", word])
                elif re.match("^(O RLY?|OIC)$", word):
                    tokens.append(["If statement keyword", word])
                elif re.match("^(YA RLY)$", word):
                    tokens.append(["True if statement", word])
                elif re.match("^(NO WAI)$", word):
                    tokens.append(["False if statement", word])
                elif re.match("^(WTF?|OIC)$", word):
                    tokens.append(["Switch Case keyword", word])
                elif re.match("^(OMG)$", word):
                    tokens.append(["Switch value keyword", word])
                elif re.match("^(OMGWTF)$", word):
                    tokens.append(["Switch default keyword", word])
                elif re.match("^(GTFO)$", word):
                    tokens.append(["Break keyword", word])
                elif re.match("^(UPPIN)$", word):
                    tokens.append(["Increment keyword", word])
                elif re.match("^(NERFIN)$", word):
                    tokens.append(["Decrement keyword", word])
                elif re.match("^(FOUND YR)$", word):
                    tokens.append(["Return keyword", word])
                elif re.match("^(TIL)$", word):
                    tokens.append(["Loop condition keyword", word])
                elif re.match("^(WILE)$", word):
                    tokens.append(["", word])
                # IDENTIFIERS matching
                elif re.match("^(HOW IZ I|IF U SAY SO)$", word):
                    tokens.append(["Function Identifier", word])
                elif re.match("^(IM IN YR|IM OUTTA YR)$", word):
                    tokens.append(["Loop Identifier", word])
                elif re.match("^([a-z][A-z_0-9]*)$", word):
                    tokens.append(["Variable Identifier", word])
                elif re.match("^IT$", word):
                    tokens.append(["Implicit Variable Identifier", word])

        return tokens, 0, "", cleanedForSyntax