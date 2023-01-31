###################################
Common Computer Science terms in L4
###################################

This section gives examples of how common terms in computer science are used in L4.

Note that boldface and italicization does not matter to L4.

-------------------------------------------------------
Simple Terms, Parties and Entities, and the AKA Keyword
-------------------------------------------------------

--------------------
Arrays AKA MultiTerm
--------------------

.. code-block:: bnf

    Arrays	AKA	MultiTerm						
											
	One or more cells on a single line:			Foo	Bar	Baz
	The cells can contain strings or numbers:		1	2	3
	Single cells are fine:			                Quux		

--------------------------------
Dictionaries AKA Parametric Text
--------------------------------

One or more lines of arrays.
Typically used to give detail to actions.
Multiple indentation styles are supported.
Here, all lines are indented at the same level.

.. code-block:: bnf

    Dictionaries    AKA	    Parametric Text							
												
    Perform		some action
    to			some standard
    with	        some detail
    in the amount of    some money

It is also possible for the 2nd and subsequent lines to be indented relative to the first line. This is fine. But they all have to be indented to the same depth.

.. code-block:: bnf

    Pay			the fee
    amount		2000
    currency		USD
    recipient		Vendor

Some conventions like to use prepositions for the keys, but this is not required.

The terms below "Pay", namely "amount", "currency" and "recipient", are commonly called "keys".

The terms below "the fee", namely "2000", "USD", and "Vendor", are called "values".

Together they are called "key/value pairs", "attributes", or "parameters".

The first line is special: in an action spec, it tends to follow the format of "Verb object". Programmers may find this idiom familiar if they think it as a function call with parameters.

Positional parameters go on the first line, and named parameters go on the subsequent lines.

Note that currently nested dictionaries are not supported. We may add support in a future version of the language.

---------------------------------
Boolean Structures AKA BoolStruct
---------------------------------

A BoolStruct of some Thing connects multiple Things with AND, OR, and NOT operators.

Nesting is supported.

.. code-block:: bnf

    	Foo	
    AND	Bar	
    AND		Baz
	OR	Quux

You can build a BoolStruct of Arrays

.. code-block:: bnf

    		is warm blooded	
    AND		is vertebrate	
    AND		milk production	
    AND			has hair
		OR	has fur
    AND			live births
		OR	monotreme

You can also build a BoolStruct of Dictionaries. However, in BoolStructs, dictionaries must have their subsequent lines indented

.. code-block:: bnf

		Red		
			hex FF0000
    OR		Green		
			hex 00FF00
    OR		Blue		
			hex 0000FF

Finally, you can also build a BoolStruct of RelationalPredicate. An example is currently in Work in progress.

---------------------
Relational Predicates
---------------------

A relational predicate can be intuitively understood through the following example:

Suppose you have two terms X and Y. They can be compared for equality (Eq) and along some dimension (Ord).

.. code-block:: bnf

    X IS Y					
    X <  Y	X <= Y
    X >  Y	X >= Y  

Maybe Y is an array:

.. code-block:: bnf

    Y  IS  Y1  Y2  Y3  Y4

Then we can see if X is in it:

.. code-block:: bnf

    X IN Y

The examples above show Relational Predicates as Constraints.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Relational Predicates inside Horn Clauses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Relational Predicates are used inside Horn Clauses. The head is a Relational Predicate. The body is a BoolStruct of Relational Predicates.

The usage looks like the following example:

.. code-block:: bnf

    DECIDE	foo	IS	bar
    WHEN	baz	IS	quux

    which parses to

    HC2    { hHead = RPConstraint ["foo" ] RPis ["bar"]
           , hBody = Just (Leaf (RPConstraint ["baz"] RPis [ "quux" ]))}

But a RelationalPredicate can also contain types we are already familiar with:

    - MultiTerm arrays
    - ParamText dictionaries											

These are used as atomic terms.

.. code-block:: bnf

    DECIDE	foo		
    WHEN	baz IS quux

    which parses to

    HC2    { hHead = RPMT ["foo"]
           , hBody = Just (Leaf (RPConstraint ["baz"] RPis ["quux"]))}													
													
.. code-block:: bnf

    DECIDE	foo
    WHEN	baz		

    which parses to

    HC2    { hHead = RPMT [ ""foo"" ]
           , hBody = Just (Leaf (RPMT ["baz"]))}

.. code-block:: bnf

    DECIDE	Color	IS	blue
    WHEN	baz	

    which parses to

    HC2    { hHead = RPConstraint ["Color"] RPis ["blue"]
           , hBody = Just ( Leaf (RPMT ["baz"]))}

Simpler cases allow for more straightforward, unconditional definitions. You may think of these as variable assignments to values.											

.. code-block:: bnf

    DECIDE	Color   IS  blue			

    which parses to

    HC2    { hHead = RPConstraint ["Color"] RPis ["blue"]
           , hBody = Nothing}	

A variety of syntaxes parse to the same Horn Clause constructs.											
													
.. code-block:: bnf

    HC2    { hHead = RPConstraint ["Color"] RPis ["blue"]
           , hBody = Nothing}
    
    The following syntaxes parse to the above Horn Clause construct.

    DECIDE	Color	IS	blue

    DECIDE	Color
    MEANS	blue

    DECIDE	Color	IS	blue

    DEFINE	Color	IS	blue

    DEFINE	Color	MEANS	blue

    DEFINE	Color
    MEANS	Blue 

------------------------------
The TYPICALLY and AKA Keywords
------------------------------

--------------------------------
Rule Labels and Scope Qualifiers
--------------------------------






													
																		




													

