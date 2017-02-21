# django-project-template
[![Build Status](https://travis-ci.org/bartromgens/django-project-template.svg?branch=master)](https://travis-ci.org/bartromgens/django-project-template) [![Coverage Status](https://coveralls.io/repos/github/bartromgens/django-project-template/badge.svg?branch=master)](https://coveralls.io/github/bartromgens/django-project-template?branch=master) [![Dependency Status](https://gemnasium.com/badges/github.com/bartromgens/django-project-template.svg)](https://gemnasium.com/github.com/bartromgens/django-project-template)

django-project-template is an example Django + bootstrap project with a basic project configuration that I often use. 

Requires Python 3.4+ and Django 1.10+

#### Configuration

- Django 1.10 and Bootstrap 3 
- Example Django app
- Base page template with,
  - Top navbar with menu, sign up/log in, and user profile
  - Page content
  - Footer
- Home, About, Contact, Contribute pages
- Sign up/log in (by username or email)
- Reset/change password
- Update userprofile
- Basic tests
- Logging
- Project version as global context variable
- Daily backups
- travis-ci config
- coveralls config
- django-debug-toolbar

TODO,
- Create/load demo data
- Instructions

## Installation

## Installation (Linux)

Get the code and enter the project directory,
```
$ git clone https://github.com/django-project-template/django-project-template.git
$ cd django-project-template
```

Install in a local environment (creates a Python 3 virtualenv with dependencies, and a sqlite database file),
```
$ ./install.sh
```

Activate the virtualenv (always do this before working on the project),
```
$ source env/bin/activate
```

### Create a superuser (optional)
This allows you to login at the website as superuser and view the admin page,
```
$ python manage.py createsuperuser
```

### Run a developement webserver
Run the Django dev web server in the virtualenv (don't forget to active the virtualenv),
```
(env)$ python manage.py runserver
```

The website is now available at http://127.0.0.1:8000 and admin http://127.0.0.1:8000/admin.

### Configuration (optional)

#### Daily backups (cronjob)
This project has a django-cronjob that makes daily backups. 
These are defined in `website/cron.py`.  
Create the following cronjob (Linux) to kickstart the `django-cron` jobs,
```
$ crontab -e
*/5 * * * * source /home/<username>/.bashrc && source /home/<path-to-openkamer>/openkamer/env/bin/activate && python /home/<path-to-openkamer>/website/manage.py runcrons > /home/<path-to-openkamer>/log/cronjob.log
```

## Testing

#### Run tests
Run all tests,
```
$ python manage.py test
```

Run specific tests (example),
```
$ python manage.py test website.test.TestCaseAdminLogin
```
