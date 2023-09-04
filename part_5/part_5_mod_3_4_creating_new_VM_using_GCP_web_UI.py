"""Creating a New VM Using the GCP Web UI"""
# Let's get started with creating a virtual machine on our Google Cloud Platform (GCP) project.
# We'll kick things off by navigating to console.cloud.google.com, which is where you'll find the cloud console for GCP.
# Here, the first step is to create a project so that our VMs are associated to that project. We need to give our
# project a name, let's name it 'First Cloud Steps'. Our project is being created, it takes a couple of seconds.
# Now that we have a project, our dashboard has a lot more info. open GCP_1.png

# Next, we want to go to the menu entry that lets us create virtual machines. To do that, we'll go into the Compute
# Engine menu, and select the VM instances entry. This screen is pretty empty because we don't have any VMs yet.
# open GCP_2.png

# We can create a VM by pressing the 'Create' button. Here we're showing the many options that we can set for
# this VM that we're creating. We can set the name, the region and zone, the machine type, the boot disk, and so on.
# open GCP_3.png

# We'll start by calling this machine 'linux-instance'. Now it's time to select the region and zone.
# If we click on the region drop-down, we can see all the regions that are currently available to create new VMs.
# If we click on the zone drop-down we can see the zones available in that region for new VMs.
# For this example, we'll just keep the default regions.

# But as we called out, if you're deploying a service, you should select something that's close to your users.

# Next, we need to select the type of machine that we want to use. We can select between general purpose and memory
# optimized. And among each of those families, we can select a bunch of different machine types. We can select how much
# CPU and how much memory we want our VM to have. The right selection will depend on what we plan to do with computer.
# For our example, we'll just keep the default machine.

# After selecting the VM, we need to select the disk that we want to use.
# The default disk is 10 Gb in size and comes with a Debian image on it. We can select a different size or
# different OS by clicking on the Change button. There's a long list of available operating systems to choose from.
# The right option will depend on what you're trying to do with your instance.
# For this example, we'll choose one of the Ubuntu versions.

# We can select which type of disk we want to use, either the standard disk which is cheaper, or the SSD version which
# is faster. And we could also change the size if we needed extra storage for our server. For now, we'll just keep the
# default values here.

# After the boot disk, we're shown options to determine how access to the machine will work.
# This can be very simple or very complex, depending on the rest of your project.
# The default access option allows you to access the instance remotely using SSH, so we'll go with that one for now.

# And finally, the creation wizard lets us pre-configure some firewall rules. Selecting one of these two options would
# let HTTP or HTTPS traffic reach our machine. Of course, there are more firewall rules that you might want to set.
# Those can be set later on, after the machine is created.
# In a later video, we'll want to connect to a web server on this machine, so let's turn HTTP on.

# There are a lot more options we can set, which are tucked away under this link. We won't look into those now, since
# the defaults make sense for our test machine. But you can check them out on your own to see what other parameters you
# can set.

# We're basically ready to create our VM, but before we do that, let's click on the command line link.
# This will show us how we would create the same VM through the command line.

# Wow, that's a long command line, but don't worry, you don't need to understand all of those parameters. open
# GCP_4.png
# The takeaway here is that you could select all the options that you want to create the VM that you need, and then
# copy this command to create a bunch of VMs that are all exactly the same as the one you selected.
# For now, we'll close this window and then create the VM using the Create button.

# Our instance is being created, this takes a bit of time. The system is assigning the necessary resources to our
# machine, deploying the operating system image, connecting the network interfaces, and so on.
# Once it's done setting up, we can connect to it using SSH. Again, it takes a little while for the system to set up
# the keys that we'll use to log on.
# But once it's done, we can use the machine remotely.

# Let's check that the machine we created is using the OS we selected. open GCP_5.png

# Once you're logged into the machine, you can treat it like any normal Linux machine, which is pretty awesome.
# For example, we can get a text version of the weather in our current location by calling the 'curl' command, which
# we can use to access web pages from the command line, and passing in wttr.in as the website:

# curl wttr.in

