# -*- coding: utf-8 -*-
from yacc import yacc
import swift


with open('testfile.c', 'r') as content_file:
    chunk = ""
    for line in content_file:
        print("")
        result = yacc.parse(line)
        print("AST is {}".format(result))
        r = swift.eval(result)
        if r is not None:
            print "Result is {}".format(r)

