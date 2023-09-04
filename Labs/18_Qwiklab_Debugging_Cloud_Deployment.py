"""Qwiklabs Assessment: Debugging Cloud Deployment"""

# Introduction
# You're an IT administrator in a small-sized startup that runs a web server named ws01 in the cloud. One day, when you try to access the website served by ws01, you get an HTTP Error 500. Since your deployment is still in an early stage, you suspect a developer might have used this server to do some testing or run some experiments. Now you need to troubleshoot ws01, find out what's going on, and get the service back to a healthy state.

# What you'll do
# - Understand what http status code means
# - Learn how to check port status with the netstat command
# - Learn how to manage services with the systemctl command
# - Know how to monitor system resources and identify the root cause of an issue

"""Debug the issue"""
# HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped into five classes:
# https://developer.mozilla.org/en-US/docs/Web/HTTP
#
# Informational responses (100–199)
# Successful responses (200–299)
# Redirects (300–399)
# Client errors (400–499)
# Server errors (500–599)
# The HyperText Transfer Protocol (HTTP) 500 Internal Server Error response code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request. Before troubleshooting the error, you'll need to understand more about systemctl.
#
# systemctl is a utility for controlling the systemd system and service manager. It comes with a long list of options for different functionality, including starting, stopping, restarting, or reloading a daemon.
#
# Let's now troubleshoot the issue. Since the webpage returns an HTTP error status code, let's check the status of the web server i.e apache2.

# sudo systemctl status apache2

# The command outputs the status of the service.
#
# Output:
# student-04-8b85d76b1eb5@ws01:~$ sudo systemctl status apache2
# × apache2.service - The Apache HTTP Server
#      Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
#      Active: failed (Result: exit-code) since Sat 2023-08-05 10:24:00 UTC; 19s ago
#        Docs: https://httpd.apache.org/docs/2.4/
#         CPU: 28ms
#
# Aug 05 10:24:00 ws01 systemd[1]: Starting The Apache HTTP Server...
# Aug 05 10:24:00 ws01 apachectl[2602]: (98)Address already in use: AH00072: make_sock: could not bind to addre>
# Aug 05 10:24:00 ws01 apachectl[2602]: (98)Address already in use: AH00072: make_sock: could not bind to addre>
# Aug 05 10:24:00 ws01 apachectl[2602]: no listening sockets available, shutting down
# Aug 05 10:24:00 ws01 apachectl[2602]: AH00015: Unable to open logs
# Aug 05 10:24:00 ws01 apachectl[2592]: Action 'start' failed.
# Aug 05 10:24:00 ws01 apachectl[2592]: The Apache error log may have more information.
# Aug 05 10:24:00 ws01 systemd[1]: apache2.service: Control process exited, code=exited, status=1/FAILURE
# Aug 05 10:24:00 ws01 systemd[1]: apache2.service: Failed with result 'exit-code'.
# Aug 05 10:24:00 ws01 systemd[1]: Failed to start The Apache HTTP Server.

# The outputs say "Failed to start The Apache HTTP Server." This might be the reason for the HTTP error status code displayed on the webpage. Let's try to restart the service using the following command:

# sudo systemctl restart apache2

# Output:
# student-04-8b85d76b1eb5@ws01:~$ sudo systemctl restart apache2
# Job for apache2.service failed because the control process exited with error code.
# See "systemctl status apache2.service" and "journalctl -xeu apache2.service" for details.

# Hmm this command also fails. Let's check the status of the service again and try to find the root cause of the issue.

# sudo systemctl status apache2

