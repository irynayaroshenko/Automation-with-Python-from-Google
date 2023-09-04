"""VCS"""
# A Version Control System keeps track of the changes that we make to our files.
# With a VCS, you can view, track and select snapshots from the history of your project.

# Since we can use a VCS to store both code and configuration files, we can make the overall IT systems more scalable
# and reliable.

# DNS zone file is a configuration file that specifies the mappings between IP addresses and host names in your network.

# Example:
# The configuration for a DHCP damon can be replicated in two or more machines, where one acts as a primary server
# and the other one acts as standby machine. The standby machines won't do much while the primary is up.
# But if the primary goes down for any reason, a standby machine can become primary and start responding to DHCP queries.
# For this to work, the configuration files on all machines need to be identical.
# This is because the DHCP protocol doesn't provide a way for standby machines to get an up-to-date version of
# the configuration files and the way DNS does. To deal with this, we can keep the up-to-date version of the DHCP
# configuration in VCS and have the machines download the configuration from the VCS.
# This means all the machines will have the exact same files.
# Say you get an urgent alert over the weekend, telling you that your DHCP server isn't responding to any queries.
# You look at the history of the changes and find that one of the changes added on Friday evening, included a duplicated
# entry causing the server to misbehave. By using a VCS, you can easily roll back the change and have the servers back
# to health in no time. You might come across a second unexpected benefit, when it's time to replace the server with
# a new one. By having all the server configuration and a version control system, it's much easier to automate
# the task of deploying a new server.
