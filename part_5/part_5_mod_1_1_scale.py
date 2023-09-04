"""What is scale?"""
# Being able to scale means that we can keep achieving larger impacts with the same amount of effort when a system
# scales.

# A scalable system is a flexible one.

# Automation is an essential tool for keeping up with the infrastructure needs of a growing business.

"""What is configuration management?"""
# Imagine your team is in charge of setting up a new server.
# This could be a physical computer running close to you or a virtual machine running somewhere in the cloud.
# To get things moving, the team installs the operating system, configures some applications and services, sets up the
# networking stack, and when everything is ready, puts the server into use.
# By manually deploying the installation and configuring the computer, we see that we're using 'unmanaged configuration'

# When we say configuration here, we're talking about everything from the current operating system and the applications
# installed to any necessary configuration files or policies, including anything else that's relevant for the server to
# do its job.

# When you work in IT, you're generally in charge of the configuration of a lot of different devices, not just servers.
# Network routers, printers and even smart home devices can have configuration that we can control.

# For example, a network switch might use a config file to set up each of its ports. All right, so now we know what we
# mean when we talk about configuration.

# We said that manually deploying a server means that the configuration is unmanaged. So what would it mean for the
# configuration to be managed? It means using a 'Configuration management system' to handle all the configuration of
# the devices in your fleet, also known as 'nodes'.

# There's a bunch of different tools available depending on the devices and services involved.
# Typically, you'll define a set of rules that have to be applied to the nodes you want to manage and then have a
# process that ensures that those settings are true on each of the nodes.

# At a small scale, unmanaged configurations seem inexpensive. If you only manage a handful of servers, you might be
# able to get away with doing that without the help of automation. You could log into each device and make changes by
# hand when necessary. And when your company needs a new database server, you might just go ahead and manually install
# the OS and the database software into a spare computer. But this approach doesn't always scale well.

# The more servers that you need to deploy, the more time it will take you to do it manually.
# And when things go wrong, and they often do, it can take a lot of time to recover and have the servers back online.

# Configuration management systems aim to solve this scaling problem.
# By managing the configuration of a fleet with a system like this, large deployments become easier to work with because
# the system will deploy the configuration automatically no matter how many devices you're managing.
# When you use configuration management and need to make a change in one or more computers, you don't manually connect
# to each computer to perform operations on it. Instead, you edit the configuration management rules and then let the
# automation apply those rules in the affected machines. This way the changes you make to a system or group of systems
# are done in a systematic, repeatable way. Being repeatable is important because it means that the results will be the
# same on all the devices.

# A configuration management tool can take the rules you define and apply them to the systems that it manages, making
# changes efficient and consistent.

# Configuration management systems often also have some form of automatic error correction built-in so that they can
# recover from certain types of errors all by themselves.

# For example, say you found that some application that was being used widely in your company, was configured to be very
# insecure. You can add rules to your Configuration management system to improve the settings on all computers.
# And this won't just apply the more secure settings once. It will continue to monitor the configuration going forward.
# If a user changes the settings on their machine, the configuration management tooling will detect this change and
# reapply the settings you defined in code.

# There are lots of configuration management systems available in the IT industry today.
# Some popular systems include Puppet, Chef, Ansible, and CFEngine.

# These tools can be used to manage locally hosted infrastructure. Think bare metal or virtual machines, like the
# laptops or work stations that employees use at a company.

# Many also have some kind of Cloud integration allowing them to manage resources in Cloud environments like Amazon EC2,
# Microsoft Azure, or the Google Cloud platform, and the list doesn't stop there.

# There are some platform specific tools, like SCCM and Group Policy for Windows. These tools can be very useful in some
# specific environments, even when they aren't as flexible as the others.