"""Customizing VMs in GCP"""
# Cloud scale deployments are often comprised of hundreds or thousands of machines. So creating a single server is only
# the beginning. Let's make some changes to that VM so that we can deploy it at scale. Once we're done, we'll use the
# instance that we configured as the base for our 'Reference image'.

# Remember that a reference image is just a file or configuration that we can deploy repeatedly and with automated tools
# This is important because it lets us build scalable services very quickly.

# Let's start by logging into the virtual machine we created in the last video. We'll use git which will let us clone
# the repository with the code for the app we want to deploy. The repo we've cloned includes a very simple web serving
# application written in Python. open customize_VM_1.png

# Let's run it to see what happens. Our script prints a single line saying that it's listening for connections on port
# 8000. open customize_VM_2.png

# What's happening behind the scenes is that the application is opening a socket and listening for HTTP connections on
# that port. In this case, it's running on port 8000. And if we were running this locally on our machine, we could
# connect to that port. But this is running on a virtual machine in the cloud which has a firewall and only a couple of
# ports enabled. What are our options?

# The script actually lets us pass the port number that it will open as a parameter. We want it to run on the HTTP port
# that we configured in our last video which is port 80. And because this is a system port, to let our application use
# it, we'll need to run it with admin privileges. So let's stop the running process now by pressing Ctrl+C.
# And then run it again with 'sudo' and pass port 80 as the parameter.
# open customize_VM_3.png

# Now we can visit the website served by our VM and see its contents. Let's navigate to it. Our web app is extra simple.
# It just prints 'Hello Cloud' to the web page generated when we make a request. open customize_VM_4.png
# It also prints the Hostname and IP Address of the machine.
# This will help us later on when we deploy the solution at scale.

# All right, we have a web serving application running on the HTTP port. That's nice, but we had to start the
# application manually so this doesn't scale. To get our application to start automatically, we need to configure this
# as a service. Fortunately, our repo already includes a service definition that we can use.
# Let's check out the contents of that file.

# This is a systemd file, which is the initializing system used by most modern Linux distributions.
# open customize_VM_5.png

# Don't worry if you don't understand what's going on here. You don't need to understand the details of this file to
# know how to deploy services to the cloud. Just notice that the configuration expects the script that we want to
# execute to be in /usr/local/bin.

# We need to copy that file over to there and then copy the service file to /etc/systemd/system, which is the directory
# used for configuring 'systemd' services.

# And finally, we need to tell the 'systemctl' command that we want to enable this service so that it runs
# automatically. open customize_VM_6.png

# Okay, now that we've done this, anytime this machine starts, it will start the web app that we've configured, and
# we'll be able to see the content that we saw before. Let's try it out by triggering a reboot.

# We've rebooted the machine. This will take a while to complete. It tells us that the connection was lost and
# that we can ask our terminal to reconnect. open customize_VM_7.png This will take a bit of time until the machine has
# finished rebooting and is ready to receive connections. Okay, our VM has rebooted.

# We can check if our application is running by using the 'ps ax' command to get a list of the running processes and
# filter it, so we keep only the ones matching a pattern using the 'grep' command and use 'hello' as the pattern.
# open customize_VM_8.png

# ps ax | grep hello

# Our application is now running on startup. We're almost ready to turn our configured VM into a template for
# creating a lot more of them. But before we do that, we need to think about how we'll upgrade our web app
# when we want to make changes to it. There's a bunch of different options here.

# One option is to create a different reference image each time there's a new version of the app.
# This would mean deleting all the old VMs and creating new ones based on the new image.

# Another option is to add a configuration management system to the images so that we can use that to manage any changes
# after the VM's created. We already know how to manage changes with Puppet.

# Let's install the Puppet client in this instance, so it's ready to use Puppet in the future:

# sudo apt install puppet

# Now when we looked into the Puppet Server and client setup, we saw that there was a bunch of steps that we need to run
# on the client side to have it ready to apply the rules. The repo we cloned includes a script we can run
# which will do the initial configuration for us. It will also set the Puppet process to run automatically on boot.
# Let's run that now. open customize_VM_9.png

# Now any time this machine starts, it will serve our website, and we want to update that website's content.
# We can do that using our Puppet infrastructure. Our VM is now ready to be used as a basis for
# a template, which we can use to create as many instances as we need.
