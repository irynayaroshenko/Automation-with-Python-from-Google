"""Automating Cloud Deployments
Cloud Scale Deployments"""
# The biggest advantage of using Cloud services is how easily we can scale our services up and down.
# Now, to make the most out of this advantage, we need to do some preparation.
# We'll set up our services so that we can easily increase their capacity by adding more nodes to the pool.
# These nodes could be virtual machines, containers, or even specific applications providing one service.
# Whenever we have a service with a bunch of different instances serving the same purpose, we'll use a Load Balancer.

# A load balancer ensures that each node receives a balanced number of requests.

# When a request comes in, the load balancer picks a node to serve the response. There's a bunch of different strategies
# load balancer uses to select the node. The simplest one is just to give each node one request called 'Round robin'.
# More complex strategies include always selecting the same node for requests coming from the same origin,
# selecting the node that's closest to the requester, and selecting the one with the least current load.

# As we called out, instance groups like these are usually configured to spin up more nodes when there's more demand,
# and to shut some nodes down when the demand falls. This capability is called Autoscaling.

# It allows the service to increase or reduce capacity as needed while the service owner only pays for the cost of
# the machines that are in use at any given time.

# Since some nodes will shut down when demand is lower, their local disks will also disappear and should be considered
# ephemeral or short-lived. If you need data persistence, you'll have to create separate storage resources to hold
# that data and connect that storage to the nodes.

# That's why the services that we run in the Cloud are usually connected to a database which is also running in Cloud.
# This database will also be served by multiple nodes behind a load balancer, but this is typically managed by the
# Cloud provider using the 'Platform as a service' model.

# To check out how this works in practice, let's look at an example of a web application with a lot of users.
# When you connect to a site through the Internet, your web browser first retrieves an IP address for the website that
# you want to visit. This IP address identifies a specific computer, the entry point for the sites.
# Commonly there will be a bunch of different entry points for a single website. This allows the service to stay
# up even if one of them fails.

# On top of that, it's possible to select an entry point that's closer to the user to reduce latency.
# In a small-scale application, this entry point could be the web server that serves the pages, and that would be it.

# For large applications where speed and availability matter, there will be a couple of layers in between
# the entry point and the actual web service.

# The first layer will be a pool of web caching servers with a load balancer to distribute the requests among them.
# One of the most popular applications for this caching is called Varnish, but of course it's not the only one.
# The Nginx web server and software also includes this caching functionality.
# There's a bunch of providers that do web caching as a service like Cloudflare and Fastly.

# No matter the software used, the result is basically the same. When a request is made, the caching servers first check
# if the content is already stored in their memory. If it's there, they respond with the contents, if it's not,
# they ask their configured backend for the content and then store it so that it's present for future requests.

# This configured backend is the actual web service that generates the webpages for the site, and it will also normally
# be a pool of nodes running under a load balancer. To get any necessary data, this service will connect to a database.

# But because getting data from a database can be slow, there's usually an extra layer of caching, specific for the
# database contents. open load_balancer.png

# The most popular applications for this level of caching are Memcached and Redis.

# As you can see, there is a lot of different nodes in this scheme.
# Fortunately, once you've done your homework and prepared your setup, you can rely on the capabilities
# offered by the Cloud provider to automatically scale the system up and down as necessary.
# The infrastructure will take care of adding and removing instances, distributing the load, making sure that each
# geographical region has the right capacity, and a bunch more things.

"""What is orchestration?"""
# Orchestration is the automated configuration and coordination of complex IT systems and services.
# In other words, orchestration means automating a lot of different things that need to talk to each other.

# This will always include a lot of different automated tasks and will generally involve configuring a bunch of
# different systems. Taking the example of the website infrastructure that we saw in our last video, we've seen how we
# can automate the creation of each instance in the system.

# Now, say you wanted to deploy a new copy of the system in a separate data center where you have no instances yet,
# you'll need to also automate the whole configuration of the system, the different instance types involved,
# how will each instance finesse the others, what the internal network looks like, and so on.
# So how does this work?

# The key here is that the configuration of the overall system needs to be automatically repeatable.
# There's a bunch of different tools that we can use to do that. These tools typically don't communicate with
# the Cloud systems through the web interface or the command line.
# They normally use an application programming interface or API that lets us interact with the Cloud infrastructure
# directly from our scripts.

# In the case of Cloud provider APIs, they typically let you handle the configuration that you want to sit directly from
# your scripts or programs without having to call a separate command. This combines the power of programming with
# all the available Cloud resources.

# The APIs offered by the Cloud providers let us perform all the tasks that we mentioned earlier like creating,
# modifying, and deleting instances and also deploying complex configurations for how these instances will talk to each
# other. All of these actions can also be completed through the web interface or the command line. But doing them from
# our programs gives us extra flexibility which can be key when automating complex setups.

