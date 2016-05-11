import ply.yacc as yacc
import re

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
               | print
               | empty'''
    print "Saw: ", p[1]
    p[0] = p[1]

def p_expressions(p):
    '''expressions : expression
                 | expressions expression'''
    p[0] = p[1]

def p_expression(p):
    '''expression : operation'''
    if p[1] is str and p[1] in stored_vars:
        p[1] = stored_vars[p[1]]
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
    '''let : LET TEXT EQUALS INTEGER
           | LET TEXT EQUALS string'''
    key = p[2]
    val = p[4]
    stored_vars[key] = val
    print("Assigning '{0}' to '{1}'".format(val, key))
    # p[0] = val


def p_string(p):
    '''string : CLSTRING'''
    string = p[1]
    string_var = re.search(r'\\\([\w-]+\)', string)
    if string_var:
        match = string_var.group(0)
        key = match[2:-1]
        if key in stored_vars:
            string = re.sub(r'\\\([\w-]+\)', str(stored_vars[key]), string)
        else:
            print("Undeclared variable \"{}\"".format(key))
    p[0] = string


def p_print(p):
    '''print : PRINT LPAREN TEXT RPAREN
             | PRINT LPAREN string RPAREN
             | PRINT LPAREN expression RPAREN'''
    if isinstance(p[3], str) and p[3] in stored_vars:
        p[3] = stored_vars[p[3]]
    print_blue(p[3])
    pass

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


