.. _keywords:

######################
Language Specification
######################

======================================
Keywords: Declarations and Definitions
======================================

This chapter introduces a handful of L4 keywords. 

-----------------------------------------------------------------
DECLARE and DEFINE, for data types and values, and HAS-Attributes
-----------------------------------------------------------------

DECLARE and DEFINE have to do with data types and values.

If you are familiar with Object-Oriented Programming, you will find the DECLARE and DEFINE concepts familiar.

We use DECLARE to set up our:

    - classes
    - records
    - types
    - schemas
    - ontology
    - templates

We use DEFINE to instantiate those templates with concrete values: the specific variables of a particular agreement.

These declarations and definitions are automatically exported to the programming language of your choice, lessening the burden of programming downstream.

Consider the following code

.. code-block:: bnf

    Type Declaration	::=		DECLARE			MultiTerm			  [Type Signature]	
					[Has-Attribute  ]								
					[       ...     ]							
																		
    Has-Attribute	::=		HAS			MultiTerm			  [Type Signature]	
					[       ...     ]
					[Has-Attribute	]	

This syntax rule means you can have multiple HAS-Attributes, listed on subsequent lines. For convenience, only the first HAS keyword is necessary; subsequent lines don't need it.

HAS-Attributes can nest, such that one record declaration can contain another.
For example:

.. code-block:: bnf

    Variable Definition	::=	DEFINE		Value Term		[Type Signature	]	//class-object instantiation				
				HAS		MultiTerm		[Type Signature	]							
						[ ... ]														

Variable definitions with the DEFINE keyword follow the same format as DECLARE.

---------------------------------------------------------
BY and WITHIN for Temporal Constraints such as Deadlines
---------------------------------------------------------

The BY and WITHIN keywords set deadlines

.. code-block:: bnf

    Temporal Constraint ::= (BEFORE | AFTER | BY | WITHIN | UNTIL) Temporal Spec				

A regulative rule without a temporal constraint is incomplete. L4 substitutes "EVENTUALLY" but will issue a warning so you are conscious that a deadline is missing.

----------------------------------------------------
MUST, SHANT, and MAY for obligations and permissions
----------------------------------------------------

Laws and contracts impose *obligations* and *prohibitions* on persons, and grant *permissions*. These ideas are central to *deontic logic*, and underlie L4's keywords MUST, SHANT, and MAY, respectively.

.. code-block:: bnf
    
    Deontic Keyword ::= (MUST | MAY | SHANT)	

Within the context of a single rule, these deontic keywords specify different consequences for the satisfaction or violation of the rule.

-------------------------------------------
FULFILLED and BREACH for consequences in L4
-------------------------------------------

The two fundamental consequences in L4 are FULFILLED and BREACH.

.. code-block:: bnf

                    If the actor does not perform the action by the deadline            If the actor performs the action by the deadline								
        MUST		    BREACHED                                                            		    FULFILLED								
        SHANT		    FULFILLED										    BREACHED								
        MAY		    FULFILLED										    FULFILLED								

We observe that a MAY rule is permissive: if you do it, fine! If you don't, fine!

L4's workflow diagrams follow a convention: a rule that is satisfied proceeds to the bottom right, while a rule that is violated proceeds to the bottom left. The ""happy path"" therefore runs along the right side of a diagram.

A MAY rule shows action to the right, and inaction to the left.

------------------------------------------------------------------
HENCE and LEST for regulative rules and connecting blocks of code
------------------------------------------------------------------

Ordinary programming languages use the IF … THEN … ELSE construct to connect blocks of code, based on whether the conditions in the IF were met.

L4 uses HENCE instead of THEN, and LEST instead of ELSE, to connect regulative rules, based on whether the preceding rule was satisfied.

.. code-block:: bnf

    Regulative Connector ::=	(HENCE | LEST)		
                            Rule Label | Regulative Rule				

Individual regulative rules connect with one another to form a graph, or a flowchart, describing a workflow.

----------------------
The Semantics of rules
----------------------

The semantics of a rule are as follows:

.. code-block:: bnf

    [Attribute Constraint   ]							
    [Conditional Constraint ]							
    [Upon Trigger	    ]							
    [HENCE				Rule Label | Regulative Rule ]	
    [LEST				Rule Label | Regulative Rule ]	
    [WHERE				Constitutive Rule							
                                        [   ...     ]                ]	