# Output:
# student-04-8b85d76b1eb5@ws01:~$ sudo systemctl status apache2
# × apache2.service - The Apache HTTP Server
#      Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
#      Active: failed (Result: exit-code) since Sat 2023-08-05 10:25:05 UTC; 18s ago
#        Docs: https://httpd.apache.org/docs/2.4/
#     Process: 3020 ExecStart=/usr/sbin/apachectl start (code=exited, status=1/FAILURE)
#         CPU: 22ms
#
# Aug 05 10:25:05 ws01 systemd[1]: Starting The Apache HTTP Server...
# Aug 05 10:25:05 ws01 apachectl[3023]: (98)Address already in use: AH00072: make_sock: could not bind to addre>   !!!
# Aug 05 10:25:05 ws01 apachectl[3023]: (98)Address already in use: AH00072: make_sock: could not bind to addre>
# Aug 05 10:25:05 ws01 apachectl[3023]: no listening sockets available, shutting down
# Aug 05 10:25:05 ws01 apachectl[3023]: AH00015: Unable to open logs
# Aug 05 10:25:05 ws01 apachectl[3020]: Action 'start' failed.
# Aug 05 10:25:05 ws01 apachectl[3020]: The Apache error log may have more information.
# Aug 05 10:25:05 ws01 systemd[1]: apache2.service: Control process exited, code=exited, status=1/FAILURE
# Aug 05 10:25:05 ws01 systemd[1]: apache2.service: Failed with result 'exit-code'.
# Aug 05 10:25:05 ws01 systemd[1]: Failed to start The Apache HTTP Server.

# Take a close look at the output. There's a line stating "Address already in use: AH00072: make_sock: could not bind to address [::]:80." The Apache webserver listens for incoming connection and binds on port 80. But according to the message displayed, port 80 is being used by the other process, so the Apache web server isn't able to bind to port 80.
#
# To find which processes are listening on which ports, we'll be using the netstat command, which returns network-related information. Here, we'll be using a combination of flags along with the netstat command to check which process is using a particular port:

# sudo netstat -nlp

# Output:
# student-04-8b85d76b1eb5@ws01:~$ sudo netstat -nlp
# Active Internet connections (only servers)
# Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
# tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      433/systemd-resolve
# tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      862/sshd: /usr/sbin
# tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1545/python3
# tcp6       0      0 :::22                   :::*                    LISTEN      862/sshd: /usr/sbin
# udp        0      0 127.0.0.53:53           0.0.0.0:*                           433/systemd-resolve
# udp        0      0 10.182.0.2:68           0.0.0.0:*                           430/systemd-network
# udp        0      0 127.0.0.1:323           0.0.0.0:*                           1369/chronyd
# udp6       0      0 ::1:323                 :::*                                1369/chronyd
# raw6       0      0 :::58                   :::*                    7           430/systemd-network
# Active UNIX domain sockets (only servers)
# Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
# unix  2      [ ACC ]     STREAM     LISTENING     14301    1/init               @/org/kernel/linux/storage/multipathd
# unix  2      [ ACC ]     STREAM     LISTENING     1502     1/init               /run/systemd/private
# unix  2      [ ACC ]     STREAM     LISTENING     1504     1/init               /run/systemd/userdb/io.systemd.DynamicUser
# unix  2      [ ACC ]     STREAM     LISTENING     1505     1/init               /run/systemd/io.system.ManagedOOM
# unix  2      [ ACC ]     STREAM     LISTENING     14299    1/init               /run/lvm/lvmpolld.socket
# unix  2      [ ACC ]     STREAM     LISTENING     14304    1/init               /run/systemd/fsck.progress
# unix  2      [ ACC ]     STREAM     LISTENING     14316    1/init               /run/systemd/journal/stdout
# unix  2      [ ACC ]     SEQPACKET  LISTENING     14319    1/init               /run/udev/control
# unix  2      [ ACC ]     STREAM     LISTENING     1542     170/systemd-journal  /run/systemd/journal/io.systemd.journal
# unix  2      [ ACC ]     STREAM     LISTENING     16470    433/systemd-resolve  /run/systemd/resolve/io.systemd.Resolve
# unix  2      [ ACC ]     STREAM     LISTENING     17923    1/init               /var/snap/lxd/common/lxd/unix.socket
# unix  2      [ ACC ]     STREAM     LISTENING     17928    1/init               /var/snap/lxd/common/lxd-user/unix.socket
# unix  2      [ ACC ]     STREAM     LISTENING     16829    1/init               /run/dbus/system_bus_socket
# unix  2      [ ACC ]     STREAM     LISTENING     16842    1/init               /run/snapd.socket
# unix  2      [ ACC ]     STREAM     LISTENING     16844    1/init               /run/snapd-snap.socket
# unix  2      [ ACC ]     STREAM     LISTENING     16846    1/init               /run/uuidd/request
# unix  2      [ ACC ]     STREAM     LISTENING     16841    1/init               @ISCSIADM_ABSTRACT_NAMESPACE

