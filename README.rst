Docker
======

Coralogix provides Docker logs integration with *gelf* driver.

Usage
-----

Before usage you must provide four variables:

* **PRIVATE_KEY** - A unique ID which represents your company, this Id will be sent to your mail once you register to Coralogix.
* **COMPANY_ID** - A unique number which represents your company. You can get your company id from the settings tab in the Coralogix dashbaord.
* **APP_NAME** - The name of your environment, for example, a company named *“SuperData”* would probably insert the *“SuperData”* string parameter or if they want to debug their test environment they might insert the *“SuperData–Test”*.
* **SUB_NAME** - Your application probably has multiple components, for example: Backend servers, Middleware, Frontend servers etc. in order to help you examine the data you need, inserting the subsystem parameter is vital.

Example
-------

If you run container manualy:

.. code-block:: bash

    $ docker run -dit \
    $ -e PRIVATE_KEY="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" \
    $ -e COMPANY_ID=XXXX \
    $ -e APP_NAME="simple-application" \
    $ -e SUB_NAME="backend" \
    $ --log-driver=gelf \
    $ --log-opt gelf-address=udp://syslogserver.coralogix.com:20001 \
    $ --log-opt env=PRIVATE_KEY,APP_NAME,SUB_NAME,COMPANY_ID \
    $ alpine echo "Hello world!"

Also you can use it with **docker-compose.yml**:

.. code-block:: yaml

    version: "3"
    services:
      web:
        restart: always
        build: app
        container_name: flask-app
        # Setup required parameters for Coralogix integration
        environment:
          - PRIVATE_KEY=${PRIVATE_KEY}
          - APP_NAME=${APP_NAME:-flask-app}
          - SUB_NAME=${SUB_NAME:-backend}
          - COMPANY_ID=${COMPANY_ID}
        # Setup logging driver
        logging:
          driver: gelf
          options:
            # Address of Coralogix syslog server
            gelf-address: "udp://syslogserver.coralogix.com:20001"
            # Required parameters for request
            env: "PRIVATE_KEY,APP_NAME,SUB_NAME,COMPANY_ID"
        ports:
          - "5000:5000"

Before usage you must create **.env** file with configurations or write them directly in **docker-compose.yml** file.

Example application:
--------------------

You can try to deploy our example application: `Source code <https://github.com/coralogix/docker-gelf-example>`_.
