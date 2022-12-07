# Python Regex from https://www.w3schools.com/python/python_regex.asp

import re
import nltk

# regex for lexemes
keywords = "^(HAI)$|^(KTHXBYE)$|^(BTW)$|^(OBTW)$|^(TLDR)$|^(I HAS A)$|^(ITZ)$|^(R)$|^(SUM OF)$|^(DIFF OF)$|^(PRODUKT OF)$|^(QUOSHUNT OF)$|^(MOD OF)$|^(BIGGR OF)$|^(SMALLR OF)$|^(BOTH OF)$|^(EITHER OF)$|^(WON OF)$|^(NOT)$|^(ANY OF)$|^(ALL OF)$|^(BOTH SAEM)$|^(DIFFRINT)$|^(SMOOSH)$|^(MAEK)$|^(A)$|^(IS NOW A)$|^(VISIBLE)$|^(GIMMEH)$|^(O RLY\?)$|^(YA RLY)$|^(MEBBE)$|^(NO WAI)$|^(OIC)$|^(WTF\?)$|^(OMG)$|^(OMGWTF)$|^(IM IN YR)$|^(UPPIN)$|^(NERFIN)$|^(YR)$|^(TIL)$|^(WILE)$|^(IM OUTTA YR)$|^(NUMBR)$|^(NUMBAR)$|^(YARN)$|^(TROOF)$|^(AN)$"
NUMBR = "^(-?[0-9]+)$"
NUMBAR = "^(-?[0-9]+\.?[0-9]+)$"
YARN = "^(\".*\")$"
TROOF = "^(WIN)$|^(FAIL)$"
variable = "^[A-Za-z][A-Za-z0-9_]*$"
function = "^[A-Za-z][A-Za-z0-9_]*$"
loop = "^[A-Za-z][A-Za-z0-9_]*$"

# function that checks if a token has any regex matches
def identifier(list):
    for j in list:
        if (re.search(keywords, j)):
            print(j, "\t == keyword")
        elif (re.search(NUMBR, j)):
            print(j, "\t == NUMBR")
        elif (re.search(NUMBAR, j)):
            print(j, "\t == NUMBAR")
        elif (re.search(YARN, j)):
            print(j, "\t == YARN")
        elif (re.search(TROOF, j)):
            print(j, "\t == TROOF")
        elif (re.search(variable, j)):
            print(j, "\t == variable")
        elif (re.search(function, j)):
            print(j, "\t == function")
        elif (re.search(loop, j)):
            print(j, "\t == loop")
        else:
            print("Unknown")

# function that checks content of tokens


def analyze_tokens(tokens):
    # temporary variable initializations
    s = ""
    fin = ""
    i = 0

    # while loop that exhausts list of tokens
    while (i == 0):
        try:
            # checks for the first detected token
            if (tokens != [] and (tokens[i] == "I" or
                tokens[i] == "SUM" or
                tokens[i] == "DIFF" or
                tokens[i] == "PRODUKT" or
                tokens[i] == "QUOSHUNT" or
                tokens[i] == "MOD" or
                tokens[i] == "BIGGR" or
                tokens[i] == "SMALLR" or
                tokens[i] == "BOTH" or
                tokens[i] == "EITHER" or
                tokens[i] == "WON" or
                tokens[i] == "ANY" or
                tokens[i] == "ALL" or
                tokens[i] == "BOTH" or
                tokens[i] == "IS" or
                tokens[i] == "O" or
                tokens[i] == "YA" or
                tokens[i] == "NO" or
                    tokens[i] == "IM")):
                # if found, concatenate to s and pop the token
                # while loop continues to exhaust the list
                s = s + tokens[i]
                tokens.pop(0)

            # if s has a partial keyword, proceeds to examine the tokens
            elif (s == "SUM" and tokens[i] == "OF" or
                  s == "DIFF" and tokens[i] == "OF" or
                  s == "PRODUKT" and tokens[i] == "OF" or
                  s == "QUOSHUNT" and tokens[i] == "OF" or
                  s == "MOD" and tokens[i] == "OF" or
                  s == "BIGGR" and tokens[i] == "OF" or
                  s == "SMALLR" and tokens[i] == "OF" or
                  s == "BOTH" and tokens[i] == "OF" or
                  s == "EITHER" and tokens[i] == "OF" or
                  s == "WON" and tokens[i] == "OF" or
                  s == "ANY" and tokens[i] == "OF" or
                  s == "ALL" and tokens[i] == "OF" or
                  s == "BOTH" and tokens[i] == "SAEM" or
                  s == "O" and tokens[i] == "RLY?" or
                  s == "YA" and tokens[i] == "RLY" or
                  s == "NO" and tokens[i] == "WAI"):

                # if found, concatenate to s and pop the token
                s = s + " " + tokens[i]
                tokens.pop(0)

                # at this point, it is sufficient to examine for any keyword regex matches
                # calls re.search function to search final string of any matches
                fin = s
                if (re.search(keywords, fin)):
                    print(fin, "== keyword")

                # resets temporary variables
                # while loop continues
                s = ""
                fin = ""

            # if there are still tokens, proceed to exhaust the list and examine
            elif (s == "I" and tokens[i] == "HAS" or
                  s == "IS" and tokens[i] == "NOW" or
                  s == "IM" and tokens[i] == "IN" or
                  s == "IM" and tokens[i] == "OUTTA"):

                # if found, concatenate to s and pop the token
                # while loop continues
                s = s + " " + tokens[i]
                tokens.pop(0)

            # checks if current string has partial identifiers, then proceeds to examine next token
            elif (s == "I HAS" and tokens[i] == "A" or
                  s == "IS NOW" and tokens[i] == "A" or
                  s == "IM IN" and tokens[i] == "YR" or
                  s == "IM OUTTA" and tokens[i] == "YR"):

                # if found, concatenate to s and pop the token
                s = s + " " + tokens[i]
                tokens.pop(0)
                fin = s

                # at this point again, enough to search for any keyword regex matches
                if (re.search(keywords, fin)):
                    print(fin, "== keyword")

                # resets temporary variables
                s = ""
                fin = ""

            # checks if a token has any regex matches other than being a keyword
            else:
                identifier(tokens)
                # sets i to 1 to break the while loop
                i = 1
        except:
            print("Lexical Error")
            break


print("\n--LEXICAL ANALYZER FOR LOL CODE--")
print("\t[1] INPUT A LINE OF CODE")
print("\t[2] READ A FILE\n")
choice = int(input("Enter choice: "))

if choice == 1:
    while True:
        userInp = input("Enter line: ")
        if (userInp == "exit"):
            break

        tokens = nltk.word_tokenize(userInp)

        analyze_tokens(tokens)


elif choice == 2:
    # read the file
    file = open('input.lol', 'r')
    data = file.read().rstrip()
    # retrieved from https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
    data = "".join([l.replace("\n", " ") for l in data])  # new lines
    data = " ".join(data.split())  # remove extra spaces

    tokens = nltk.word_tokenize(data)

    analyze_tokens(tokens)

else:
    print("Wrong input!")
