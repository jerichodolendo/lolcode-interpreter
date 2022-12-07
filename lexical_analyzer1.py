# Python Regex from https://www.w3schools.com/python/python_regex.asp

import re
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
# from tkinter.messagebox import showinfo


def execute():
    lines = []
    code = text.get("1.0", "end-1c")
    temp = code.split(" " and "\n")
    for tempLine in temp:
        x = tempLine.strip()
        lines.append(x)

    print(lines)

    for line in lines:
        if (line == ""):
            continue

        temp = line.split(" ")
        analyze_tokens(temp)


def openFile():
    file = fd.askopenfilename(
        title='Open files',
        initialdir='/')
    file = open(file, "r")
    data = file.read()

    text.insert('1.0', data)
    file.close()


root = Tk()
root.title('mema peepz interpreter xd')
root.resizable(False, False)
root.geometry('1430x700')

# selecting and reading files: https://pythonguides.com/python-tkinter-read-text-file/
# scrollbars: https://stackoverflow.com/questions/42006805/python-scrolledtext-module

# input box for code
inpContainer = Frame(root, borderwidth=1, relief="sunken")
text = Text(inpContainer, height=18, width=50, wrap=NONE)
scrollX = Scrollbar(inpContainer, orient='horizontal', command=text.xview)
scrollY = Scrollbar(inpContainer, orient='vertical', command=text.yview)
text.configure(xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)

text.grid(row=0, column=0, sticky='nsew')
scrollX.grid(row=1, column=0, sticky='ew')
scrollY.grid(row=0, column=1, sticky='ns')

inpContainer.grid_rowconfigure(0, weight=1)
inpContainer.grid_columnconfigure(0, weight=1)

inpContainer.grid(row=1, column=0, sticky='nsew', padx=15)

# treeview for table: https://www.pythontutorial.net/tkinter/tkinter-treeview/#:~:text=Introduction%20to%20the%20Tkinter%20Treeview,has%20one%20or%20more%20columns.

# tabular view for lexemes
lexVar = StringVar()
lexLbl = Label(root, textvariable=lexVar)

lexVar.set("Lexemes")

lexContainer = Frame(root, borderwidth=1, relief="sunken")
lexCols = ('lexemes', 'class')
lexTbl = ttk.Treeview(lexContainer, columns=lexCols, show="headings")
lexTbl.heading('lexemes', text='Lexemes')
lexTbl.heading('class', text='Classification')
lexScrollX = Scrollbar(lexContainer, orient='horizontal', command=lexTbl.xview)
lexScrollY = Scrollbar(lexContainer, orient='vertical', command=lexTbl.yview)
lexTbl.configure(xscrollcommand=lexScrollX.set, yscrollcommand=lexScrollY.set)

lexTbl.grid(row=0, column=0, sticky='nsew')
lexScrollX.grid(row=1, column=0, sticky='ew')
lexScrollY.grid(row=0, column=1, sticky='ns')

lexContainer.grid_rowconfigure(0, weight=1)
lexContainer.grid_columnconfigure(0, weight=1)

lexLbl.grid(row=0, column=1, padx=15)
lexContainer.grid(row=1, column=1, sticky='nsew', padx=15)

# tabular view for symbols (symbol table)
symbVar = StringVar()
symbLbl = Label(root, textvariable=symbVar)

symbVar.set("Symbol Table")

symbContainer = Frame(root, borderwidth=1, relief="sunken")
symbCols = ('ident', 'val')
symbTbl = ttk.Treeview(symbContainer, columns=symbCols, show="headings")
symbTbl.heading('ident', text='Identifier')
symbTbl.heading('val', text='Value')
symbScrollX = Scrollbar(
    symbContainer, orient='horizontal', command=symbTbl.xview)
symbScrollY = Scrollbar(
    symbContainer, orient='vertical', command=symbTbl.yview)

symbTbl.configure(xscrollcommand=symbScrollX.set,
                  yscrollcommand=symbScrollY.set)
symbTbl.grid(row=0, column=0, sticky='nsew')
symbScrollX.grid(row=1, column=0, sticky='ew')
symbScrollY.grid(row=0, column=1, sticky='ns')

symbContainer.grid_rowconfigure(0, weight=1)
symbContainer.grid_columnconfigure(0, weight=1)

symbLbl.grid(row=0, column=2, padx=15)
symbContainer.grid(row=1, column=2, sticky='nsew', padx=15)

# execute button
outputFrm = Frame(root, borderwidth=1)
execBttn = Button(outputFrm, text='Execute', width=180, command=execute)
execBttn.pack()

outputFrm.grid_rowconfigure(0, weight=1)
outputFrm.grid_columnconfigure(0, weight=1)
outputFrm.grid(row=3, columnspan=3, padx=15, pady=15)

# console
console = Text(outputFrm, height=17, width=170)
console.pack(pady=10)

openFileBttn = Button(
    root,
    text='Open Files',
    command=openFile,
    width=70
)

openFileBttn.grid(column=0, row=0, sticky='w', padx=15, pady=10)


