"""Deploying Puppet Locally. Applying Rules Locally"""
# We can also use Puppet as a stand-alone application run from the command line.
# This is common when testing new configurations. It can be the preferred configuration for complex setups where
# connecting to a master is no longer the best approach.

# When using a stand-alone Puppet, the same computer processes facts, calculates the rules that need to be applied,
# and makes any necessary changes locally. So to get started with our Puppet deployment, let's first install Puppet,
# and then we can start experimenting with running rules locally.

# Puppet is available on a number of different platforms.
# We can either install it from the package management system available in the OS or download it from official website.
# Both options work fine and the best one to choose will depend on our specific needs.

# For this exercise, we'll just go with the Puppet packages provided by the Ubuntu distribution.
# We'll do that by installing the Puppet master package using 'sudo apt install puppet-master'.
# We now have the package installed and can start trying out a few rules.

# We'll begin by creating the simplest possible Puppet file and make it more complex as we improve our deployments.
# For this example, we want to use Puppet to make sure that some useful tools for debugging problems are installed
# on each computer in our fleet. To do this, we first have to create a file where we'll store the rules that we want to
# apply.

# In Puppet lingo, these files are called 'manifests', and they must end with '.pp' extension.
# So we'll create a new file called 'tools.pp' and in this file, we'll create a package resource.
# We'll start by managing the 'htop' package which is a tool similar to 'top' that can show us some extra information.
# We'll state that we want Puppet to ensure that we have this package present on our computer.
# This resource will take care of installing the package for us:

# package { 'htop':
#     ensure => present,
# }

# Let's save the file and try it out. But before actually applying the rules, we want to check that the command isn't
# present yet:

# htop
# Output:
# Command 'htop' not found, but can be installed...

# Htop isn't installed yet. Let's fix that by running our rules using (open puppet_locally_1.png):

# sudo puppet apply -v tools.pp

# The -v flag tells Puppet that we want to get verbose output which will tell us what's going on while Puppet is
# applying the rules in the file that we pass to it.
# So here, Puppet first told us that it was loading the facts. Then, that it compiled a catalog. After that, it told us
# that it was applying the current configuration. Then, that it installed the package we requested.
# Finally, it let us know that it finished applying this catalog.

# What's a 'catalog'?
# After loading all facts for a computer, the server calculates which rules actually need to be applied.
# For example, if a packet should only be installed when a certain condition is met, this condition is evaluated on
# the server side based on the gathered facts.

# Catalog is the list of rules that are generated for one specific computer once the server has evaluated all variables,
# conditionals, and functions.

# In this example, the catalog will be exactly the same as our code because the code didn't include any variables,
# functions, or conditionals. More complex sets of rules can lead to different catalogs depending on fact values.

# It's now time to check if our rules actually work.
# Let's try running the htop command again now that Puppet has installed it for us.
# Yes, this time it worked. open puppet_locally_2.png

# If our computer was misbehaving, we could now use this tool to get a better idea why. But fortunately, our computer's
# on its best behavior. Exit with 'q'.

# Let's see what happens if we try to apply the Puppet rules again now that the package is installed.
# open puppet_locally_3.png
# Puppet's smart. It noticed that the package is already installed, so it didn't try to install the package again.
# This means it applied the catalog much faster because nothing had to be changed.

"""Managing Resource Relationships"""
# The Puppet manifests that we use to manage computers in our fleet usually include a bunch of different resources that
# are related to each other. You're not going to configure a package that's not installed, and you don't
# want to start a service until both the package and the configuration are in place.

# Puppet lets us control this with 'Resource relationships'.

# Let's check this out in an example.
# We have a file called ntp.pp, that has a bunch of resources related to the 'ntp' configuration like the one we've seen
# in an earlier video. This time, on top of declaring the resources that we need to manage, we're also declaring a few
# relationships between them.

# open puppet_locally_4.png
# We see that configuration 'file' requires the NTP Package and the 'service' requires the configuration File (ntp.conf)
# This way, Puppet knows that before starting the service, the configuration file needs to be correctly set, and before
# sending the configuration file, the package needs to be installed.

# We're also declaring that the NTP 'service' should be notified if the configuration file changes. That way, if we make
# additional changes to the contents of the configuration file in the future, the service will get reloaded with the new
# settings.

# If you look closely, you might notice that the resource types are written in lowercase, but relationships like require
# or notify use uppercase for the first letter of the resource. This is part of Puppet syntax.

# We write resource types in lowercase when declaring them, but capitalize them when referring to them from another
# resource's attributes.

# At the bottom of the file, we have a call 'include ntp'
# That's how we told Puppet that we want to apply the rules described in a class. For this example, we put the
# definition of the class and the call to include the class in the same file.

# Typically, the 'class' is defined in one file and 'include' - in another.
# We'll check out examples for this in later videos.

