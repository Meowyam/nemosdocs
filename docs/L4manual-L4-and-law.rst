=====================
How L4 Approaches Law
=====================

--------------------------------------------------------------
Analogies between Computer Science Concepts and Legal Concepts
--------------------------------------------------------------

A computer scientist can learn to recognise familiar concepts, expessed differently, in law. For example:

    - Programmers are familiar with "default logic" in the form of if / then / else-if / then / else statements: each if condition is evaluated in turn. If all the branches are false, the default else is chosen. 
    
    In law: The order is reversed in legal writing; the default rule is stated first, and the exceptions follow.

    - As programs grow over time, periods of incremental, "organic" evolution are punctuated by refactorings. 
    
    In law: Legal documents similarly tend to grow organically, as exceptions are piled upon exception to accommodate previously unanticipated scenarios; an experienced drafter reading a text will often remark to themselves, "ah, this was written first, and then this other bit was added later; you can tell."

    - In software, refactoring efforts are facilitated by the compiler and by test suites, which give confidence that the refactored code still works. 
    
    In law: As `Ken Adams (MSCD) <https://www.adamsdrafting.com/writing/mscd/>`_ and `Claire Hill (Why Contracts are Written in Legalese) <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=332941>`_ observe, refactorings tend to be rarer: lawyers can be superstitous about "time-tested" phrasing, which has been before a judge and given objective interpretation.

This shows that "objective truth" tends to be expensive in law. Human lawyers advise human clients that the ultimate truth requires a human judge,
and that in turn often requires a full-fledged lawsuit.

---------------------------------------------------------
The relationship between L4 and contracts and legislation
---------------------------------------------------------

The L4 approach considers contracts and legislation to be *attempts at specification* and models these attempts with a formal system.

- The behaviour of actors is regulated by rules which describe state transition systems. The transitions between states are themselves governed by decision rules.

- Both kinds of rules are expressible ultimately in first-order logic and are recursively subject to meta-rules like priority ordering.

- The evaluation at run-time of decision elements to binary truth values is dependent on human input.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Advantages of modelling using a formal system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using a formal system to model the above ideas makes it possible to apply software engineering practices to the legal sphere. New technologies and tools can help both lawyers and non-lawyers perform legally-oriented work in different and better ways. 

Consider the following examples:

- **Syntax Errors**: Ambiguities in complicated sentences, commonly laid at the door of the "Oxford comma", and sometimes the cause of lawsuits, can be considered syntax errors. 

- **Misunderstandings betwen parties**: We can think of misunderstandings between parties as failures of requirements elicitation. We can solve this issue before contract signing using methods like behaviour-driven development and unit testing.

- **Ambiguity**: Under-specification can be mechanically detected by methods borrowed from functional programming such as type checking and totality analysis. 

- **"Contract Draft version" problems**: Finally, more mundanely, version control and structured data embedded in documents provide basic levels of machine-readability lacking today.

----------------------------
Expanding on technical terms
----------------------------

This section explains the technical terms and domains found in `The relationship between L4 and contracts and legislation`_.

~~~~~~~~~~~~~~~~~~~~~~~~~~
On Specification Languages
~~~~~~~~~~~~~~~~~~~~~~~~~~

L4 is a "domain-specific modelling language", which is a type of "specification language". Specification languages are distinct from programming languages because they are considered "higher-level", and are used primarily for analyzing the properties of systems even before the systems are implemented or run.

Examples of specification languages include `Alloy <https://alloytools.org/>`_ and `TLA+ <http://lamport.azurewebsites.net/tla/tla.html>`_.

Both specification and programming languages are *formal languages*, which we expand upon below.

~~~~~~~~~~~~~~~~
On Formalisation
~~~~~~~~~~~~~~~~

Computer scientists are familiar with `state machines <https://en.wikipedia.org/wiki/Finite-state_machine>`_, which represent discrete change over time.

One of the earliest papers in computational law identified `Petri Nets <https://en.wikipedia.org/wiki/Petri_net>`_ as a useful formalism for representing state.

