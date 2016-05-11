# PLFinalProject

**Lisp:**

Run: `mini-lisp.py`
* Math using exec and Jython:
  * `(+ 1 (exec 'from java.lang import Math; toReturn = Math.max(23, 34)'))` --> `35`
  * `(+ 1 (exec 'import Addition; toReturn = Addition.add(23, 34)'))` --> `58`
* Python closure using exec:
  * `(exec 'from Person import Person; p1 = Person(); p1.run('name')')` --> `Bob`
* Python lambda functions and list comprehension:
  * `(++ '(1 2 3))` --> `[2 3 4]`
  * `(-- '(1 2 3))` --> `[0 1 2]`


**Swift:**





