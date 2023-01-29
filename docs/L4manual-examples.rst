.. _examples:

=======================================================================
Examples in L4 and the concepts and keywords introduced in each example
=======================================================================

Examples illustrate key concepts along the way.

----------------------------------------------
Rules, Booleans, and Syntax: Must Sing Example
----------------------------------------------

`Link to 'Must Sing' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=1505307398>`_

This example gives an overview of how to write a simple rule in L4 using the simple rule: "Every person who walks and eats or drinks must sing".

We thank Matthew Waddington for originally authoring the case from which this example is drawn.

Concepts introduced:

1. Constitutive and Regulative Rules

2. Boolean Structures

3. Inline Syntax

Keywords introduced:

    - EVERY
    - WHO
    - MUST
    - AND
    - OR
    - MEANS

This chapter begins with a very simple rule:

.. code-block:: bnf

    EVERY   Person
    WHO     walks
    MUST    sing

L4 has two types of basic rules: regulative, and constitutive.

The basic syntax for regulative, or prescriptive, rules is as follows:

.. code-block:: bnf

    Regulative Rule ::= EVERY | PARTY           Entity Label				
	                [ WHO | WHICH		Boolean Structure	]
	                MUST | MAY | SHANT      Action Spec				

~~~~~~~~~~~~~~~~
Regulative Rules
~~~~~~~~~~~~~~~~

Legal sentences for regulative rules, according to the syntax definition above, include:

.. code-block:: bnf
    
    1. 
    EVERY   Person
    WHO     walks
    MUST    sing

    2.
    EVERY   Organization
    WHICH   creates art
    MAY     brag

    3.
    PARTY   Alice

    MUST    pay Bob

    4.
    PARTY   Bob

    MUST    say bad things about Alice

~~~~~~~~~~~~~~~~~~~
Syntax (Meta-)Rules
~~~~~~~~~~~~~~~~~~~

The syntax definition above obeys syntax rules of its own.

- A ``|`` indicates alternatives: the first word of the sentence can be either EVERY or PARTY. The last keyword can be MUST, MAY, or SHANT.

- A pair of [brackets] indicates that the text between them is optional: that's why in examples 3 and 4, Alice and Bob have no WHO or WHICH.

- The terms to the right of the keywords hold space for expressions that have syntax rules of their own.

Just as the above stanza defines the syntax for "Regulative Rule", you can expect to find stanzas elsewhere that define the syntax for "Entity Label", "Boolean Structure", and "Action Spec".

- "Alice", "Bob", "Person", and "Organization" all satisfy the definition for an "Entity Label".

- "Boolean Structure" is satisfied by "walks" and "creates art". The simplest Boolean Structure is a single word.

- "Sing", "brag", "pay Bob", and "say bad things about Alice" are all examples of an "Action Spec".

Together, these syntax rules give the "grammar" of the L4 language.

L4's grammar is based on familiar English grammar. Entity Labels are nouns. Action Specs are verbs (technically, verb phrases).

~~~~~~~~~~~~~~~~~~
Constitutive Rules
~~~~~~~~~~~~~~~~~~

The basic syntax for constitutive rules is as follows:

.. code-block:: bnf

    Constitutive Rule ::= MultiTerm
                            MEANS   Boolean Structure

In legal writing, definitions appear near the top of the document. Defined Terms are usually identified with Capital Letters.

L4 uses constitutive rules to define terms.

This "Must Sing" chapter gives an example of a constitutive rule:

.. code-block:: bnf

    		Qualifies	
	MEANS	walks	
	AND		eats
		OR	drinks

The "MultiTerm" being defined is "Qualifies". The detailed syntax for "MultiTerm" is given below. In short, it consists of one or more words in separate cells.

The Boolean Structure contains "walks AND eats OR drinks".

~~~~~~~~~~~~~~~~~~
Boolean Structures
~~~~~~~~~~~~~~~~~~

Let's look more closely at Boolean Structures.

.. code-block:: bnf

    Boolean Structure ::=   Boolean Structure
                            AND | OR | UNLESS   Boolean Structure
                                                Element

The third line of the definition, "Element", bottoms out at a leaf node: just some word, without any ANDs or ORs within.

In this first lesson, elements are single words.

These are the most essential forms of syntax in L4. Advanced versions of these clauses and constituent elements will be presented later.

