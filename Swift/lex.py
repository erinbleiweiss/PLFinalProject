#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# Reserved words
reserved = {
    'nil'       : 'NIL',
    'IF'        : 'if',
    'ELSEIF'    : 'else if',
    'ELSE'      : 'else',
    'PRINT'     : 'print',
    'LET'       : 'let',
    'VAR'       : 'var'
}

# List of token names.
tokens = ('QUOTE', 'LPAREN', 'RPAREN', 'NIL', 'TRUE', 'FALSE', 'TEXT',
          'INTEGER', 'PLUS', 'MINUS', 'MULT', 'DIV', 'EQUALS', 'LET',
          'SQUOTE', 'CLSTRING')


         # + tuple(reserved.keys())


def t_CLFLOAT(t):
    r'[0-9]+[\.][0-9]*'
    return t

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SQUOTE = r'\''
t_QUOTE = r'\"'
t_TRUE = r'\#t'
t_FALSE = r'\#f'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_EQUALS = r'='


def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

# def t_SIMB(t):
#     r'[a-zA-Z_+=\*\-][a-zA-Z0-9_+\*\-]*'
#     t.type = reserved.get(t.value,'SIMB')    # Check for reserved words
#     return t


def t_CLSTRING(t):
    r'\"[a-zA-Z0-9_+\*\- :,\\\(\)]*\"'
    "Saw CLString"
    return t

def t_LET(t):
    r'\blet\b'
    return t

def t_TEXT(t):
    r'\b[\w-]+\b'
    print("Saw text")
    t.type = reserved.get(t.value,'TEXT')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
