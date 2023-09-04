"""What are domain-specific languages (DSL)?"""
# Up until now, we've seen examples of very simple Puppet rules they just define one or more resources.
# These resources are the building blocks of Puppet rules, but we can do much more complex operations
# using Puppet's domain specific language or DSL.

# Typical programming languages like Python, Ruby, Java or Go are general purpose languages that can be used to write
# lots of different applications with different goals and use cases.

# On the flip side, a domain specific language is a programming language that's more limited in scope.
# Learning a DSL is usually much faster and easier than learning a general purpose programming language because there's
# a lot less to cover. You don't need to learn as much syntax or understand as many keywords or taking to account a lot
# of overhead in general.

# In the case of Puppet, the DSL is limited to operations related to 'when' and 'how' to apply configuration management
# rules to our devices.

# For example, we can use the mechanisms provided by the DSL to set different values on laptops or desktop computers,
# or to install some specific packages only on the company's web servers.

# On top of the basic resource types, Puppet's DSL includes variables, conditional statements, and functions.
# Using them, we can apply different resources or set attributes to different values depending on some conditions.
# Before we jump into an example of what that looks like, let's talk a bit about Puppet facts.

# Facts - variables that represent the characteristics of the system.
# When the Puppet agent runs, it calls a program called 'factor' which analyzes the current system, storing the
# information it gathers in these facts. Once it's done, it sends the values for these facts to the server,
# which uses them to calculate the 'rules' that should be applied.

# Puppet comes with a bunch of baked-in core facts that store useful information about the system like what the current
# OS is, how much memory the computer has, whether it's a virtual machine or not, or what the current IP address is.
# If the information we need to make a decision isn't available through one of these facts, we can also write a script
# that checks for the information and turns it into our own custom fact.

# Let's check out an example of a piece of Puppet code that makes use of one of the built-in facts:

# if $facts['is_virtuel'] {
#     package { 'smartmontools':
#         ensure => purged,
#     }
# } else {
#     package { 'smartmontools':
#         ensure => installed,
#     }
# }

# This piece of code is using the 'is-virtual' fact together with a conditional statement to decide whether
# the 'smartmontools' package should be installed or purged. This package is used for monitoring the state of hard
# drives using 'smart'. So it's useful to have it installed in physical machines, but it doesn't make much sense to
# install it in our virtual machines.

# We can see several of the characteristics of Puppets domain specific language in this block.

# First, 'facts' is a variable. All variable names are preceded by a dollar sign ($) in Puppet's DSL.
# In particular, the 'facts' variable is what's known as a 'hash' in the Puppet DSL, which is equivalent to a dict in
# Python. This means that we can access the different elements in the hash using their keys. In this case, we're
# accessing the value associated to the is virtual key.

# Second, we see how we can write a conditional statement using 'if-else', enclosing each block of the conditional with
# curly braces ({}).

# Finally, each conditional block contains a 'package' resource.

# Every resource starts with the type of resource being defined. In this case, package and the contents of the resource
# are then enclosed in curly braces. Inside the resource definition, the first line contains the title followed by a
# colon. Any lines after that are attributes that are being set.
# We use '=>' than to assign values to the attributes and then each attribute ends with a comma.

# We've now covered a large chunk of puppet's DSL syntax. If you look back to what it was like to learn your first
# programming language, you'll probably notice how much less syntax there is to learn here.
# That's typical of the domain specific languages used by configuration management tools. While each tool uses their own
# DSL, they're usually very simple and can be learned very quickly.

"""The Driving Principles of Configuration Management"""
# Up to now, we've seen a few examples of what Puppet rules look like, including a bunch of different resources and even
# a conditional expression. You might have noticed that in all the examples we've checked out, we were never telling the
# computer the steps it should follow in order to do what we wanted.