# regex for lexemes
keywords = "^(R)$|^(ANY OF)$|^(ALL OF)$|^(BOTH SAEM)$|^(DIFFRINT)$|^(SMOOSH)$|^(MAEK)$|^(A)$|^(IS NOW A)$|^(VISIBLE)$|^(GIMMEH)$|^(O RLY\?)$|^(YA RLY)$|^(MEBBE)$|^(NO WAI)$|^(OIC)$|^(WTF\?)$|^(OMG)$|^(OMGWTF)$|^(IM IN YR)$|^(UPPIN)$|^(NERFIN)$|^(YR)$|^(TIL)$|^(WILE)$|^(IM OUTTA YR)$|^(NUMBR)$|^(NUMBAR)$|^(YARN)$|^(TROOF)$"
not_operator = "^(NOT)$"
xor_operator = "^(WON OF)$"
and_operator = "^(BOTH OF)$"
or_operator = "^(EITHER OF)$"
plus = "^(SUM OF)$"
difference = "^(DIFF OF)$"
multiply = "^(PRODUKT OF)$"
divide = "^(QUOSHUNT OF)$"
modulo = "^(MOD OF)$"
max = "^(BIGGR OF)$"
minimum = "^(SMALLR OF)$"
declaration = "^(I HAS A)$"
assignment = "^(ITZ)$"
start = "^(HAI)$"
end = "^(KTHXBYE)$"
single_line = "^(BTW)$"
multiple_start = "^(OBTW)$"
multiple_end = "^(TLDR)$"
NUMBR = "^(-?[0-9]+)$"
NUMBAR = "^(-?[0-9]+\.?[0-9]+)$"
YARN = "^(\".*\")$"
TROOF = "^(WIN)$|^(FAIL)$"
variable = "^[A-Za-z][A-Za-z0-9_]*$"
function = "^[A-Za-z][A-Za-z0-9_]*$"
loop = "^[A-Za-z][A-Za-z0-9_]*$"

# function that checks if a token has any regex matches
def identifier(tokens):
    j = 0

    if (type(tokens) == str):
        tokens = tokens.strip()

        if (re.search(declaration, tokens)):
            print(tokens, "\t == Variable declaration")   
        elif (re.search(plus, tokens)):
            print(tokens, "\t == Addition operator")   
        elif (re.search(difference, tokens)):
            print(tokens, "\t == Subtraction operator")   
        elif (re.search(multiply, tokens)):
            print(tokens, "\t == Multiplication operator")   
        elif (re.search(divide, tokens)):
            print(tokens, "\t == Division operator")
        elif (re.search(modulo, tokens)):
            print(tokens, "\t == Modulo operator")
        elif (re.search(max, tokens)):
            print(tokens, "\t == Max operator")    
        elif (re.search(minimum, tokens)):
            print(tokens, "\t == Minimum operator")
        elif (re.search(or_operator, tokens)):
            print(tokens, "\t == OR operator")
        elif (re.search(and_operator, tokens)):
            print(tokens, "\t == AND operator")  
        elif (re.search(xor_operator, tokens)):
            print(tokens, "\t == XOR operator")     

        return(tokens)

    elif (type(tokens) == list):
        if (re.search(start, tokens[j])):
            print(tokens[j], "\t == PROGRAM START")
        elif (re.search(end, tokens[j])):
            print(tokens[j], "\t == PROGRAM END")
        elif (re.search(not_operator, tokens[j])):
            print(tokens[j], "\t == NOT operator")
        elif (re.search(assignment, tokens[j])):
            print(tokens[j], "\t == Assignment operator")        
        elif (re.search(single_line, tokens[j])):
            print(tokens[j], "\t == Single line comment")
        elif (re.search(multiple_start, tokens[j])):
            print(tokens[j], "\t == Multiple line comment starts")
        elif (re.search(multiple_end, tokens[j])):
            print(tokens[j], "\t == Multiple line comment ends")
        elif (re.search(keywords, tokens[j])):
            print(tokens[j], "\t == Keyword")
        elif (re.search(NUMBR, tokens[j])):
            print(tokens[j], "\t == NUMBR")
        elif (re.search(NUMBAR, tokens[j])):
            print(tokens[j], "\t == NUMBAR")
        elif (re.search(YARN, tokens[j])):
            print(tokens[j], "\t == YARN")
        elif (re.search(TROOF, tokens[j])):
            print(tokens[j], "\t == TROOF")
        elif (re.search(variable, tokens[j])):
            print(tokens[j], "\t == variable")
        elif (re.search(function, tokens[j])):
            print(tokens[j], "\t == function")
        elif (re.search(loop, tokens[j])):
            print(tokens[j], "\t == loop")
        else:
            print(tokens[j], "\t == Unknown")

        tokens.pop(0)
        return (tokens)

    # for j in list:
    #     print(list)


# function that checks content of tokens
def analyze_tokens(tokens):
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
                identifier(fin)

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
                identifier(fin)

                
                

                # resets temporary variables
                s = ""
                fin = ""

            # checks if a token has any regex matches other than being a keyword
            elif (tokensCop[i] == ""):
                continue
            else:
                tokensCop = identifier(tokensCop)
                # sets i to 1 to break the while loop
        except Exception as e:
            print(repr(e))
            print("Lexical Error")
            break


# print("\n--LEXICAL ANALYZER FOR LOL CODE--")
# print("\t[1] INPUT A LINE OF CODE")
# print("\t[2] READ A FILE\n")
# choice = int(input("Enter choice: "))

# if choice == 1:
#     while True:
#         userInp = input("Enter line: ")
#         if (userInp == "exit"):
#             break

#         tokens = userInp.split(" ")

#         analyze_tokens(tokens)


# elif choice == 2:
#     # read the file
#     file = open('input.lol', 'r')
#     data = file.read().rstrip()
#     # retrieved from https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
#     data = "".join([l.replace("\n", " ") for l in data])  # new lines
#     data = " ".join(data.split())  # remove extra spaces

#     tokens = data.split(" ")

#     analyze_tokens(tokens)

# else:
#     print("Wrong input!")

root.mainloop()
