import ply.lex as lex
import ply.yacc as yacc

# we just naming initial list of lexical unit 

initial=[
    "ID",
    "ADD",
    "SUB",
    "MUL",
    "DIV",
    "MOD",
    "OP_PAR",
    "CL_PAR",
    "CST",
    "AND",
    "OR",
    "NOT",
    "EQUALS",
    "LT",
    "LTE",
    "GT",
    "GTE",
    "NEQ",
    "ASSIGN",
    "OP_BRACE",
    "CL_BRACE",
    "SEM_COLON"
]

# dictionary for reserved words 

reserved={
    "int":"INT","boolean":"BOOLEAN","while":"WHILE","if":"IF","true":"TRUE","false":"FALSE"
}

# lexical units list ..initial tokens + reserved word tokens

tokens=initial + list(reserved.values())

# tokenization rules for operators and symbols

t_ADD=r"\+"  # "+" is recognized as t_ADD 
t_SUB="-"    # "-" as t_SUB 
t_MUL=r"\*"  # "*" as t_MUL
t_DIV="/"
t_MOD="%"
t_OP_PAR=r"\("
t_CL_PAR=r"\)"
t_AND="&&"
t_OR=r"\|\|"
t_NOT="!"
t_EQUALS="=="
t_LT="<"
t_LTE="<="
t_GT=">"
t_GTE=">="
t_NEQ="!="
t_ASSIGN="="
t_OP_BRACE=r"\{"
t_CL_BRACE=r"\}"
t_SEM_COLON=";"

# simply we want to recognize and categorize different parts fo the code like names or id's

def t_ID(t): #name we just gave ...
    r"[a-zA-Z_]\w*" #pattern that looks for sequences of characters that form and identifier
                    #we check if name starts with a letter or an underscore(_) and if it's followed by letters or digitsor...
                    
# again when we find a name in the code we want to know if it's a special word that has a reserved meaning like "if" or "while" or if it's just a regular 
    t.type = reserved.get(t.value, "ID") #checking if the name is in our list of reserved words
                                         #if so we use the type assigned to that word else we use ID to indicate it's a regular 
    return t


# recognizing whole numbers integer & constants inside the code
def t_CST(t):
    r"(?P<CST>[1-9][0-9]*)" #pattern that looks for sequences of digits in the code (numbers)
    t.value = int(t.lexer.lexmatch.group("CST")) # When we find a number we save it as t.value so we can use it and work with it
    return t

# Ignoring spaces, tabs, and newlines also non-word characters like !, @, #, $, % (PLEASE NOTE SOME PYTHON VERSIONS) will see "\" as an unknown character
# so we can also use ###t_ignore  = " \t\n\r" 
t_ignore  = r'[^\w]' 


# hANDLING Erros
def t_error(t):
    message = f"Character Error {t.value[0]}" # Error Message
    print(message)
    t.lexer.skip(1)  # skip the incorrect character if found

# lexer instance
lexer = lex.lex()

# Open and read the content from "code.java" 
with open("code.java") as f:
    text = f.read()

# Input the code into the lexer
lexer.input(text)

# Use a for loop and list comprehension to print the tokens (print each token on a separate line)
tokens = list(iter(lexer.token, None))
print(*tokens, sep='\n')
