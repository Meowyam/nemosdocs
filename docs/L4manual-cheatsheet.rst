=============
L4 Cheatsheet
=============

--------------------------
Types of Expressions in L4
--------------------------

This `Backus-Naur Form (BNF) <https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form>`_ cheatsheet describes the syntax of the L4 language.

---------
Top Level
---------

.. code-block:: bnf

    Toplevel::=	Regulative Rule			
            |	Constitutive Rule			
            |	Type Declaration			
            |	Variable Definition			
            |	Full Scenario Rule			
            |	Simple Scenario Rule			

-----
Rules
-----

~~~~~~~~~~~~~~~~~~
Full Scenario Rule
~~~~~~~~~~~~~~~~~~

.. code-block:: bnf

    Full Scenario Rule::=	[Toplevel...] \\(except Scenario Rules)				
				\\this allows us to reduce the ruleset as more and more data is available	

~~~~~~~~~~~~~~~~~~~~
Simple Scenario Rule
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bnf

    Simple Scenario Rule::=	SCENARIO    RuleName    \\(except Scenario Rules)				
			        GIVEN	RelationalPredicate													
					[       ...       ]														
				EXPECT  RelationalPredicate													
					[       ...       ]			

~~~~~~~~~~~~~~~
Regulative Rule
~~~~~~~~~~~~~~~

.. code-block:: bnf

    Regulative Rule	::=	EVERY | PARTY	Entity Label						
					[Subject Constraint]						
					[Attribute Constraint]						
					[Conditional Constraint]						
					[Upon Trigger]						
					    Deontic Action Temporal | Deontic Temporal Action					
					[HENCE	         Rule Label | Regulative Rule]
					[LEST	         Rule Label | Regulative Rule]
					[WHERE	         Constitutive Rule						
							        [...]				]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Constitutive Rule and Hornlike Rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hornlike clauses have the form: Head if Body

.. code-block:: bnf

    Constitutive Rule ::= [GIVEN  MultiTerm]					
    Hornlike Rule     ::= [Upon   Trigger  ]												
			    DECIDE          Relational Predicate  [AKA Alias] [Typically Boolish]
			  | IS	            BoolStructR															
			  | MEANS           BoolStructR															
			  | HAS		    Relational Predicate															
			  | INCLUDES        Set Group															
			    WHEN            RelationalPredicate BoolStruct															

~~~~~~~~~~~~~~~~~~~~~
Compact Constitutives
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bnf

    Compact Constitutives ::= [GIVEN        MultiTerm]					
                              [Upon Trigger          ]					
			      DECIDE	    Relational Predicate    WHEN	Relational Predicate		
										[ ... ]								
					|   Relational Predicate    OTHERWISE | GENERALLY

----------------
Labels and Names
----------------

.. code-block:: bnf

    Entity Label    ::= Aliasable Name		

    Aliasable Name  ::= MultiTerm [AKA MultiTerm]	 
    // in future – extend to BoolStruct of SetGroup							

------------------------------
Constraints and 'Upon Trigger'
------------------------------

.. code-block:: bnf

    Subject Constraint      ::= WHO             RelationalPredicate BoolStruct	        
    \\evaluated against the subject of the rule

    Attribute Constraint    ::= WHOSE           RelationalPredicate BoolStruct

    Conditional Constraint  ::= (WHEN | IF)	RelationalPredicate BoolStruct
                                [UNLESS         RelationalPredicate BoolStruct]

.. code-block:: bnf

    Upon Trigger ::= UPON		Aliasable Name			

--------
Deontics
--------

.. code-block:: bnf

    Deontic Temporal Action	::=	Deontic Keyword             Temporal Constraint			
                                        -> | DO		            Action Expression			

    Deontic Keyword	        ::=	(MUST | MAY | SHANT)

A semantically equivalent syntactic alternative allows the temporal keyword to line up with the other keywords:

.. code-block:: bnf

    Deontic Action Temporal ::= Deontic Keyword            Action Expression		
                                Temporal Constraint						

