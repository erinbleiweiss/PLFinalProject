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
    '''addition : operable PLUS operable
                | operable PLUS addition'''
    p[0] = [p[2]] + [p[1], p[3]]

def p_subtraction(p):
    '''subtraction : operable MINUS operable
                   | operable MINUS subtraction'''
    p[0] = [p[2]] + [p[1], p[3]]

def p_multiplication(p):
    '''multiplication : operable MULT operable
                   | operable MULT multiplication'''
    p[0] = [p[2]] + [p[1], p[3]]

def p_division(p):
    '''division : operable DIV operable
                   | operable DIV division'''
    if p[3] == 0:
        raise DivideByZeroError
    else:
        p[0] = [p[2]] + [p[1], p[3]]

def p_operable(p):
    '''operable : INTEGER
                | CLFLOAT
                | TEXT'''
    try:
        p[1] = eval(p[1])
    except Exception:
        pass

    if isinstance(p[1], int) or isinstance(p[1], float):
        p[0] = p[1]
    elif isinstance(p[1], str):
        if p[1] in stored_vars:
            p[1] = stored_vars[p[1]]
            p[0] = p[1]
        else:
            print("Error: Undefined variable '{}'".format(p[1]))
    else:
        print("Error: Invalid symbol '{}'".format(p[1]))

def p_declaration(p):
    '''declaration : let'''
    p[0] = p[1]

def p_let(p):
    '''let : LET TEXT EQUALS INTEGER
           | LET TEXT EQUALS string
           | LET TEXT EQUALS expression'''
    key = p[2]
    val = p[4]
    stored_vars[key] = val
    print("Assigning '{0}' to '{1}'".format(val, key))
    p[0] = val


def p_string(p):
    '''string : CLSTRING
              | string expression string'''
    expr_regex = r'\\\([\w\s\-\+]+\)'
    string = p[1]
    string_var = re.search(expr_regex, string)
    if string_var:
        match = string_var.group(0)
        key = match[2:-1]
        if key in stored_vars:
            string = re.sub(expr_regex, str(stored_vars[key]), string)
        else:
            idx = string_var.start()
            length = len(match)
            s1 = string[0:idx]
            s2 = string[idx+length:]
            p[0] = [s1, match, s2]
            # print("s1: {}, s2: {}".format(s1, s2))
            print("Error: Undeclared variable \"{}\"".format(key))
    p[0] = ["str", string]



def p_print(p):
    '''print : PRINT LPAREN TEXT RPAREN
             | PRINT LPAREN string RPAREN
             | PRINT LPAREN expressions RPAREN'''
    if isinstance(p[3], str) and p[3] in stored_vars:
        p[3] = stored_vars[p[3]]
    p[0] = ['print', p[3]]

def p_empty(p):
    'empty : '
    pass

# Error rule for syntax errors
def p_error(p):
    if p == None:
        print("Syntax error at '%s'" % p)
    else:
        print("Syntax error at '%s'" % p.value)




# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()