------------------------------------------------------
Booleans and Visualization: Rodents and Vermin Example
------------------------------------------------------

`Link to 'Rodents and Vermin' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=1206725099>`_

This example focus on a single decision rule drawn from a home insurance policy and its transformations to more easily understood forms.

Decisions express first-order logic, functions, predicates, judgements, and calculation in general.

Concepts introduced:

1. Boolean Structures in detail. 

2. Visualization as an electrical circuit diagram.						

Keywords introduced:

   - DECIDE
   - WHEN
   - UNLESS
   - AND
   - OR
   - NOT

~~~~~~~~~
Decisions
~~~~~~~~~

Decisions express first-order logic, functions, predicates, judgements, and calculation in general.

.. code-block:: bnf

    Hornlike ::= [GIVEN        ParamText            ]
                  DECIDE       RelationalPredicate				
                 [WHEN | IF    Boolean Structure    ]

If you happen to know Prolog, you will be familiar with the notion of a Horn clause.

``head(param1, param2, …) :- body1(param3, param4), body2(param5, param6).``

The head, to the left of the :- symbol, is the conclusion of the rule.

The body, to the right of the :- symbol, contains the list of predicates that, when satisfied, conclude that the head of the rule is true.

In L4, the relational predicate on the DECIDE line gives the conclusion of the rule.

The Boolean Structure introduced by the WHEN keyword gives the conditions of the rule.

The keywords WHEN and IF are synonymous in a DECIDE context.

The GIVEN keyword provides other arguments to the decision rule, and is conjoined with the WHEN | IF material.

The expression context of the GIVEN and WHEN | IF includes the history available to the calling context. For example, if the decision is being evaluated for the purposes of executing a certain regulative rule, the trace prior to that state transition is available to the DECIDE rule.

Constitutive rules using WHEN are a subset of Hornlike rules that use DECIDE.

~~~~~~~~~~~~~~~~~
Decision Diagrams
~~~~~~~~~~~~~~~~~

Visualization of a decision rule produces a "circuit diagram": it is based on electrical circuit diagrams. If you can find a path from the left side of the diagram to the right, where the relevant terms have the required values,
the overall value of the decision diagram is true.

This is useful because it shows the "big picture" of a legal construct, and suggests ways to short-circuit a particular decision rule.

------------------------------------------------------------------------
Events & Consequences, Obligations vs Permissions: Contract as Automaton
------------------------------------------------------------------------

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

Some of the earliest written agreements, carved in stone millennia ago, deal with the lending of property. Following in this tradition, this chapter formalizes a simple financial agreement in L4. The ruleset weaves multiple regulative rules together, in series and in parallel. It shows how a "flowchart"-style diagram is automatically generated from the ruleset.
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

---------------------------------------------------------------------------------
Entity Relations, Ontology Inference, and Predicate Logic Syntax: Motor Insurance
---------------------------------------------------------------------------------

`Link to the case study 'Motor Insurance' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=2061671536>`_

Entity Relations, Ontology Inference, and Convenient Syntax for Predicate Logic.

Concepts introduced:

1. Combining regulative and constitutive rules

2. Guards in state transitions

Keywords introduced:

    - DECIDE
    - UNLESS
    - WHO
    - WHICH
    - WHEN
    - IF
    - TYPICALLY

---------------------------------------
Encoding of Real Legislation: PDPA DBNO
---------------------------------------

`Link to the case study 'PDPA DBNO' example <https://docs.google.com/spreadsheets/d/1leBCZhgDsn-Abg2H_OINGGv-8Gpf9mzuX1RR56v0Sss/edit?pli=1#gid=1779650637>`_

L4 automatically generates a web app from real-world legislation & regulation. It is an encoding of a fragment of real-world legislation.

Concepts introduced:

1. Reference and Expansion

2. Temporal Keywords

3. State transitions

Keywords introduced:

    - DECIDE
    - UNLESS
    - WHO
    - WHICH
    - WHEN
    - IF
    - TYPICALLY

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Petri Net representation of PDPA DBNO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We will continue our examination of the PDPA DBNO case with a deep dive into Petri Nets; it is intended to be a Petri Net representation of the PDPA DBNO example.

Concepts introduced:

1. Workflow diagrams in detail

2. BPMN used in industry

3. Process algebras

Keywords introduced:

    - HENCE