.. code-block:: bnf

    Temporal Constraint     ::=	(BEFORE | AFTER | BY | UNTIL)   Temporal Spec

--------------------------------------
Dictionaries and Key/Value expressions
--------------------------------------

.. code-block:: bnf

    Action Expression   ::= Dictionary	
    example		        pay     vendor	
				amount|	$20	
				by    |cheque	

    Dictionary		::= Detail Key/Value			
                            [     ...       ]

    Detail Key/Value    ::= Single Term		    [MultiTerm]			
                            [newline indented       [Dictionary]  ] 

    Detail Key		::= Single Term		

-------------------------
Single Term and MultiTerm
-------------------------

.. code-block:: bnf

    Single Term		::= a string or number within a single cell	

    MultiTerm		::= Single Term     [Single Term...	]					

----------------------------------------
Type Declaration and Variable Definition
----------------------------------------

.. code-block:: bnf

    Type Declaration    ::= DECLARE	MultiTerm	[Type Signature	]
			    HAS		MultiTerm	[Type Signature	]
							[ ... ]							
    example                 DECLARE	Point					
                            HAS	        position x	IS A Number
				        position y	IS A Number

    Variable Definition ::= DEFINE	Value Term	[Type Signature] //class-object instantiation				
			    HAS	        MultiTerm       [Type Signature]							
						        [ ... ]	

------------------------
Booleans and BoolStructs
------------------------

.. code-block:: bnf
    
    Boolish	         ::= (TRUE | FALSE | Yes | No)

    BoolStruct Expression::= Expression		
    "BSE"		    | BSE AND BSE
                            | BSE OR  BSE
                            | NOT     BSE
                            | (Expression)	

    BoolStructR          ::= BoolStruct      Relational Predicate

--------------------
Relational Predicate
--------------------

------------------------
Value Term and Set Group
------------------------

===========================
Syntax Reference by Keyword
===========================

-----
WHOSE
-----
~~~~~~~~~~~~~~~~~~~~~~~~~~
WHOSE in a regulative rule
~~~~~~~~~~~~~~~~~~~~~~~~~~

The "WHOSE" keyword can appear at the top level in a regulative rule, where it acts as a qualifier constraint.

.. code-block:: bnf

    EVERY   P				
    WHOSE   attribute   predicate		[TYPICALLY Boolean-expression]	
    WHOSE   color   IS  blue		

The WHOSE line adds a precondition to the rule. If the WHOSE block does not return a true result, the rest of the rule does not proceed.

The attribute term is interpreted with respect to the party P.

The predicate takes up the rest of the line and applies to the attribute. As with most predicates, a TYPICALLY default can be supplied to improve UX.

This is operationally equivalent to:

