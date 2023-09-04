"""Spinning up VMs in the Cloud"""
# As we've called out, there's a bunch of different Cloud providers that you can use for your projects, each with some
# specific advantages depending on what you're trying to achieve. And while some terms used by one provider might not
# exactly match the ones used by other providers, the concepts are the same.

# In these videos, we'll use the Google Cloud platform to demonstrate our examples.
# All Cloud providers give you a console that lets you manage the services that you're using.
# This console includes pointers to a lot of different services that the providers offer. Seeing all the options
# available, it can be a little dizzying at first. So it's a good idea to start just by familiarizing yourself with the
# platform before you try to do something with it.

# This can mean, for example, looking at the available menus and options, and figuring out where the sections that let
# you use infrastructure-as-a-service are located. No matter the exact menu entries, when you want to create a VM
# running in the Cloud, there are a bunch of parameters that you need to set. These parameters are used by the Cloud
# infrastructure to spin up the machine with the settings that we want.

# You'll start by choosing the 'name' assigned to the instance. This name will later let you identify instance if you
# want to connect to it, modify it, or even delete it. You'll also have to choose the 'region' and 'zone' where the
# instance is running. You'll generally want to choose a region that's close to your users so that you provide better
# performance.

# Another important option that you'll need to select is the 'machine type' for your VM.
# Cloud providers allow users to configure the characteristics of their virtual machines to fit their needs.
# This means selecting how many processing units, or virtual CPUs, and how much memory the virtual machine will b
# allocated. You might be tempted to select the most powerful VM available, but of course the more powerful the VM,
# the more money it will cost to run it. As a sysadmin, you may need to decide between costs and processing power to
# fit the needs of your organization. When setting up instances like these, it's a good idea to start small and
# scale as needed.

# On top of the CPU and memory available, you'll also need to select the boot disk that the VM will use.
# Each virtual machine running in the Cloud has an associated disk that contains the operating system it runs and some
# extra disk space. When you create the VM, you select both how much space you want to allocate for the virtual disk
# and what operating system you want the machine to run. To create these resources, we can use the web interface or
# the command line interface.

# The web UI can be very useful for quickly inspecting the parameters that we need to set. The UI will let us compare
# the different options available and even show us an estimation of how much money our selected VM would cost per month.
# This is great for experimenting, but it doesn't scale well if we need to quickly create a bunch of machines or if we
# want to automate the creation.

# In those cases, we'll use the command line interface, which lets us specify what we want once, and then use the same
# parameters many times. Using the command line interface lets us create, modify, and even delete virtual machines from
# our scripts. This is a great step towards automation, but it doesn't stop there.

# We can also automate the preparation of the contents of those virtual machines.
# Imagine spending an afternoon installing and configuring your new web server. You can do this on one machine, and the
# process is fairly straightforward. You install any necessary software, you modify any configuration settings, and
# then make sure that it's working correctly. But it would be hard to reproduce this exactly on another machine, and
# impossible to do it on thousands of machines.

# This is where reference images and templating come into play.

# Reference images store the contents of a machine in a reusable format, while templating is the process of capturing
# all the system configuration to let us create VMS in a repeatable way.

# That exact format of the reference image will depend on the vendor. But often, the result is a file called a disk image.
# A disk image is a snapshot of a virtual machine's disk at a given point in time. Good templating software lets you
# copy an entire virtual machine and use that copy to generate new ones.

# Depending on the software, the disk image might not be an exact copy of the original machine because some machine data
# changes, like the hostname and IP address. But it will have the data that we need to make it reusable on
# lots of virtual machines. This can be super helpful if we want to build a cluster of 10,000 machines
# which all have identical software.