The notion of contract as state machine can be found at the heart of the `Business Process Modeling Notation (BPMN) standard <https://www.visual-paradigm.com/guide/bpmn/what-is-bpmn/>`_ for business processes.

~~~~~~~~
On Logic
~~~~~~~~

Computer scientists are also familiar with `propositional <https://en.wikipedia.org/wiki/Propositional_calculus>`_ `predicate <https://en.wikipedia.org/wiki/First-order_logic>`_, and `Boolean logics <https://en.wikipedia.org/wiki/Boolean_algebra>`_.

They deal with True and False values, combined using AND / OR / NOT connectors into potentially large trees of conditions. These logics lie at the heart of "rule systems", which calculate Boolean outputs based on inputs that are either natively Boolean or are reducible to Booleans, like x == 42. First-order predicate logic helps reduce a complex universe of many types, to Boolean values.

The values of terms are often debatable: reducing a messy, real-world, real-valued term to a Boolean is not always straightforward. "No Vehicles In The Park" provides the classic example of such difficulties.

    - What is a vehicle? 
    - Where does the park end? 
    - If the park is flooded, does the rule still apply?

Different logics may provide different methods of performing such reduction. 

Logic programming offers ""negation as failure"" but that is not the only choice. And vacuous truths may lead to state explosion.

This reduction problem lies at the heart of many legal conflicts: parties may disagree about the values of terms, and further disagree about the choice of logic.

In the real world it is often necessary to take unknown and undefined values into account: hence the need for a ternary logic.

~~~~~~~~~~~
On Rewrites
~~~~~~~~~~~

The primary specifications which attempt to establish a rule system are themselves subject to rewriting according to further meta-rule systems.

Some of these rewrites may be within the primary specification itself. In this section, any reference to dollars shall mean United States Dollars.

Other rewrites may occur "beyond the awareness" of the primary specification: "any clause of any contract which attempts to establish a non-compete shall be unenforceable."

These transformations are familiar to computer science. Given the text of a program, a compiler may perform transformations and optimizations and dead-code elimination through tree-shaking.

An operating system may choose to block certain system calls depending on access control privileges, or attach a debugger to an executing instance.

A microprocessor may perform speculative execution and out-of-order instruction pipelining.

When multiple rules collide, they can be resolved using a ordering mechanism: firewall rules, for example, include priorities.

~~~~~~~~~~~~~
On Evaluation
~~~~~~~~~~~~~

The "evaluation" of a specification depends on its `run-time environment <https://www.techopedia.com/definition/5466/runtime-environment-rte>`_ and often on *human input*.

Computer science is familiar with the notion of "static analysis", which attempts to show that a program, or specification, satisfies or violates certain properties.

In other words, it should be possible to identify, at the time of drafting, if a law or contract contains undesirable loopholes by which parties may escape intended consequences.

Static analysis methods include `SAT solving <https://en.wikipedia.org/wiki/SAT_solver>`_, which can be said to attempt to anticipate every eventuality. 

However, such methods cannot anticipate meta-rules operating outside the bounds of the system. A war of foreign occupation, for instance, may invalidate existing laws and contracts in unpredictable ways.

In any case, it is frequently impossible to determine in advance if a particular event will be considered to have met a certain standard.

Some degree of vagueness is inevitable, and, frequently, desirable: when a thing cannot be defined in any more detail, or it depends on which way the wind is blowing at the time, we need a human to step in and decide.

Did a party apply "reasonable efforts" to a particular action? It depends … on a decision tree which, sooner or later, bottoms out and needs to call an external decider for input.

~~~~~~~~~~~~~~~~~~~
On Natural Language
~~~~~~~~~~~~~~~~~~~

Because laws and contracts have, to date, been written in natural languages like English, drafters sometimes introduced ambiguities into their text.

Sometimes, it is up to a judge to make sense of manifestly ungrammatical sentences. Interpretive doctrines like purposive intent help them do their job.

The logical conjunction "A, B, C and D or E" can be interpreted at least four different ways.

Formal languages, like L4, force the drafter to clarify their meaning, by triggering compiler warnings upon encountering statements that are not well-formed.