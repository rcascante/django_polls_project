# DJANGO POLLS PROJECT

Replication of polls following the instructions written in https://docs.djangoproject.com/en/2.1/intro/tutorial01/

It consist of two parts:

- A public site that lets people view polls and vote in them.
- An admin site that lets you add, change, and delete polls.

## Table of Contents
1. Implementation

## Implementation
### Dependencies
1. virtualenvironment
2. virtualenvwrapper
3. Django 2.1.1

## Instalation 
### Installation  virtualenvironment and virtualenvwrapper
Follow this instructions if you don't have some of this dependencies not installed
1. `sudo pip install virtualenv`
2. `sudo pop install virtualenvwrapper`
3. `vim .profile`paste the code snippet below 
```
# Start virtualenvwrapper
# https://virtualenvwrapper.readthedocs.io/en/latest/install.html
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
4. `esc :wq`to exit vim and save the changes

### Creation of virtualenvironment and installation of project dependencies
1. Clone repository `git clone https://github.com/rcascante/django_polls_project.git`
2. Go to the directory where you cloned the repository
3. Create virtualenvironment `mkvirtualenv -a project_name -p python3 project_name`
4. Activate de virtualenvironment `workon project_name``
5. `pip install Django==2.1.1`

