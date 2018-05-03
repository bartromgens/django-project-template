# django-project-template
[![Build Status](https://travis-ci.org/bartromgens/django-project-template.svg?branch=master)](https://travis-ci.org/bartromgens/django-project-template) [![Coverage Status](https://coveralls.io/repos/github/bartromgens/django-project-template/badge.svg?branch=master)](https://coveralls.io/github/bartromgens/django-project-template?branch=master) [![Dependency Status](https://gemnasium.com/badges/github.com/bartromgens/django-project-template.svg)](https://gemnasium.com/github.com/bartromgens/django-project-template)

django-project-template is an example Django 2 + Bootstrap 4 project with a basic project configuration.

Requires Python 3.4+ and Django 2.0+

#### Configuration

- Django 2.0 and Bootstrap 4
- Example Django app, with empty views.py and models.py
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

#### TODO
- Create/load demo data

## Installation (Linux)

Get the code and enter the project directory,
```
git clone https://github.com/bartromgens/django-project-template.git
cd django-project-template
```

Install dependencies that you will need,
```
apt-get install virtualenv
```
or
```
pip install virtualenv
```

Make sure you have a recent version of pip,
```
pip install --upgrade pip
```

Create a virtual environment,
```
virtualenv -p python3 env
```

Activate the virtualenv (always do this before working on the project),
```
source env/bin/activate
```

Install python packages in the local env,
```
pip install -r requirements.txt
```

Generate a `local_settings.py` file from the example,
```
python create_local_settings.py
```

Create a database (default is sqlite),
```
python manage.py migrate
```

#### Create a superuser (optional)
This allows you to login at the website as superuser and view the admin page,
```
python manage.py createsuperuser
```

#### Run a developement webserver
Run the Django dev web server in the virtualenv (don't forget to active the virtualenv),
```
python manage.py runserver
```

The website is now available at http://127.0.0.1:8000 and admin http://127.0.0.1:8000/admin.

## Configuration (optional)

#### local_settings.py

The local settings are defined in `website/local_settings.py`. 
These are not under version control and you are free change these for your personal needs.
This is also the place for secret settings. An example, on which this file is based, is found in `website/local_settings_example.py`.

#### Daily backups (cronjob)
This project has a django-cronjob that makes daily backups of the raw database (includes everything), and a json dump of the data.
These are defined in `website/cron.py`. The location of the backup files is defined in `website/local_settings.py`. 
Create the following cronjob (Linux) to kickstart the `django-cron` jobs,
```
$ crontab -e
*/5 * * * * source /home/<username>/.bashrc && source /home/<path-to-project>/env/bin/activate && python /home/<path-to-project>/website/manage.py runcrons > /home/<path-to-project>/log/cronjob.log
```

## Testing

Run all tests,
```
python manage.py test
```

Run specific tests (example),
```
python manage.py test website.tests.TestCaseAdminLogin
```

## Logging
There are 3 log files (`debug.log`, `error.log`, `django.log`) available, with different log levels and for different applications.
The log files are found in the `log` directory of the project.
The log statements contain the time, log level, file, class, function name and line. 

The log something, create a logger at the top of you python file,
```python
import logging
logger = logging.getLogger(__name__)
```
then create a log statement as follows,
```python
logger.debug('an info log message')
logger.info('an info log message')
logger.warning('a warning log message')
logger.error('a error log message')
logger.exception(exception_object)
```