# Say you wanted to deploy a system that combines some services running on a Cloud provider and some services running
# on-premise, this is known as a hybrid Cloud setup, or only part of the services are in the Cloud. The setup is super
# common in the industry right now.

# Orchestration tools can be a pretty useful tool to make sure that both the on-premise services and the Cloud services
# know how to talk to each other and are configured with the right settings.

# Going back to the website example that we discussed earlier to make sure that the service is running smoothly,
# we should set up a monitoring and alerting. This lets us detect and correct any problems with our service before users
# even notice. This is a critical piece of infrastructure but setting it up correctly can take quite some time.

# By using orchestration tools, we can automate the configuration of any monitoring rules that we need to set,
# which metrics we want to look for, when we want to be alerted, and so on, and automatically apply these to
# a complete deployment no matter which datacenter the services are running in.

"""Cloud Infrastructure as Code"""
# In our last video, we talked about how we need to orchestrate complex Cloud setups. This includes handling a bunch of
# different nodes with different workloads, managing the complexity of deploying a hybrid setup, or modifying
# deployments across several Data centers.

# Back at the beginning of the course, we talked about infrastructure as Code (IaC uses special machine-readable config
# files to automate configuration management.), and we called out that storing our infrastructure in a code-like format,
# lets us create repeatable infrastructure, and that using Version control for the storage, means that we can keep a
# history of what we've done and easily rollback mistakes. These principles also apply to Cloud infrastructure.

# The way we store it might be a little different depending on the tools that we use, but we'll still be storing
# this configuration in a code like format using Version control to keep track of the changes.
# This lets us manage large-scale solutions with a small team. We can very quickly have an idea of what the deployment
# looks like, by looking at the configuration. We can try new things out and roll back if anything goes wrong.
# We can look at the history of changes to figure out why a specific change was made, and much more.

# Most Cloud providers offer their own tool for managing resources as code.
# Amazon has Cloud Formation, Google has Cloud Deployment Manager, Microsoft has Azure Resource Manager, and OpenStack
# has Heat Orchestration Templates. These tools are specific to the Cloud provider, which means it can be complex and
# cumbersome to move to a different provider or combine a Cloud deployment with an on-premise deployments.

# An option that's becoming really popular in the Orchestration field, is called Terraform.
# Similar to Puppet, Terraform uses its own Domain-specific language which lets us specify what we want our Cloud
# infrastructure to look like. The cool thing about Terraform is that it knows how to interact with a lot of
# different Cloud providers and automation vendors.

# So you can write your Terraform rules to deploy something on one Cloud provider, and then use very similar rules to
# deploy the service to a different Cloud provider. Terraform uses each Cloud provider's API to accomplish this.
# This keeps you from having to learn a new API when moving to a different Cloud provider, and lets you focus on the
# infrastructure design.

# We saw in earlier videos how we can have a puppet rule that specifies that a computer should install a given package,
# and that the local puppet agent analyzes the computer and decides which installation mechanism to use depending on
# the operating system, the specific Linux distro and so on.

# A similar thing happens with Terraform. The rules that define the resources like the VMs or containers to use,
# will use specific values related to the Cloud provider like selecting which machine type to use or in what region to
# deploy it. But a lot of the overall configuration is independent of the provider, and can be reused if we
# decide to move our configuration to a different provider, or we want to use a hybrid setup.

# Of course Terraform isn't the only option. Puppet itself also ships with a bunch of plug-ins that can be used to
# interact with the different Cloud providers to create and modify the desired Cloud infrastructure.

# Finally, let's spend a moment talking about the contents of the nodes or instances managed by the Orchestration tools.
# When dealing with nodes in the Cloud, there are basically two options.
# Either they're long-lived and their contents need to be periodically updated, or they are short-lived and updates are
# made by deleting the old instances and deploying new ones.

# Long-lived instances are typically servers that are not expected to go away. Things like your company's internal mail
# server or internal document sharing servers, will manage these instances using a configuration management system like
# Puppet, which can deploy any necessary changes to the machines while they're running. This keeps them updated to the
# latest state.

# On the flip side, short-lived instances come and go very quickly. For these cases, it makes less sense to apply
# changes while they're running. Instead, we normally apply the configuration that we want the instances to have when
# they start, and we deploy any future changes by replacing the instances with new ones.
# We can still use Puppet for the initial setup, but we don't need to run the agent periodically, only at the start.


"""More About Cloud & GCP"""
# Getting started on GCP with Terraform https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform
# Creating groups of unmanaged instances https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances
# Official documentation: https://cloud.google.com/load-balancing/docs/https/
# https://geekflare.com/gcp-load-balancer/

# Interesting articles about hybrid setups:
# https://blog.inkubate.io/create-a-centos-7-terraform-template-for-vmware-vsphere/
# https://www.terraform.io/docs/enterprise/before-installing/reference-architecture/gcp.html
# https://www.hashicorp.com/resources/terraform-on-premises-hybrid-cloud-wayfair