# Instead, we were just declaring the end goal that we wanted to achieve.
# The providers, that we mentioned earlier, like APT and Yum are the ones in charge of turning our goals into whatever
# actions are necessary. We say that Puppet uses a declarative language because we declare the state that we want to
# achieve rather than the steps to get there.

# Traditional languages like Python or C are called procedural because we write out the procedure that the computer
# needs to follow to reach our desired goal.
# When it comes to configuration management, it makes sense to simply state what the configuration should be,
# not what the computer should do to get there.

# Say you're using a resource to declare that you want a package installed: you don't care what commands a computer
# has to run to install it, you only care that after the configuration management tool has run, the package is installed

# Another important aspect of configuration management is that operations should be IDEMPOTENT.
# In this context, an idempotent action can be performed over and over again without changing the system after
# the first time the action was performed, and with no unintended side effects.

# Let's check this out with an example of a 'file' resource:

# file { '/etc/issue':
#     mode => '0644',
#     content => "Internal system \l \n",
# }

# This resource ensures that the '/etc/issue' file has a set of permissions and a specific line in it.
# Fulfilling this requirement is an idempotent operation: if the file already exists and has the desired content,
# then Puppet will understand that no action has to be taken.
# If the file doesn't exist, then puppet will create it.
# If the contents or permissions don't match, Puppet will fix them.

# No matter how many times the agent applies the rule, the end result is that this file will have the requested contents
# and permissions.

# Idempotency is a valuable property of any piece of automation.
# If a script is idempotent, it means that it can fail halfway through its task and be run again without problematic
# consequences.

# Say you're running your configuration management system to set-up a new server.
# Unfortunately, the setup fails because you forgot to add a second disk to the computer and the configuration required
# two disks. If your automation is idempotent, you can add the missing disk and then have the system pick up from where
# it left off.

# Most Puppet resources provide idempotent actions, and we can rest assured that two runs of the same set of rules will
# lead to the same end result.

# An exception to this is the 'exec' resource, which runs commands for us.
# The actions taken by the exec resource might not be idempotent since a command might modify the system each time it's
# executed. To understand this, let's check out what happens when we execute a command that moves a file on our computer

# open not_idempotent _exec.png

# First, we'll check that the example.txt file is here, and then we'll move it to the desktop directory.
# This works fine now, but what happens if we run the exact same command again after it's been executed once?
# We receive an error because the file is no longer in the same place.
# In other words, this was not an idempotent action, as executing the same action twice produced a different result and
# the unintended side effect of an error.

# If we were running this inside Puppet, this would cause our Puppet run to finish with an error.
# So if we need to use the 'exec' resource to run a command for us, we need to be careful to ensure that the action is
# idempotent.

# We could do that for example by using the 'onlyif' attribute like this:

# exec { 'move example file':
#     command => 'mv /home/user/example.txt /home/user/Desctop',
#     onlyif => 'test -e /home/user/example.txt',
# }

# Using the 'onlyif' attribute, we specified that this command should be executed only if the file that we want to move
# exists. This means that the file will be moved if it exists and nothing will happen if it doesn't.

# By adding this conditional, we've taken an action that's not idempotent and turned it into an idempotent one.

# Another important aspect of how configuration management works is the 'TEST and REPAIR' paradigm.
# This means that actions are taken only when they are necessary to achieve a goal.

# Puppet will first test to see if the resource being managed like a file or a package, actually needs to be modified.
# If the file exists in the place we want it to, no action needs to be taken.
# If a package is already installed, there's no need to install it again.
# This avoids wasting time doing actions that aren't needed.

# Finally, another important characteristic is that Puppet is STATELESS, this means that there's no state being
# kept between runs of the agent.

# Each Puppet run is independent of the previous one, and the next one. Each time the puppet agent runs,
# it collects the current facts. The Puppet master generates the rules based just on those facts,
# and then the agent applies them as necessary.


"""More Information About Configuration Management"""
# https://en.wikipedia.org/wiki/Domain-specific_language
# http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html
