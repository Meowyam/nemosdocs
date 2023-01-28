======================================
Meta-Rules,Defeasibility, and Defaults
======================================

We borrow from Default Logic the notion of priorities, as given in `Brewka 2000 <https://link.springer.com/chapter/10.1007/978-94-015-9383-0_3>`_ and `Brewka 1994 <https://www.aaai.org/Papers/AAAI/1994/AAAI94-144.pdf>`_.

**Notwithstanding**

Let us consider Example Def-1:

.. code-block:: bnf

    Clause A    No integers are prime.

    Clause B    Notwithstanding Clause A, some integers are prime: 
                if a positive integer has no factors besides 1 and itself, 
                then it is prime.

In this example, the default is Clause A, and the priority relation is B < A, meaning B describes exceptions to A.

**Subject To**

Let us consider Example Def-2:

.. code-block:: bnf

    Clause A    Subject to Clause B, no integers are prime.
    Clause B    Some integers are prime: 
                if a positive integer has no factors besides 1 and itself, 
                then it is prime.

In this example, the default is Clause A, and the priority relation is B < A, meaning B describes exceptions to A.

**Symmetry**

In both examples above, the effective semantics are the same: B < A.

The examples differ only in the choice of which clause explicitly states the priority relation.

**Operationalization**

The above examples reduce to the same program:

.. code-block:: haskell

    isP n
    |   n > 0 &&
        primeFactors n `remove` 1 `remove` n == [] = True
    |   Otherwise                                  = False
    where
        a `remove` b = filter (/= b) a

The priority relation is made explicit by the ordering.

The "otherwise" line gives the default answer "False", and is placed last.

The exception is tested before the default, and thus is placed above.

**Scope**

Note that priority relations do not wholly knock out the overridden clause. 

Clause B is only dispositive when there are no other factors besides 1 and n. 

If there are no other factors, Clause B is not dispositive, so the default applies.

Let us advance through the history of mathematics to 1938, and add:

.. code-block:: bnf

    Clause C    Notwithstanding Clause B, we deem 1 to be non-prime.

This clause C does not override clause B in full: it only removes a single element 1 from the domain.

.. code-block:: haskell

    isP n
    |   n == 1                                              = False
    |   n > 0 &&                                            
        primeFactors n `remove` 1 `remove` n == []          = True
    |   Otherwise                                           = False
    where
        a `remove` b = filter (/= b) a

Above, the priority clause (""notwithstanding B"") was placed in clause C.

But we could also have placed the priority clause inside Clause B:

.. code-block:: bnf

    Clause B		Subject to Clause C, ...
    Clause C		We deem 1 to be non-prime.

**The Defeasibility Graph**

The above examples are deliberately simple, and create a linear chain of overrides: C < B < A.

These overrides, ordered for correct execution in a program, constitute a topological sort of a graph.

One could imagine a more complex set of overrides, with two main branches rooted at X:

.. code-block:: bnf

    A < E < I < O < U < X	\\the "vowel branch"
    B < C < D < F < G < X	\\the "consonant branch"

Such a graph admits multiple topological sorts.

**In terms of Logic Programming**

We can map the above example to logic programming.

If the body of a Horn clause is satisfied, we say the rule applies.

The head of the Horn clause is then evaluated (or unified), and gives the effect of the rule.

In the above examples, first we decide if each clause applies;
if it does, the rest of the clause gives a True/False answer, which is its effect.

**In terms of traditional programming**

Conventional programming languages use the IF/THEN construct.

The IF part tests if the rule applies.
The THEN part gives the effect.