.. code-block::

    function rule (..., party, attribute, value,... ) {
        if (! predicate(party[attribute]) { return }
    }

and is logically equivalent to (See swipl dicts for syntax):

.. code-block:: 

    rule(…, Party, Attribute, Predicate, ...) :-
    call(Predicate, Party.Attribute), ...

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WHOSE in top-level constitutive definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "WHOSE" keyword can appear in a top-level constitutive definition, where it acts as a qualifier constraint.

.. code-block:: bnf

    DEFINE	Retriever					
    IS A	Dog					
    WHOSE       Breed   IS IN   Chesapeake Bay		Golden
                                Curly-Coated		Labrador
                                Flat-Coated		Nova Scotia Duck Tolling

A Retriever is a Dog whose attribute Breed matches one or more of the elements given in the following list.

If the Breed attribute is itself a list, then the test is a set intersection.

If the Breed attribute is not defined, the test is negative.

See remarks about **vacuous truth**.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
WHOSE in inline constitutive definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "WHOSE" keyword can appear in an inline constitutive definition in a regulative rule, where it acts as a qualifier constraint.

.. code-block:: bnf

    EVERY   Dog Walker					
    MUST    muzzle  their   Dog			
		            WHOSE   Breed   IS IN   Pit Bull
                                                    German Shepherd

Assuming the MUST does not contain any AND or OR branches, this is effectively similar to saying, at the top level,

.. code-block:: bnf

    WHEN    Dog	Breed   IS IN	    Pit Bull German Shepherd

Because the WHOSE does not appear under an AND/OR/XOR limb, the qualifier attaches to the top-level rule, and voids the entire rule if the constraint is not met.

~~~~~~~~~~~~~~~~~~~~~~~~
WHOSE in a junction list
~~~~~~~~~~~~~~~~~~~~~~~~

The "WHOSE" keyword can appear under a limb of a junction list, where it acts as a qualifier constraint on the associated limb.

.. code-block:: bnf

            Motorcycle						
    MEANS   Two-wheeled	    vehicle     equipped with an    internal combustion engine	
    OR      Two-wheeled     vehicle     equipped with a	    battery-powered motor	
            WHOSE	    maximum speed   >               11  miles per hour	

Because the WHOSE appears under an AND/OR/XOR limb, the constraint is ANDed within the nearest limb.

Internally, with the help of some DEFINE rules (shown below) the rule is transformed to:

.. code-block:: bnf

    	Motorcycle						
    MEANS	vehicle	wheel count		IS	4	
    OR		vehicle	wheel count		IS	2	
	AND	vehicle	engine		        IS	internal combustion engine
	AND	vehicle	maximum speed		>	11 miles per hour

---
WHO
---

~~~~~~~~~~~~~~~~~~~~~~~~
WHO in a regulative rule
~~~~~~~~~~~~~~~~~~~~~~~~

The "WHO" keyword can appear at the top level in a regulative rule, where it acts as a qualifier constraint.

.. code-block:: bnf

    EVERY	P
    WHO	parameterizable attribute

The WHO line adds a precondition to the rule. If the WHO block does not return a true result, the rest of the rule does not proceed.

The parameterizable attribute term is interpreted with respect to the party P.

This is operationally equivalent to:

.. code-block:: 

    function rule (…, party, attribute, …) {
        if (! party.attribute) { return }
    }

and is logically equivalent to:

.. code-block:: 

    rule(…, Party, Attribute, …) :-
    call(Verb, Attribute), ….

There is some subtlety here: sometimes an attribute turns out to be a method, meaning a function that runs against the party, with arguments.

In other words, you might want:

.. code-block:: 

    function rule (…, party, attribute, attributeParameters, …) {
        if (! party.attribute( attributeParameters )) { return }
    }

The arguments are given as a dictionary of sub-attributes and predicates:

.. code-block:: bnf

    EVERY   P		
    WHO	    attribute		
                sub-attribute	predicate
                sub-attribute	predicate

This enables the more natural phrasing:

.. code-block:: bnf

    EVERY   P				
    WHO	    runs				
	    with	scissors		
	    speed	>3 mph

------
DEFINE
------

.. code-block:: bnf

    DEFINE	F		
    GIVEN	P1	P2	P3

    DEFINE	F1	F2
    MEANS	something possibly involving F1 and F2	

    DEFINE		two-wheeled vehicle			
    MEANS		vehicle	wheel count     IS   2

    Note that the indentation follows the first word of the rewritten phrase.

    DEFINE		vehicle	equipped with an      X
    MEANS		vehicle	drive	        IS    X

Note that you get a/an-equivalence for free, when it appears at the end of a cell, as above.

When a rewrite rule operates twice against the same sentence, on both the left and the right of the central term, the limbs are conjoined with an AND and reindented accordingly.

-----
AS IN
-----

This keyword is shorthand for importing a particular keyword block from another section.

Suppose we have:

.. code-block:: bnf

    §       Section One			
    PARTY   Seller			
    WHEN    sale	date	IS IN	promotional period
    AND     sale	store	IS IN	stores participating in promotion
    AND     blah	blah		
    MUST    do something			

Rather than repeat all the WHEN bits,

.. code-block:: bnf

    §	Section Two	
    PARTY   Buyer	
    WHEN    AS IN       Section One
    MUST    do something else	

    