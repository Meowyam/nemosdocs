.. _eg_mustsing:

#################
Must Sing Example
#################

===========================
Rules, Booleans, and Syntax
===========================

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