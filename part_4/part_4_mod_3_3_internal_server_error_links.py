"""Internal Server Error"""
# A colleague has alerted us that a webpage on our Web server isn't working.
# We asked our colleague for more details, and they told us that the failing webpage is at site.example.com/logs.
# open internal_server_error_1.png

# Let's check out if this is failing for us as well. There it is, the server responded with a 500 error.
# This error usually means that something on the server side of the application crashed, but we have no idea what.
# We'll need to investigate to find out more information.

# Let's connect to the Web server and try to figure out what's up:

# ssh webserver

# The first step is looking at logs, as we called out on Linux systems, logs are located in /var/log.
# To do that, we'll use the 'date' command to check the current date.

# date

# Let's change into that directory and check out if there are any recent logs about our error and then the 'ls -lt'
# command which sorts the files by the last modified date connecting it to the 'head' command to keep the top 10 lines:

# cd /var/log/
# ls -lt | head

# open internal_server_error_2.png

# We just triggered the error but there doesn't seem to be anything recent in the logs.
# Just in case, let's check out the last lines insists log using 'tail' - nothing interesting here,
# open internal_server_error_3.png

# tail syslog

# We need to figure out how we can get more information, but we don't even know which web surfing software is being used
# on this computer.
# But we do know that the Web server is running on port 80, the default web serving port.

# How can we find which software is listening on port 80?
# We can use the 'netstat' command which can give us a bunch of information about our network connections depending on
# the flags we pass. This command accesses a bunch of sockets that are restricted to 'root' administrator user on Linux.
# So we'll need to call it with 'sudo' which lets us run commands as root, and pass a bunch of flags netstat.
# '-n' to print numerical addresses instead of resolving host names.
# 'l' to only check out the sockets that are listening for connection.
# 'p' to print the process ID and name to which each socket belongs.

# Since we only care about port 80, we'll connect the output to 'grep' checking for ':80'.

# sudo netstat -nlp | grep :80


# open internal_server_error_4.png
# The process listening in port 80 is called "nginx" - one of the popular web serving applications out there.
# We now want to check out the configuration for our site. Configuration files on Linux are stored in the 'etc/' dir.
# So let's look at 'etc/nginx':

# ls -l /etc/nginx/

# open internal_server_error_5.png
# There's a bunch of files here. Lots of different configuration options that you can set in the Web server. We're
# looking for the configuration related to a specific site.
# So let's look at etc/nginx/sites-enabled:

# ls -l /etc/nginx/sites-enabled/

# open internal_server_error_6.png
# There are two files here one for the default site and one for the site.example.com that's the one we want.
# Let's open it with the VI (vim) editor.

# vim /etc/nginx/sites-enabled/site.example.com.conf

# open internal_server_error_7.png
# There's not a lot here, but at the bottom we see that it says 'uwsgi_pass', and then the local host address followed
# by a different port number. It seems that this website isn't being served directly from nginx, instead,
# the software is passing the control of the connections to uWSGI which is a common solution used to connect
# a Web server to programs that generate dynamic pages.

# So let's see if we can find the configuration for that one.
# Exit VI with ':q' and then see if there's anything interesting in etc/uwsgi.

# ls -l /etc/uwsgi/

# open internal_server_error_8.png
# Here we only see two directories: apps-available and apps-enabled.
# Let's say it's an apps-enabled. We found the uWSGI configuration for our site. Let's check it out.

# ls -l /etc/uwsgi/apps-enabled/
# vi /etc/uwsgi/apps-enabled/site.example.com.ini

# open internal_server_error_9.png  This file has a lot more information. open internal_server_error_10.png
# We see that the main directory for the application is srv/site.example.com that the applications run as
# www-data User (uid) and Group (gid), that it's running a Python3 script called prod.py, that the log is stored in
# /var/log/site.log and a bunch of other things.

# Let's use this extra information and see if we can find out what's that.
# Exit with ':q' once more and then check out that log file.