# Let's apply these rules locally. open puppet_locally_5.png
# Great. Our rules have run and in the verbose output, we can see that it did a bunch of things.
# First, it installed the package (1), then it checked that the configuration file needed to
# be updated and so it changed its contents (2). Finally, after changing the contents of the configuration,
# Puppet knew to restart the NTP service (3).

# We see here how our Puppet rules have translated into a few different actions. That's cool, but it's about to get even
# better. Let's make a change to the configuration file by editing the ntp.com file in this directory.

# This is the configuration values by the NTP service. It's currently using a bunch of servers from ntp.org.
# But instead of those servers, we want to try out the NTP servers provided by Google. These are called
# time1.google.com, and then time2, time3, and time4. open puppet_locally_6.png

# We've made the change, save with ':wq' and rerun our Puppet rules with the new configuration file.
# open puppet_locally_7.png

# Puppet updated the configuration file with the new contents and then refresh the service, so it loaded the config.

"""Organizing Your Puppet Modules"""
# In any configuration management deployment, there's usually a lot of different things to manage. We might want to
# install some packages, copy some configuration files, start some services, schedule some periodic tasks, make sure
# some users and groups are created and have access to specific devices, and maybe execute a few commands that
# aren't provided by existing resources.

# On top of that, there might be different configurations applied to the different computers in the fleet.
# For example, workstations and laptops might include resources that aren't used on servers. Each distinct type of server
# will need its own specific setup. There's a lot of different things to manage. We need to organize all these resources
# and information in a way that helps us maintain them long-term.

# This means grouping related resources, giving the groups good names, and making sure that the organization
# will make sense to new users.

# In Puppet, we organize our manifests into modules.
# Module is a collection of manifests and associated data.

# We can put any resource we want into a module, but to keep our configuration management organized, we'll group things
# together under a sensible topic. For example, we could have a module for everything related to monitoring the
# computer's health, another one for setting up the network stack, and yet another one for configuring a web serving
# application. So the module ship the manifest in the associated data, but how is this organized?

# All manifests get stored in a directory called 'manifests'.
# The rest of the data is stored in different directories depending on what it does. The 'Files' directory includes files
# that are copied into the client machines without any changes, like the 'ntp.conf' file that we saw in our last video.

# The 'Templates' directory includes files that are preprocessed before they've been copied into the client machines.
# These templates can include values that get replaced after calculating the manifests, or sections that are only
# present if certain conditions are valid.

# There's a bunch more directories that can be part of a module depending on what exactly the module does.
# But you don't need to worry about these when creating your first puppet module. You can start with the simple module
# that just has one manifest in the 'Manifest' directory.
# This file should be called 'init.pp' and should define a class with the same name as the module that you're creating.
# Then any files that your rules use need to be stored in the 'Files' or'Templates' directories depending on whether you
# copy them directly or need to preprocess them.

# For example, this is how the NTP class that we saw in our last video looks like when turned into a module.
# open puppet_locally_8.png There's an init.pp file, which contains the NTP classes that we saw before,
# and the ntp.conf file that gets deployed onto the machine is now stored in the Files directory.

# Modules like these can look pretty much the same no matter who's using them. That's why over time, system
# administrators using puppet have shared the modules they've written, letting others use the same rules.
# By now, there's a large collection of prepackaged modules that are shipped and ready to use.
# If one of those modules does what we want, we can just install it on our Puppet server and use it in our deployments.

# Let's install the Apache module provided by Puppet Labs to check out how this works.
# We've installed the module. Let's have a quick look at its contents. First, we'll change into the directory where
# the module files are stored and list its contents. open puppet_locally_9.png
# We see the files, manifests, and templates directories that we mentioned.
# On top of that, there's a lib directory that adds functions and fact to the ones already shipped by puppet.

# The metadata.json file includes some additional data about the module we just installed, like which versions of which
# operating systems it's compatible with.

# Let's peek into the manifest directory. open puppet_locally_10.png
# That's a lot of files, like how we split the different things that we want to manage into separate modules.
# We can also split each separate functionality that we want to configure into separate manifests.
# This helps us organize our code when we make changes to it, and to see how this directory also contains its own init.pp.

# As we called out, this manifest is special. It needs to always be present because it's the first one that's read by
# puppet when a module gets included.

# So how do we include a module like this one?
# It's pretty easy. Let's create a manifest file that includes the module we've just installed:

# include ::apache

# Here, we're telling Puppet to include the Apache module.
# The double colon before the module name, lets puppet know that this is a global module. Let's save this file now and
# apply it using Puppet apply like we did before. open puppet_locally_11.png
# Our manifest was super-simple, it just includes the Apache module. But by including the module, we got puppet to apply
# all the rules run by default in the module. We now have an Apache server configured and ready to run on this machine.

"""More Information About Deploying Puppet Locally"""
# https://puppet.com/docs/puppet/latest/style_guide.html
# https://puppet.com/docs/puppetserver/latest/install_from_packages.html
