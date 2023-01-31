#############################
Contract as Automaton Example
#############################

=================================================
Events & Consequences, Obligations vs Permissions
=================================================

`Link to 'Contract as Automaton' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=2000125343>`_

A loan is repaid in two instalments. The borrower has to stay out of trouble.

Concepts introduced:

1. Events and consequences

2. Obligations vs permissions

3. Process workflow diagrams

Keywords introduced:

    - DECLARE
    - DEFINE
    - HAS
    - IS A
    - DO
    - HENCE
    - LEST
    - MAY
    - BY
    - WITHIN

Some of the earliest written agreements, carved in stone millennia ago, deal with the lending of property. Following in this tradition, this chapter formalizes a simple financial agreement in L4. 

The ruleset weaves multiple regulative rules together, in series and in parallel. It shows how a "flowchart"-style diagram is automatically generated from the ruleset.
Such diagrams give people an alternative way to understand legal documents: visually instead of textually.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Declarations and Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This chapter introduces a handful of keywords. DECLARE and DEFINE have to do with data types and values.

If you are familiar with Object-Oriented Programming, from languages like Python, Java, C++, or Javascript, you will find the DECLARE and DEFINE concepts familiar.

We use DECLARE to set up our classes, our records, our types, our schemas, our ontology, our templates.

We use DEFINE to instantiate those templates with concrete values: the specific variables of a particular agreement.

These declarations and definitions are automatically exported to the programming language of your choice, lessening the burden of programming downstream. Some call this "model-driven engineering"; others, "low-code".

.. code-block:: bnf

    Type Declaration ::= DECLARE    MultiTerm   [Type Signature]	
                        [   Has-Attribute       ]
                        [       ...             ]								
																		
    Has-Attribute    ::= HAS        MultiTerm   [Type Signature]	
                        [   ...                 ]
                        [   Has-Attribute       ]								

This syntax rule means you can have multiple HAS-Attributes, listed on subsequent lines. For convenience, only the first HAS keyword is necessary; subsequent lines don't need it. 

HAS-Attributes can nest, such that one record declaration can contain another.
For example:

.. code-block:: bnf

    DECLARE     Point								
    HAS         position x          IS A        Number			
                position y          IS A        Number			
                details             IS A        PointDetail			
                HAS	color       IS ONE OF   Red Green Blue
                	value       IS A        Number			
                	onHover     IS A        String			

We'll talk more about the elementary data-types of L4 later: sum types, product types, lists, and dictionaries. We'll also talk about type inference and type checking.

.. code-block:: bnf

    Variable Definition ::= DEFINE      Value Term  [Type Signature]    // class-object instantiation
                            HAS         MultiTerm   [Type Signature]			
                                        [ ... ]										

Variable definitions with the DEFINE keyword follow the same format as DECLARE.

~~~~~~~~~
Deadlines
~~~~~~~~~

This chapter also introduces temporal constraints: the BY and WITHIN keywords set deadlines.

.. code-block:: bnf

    Temporal Constraint ::= (BEFORE | AFTER | BY | WITHIN | UNTIL)  Temporal Spec		

A regulative rule without a temporal constraint is incomplete. L4 substitutes "EVENTUALLY" but will issue a warning so you are conscious that a deadline is missing.

~~~~~~~~
Deontics
~~~~~~~~

Laws and contracts impose obligations and prohibitions on persons, and grant permissions.

These ideas are central to deontic logic, and underlie L4's keywords MUST, SHANT, and MAY, respectively.

.. code-block:: bnf

    Deontic Keyword ::= MUST | MAY | SHANT

Within the context of a single rule, these deontic keywords specify different consequences for the satisfaction or violation of the rule.

The two fundamental consequences in L4 are FULFILLED and BREACH.

.. code-block:: bnf

            If the actor does not perform the action 
            by the deadline                             If the actor performs 
                                                        the action by the deadline	
                                 
    MUST        BREACHED                                FULFILLED	
    SHANT       FULFILLED                               BREACHED	
    MAY	        FULFILLED                               FULFILLED	

We observe that a MAY rule is permissive: if you do it, fine! If you don't, fine!

l4's workflow diagrams follow a convention: a rule that is satisfied proceeds to the bottom right, while a rule that is violated proceeds to the bottom left. The "happy path" therefore runs along the right side of a diagram. A MAY rule shows action to the right, and inaction to the left.

~~~~~~~~~~~
Connections
~~~~~~~~~~~

Ordinary programming languages use the IF ... THEN ... ELSE construct to connect blocks of code, based on whether the conditions in the IF were met.
L4 uses HENCE instead of THEN, and LEST instead of ELSE, to connect regulative rules, based on whether the preceding rule was satisfied.

.. code-block:: bnf

    Regulative Connector ::= HENCE | LEST   Rule Label | Regulative Rule

Individual regulative rules connect with one another to form a graph, or a flowchart, describing a workflow.

What are the semantics of a rule?

.. code-block:: bnf

    [Attribute Constraint               ]						
    [Conditional Constraint             ]						
    [Upon Trigger                       ]						
    [HENCE  Rule Label | Regulative Rule]
    [LEST   Rule Label | Regulative Rule]
    [WHERE  Constitutive Rule
            [ ... ]                     ]