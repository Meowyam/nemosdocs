:orphan:

##############
Advanced Users
##############

.. grid:: 2

    .. grid-item-card:: Backend Setup Instructions
        :link: links-advanced-setup-instructions
        :link-type: doc

        Instructions for the setup of the necessary tools.

    .. grid-item-card:: Conceptual Explanation of the Backend
        :link: advanced-explanations
        :link-type: doc

        In-depth conceptual explanation of how the L4 backend works.

============================================
Installing the L4 Backend: Intended Audience
============================================

This section is aimed at a **full-stack developer, web application architect, or product manager** who wishes to install the Web Tool for their organisation. Users should be familiar with some of the following technologies commonly involved in web and mobile app development:

- Unix and Linux
- HTML, CSS, and Javascript
- Python for server-side programming
- RESTful APIs [#f1]_ for web applications
- Git and Github for source-code distribution and version control
- Amazon Web Services EC2 (Elastic Compute Cloud)
- HTTP, HTTPS, and SSL certificates

A developer experienced with single-page apps should recognize the general architecture of the Web Tool. The Web Tool and the L4 backend which supports it are built using the following technologies:

- the Vue 3 framework for Javascript (a framework similar to React)
- the Purescript language (used for web development)
- the Haskell language (used for the interpreter)

.. rubric:: Footnotes

.. [#f1] https://www.redhat.com/en/topics/api/what-is-a-rest-api