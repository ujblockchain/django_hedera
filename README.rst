.. image:: https://blockchain.uj.ac.za/static/images/main-logo.png


=============================================
Demystifying Blockchain April Edition 2024 
=============================================

South Africa-Switzerland Bilateral Research Chair in Blockchain Technology (UJ Blockchain) aims to explore blockchain 
integrations with real-world applications and development in Agric food.

============

Setup
==========

Set environment variable for Django Secret Key, Debug, Allowed Host, and Admin Path. Also add configuration for
Django Axes and Email with SMTP Host.


.. code-block:: bash
    SECRET_KEY = '...'
    DEBUG = ..
    ALLOWED_HOSTS = '...'
    ADMIN_PATH = '...'

    ENGINE = '...'
    NAME = '...'
    HOST = '...'
    USER = '...'
    PASSWORD = '...'
    PORT = '...'

    SILENCED_SYSTEM_CHECKS = '...'
    AXES_FAILURE_LIMIT = '...'
    AXES_COOLOFF_TIME = '...'
    AXES_ONLY_ADMIN_SITE = '...'
    AXES_USERNAME_FORM_FIELD = '...'
    AXES_RESET_ON_SUCCESS = '...'
    AXES_NEVER_LOCKOUT_WHITELIST = '...'
    AXES_IP_WHITELIST = '...'
    AXES_ENABLE_ACCESS_FAILURE_LOG = '...'
    AXES_RESET_ON_SUCCESS = '...'
    AXES_LOCKOUT_PARAMETERS = '...'

    EMAIL_BACKEND = '...'
    EMAIL_PORT = '...'
    EMAIL_HOST = '...'
    EMAIL_HOST_USER = '...'
    EMAIL_HOST_PASSWORD = '...'
    DEFAULT_FROM_EMAIL = '...'
    SERVER_EMAIL = '...'
    EMAIL_SUBJECT_PREFIX = '...'
    EMAIL_USE_TSL = '...'


Recaptcha Setup
----------------

Set *google recaptcha* public and private key in environment variables. Public and private key can be gotten from *https://developers.google.com/recaptcha/*. Ensure you use :emphasis:`reCAPTCHA v3`.

.. code-block:: python

    RECAPTCHA_PUBLIC_KEY = '...'
    RECAPTCHA_PRIVATE_KEY = '...'
    RECAPTCHA_REQUIRED_SCORE = '...'


Running Project
----------------

Setup
^^^^^^^^^^^
.. code-block:: bash

    make setup


create Superuser
^^^^^^^^^^^^^^^^^^
.. code-block:: bash

    make superuser


Run Server
^^^^^^^^^^^
.. code-block:: bash

    make runserver