# ls -l site.log

# open internal_server_error_11.png
# Weird, the log file has a size of zero, that doesn't seem right. Let's see if we can find out anything else by looking
# at the Python script that's executed by uwsgi /srv/site.example.com/prod.py:

# vi /srv/site.example.com/prod.py

# open internal_server_error_12.png
# There's a few different webpages configured in this file. It uses bottle which is a Python module to generate dynamic
# web pages. At the bottom, we see the configuration for the logs page that's currently failing.

# A colleague left a comment saying that we can get debugging information by uncommenting the line that
# calls bottle.debug().

# To uncomment this line, we need to have write access to the file though, and VI is open in read only mode currently.
# Let's exit an open again with 'sudo' to be able to modify it:

# sudo vi /srv/site.example.com/prod.py

# open internal_server_error_13.png
# We've made the change, let's save it (:wq) and reload uwsgi as the instructions say. We'll do this by running sudo
# service uwsgi reload:

# sudo service uwsgi reload

# We've added debugging information. Hopefully, that will tell us why the pages failing. Reload the website to see
# what happens.This time we see a trace back of the error, and we see that the issue is that the application is getting
# a 'Permission denied' error when trying to open /var/log/site.log. open internal_server_error_14.png

# Remember that we thought it was weird that the file was empty, it seems that it's somehow broken.
# Let's check if there are any other files that start with 'site':

# ls -l site*

# open internal_server_error_15.png
# So there's a site.log file and a site.log.1 file. That's pretty common when using log rotate to rotate the logs and
# avoid them getting too big. But there's something else afoot here.

# See how one file belongs to the 'root' user and the other belongs to the www-data user?
# If you look at the permissions of the file, you might notice that they are set to allow the owner to
# write them and the owner and the group to read them, but the rest of the users can't access them.
# We saw earlier that the application is running with the www-data user. So if site.log belongs to the root user,
# the application won't be able to either read or write to this log file.
# Seems like we found the root cause of our issue.
# Let's change the owner of the site.log file to fix the immediate problem:

# sudo chown www-data.www-data site.log

# Reload our page now. It works. open internal_server_error_16.png

# The log is empty now because the application have not been able to write to it. But if we keep reloading,
# we'll see how it populates with our entries. open internal_server_error_17.png

# We've fixed the immediate problem our Web pages working once again, but we still need to take care
# of the long-term remediation.

# Why was the ownership of the file wrong? We suspect that there might be something wrong with the log rotate
# configuration, but we'd need to keep looking to find out what's up with that.

"""Resources for Understanding Crashes"""
# There's a ton of different reasons why a computer might crash. This Scientific American article
# https://www.scientificamerican.com/article/why-do-computers-crash/
#  discusses many of the possible reasons, including hardware problems and issues with the overall operating system or
#  the applications on top.
#
# On Linux or MacOS, the worst kind of crash is called Kernel Panic. On Windows, it's known as the Blue Screen of Death.
#
# https://en.wikipedia.org/wiki/Blue_Screen_of_Death
# These are situations where the computer completely stops responding and only a reboot can make it work again.
# They don't happen often, but it's good to understand what they mean: the whole OS encountered an error, and it can't
# recover.
#
# We called out that reading logs is super important. You should know how to read logs on the OS that you're using.
# Here are some resources for this:

# How to find logs on Windows 10 https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/
# How to view the System Log on a Mac https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/
# How to check system logs on Linux https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm

# You also need to be familiar with the tools available in your OS to diagnose problems. These are the tools we called
# out, but you don't need to limit yourself to them:

# Process Monitor for Windows (Microsoft) https://docs.microsoft.com/en-us/sysinternals/downloads/procmon
# Linux strace command tutorial for beginners (HowtoForge) https://www.howtoforge.com/linux-strace-command/
# How to trace your system calls on Mac OS (/etc/notes) http://neurocline.github.io/dev/2015/05/24/Tracing-System-Calls.html