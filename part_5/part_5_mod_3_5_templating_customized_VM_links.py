"""Templating a Customized VM"""
# We can now use this VM as a basis for creating an instance template, and then use the template to create a bunch of
# VMs based on it. Let's do that.

# To create a reference image, we need to have access to the current virtual disk that's running on the computer.
# So the first step to create the image is to stop the VM. It takes a while for the machine to shut down cleanly.
# Once it's finished, we can click on the machine's name to see all its details, and then we can click on the boot disk.
# These are the details of the disk attached to the VM.

# We can create a snapshot, which is a full copy of the current state of the disk, or an image, which lets us create a
# template based on it. Let's click 'Create image'. We'll call our image 'webserver-image'.

# Here, the creation wizard shows that we'll be creating the image based on the Linux-instance disk, which is what we
# want. For this example, we'll leave the rest of the settings with the default values. Okay, let's create our image.

# This is now creating the image that we'll use for our template.
# As we called out earlier, the tools we keep most of the contents of the image, but remove things that should be
# different across VMs.

# Once it's finished creating, it shows us the list of all images that we can access. open template_customized_VM_1.png
# As you can see, this is a long list that includes a bunch of stuff along with our image.
# The other images are public images that we can use to deploy different types of VMs.

# We're now ready to create our instance template.
# To do that, we'll go to the instance template option, and then click create new instance template.
# As usual, we're shown a wizard that includes a bunch of different options that we can set.
# We'll keep most of the defaults, and change only a couple of things. We'll name our template 'webserver-template'.
# We'll change the boot disk to use the image we've created.
# In this screen, we can see the list of all the available images.

# By default, the list shows the official operating system images provided by the platform.
# For our template, we want to use the custom Image we've created.
# And finally, we'll also want to enable HTTP access to the instances created with this template.
# That's it. We're ready to create our new template.

# Once it's done, we can create instances based on our images. We'll do it once more from the web interface, and
# then we'll check out how to do it from the command line.

# Let's go back to the VM instances entry, and then click on create instance.
# This time, instead of creating an instance from scratch, we'll use the template we've prepared.
# We'll name our instance 'webserver-1'. Everything else we'll leave as is.

# Check out how it says that it will use the base image we selected, and that HTTP traffic will be allowed.
# All right, we've created our second VM based on the template. We didn't have to change any options,
# because all the values were already pre-selected in the template.
# And the web app that we want is ready to run, without us having to configure anything.

# Our application is already running successfully on this machine.
# This is great, but it's still a bit cumbersome if we want to create 10 VMs like this one.
# For a batch action like that, it's better to use the command line interface.

# To interact with Google Cloud, we'll be using the 'gcloud' command.
# We've already installed the gcloud command on this machine. You'll find pointers on how to install gcloud on different
# platforms in the next reading.

# We'll start by running the 'gcloud init' command, which sets up the authentication mechanisms between this computer
# and Google Cloud. We need to authenticate to the Google Cloud system to be able to use the gcloud command to interact
# with it. Let's say yes here.
# This opened a new tab in our browser that we can use to authenticate with our account.
# Let's follow the process here, and authenticate. We're now logged into our cloud account.
# We can choose which will be our default project. Let's select one here. We've selected the default project.

# On top of that, the initializing wizard lets us select the default region and zone.
# It's a good idea to select this, as the commands that we use in the future will use that zone and region if we don't
# specify a different one. This is a long list.
# There are a lot of different zones available for our instances. As we called out earlier, when selecting where to run
# your services, you should go with the one that's closest to you. For this example, we'll just go with Zone 1.

# Once we've completed this authentication, we can use the gcloud command to operate on our Cloud project.
# We can modify the VMs we've created, create new ones, delete some of the existing ones, and a lot more.

# For our example, we'll use it to create 5 additional VMs.
# First, we call 'gcloud', then we pass the 'compute' parameter that's used for everything that has to do with VMs.
# Then we pass the 'instances' parameter, as we'll be dealing with the VM instances themselves.
# So then, we pass 'create', as we want to create instances.
# We'll see that we want to use the source instance template called 'webserver-template'.
# And finally, we'll give the name of the instances that we want to deploy.
# Let's call them ws1, ws2, ws3, ws4, and ws5:

#  gcloud compute instances create --source-instance-template webserver-template ws1 ws2 ws3 ws4 ws5

# open template_customized_VM_2.png
# It takes only a short while until all instances are created.
# This is definitely much faster than going through the web interface, and much easier to automate through our scripts.
# And with that, we've seen how we can create a virtual machine, customize it, create a template out of it, and
# use that template to create a bunch of new identical virtual machines.


"""Managing VMs in GCP"""
# Over the last few videos we learned how to create and use virtual machines running on GCP. We then explored how we can
# use one VM as a template for creating many more VMs with the same setup. You can find a lot more information about
# this in the following tutorials:

# https://cloud.google.com/compute/docs/quickstart-linux
# https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template
# https://cloud.google.com/sdk/docs