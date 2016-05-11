import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = False

# Namespace & built-in functions

stored_vars = {}

class DivideByZeroError(Exception):
    def __init___(self):
        Exception.__init__(self,"Divide by zero error")

# BNF

def p_program(p):
    '''program : expressions
               | declaration
               | string
               | empty'''
    print "Saw: ", p[1]
    p[0] = p[1]

def p_expressions(p):
    '''expressions : expression
                 | expressions expression'''
    p[0] = p[1]

def p_expression(p):
    '''expression : operation'''
    ast = []
    ast += p[1]
    p[0] = ast

def p_operation(p):
    '''operation : addition
                 | subtraction
                 | multiplication
                 | division'''
    p[0] = p[1]

def p_addition(p):
    '''addition : INTEGER PLUS INTEGER
                | INTEGER PLUS addition'''
    p[0] = [p[2]] + [p[1], p[3]]

def p_subtraction(p):
    '''subtraction : INTEGER MINUS INTEGER
                   | INTEGER MINUS subtraction'''
    p[0] = [p[2]] + [p[1], p[3]]

def p_multiplication(p):
    '''multiplication : INTEGER MULT INTEGER
                   | INTEGER MULT multiplication'''
    p[0] = [p[2]] + [p[1], p[3]]

def p_division(p):
    '''division : INTEGER DIV INTEGER
                   | INTEGER DIV division'''
    if p[3] == 0:
        raise DivideByZeroError
    else:
        p[0] = [p[2]] + [p[1], p[3]]


def p_declaration(p):
    '''declaration : let'''
    p[0] = p[1]

def p_let(p):
    '''let : LET TEXT EQUALS INTEGER'''
    key = p[2]
    val = p[4]
    stored_vars[key] = val
    p[0] = val


def p_string(p):
    '''string : CLSTRING'''
    print("Saw string")
    print(p[1])
    # p[0] = p[1]


def p_empty(p):
    'empty : '
    pass

# Error rule for syntax errors
def p_error(p):
    if p == None:
        print("Syntax error at '%s'" % p)
    else:
        print("Syntax error at '%s'" % p.value)


# Differentiate info output with blue color
def print_blue(s):
    print "\033[0;34m{0}\033[0m".format(s)

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()


