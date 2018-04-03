Example Flask application
=========================

This is example application which show integration of Docker **gelf** log driver with *Coralogix* logs collector.

Installation
------------

Before installation rename file **.env.example** to **.env** and write into it your *Coralogix* information.

.. code-block:: bash

    $ docker-compose up -d

Usage
-----

Now you can open your browser and write: *http://localhost:5000/hello/<name>/*, where *<name>* will be replaced with your name.
Application send log record to default logger(stdout).
And then Docker send this record to *Coralogix* service.