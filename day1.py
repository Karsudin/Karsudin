""" 
Python Keywords = False, None, True, and, as, assert, async,
await, break, class, continue, def, del, elif, 
else, except, finally, for, from, global, if,
import, in, is, lambda, nonlocal, not, or,
pass, raise, return, try, while, with, yield
"""

""" 
Python Identifiers
1. Identifiers can be a combination of letters in lowercase
	(a to z) or uppercase (A to Z) or digits (0 to 9) or an
	underscore (_). Names like (myClass), var_1 and
	(print_this_to_screen), all are valid example.

2. An identifier cannot start with a digit. (1variable) is 
	invalid, but (variable1) is a valid name.

3. Keywords cannot be used as identifiers.
	Example :

		global = 1

	Output will be :

			File "<interactive input>", line 1
    		global = 1
           ^
		SyntaxError: invalid syntax

4. We cannot use special symbols like !, @, #, $, % etc. in
	our identifier.
	Example :

		a@ = 0

	Output will be :

			File "<interactive input>", line 1
    		a@ = 0
           ^
		SyntaxError: invalid syntax

5. An identifier can be of any length.
"""

"""
Things to Remember

Python is a case-sensitive language. This means,
(Variable) and (variable) are not the same. And
always give the identifiers a name that make sense.
"""