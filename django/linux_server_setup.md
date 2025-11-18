# Linux Server Setup

## Step 1. Setup Server
`ssh` into the server for the first time.

Update and upgrade server.

`sudo apt-get update && apt-get upgrade`

Check if hostname is correct with

`hostname`

`hostnamectl set-hostname SERVER_NAME`

Used the following command to add the IP address and server name to the file.

`nano /etc/hosts`

## Step 2. Adding Limited User
Add a limited user for best practice.
`adduser <USER_NAME>`

Give the limited user sudo permissons.
`adduser <USER_NAME> sudo`

## Step 3. Setting Up SSH Key Vased Authentication
Add a new SSH-key on my local machine.

`ssh-keygen -b 4096`

Be sure that the `.ssh` dir exists under the user.

`mkdir .ssh`

Copy the public key to the server.

`scp ~/.ssh/<SSH_KEY> <USER_NAME>:<SERVER_IP>:~/.ssh/authorized_keys`

Limit the permissions for SSH directory.

Allowed the owner to read, write and execute, while the rest doesn't have any permissions.

`sudo chmod 700 ~/.ssh/`

Allowed the owner to read and write, while the rest doesn't have any permissions.

`sudo chmod 600 ~/.ssh/*`

## Step 4. Forbiding Root Login and Password Authentication
Used the following command to forbit `#PermitRootLogin` and `#PasswordAuthentification` by commening them out.

`PermitRootLogin yes` to `PermitRootLogin no`

`#PasswordAuthentication yes` to `PasswordAuthentication no`

`sudo nano /etc/ssh/sshd_config`


## Step 5. Setting Up A Firewall

`sudo apt-get install ufw`

`sudo ufw default allow outgoing`

`sudo ufw default deny incoming`

`sudo ufw allow ssh`

`sudo ufw allow 8000`

`sudo ufw enable`

## Step 6. Copy Django Application on to the Server

`uv pip freeze > requirements.txt`

`scp -r /folder/ user@serverip:~/`

## Step 7. Setup Virtual Environment on the Server

`sudo apt-get install python3-pip`

`sudo apt-get install python3-venv`

`python3 -m venv <PROJECT>/venv`

`source venv/bin/acticate`

`pip install -r requirements.txt`

## Step 8. Change Django Settings to reflex

`sudo nano django_project/settings.py`

and add the IP to allowed hosts list.

`python manage.py collectstatic`


## Step 9. Test Application

`python manage.py runserver 0.0.0.0:8000`

## Step 10. Apache2 & ModWSGI

`sudo apt-get install apache2`

`sudo apt-get install libapache2-mod-wsgi-py3`

`cd /etc/apache2/sites-available/`

`sudo cp 000-default.conf django_project.conf`

`sudo nano django_project.conf`

`sudo a2ensite django_project`

`sudo a2dissite 000-default.conf`

## Step 11. Update permissions

`sudo chown :www-data django_project/db.sqlite3`

`sudo chmod 664 django_project/db.sqlite3`

`sudo chown :www-data django_project/`

`sudo chmod 755 /home/<USER>/<PROJECT>/`

## Step 12. Restarting the Server & Running the Site

`sudo service apache2 restart`
