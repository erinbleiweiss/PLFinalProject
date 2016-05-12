# PLFinalProject

**Lisp:**

Run: `mini-lisp.py`
* Python closure using exec:
  * `(exec 'from Person import Person; p1 = Person(); p1.run('name')')` --> `Bob`
  * `(exec 'from Person import Person; p1 = Person(); p1.run('set_name')('Sam'); p1.run('name')')` --> `Sam`
* Math using exec and Jython:
  * `(+ 1 (exec 'from java.lang import Math; toReturn = Math.max(23, 34)'))` --> `35`
  * `(+ 1 (exec 'import Addition; toReturn = Addition.add(23, 34)'))` --> `58`
* Java stream operations using exec:
  * `(exec 'import ListComprehension; ListComprehension.create_list(); ListComprehension.stream1();')`
  * `(exec 'import ListComprehension; ListComprehension.create_list(); ListComprehension.stream2();')`
  * `(exec 'import ListComprehension; ListComprehension.create_list(); ListComprehension.stream3();')`
  * `(exec 'import ListComprehension; ListComprehension.create_list(); ListComprehension.stream4();')`
* Python lambda functions and list comprehension:
  * `(++ '(1 2 3))` --> `[2 3 4]`
  * `(-- '(1 2 3))` --> `[0 1 2]`


**Swift:**

Run `mini-swift.py,` which reads in `testfile.c`



