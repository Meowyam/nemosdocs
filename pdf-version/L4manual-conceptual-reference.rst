====================
Conceptual Reference
====================

The following discusses law as a problem in computer science.

The law encompasses a rich and majestic history of monarchs and parliaments, human rights and natural justice, torts and equity, judgements and appeals, death sentences and stays of execution. Movies and TV shows from "A Few Good Men" to "She-Hulk" glamourize the profession.

By comparison, computational law, a new field whose history is measured in decades, not centuries, is bloodless and dry; there are no movies, no TV shows. But the growing overlap between law and software portends a quiet digital transformation of the way people conduct business and organize their lives.

The overarching theme of computational law, consistent with the aphorism "`software is eating the world <https://a16z.com/2011/08/20/why-software-is-eating-the-world/>`_", is the analysis of legal problems from the perspective of computer science.

.. _L4_approach:

-------------------------------------
The L4 approach to the problem of law
-------------------------------------

The L4 approach considers contracts and legislation to be *attempts at specification*. 

The behaviour of actors is regulated by rules which describe state transition systems. The transitions between states are themselves governed by decision rules.

Both kinds of rules are expressible ultimately in first-order logic and are recursively subject to meta-rules like priority ordering.

The evaluation at run-time of decision elements to binary truth values is dependent on human input.

Legacy legal drafting is frequently marred by undesirable ambiguities which are attributable to the lack of a formal language.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Advantages of modelling using a formal system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modelling the above ideas in a formal system makes it possible to apply software engineering practices to the legal sphere. New technologies and tools can help both lawyers and non-lawyers perform legally-oriented work in different and better ways.

For example: ambiguities in complicated sentences, commonly laid at the door of the "Oxford comma", and sometimes the cause of lawsuits, can be considered syntax errors. 

Misunderstandings between parties can be considered failures of requirements elicitation, and can be discovered prior to contract signing using methodologies like behaviour-driven development and unit testing.

Under-specification can be mechanically detected by methods borrowed from functional programming such as type checking and totality analysis. 

Finally, more mundanely, version control and structured data embedded in documents provide basic levels of machine-readability lacking today.

---------------------------
Limits to Computational Law
---------------------------

Not every problem in the legal world will be solved by software. Most commonly, terms which "ground out" in some English phrase not further defined will need human interpretation, typically via resort to case law.

Computational law has little to contribute in situations where contracting parties are less concerned with the details of their agreement than on agreeing that they have agreed, or where at least one party is aware that their counterparties may understand the agreement quite differently or not at all, but is prepared to resolve those differences at a later time, after the contract is signed.

----------------------------
Expanding on technical terms
----------------------------

Let us return to the technical terms mentioned in :ref:`L4_approach`. 

~~~~~~~~~~~~~~~~~~~~~~~~~~
On Specification Languages
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Specification languages* are distinct from programming languages. They are considered "higher-level", and are used primarily for analyzing the properties of systems even before the systems are implemented or run.

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

The values of terms are often debatable: reducing a messy, real-world, real-valued term to a Boolean is not always straightforward. "No Vehicles In The Park" provides the classic example of such difficulties. What is a vehicle? Where does the park end? If the park is flooded, does the rule still apply?

Different logics may provide different methods of performing such reduction. Logic programming offers ""negation as failure"" but that is not the only choice. And vacuous truths may lead to explosion.

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

----------------------
Machines consuming Law
----------------------

One of the motivations for computational law is to apply the tools and techniques of computer science to represent legal constructs and automate legal reasoning in more formal ways, that are consumable by machine and ultimately useful to lay end-users.

The Contract Lifecycle Management industry was sized at $1.7B in 2021 and is expected to double to $3B by 2026. Similarly, there is increasing interest in "`Rules as Code <https://govinsider.asia/intl-en/article/four-things-you-should-know-about-rules-as-code>`_" by governments around the world as it promises to bring "digital transformation" to service delivery. 

In 2021, `Gartner identified machine-readable legislation as a key emerging technology to watch <https://www.gartner.com/en/newsroom/press-releases/2021-08-23-gartner-identifies-key-emerging-technologies-spurring-innovation-through-trust-growth-and-change>`_. If computational law is successful in putting laws and contracts on a firmly digital basis, it can serve as a basis for innovation in the CLM industry, the legal industry, and e-government.

----------------------------------------------
Comparing concepts in Law and Computer Science
----------------------------------------------

For the computer scientist new to law, it helps to recognize familiar concepts in unfamiliar guises.

For example, programmers are familiar with "default logic" in the form of if / then / else-if / then / else statements: each if condition is evaluated in turn. If all the branches are false, the default else is chosen. 

In legal writing, the order is reversed: *the default rule is stated first, and the exceptions follow*.

Another example: as programs grow over time, periods of incremental, "organic" evolution are punctuated by refactorings. 

Legal documents similarly tend to grow organically, as exceptions are piled upon exception to accommodate previously unanticipated scenarios; an experienced drafter reading a text will often remark to themselves, "ah, this was written first, and then this other bit was added later; you can tell."

In software, refactoring efforts are facilitated by the compiler and by test suites, which give confidence that the refactored code still works. 

In law, as `Ken Adams (MSCD) <https://www.adamsdrafting.com/writing/mscd/>`_ and `Claire Hill (Why Contracts are Written in Legalese) <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=332941>`_ observe, refactorings tend to be rarer: lawyers can be superstitous about "time-tested" phrasing, which has been before a judge and given objective interpretation.

This shows that "objective truth" tends to be expensive in law. Human lawyers advise human clients that the ultimate truth requires a human judge,
and that in turn often requires a full-fledged lawsuit.

---------------
How L4 can help
---------------

We address some of the above difficulties by presenting L4, a DSL for law that allows some form of ""agreed truth"" to be calculated through computational means, rather than disputed before a judge: if the logic is explicit, the facts can be affirmed, and the outputs can be verified, then the meaning of a legal construct should be accessible to anyone with a computer. 

This approach, while not universally applicable, can be useful in many situations where a dispute has not yet arisen, and parties are working in good faith toward a meeting of the minds.

Still, we regard it as a starting point and invite exploration and elaboration.