# You can see a process ID (PID) and an associated program name that's using port 80. A python3 program is using the port.
#
# Note: Jot down the PID of the python3 program in your local text editor, which will be used later in the lab.
#
# Let's find out which python3 program this is by using the following command:

# ps -ax | grep python3

# Output:
# student-04-8b85d76b1eb5@ws01:~$ ps -ax | grep python3
#     588 ?        Ss     0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
#     741 ?        Ssl    0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
#    1545 ?        Ss     0:00 python3 /usr/local/bin/jimmytest.py
#    3141 pts/0    R+     0:00 grep --color=auto python3
# student-04-8b85d76b1eb5@ws01:~$ cat /usr/local/bin/jimmytest.py


# There is a list of python3 processes displayed here. Now, look out for the PID of the process we're looking for and match it with the one that's using port 80 (output from netstat command).
#
# You can now obtain the script /usr/local/bin/jimmytest.py by its PID, which is actually using port 80.
#
# Have a look at the code using the following command:

# cat /usr/local/bin/jimmytest.py

# This is indeed a test written by developers, and shouldn't be taking the default port.
#
# Let's kill the process created by /usr/local/bin/jimmytest.py by using the following command:

# sudo kill [process-id]

# Replace [process-id] with the PID of the python3 program that you jotted down earlier in the lab.
#
# List the processes again to find out if the process we just killed was actually terminated.

# ps -ax | grep python3

# This time you'll notice that similar process running again with a new PID.
#
# This kind of behavior should be caused by service. Since this is a python script created by Jimmy, let's check for the availability of any service with the keywords "python" or "jimmy".

# sudo systemctl --type=service | grep jimmy

# Output:
# student-04-8b85d76b1eb5@ws01:~$ sudo systemctl --type=service | grep jimmy
#   jimmytest.service                              loaded failed failed Jimmy python test service

# There is a service available named jimmytest.service. We should now stop and disable this service using the following command:

# sudo systemctl stop jimmytest && sudo systemctl disable jimmytest

# Output:
# student-04-8b85d76b1eb5@ws01:~$ sudo systemctl stop jimmytest && sudo systemctl disable jimmytest
# Removed /etc/systemd/system/default.target.wants/jimmytest.service.

# The service is now removed.
#
# To confirm that no processes are listening on 80, using the following command:

# sudo netstat -nlp

# Output:
# student-04-8b85d76b1eb5@ws01:~$ sudo netstat -nlp
# Active Internet connections (only servers)
# Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
# tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      433/systemd-resolve
# tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      862/sshd: /usr/sbin
# tcp6       0      0 :::22                   :::*                    LISTEN      862/sshd: /usr/sbin
# udp        0      0 127.0.0.53:53           0.0.0.0:*                           433/systemd-resolve
# udp        0      0 10.182.0.2:68           0.0.0.0:*                           430/systemd-network
# udp        0      0 127.0.0.1:323           0.0.0.0:*                           1369/chronyd
# udp6       0      0 ::1:323                 :::*                                1369/chronyd
# raw6       0      0 :::58                   :::*                    7           430/systemd-network

# Since there are no processes listening on port 80, we can now start apache2 again.

# sudo systemctl start apache2

# Refresh the browser tab that showed 500 Internal Server Error! Or you can open the webpage by typing the external IP address of ws01 in a new tab of the web browser. The external IP address of ws01 can be found in the Connection Details Panel on the left-hand side.

# You should now be able to see the Apache2 Ubuntu Default Page.