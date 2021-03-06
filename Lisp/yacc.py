import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

# Namespace & built-in functions

name = {}
stored_vars = {}

def cons(l):
    return [l[0]] + l[1]

name['cons'] = cons

def concat(l):
    return l[0] + l[1]

name['concat'] = concat

def listar(l):
    return l

name['list'] = listar

def car(l):
    return l[0][0]

name['car'] = car

def cdr(l):
    return l[0][1:]

name['cdr'] = cdr

def eq(l):
    return l[0] == l[1]

name['eq'] = eq
name['='] = eq

def _and(l):
    return not False in l

name['and'] = _and

def _or(l):
    return True in l

name['or'] = _or

def cond(l):
    if l[0]:
        return l[1]

name['cond'] = cond

def read_vars(l):
    for idx, item in enumerate(l):
        if not isinstance(item, int):
            l[idx] = stored_vars[item]
    return l

def add(l):
    l = read_vars(l)
    return sum(l)

name['+'] = add

def minus(l):
    l = read_vars(l)
    if len(l) == 1:
        '''Unary minus'''
        return -l[0]
    elif len(l) == 2:
        return l[0] - l[1]

name['-'] = minus

def multiply(l):
    l = read_vars(l)
    return l[0] * l[1]

name['*'] = multiply

def divide(l):
    l = read_vars(l)
    if l[1] == 0:
        print("Divide by 0 error")
    else:
        return l[0] / l[1]

name['/'] = divide


def let(l):
    if len(l) > 1:
        assignment = l[0]
        for i in assignment:
            if not isinstance(i, int):
                del stored_vars[i]
        print(l[-1])
    else:
        print(l[0][1])

name['let'] = let


def bool_if(l):
    if len(l) == 3:
        exp = l[0]
        if exp:
            print l[1]
        else:
            print l[2]
    else:
        print("Invalid number of arguments")

name['if'] = bool_if


# BNF

def p_exp_atom(p):
    'exp : atom'
    p[0] = p[1]

def p_exp_qlist(p):
    'exp : quoted_list'
    p[0] = p[1]

def p_exp_call(p):
    'exp : call'
    p[0] = p[1]

def p_quoted_list(p):
    'quoted_list : QUOTE list'
    p[0] = ["quote"] + [p[2]]
    print "Quote p[0] is: ", p[0]

def p_list(p):
    'list : LPAREN items RPAREN'
    p[0] = p[2]

def p_items(p):
    'items : item items'
    p[0] = [p[1]] + p[2]

def p_items_empty(p):
    'items : empty'
    p[0] = []

def p_empty(p):
    'empty :'
    pass

def p_item_atom(p):
    'item : atom'
    p[0] = p[1]

def p_item_list(p):
    'item : list'
    p[0] = p[1]

def p_item_list(p):
    'item : quoted_list'
    p[0] = p[1]
        
def p_item_call(p):
    'item : call'
    p[0] = p[1]

def p_item_empty(p):
    'item : empty'
    p[0] = p[1]

def p_call(p):
    'call : LPAREN SIMB items RPAREN'
    if DEBUG: print "Calling", p[2], "with", p[3]
    # p[0] = lisp_eval(p[2], p[3])
    p[0] = [p[2]] + [i for i in p[3]]

def p_atom_simbol(p):
    'atom : SIMB'
    p[0] = p[1]

def p_atom_bool(p):
    'atom : bool'
    p[0] = p[1]

def p_atom_num(p):
    'atom : NUM'
    p[0] = p[1]

def p_atom_word(p):
    'atom : TEXT'
    p[0] = p[1]

def p_atom_empty(p): 
    'atom :'
    pass

def p_true(p):
    'bool : TRUE'
    p[0] = True

def p_false(p):
    'bool : FALSE'
    p[0] = False

def p_nil(p):
    'atom : NIL'
    p[0] = None


# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()


