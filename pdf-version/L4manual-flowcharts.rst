============================================================================
Flowcharts: Practical Considerations from a Software Engineering Perspective
============================================================================

-------------------------------------------------
Flowcharts representing both statics and dynamics
-------------------------------------------------

Flowcharts are commonly taught in school. So, when formalizing the law, people often reach first for flowcharts.

The flowcharts approach is the least common denominator, used when other tools are not available, or when staff are not trained in them.

They use flowcharts to represent the statics: these are really decision trees.

They use flowcharts to represent the dynamics: these are really state diagrams.

These dual aspects tend to be highly coupled into a single flowchart.

The flowcharts tend to be drawn in a simple drawing app, at the level of syntax, not semantics. Boxes with text, arrows with nearby text.

From such a flowchart, a web interview is produced, in a direct and imperative form.

The output of the interview feeds into a document assembly system.

Often, such documents are intended to be finally embodied on paper.

------------------------------------
Adding functionalities to flowcharts
------------------------------------

A less imperative and more declarative approach preserves all the features of flowcharts, while adding functionality.

Statics are extracted to decision tables and diagrams, in DMN / DRD format.

Dynamics are left in the flowchart, and upgraded with swimlanes and deadlines to look more like BPMN format.

At this point we can reconstruct the original flowchart, but from a less tightly coupled source.

From these elements we can extract an interview.

The results of the interview can be submitted digitally.

Isomorphism can be preserved when the authoritative version of the rules are written in a higher-level language.

----------------------------------------------------
Why a functionality enhanced flowchart is preferable
----------------------------------------------------

Flowcharts are not the best way to represent decision logic. "The sorrow is obvious," says the `Camunda DMN tutorial <https://camunda.com/dmn/>`_.

This approach is more amenable to automated verification. What edge cases are lacking?

With this approach, interfaces can be made interactive. Irrelevant subtrees trees can be folded away hidden from view.

The end-user can trace their way through the flowchart and examine alternative routes.

The availability of user-provided information does not always match the pre-determined order of questions.

