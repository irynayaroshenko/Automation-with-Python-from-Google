"""What is Puppet?"""
# Puppet is the current industry standard for managing the configuration of computers in a fleet of machines.
# Part of the reason why Puppet is so popular is that it's a cross-platform tool that's been around for a while.
# It's an open source project that was created in 2005, and it's gone through several versions.
# The latest available version at the time this Google course went live is Puppet 6, which came out in late 2018.

# We typically deploy puppet using a client-server architecture.
# The client is known as the Puppet agent, and the service is known as the Puppet master.
# When using this model, the agent connects to the master and sends a bunch of facts that describe the computer to the
# master. The master then processes this information, generates the list of rules that need to be applied on the device,
# and sends this list back to the agent. The agent is then in charge of making any necessary changes on the computer.

# Puppet is a cross-platform application available for all Linux distributions, Windows, and MacOS.
# This means that you can use the same puppet rules for managing a range of different computers.
# What are these rules that we keep talking about?

# Let's check out a very simple example:

# class sudo {
#     package { 'sudo':
#         ensure => present,
#     }
# }

# This block is saying that the package 'sudo' should be present on every computer where the rule gets applied.
# If this rule is applied on 100 computers, it would automatically install the package in all of them.
# This is a small and simple block but can already give us a basic impression of how rules are written in puppet.

# There are various installation tools available depending on the type of OS.
# Puppet will determine the type of OS being used and select the right tool to perform the package installation.

# On Linux distributions, there are several package management systems: APT, Yum, and DNF.
# Puppet will also determine which package manager should be used to install the package.

# On MacOS, there's a few different available providers depending on where the package is coming from.
# The Apple Provider is used for packages that are part of the OS, while the MacPorts provider is used for
# packages that come from the MacPorts Project.

# For Windows, we'll need to add an extra attribute to our rule, stating where the installer file is located: on
# the local disk or a network mounted resource. Puppet will then execute the installer and make sure that it finishes
# successfully.

# If you use Chocolatey to manage your windows packages, you can add an extra Chocolatey provider to Puppet to support.

# Using rules like this one, we can get Puppet to do a lot more than just install packages for us.
# We can add, remove, or modify configuration files stored in the system, or change registry entries on Windows.
# We can also enable, disable, start, or stop the services that run on our computer.
# We can configure crone jobs, the scheduled tasks, add, remove, or modify Users and Groups or even execute external
# commands, if that's what we need.

"""Puppet Resources"""
# In Puppet, resources are the basic unit for modeling the configuration that we want to manage.
# In other words, each resource specifies one configuration that we're trying to manage, like a service, a package, or
# a file.

# Let's look at another example:

# class sysctl {
#     # Make sure the directory exists, some distros don't have it
#     file { '/etc/sysctl.d':
#         ensure => directory,
#     }
# }

# In this case, we're defining a 'file' resource. This resource type is used for managing files and directories.
# In this case, it's a very simple rule that ensures that etc/sysctl.d exists and is a directory.

# About syntax.
# In both, our last example and this one, we could see that when declaring a resource in puppet, we write them in a
# block that starts with the resource type, in this case 'file'.
# The configuration of the resource is then written inside a block of curly braces. Right after the opening curly brace,
# we have the 'title' of the resource, followed by a colon: '/etc/sysctl.d':
# After the colon come the attributes that we want to set for the resource. In this example, we're once again setting
# the 'ensure' attribute with 'directory' as the value (ensure => directory), but we could set other attributes too.

# Let's check out a different file resource:

# class timezone {
#     file { '/etc/timezone':
#         ensure => file,
#         content => "UTC\n",
#         replace => true,
#     }
# }

# In this example, we're using a 'file' resource to configure the contents of 'etc/timezone,' - file, that's used in
# some Linux distributions to determine the time zone of the computer.

# This resource has three attributes:
# 1. we explicitly say that this will be a 'file' instead of a directory or a symlink
# 2. we set the content of the file to the UTC time zone
# 3. we set the 'replace' attribute to true, which means that the contents of the file will be replaced even if the file
# already exists.

# We've now seen a couple examples of what we can do with the 'file' resource.
# There are a lot more attributes that we could set, like file permissions, the file owner, or the file modification
# time, etc.

# How do these rules turn into changes in our computers?

# When we declare a resource in our puppet rules, we're defining the desired state of that resource in the system.
# The puppet agent then turns the desired state into reality using providers. The provider used will depend on the
# resource defined and the environment where the agent is running. Puppet will normally detect this automatically
# without us having to do anything special.

# When the puppet agent processes a resource, it first decides which provider it needs to use, then passes along the
# attributes that we configured in the resource to that provider. The code of each provider is in charge of making our
# computer reflect the state requested in the resource. In these examples, we've looked at one resource at a time.

"""Puppet Classes"""
# In the examples of Puppet code that we've seen so far, we've declared classes that contain one resource.
# You might have wondered what those classes were for.

# We use these classes to collect the resources that are needed to achieve a goal in a single place.

# For example, you could have a class that installs a package, sets the contents of a configuration file, and starts the
# service provided by that package.

# Let's check out an example like that:

# class ntp {
#     package {'ntp':
#         ensure => learn_and_test
#     }
#     file { 'etc/ntp.conf':
#         sourse => 'puppet:///modules/ntp/ntp.conf'
#         replace => true,
#     }
#     service { 'ntp':
#         enable => true,
#         ensure => running,}
# }

# In this case, we have a class with three resources,: a package, a file, and a service.
# All of them are related to the Network Time Protocol, or NTP, the mechanism our computers use to synchronize clocks.
# Our rules are making sure that the NTP package is always upgraded to the latest version. We're setting the contents of
# the configuration file using the source attribute, which means that the agent will read the required contents from
# the specified location. And we're saying that we want the NTP service to be enabled and running.

# By grouping all the resources related to NTP in the same class, we only need a quick glance to understand how the
# service is configured and how it's supposed to work. This would make it easier to make changes in the future since we
# have all related resources together. It makes sense to use this technique whenever we want to group related resources.

# For example, you could have a class grouping all resources related to managing log files, or configuring the time
# zone, or handling temporary files and directories. You could also have classes that group all the settings related to
# your web serving software, your email infrastructure, or even your company's firewall.

"""Puppet Resources"""
# https://puppet.com/docs/puppet/latest/lang_resources.html
# https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/
