# work-genie 0.0.5

Work Genie is a peer to peer marketplace for online freelancer services, built using the Python web framework Django


**Features**
    <ul>
        <li>A two sided marketplace which is suitable for crowdsourcing idea.</li>
        <li>Facebook OAuth</li>
        <li>Administration Dashboard for Super Admin.</li>
        <li>Payment Gateway with Braintree/PayPal.</li>
        <li>Uploading photos from client to server side.</li>
        <li>Dashboard for end-users.</li>
        <li>Creating Review for gigs.</li>
    </ul>



## Getting Started

Working Environment
===================

You have several options in setting up your working environment.  We recommend
using virtualenv to separate the dependencies of your project from your system's
python environment.  If on Linux or Mac OS X, you can also use virtualenvwrapper to help manage multiple virtualenvs across different projects.

Virtualenv Only
---------------

First, make sure you are using virtualenv (http://www.virtualenv.org). Once
that's installed, create your virtualenv::

    $ virtualenv workgenie

You will also need to ensure that the virtualenv has the project directory
added to the path. Adding the project directory will allow `django-admin.py` to
be able to change settings using the `--settings` flag.


### Prerequisites

```
Python Version 3.6.2
Django Version 1.9.5

See requirements.txt
```

### Installing

How to get development env running:

Make sure the correct versions of Python and Django are installed on your system. Fire command prompt and run command:

```
source myvirtualenv/workgenie/bin/activate
python manage.py runserver
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Chris Bradshaw** - *Version 0.0.5* - [chrisbradshaw](https://github.com/chrisbradshaw)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Coming soon

