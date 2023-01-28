.. _auto_config:

=========================================================
Installations to compile an edited Natural L4 Spreadsheet
=========================================================

This section is only required if you want to edit the L4 Spreadsheet and compile a new version of the web app out of this edited L4 Spreadsheet.

---------------------------------------
Automatic configuration of the Web Tool
---------------------------------------

The following code block shows a launch and run of the hello.py script by way of gunicorn, detailed in section :ref:`6.4_gunicorn` This run shows hello.py calling natural4-exe and v8k, each detailed below.

.. code-block::

    $ gunicorn --certfile /etc/letsencrypt/live/cclaw.legalese.com/cert.pem --keyfile /etc/letsencrypt/live/cclaw.legalese.com/privkey.pem --workers=5 --bind 0.0.0.0:8081 --pythonpath /home/mengwong/pyrest/lib/python3.8/site-packages/ wsgi:app

The command-line arguments will need to be adapted to the circumstances of your local development environment. In particular, the pythonpath option may be omitted or customized to match your Python installation. See section :ref:`6.4_gunicorn` for details.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Installing the L4 interpreter: natural4-exe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This subsubsection is only required if you need to edit the web tool. You might want to edit the web tool if, for example, the law changes and you need to update content. If you are happy with the web tool as it is, you may skip this section.

The interpreter for Natural L4 is contained in the natural4-exe executable, whose source code is available at
https://github.com/smucclaw/dsl/tree/main/lib/haskell/natural4

Contact the L4 developers for a ZIP file containing natural4-exe executables compiled for the following platforms:
- Linux
- MacOS
- Windows

The executable may be recompiled from source. While the codebase is written in Haskell, no expertise in Haskell is required, beyond installing and running the “Stack” package manager and build tool [#f1]_. The stack tool plays roughly the same role for Haskell that pip does for Python and npm does for Javascript. Detailed build and install instructions are available in the Github repository above.

------------------------
Purescript configuration
------------------------

Generation of the Purescript output file is described in the previous section.

To become part of the running web app which is linked from the sidebar, the Purescript output file needs to be copied into the source tree of the Web Tool at src/RuleLib/PDPADBNO.purs. The helper script v8k available at vue-pure-pdpa/bin/v8k performs this function automatically when called by the hello.py script.

The back-end of the Web Tool consumes that file as content and configuration, which controls the Web Tool’s interactive Q&A front end user interface.

---------------
Maintaining vue
---------------

The Vue web tool distributed above originates in the smucclaw/vue-pure-pdpa repository. If it is necessary to update or upgrade the package, the above repository should be used as the main “working directory”, then changes should be synced downstream to the vue-big and vue-small copies.

Updates involving npm should be performed as far upstream as possible, meaning in vue-big, and then reflected out to the vue-small and vue-NN copies (through the symlink and the rsync respectively), to minimize the build times incurred by npm run serve.

--------------------------------------------
The L4 spreadsheet can choose a backend port
--------------------------------------------

In the L4 spreadsheet, a commented-out line at the top of the spreadsheet can contain two adjacent cells containing “devMode port” and “8081”. That will instruct pathsCode.gs to access the Pyrest endpoints on port 8081 of the backend server. If that instruction is not present, the default port is 8080.

.. _https-needed:

---------------------------------------------------
Https is needed; letsencrypt refreshes certificates
---------------------------------------------------

Both the Web Tool and gunicorn/hello.py need to be made aware of the SSL certificate paths.

gunicorn is given those paths on the command line, as seen in section :ref:`6.4_gunicorn` above.

The vue system is given those paths in ``$V8K_WORKDIR/vue-xx/vue.config.js``:

.. code-block:: 

    ┌─[20221102-23:34:05]   [mengwong@cclaw:~/wow/much/vue-04]
    └─[0] <git:(main 89d183a✱✈) > grep -1 letsencrypt vue.config.js
        https: {
        key:  fs.readFileSync('/etc/letsencrypt/live/cclaw.legalese.com/privkey.pem'),
        cert: fs.readFileSync('/etc/letsencrypt/live/cclaw.legalese.com/cert.pem')
        }

To run this system locally you will need to bring up SSL certificates for your own domain name. One popular SSL provider is https://letsencrypt.org/

Google Apps Script refuses to load image assets in the sidebar if those assets are not retrieved via https. To serve https on the backend server, pick a domain name under your control and set up an SSL certificate for that domain name. 

Configure DNS to point that domain name at your backend server. In our implementation we used Let’s Encrypt to set up and auto-refresh the SSL certificate. The files are saved under the /etc/letsencrypt directory. 

We relied on DNS resources kindly provided by industry partner Legalese.com to set up SSL certificates at the domain cclaw.legalese.com. We do not have DNS control of the Amazon AWS hostname, meaning that we have to use the cclaw.legalese.com hostname.

.. rubric:: Footnotes

.. [#f1] available at https://www.haskellstack.org/ 