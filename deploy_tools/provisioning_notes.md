# Provisioning a new site

## Required packages:

* nginx
* Python 3.6
* virualenv + pip
* Git

eg, on Ubuntu

	sudo add-apt-repository ppa:fkrull/deadsnakes
	sudo apt-get instlal nginx git python36 python3.6-venv
	
## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com
* replace STG_FOLDER with, e.g., www.staging.friedassuperlists.de

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com 
* replace STG_FOLDER with, e.g., www.staging.friedassuperlists.de

## Folder structure
Assume we have a user account at /home/username

/home/username

	|___sites
		|___SITENAME
				|-- database
				|-- source
				|-- static
				|-- virtualenv