# For this course, we've chosen to focus on Puppet because it's current industry standard for configuration management.
# Keep in mind though that selecting a configuration management system is a lot like deciding on a programming language
# or version control system.
# You should pick the one that best fits your needs and adapt accordingly, if necessary.
# Each has its own strengths and weaknesses. So a little research beforehand can help you decide which system is best
# suited for your particular infrastructure needs.

"""What is infrastructure as code?"""
# We've called out that when we use a configuration management system, we write rules that describe how the computers in
# our fleet should be configured. These rules are then executed by the automation, to make the computers match our
# desired state. This means that we can model the behavior of our IT infrastructure in files that can be processed by
# automatic tools. These files can then be tracked in a version control system.

# Remember, VCS help us keep track of all changes done to the files, helping answer questions like who, when, and why.
# More importantly, they're super-useful when we need to revert changes.

# Infrastructure as Code (IaC) - paradigm of storing all the configuration for the managed devices in version controlled
# files. In other words, we see that we're using Infrastructure as Code when all the configuration necessary to deploy
# and manage a node in the infrastructure is stored in version control. This is then combined with automatic tooling
# to actually get the nodes provisioned and managed.

# If you have all the details of your Infrastructure properly stored in the system, you can very quickly deploy
# a new device if something breaks down. Simply get a new machine, either virtual or physical, use the automation to
# deploy the necessary configuration, and you're done.

# The principals of Infrastructure as Code are commonly applied in cloud computing environments, where machines are
# treated like interchangeable resources, instead of individual computers. This principle is also known as
# treating your computers as cattle instead of pets because you care for them as a group rather than individually.

# This concept isn't just for managing computers in huge data centers or globe spanning infrastructures, it can work for
# anything: from servers to laptops, or even workstations in a small IT department. Even if your company only has
# a single computer working as the mail server, you can still benefit from storing all the configuration needed
# to set it up in a configuration management system. That way if the server ever stops working, you can deploy a
# replacement very quickly by simply applying the rules that configure the mail server to the new computer.

# One valuable benefit of this process is that the configuration applied to the device doesn't depend on a human
# remembering to follow all the necessary steps.

# As mentioned, having Infrastructure as Code means that we can also apply the benefits of VCS to your infrastructure.
# Since the configuration of our computers is stored in files, those files can be added to a VCS.

# This has all the benefits that VCS bring:
# - gives us an audit trail of changes,
# - lets us quickly rollback if a change was wrong,
# - lets others reviewed our code to catch errors and distribute knowledge,
# - improves collaboration with the rest of the team,
# - lets us easily check out the state of our infrastructure by looking at the rules that are committed.

# The ability to easily see what configuration changes were made and roll back to a known good state is super important.
# It can make a big difference in quickly recovering from an outage, especially since changing the contents
# of the configuration file can be as dangerous as updating the version of an application.

# On top of that, having the rules stored in files means that we can also run automated tests on them.

# In a complex or large environment, treating your IT IaC can help you deploy a flexible scalable system.
# A configuration management system can help you manage that code by providing a platform to maintain and provision
# that infrastructure in an automated way. Having your infrastructure stored as code means that you can
# automatically deploy your infrastructure with very little overhead.

# If you need to move it to a different location, it can be deployed, de-provisioned, and redeployed at scale
# in a different locale with minimal code level changes.

# Managing your Infrastructure as Code means that your fleet of nodes are:
# 1. consistent,
# 2. versioned,
# 3. reliable,
# 4. repeatable.

# Instead of being seen as precious or unique, machines are treated as replaceable resources that can be deployed
# on-demand through the automation. Any infrastructure that claims to be scalable must be able to handle
# the capacity requirements of growth.

# Performing an action like adding more servers to handle an increase in requests is just a possible first step.
# There are other things that we might need to take into account, such as the amount of traffic that network can
# handle or the load on the backend servers like databases.

# Viewing your infrastructure in this way helps your IT team adapt and stay flexible.
# The technology industry is constantly changing and evolving.
# Automation and configuration management can help you embrace that change instead of avoiding it.
