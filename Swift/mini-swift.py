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
            print r


        # print("")
        # result = yacc.parse(line)
        # if result is None:
        #     chunk += line
        #     if len(chunk) > 0:
        #         print("chunk: {}".format(chunk))
        #         chunk_res = yacc.parse(chunk)
        #         if chunk_res is not None:
        #             print("AST is {}".format(chunk_res))
        #             r = swift.eval(chunk_res)
        #             if r is not None:
        #                 print r
        #                 chunk = ""
        # else:
        #     print("AST is {}".format(result))
        #     r = swift.eval(result)
        #     if r is not None:
        #         print r
