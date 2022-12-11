# Python Regex from https://www.w3schools.com/python/python_regex.asp

import re
from lexical_analyzer import *
from syntax_analyzer import *
from semantic_analyzer import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText
# from tkinter.messagebox import showinfo


def clear_all():
    for item in lexTbl.get_children():
        lexTbl.delete(item)


def execute():
    clear_all()
    tokenList = []  # includes all tokens in input
    lexemeTups = []  # contains tuples of lexemes with their classifications, for inserting to lexeme table
    code = text.get("1.0", "end-1c")    # get input from text box
    lineRgx = r"\"?.+\??\"?\n?"  # regex for getting line
    result = re.findall(lineRgx, code)  # returns list containing lines

    for line in result:
        analyze_tokens(lexemeTups, line)

    # after all analysis, we have lexeme tuples
    # insert them to Treeview
    for item in lexemeTups:
        lexTbl.insert("", "end", values=item)

    for x in range(len(lexemeTups)):
        print(f"lexeme: {lexemeTups[x][0]}\tclass: {lexemeTups[x][1]}")

    validSyntax = program(lexemeTups)

    evaluate(validSyntax)


def openFile():
    file = fd.askopenfilename(
        title='Open files',
        initialdir='/')
    file = open(file, "r")
    data = file.read()

    text.delete('1.0', 'end')
    text.insert('1.0', data)
    file.close()


root = Tk()
root.title('mema peepz interpreter xd')
root.resizable(False, False)
root.geometry('1430x700')


# selecting and reading files: https://pythonguides.com/python-tkinter-read-text-file/
# scrollbars: https://stackoverflow.com/questions/42006805/python-scrolledtext-module

openFileBttn = Button(
    root,
    text='Open Files',
    command=openFile,
    width=70
)

openFileBttn.grid(column=0, row=0, sticky='w', padx=15, pady=10)

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

root.mainloop()
