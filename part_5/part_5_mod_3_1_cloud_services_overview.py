"""Cloud computing
Cloud Services Overview
"""
# When we say that a service is running in the Cloud, it simply means that the service is running somewhere else: either
# in a data center or in other remote servers that we can reach over the Internet. These data centers house a large
# variety of machines, different types of machines are used for different services.

# For example, some machines may have local solid-state drive or SSD, for increased performance while others may rely on
# virtual drives mounted over the network to lower costs. Cloud providers typically offer a bunch of different service
# types, the ones used most by users are in the Software as a Service category.

# Software as a Service or SaaS, is when a Cloud provider delivers an entire application or program to the customer.
# If you choose a Cloud e-mail solution like Gmail, a Cloud storage solution like Dropbox, or a Cloud productivity suite
# like Microsoft Office 365, there are only a small number of options for you to select or customize.
# The Cloud provider manages everything related to the service for you including deciding where it's hosted,
# ensuring the service has enough capacity to serve your needs, performing backups frequently and reliably, etc.

# There's a lot of software being offered as a service by many Cloud providers or other Internet companies.
# But of course, not all of our needs can be solved by prepackaged software, sometimes we need to develop our own.
# For some components of our software, we might choose to use Platform as a Service.

# Platform as a Service or PaaS, is when a Cloud provider offers a preconfigured platform to the customer.
# When we say platform here, it can be a bit confusing because there are lots of different platforms that exist under
# PaaS model. Let's check out an example to understand this better.

# Say you need an SQL database to store some of your application's data, you could choose to host the database in your
# own hardware. To do this, you'd need to install an operating system on that computer and then install the SQL software
# on top of the chosen OS. This requires a basic understanding of all of these different pieces just to get the database
# running. There's a bunch of things that could go wrong and even if you can eventually solve all of them, it can take
# a while.

# Instead, you could decide to use a Cloud provider that offers an SQL database as a service, that way you can just
# focus on writing SQL queries and using the platform, and let the Cloud provider take care of the rest.

# There's a bunch of different platforms offered as a service by Cloud providers, but of course they are unlikely
# to cover all of your needs. If you need a high level of control over the software you're running and how it interacts
# with other pieces in your system, you might want to choose Infrastructure as a Service.

# Infrastructure as a Service or IaaS, is when a Cloud provider supplies only the bare-bones computing experience.
# Generally, this means a virtual machine environment and any networking components needed to connect virtual machines,
# the Cloud provider won't care what you're using the VMs for.

# You could use them to host a web server, a mail server, your own SQL database with your own configuration settings,
# or a lot more possibilities. Running your IT infrastructure on the Cloud provider's IaaS offering is a very popular
# choice. There's a lot of different providers out there, big and small that offer a service where you
# can run virtual machines in their Cloud.

# Some IaaS products include: Amazon's EC2, Google Compute Engine, and Microsoft Azure Compute.
# No matter the service model and the provider you use, when you set up Cloud resources you'll need to consider regions.

# A region is a geographical location containing a number of data centers, regions contain zones and zones can contain
# one or more physical data centers. If one of them fails for some reason, the others are still available and services
# can be migrated without notably affecting users.

# Large Cloud providers usually offer their services in lots of different regions around the world.
# Generally, the region and zone you select should be closest to your users, the further your users are from the
# physical data center the more latency they may experience.

# This might sound a bit strange but imagine if you are on vacation overseas, you might notice that your bank website
# loads a little slower. That's why it's common practice to locate data centers close to where users actually live,
# work, and bank.

# Latency isn't the only factor to take into account when selecting a region or zone, some organizations require their
# data to be stored in specific cities or countries for legal or policy reasons. If your service uses other services as
# dependencies, it's a good idea to host the service physically close to its dependencies.

# For example, if a mail server requires a database server to send an e-mail, it makes sense to host the database server
# and the mail server in the same zone.

# Recall that earlier, that Qwiklabs is a service using Cloud infrastructure. So what kind of Cloud service does
# Qwiklabs use? Qwiklabs uses Infrastructure as a Service, the VMs get provisioned with just the OS and
# the lab automation then deploys any additional files and software into the OS.

"""Scaling in the Cloud"""
# One of the coolest features of deploying solutions to the Cloud is how easily and quickly we can scale our deployments
# In a traditional IT setting, if your team needs an extra server to improve the service, you need to buy additional
# hardware, install the operating system and application software and then integrate the new computer with the rest of
# the infrastructure. Doing all of these takes time, so it's not easy to quickly scale up or down if the service gets
# more or less usage. In other words, it takes a significant amount of time to modify the capacity of the deployment.

# In this context, Capacity is how much the service can deliver.

# The available capacity is tied to the number and size of servers involved. We get more capacity by adding more servers
# or replacing them with bigger servers.

# The way we measure the capacity of a system depends on what the system is doing. If we're storing data, we might care
# about the total disk space available. If we have a web server responding to queries from external users, we might care
# about the number of queries that can be answered in a second which is called 'queries per second' or QPS.
# Or maybe the total bandwidth served in an hour.

# We can measure capacity in other fun ways like the number of cat videos served in an hour or the number of digits of
# pi a system can calculate. Our capacity needs can change over time.

# Say you're hosting an e-commerce site that needs a hundred servers to meet user demands. As the service becomes more
# popular, demand might grow, and you'll need to increase the available capacity. Eventually, the system could need
# a thousand servers to meet user demands.

# This capacity change is called Scaling. In particular, we call it upscaling when we increase our capacity and
# downscaling when we decrease it. This could happen for example if the demand for a product decreased or if the system
# was improved to need fewer resources.

# Cloud providers typically have a lot of available capacity that can be used by their customers.
# When we choose to host our infrastructure in the Cloud, we're purchasing and using some providers capacity to
# supplement or completely replace our on-premise capacity. This lets us easily scale our service to satisfy demand.

# There are a couple of different ways that we can scale our service in the Cloud, horizontally and vertically.

# To scale a deployment horizontally, we add more nodes into the pool that's part of a specific service.
# Say your web service is using Apache to serve web pages. By default, Apache is configured to support 150 concurrent
# connections. If you want to be able to serve 1,500 connections at the same time, you can deploy 10 Apache web servers
# and distribute the load across them. This is called horizontal scaling. You add more servers to increase your capacity
# If the traffic goes up you could just add more servers to keep up with it.

# On the flip side, if you're scaling a deployment vertically, it means you're making your nodes bigger.
# When we say bigger here we're talking about the resources assigned to the nodes like memories, CPU, and disk space.
# For example, a database server with 100 gigabytes of disk space can store more data than with only 10 Gb of space.
# To scale this deployment we can just add a bigger disk to the machine and the same idea works for a CPU and memory too

# Say you have a caching server, and you notice it's using 95% of the available memory. You can deal with that by adding
# more memory to the node.

# Depending on our deployment and our needs, we might need to scale both horizontally and vertically to scale the
# capacity of our service. In other words, adding more and bigger nodes to our pool.

# This approach to scaling isn't too different from what you'd need to do if you have your servers running on-premise.
# Instead of sending someone to change the physical deployment, for example adding more physical RAM to a server
# or adding 10 more physical machines in a server rack, we just modify our deployment by clicking some buttons in web UI
# or using a configuration management system to automate the scaling for us. The infrastructure built by the Cloud
# provider will deploy any additional resources we need.

# When talking about scaling in the Cloud, another aspect we need to take into account is whether the scaling is done
# automatically or manually.

# When we set our service to use automatic scaling, we're using a service offered by the Cloud provider.
# This service uses metrics to automatically increase or decrease the capacity of the system.

# Say you have a system that currently has the capacity to serve 1,000 cat videos per minutes. If the demand for these
# videos increases to 10,000 per minute, and it will, the software in-charge of the automatic scaling will add
# resources and increase the overall capacity to meet this demand. When the users stop watching cat videos,
# the automation will remove any unused resources, so the operating costs stay small.
# But really who wants to stop watching cat videos?

# But make sure you set a reasonable quotas for your autoscaling systems. Otherwise, that viral video of a cute cat
# wearing a hat might surprise you with a very uncute big bill from your Cloud provider.

# On the flip side, using manual scaling means that changes are controlled by humans instead of software.
# Manual scaling has its pros and cons too.

# When the Cloud deployment isn't very complex, it's usually easier for smaller organizations to use manual scaling
# practices. Say your company currently has a single mail server, and you know that you'll want to have another one in
# six months. In that case, there's no need to overcomplicate that system with an autoscaler. You could simply add the
# extra server sometime along the way. The trade-off here is that# without good monitoring or alerting, a system without
# autoscaling technologies might suffer from unexpected increases in demand.

# If you're using manual scaling for a service that becomes popular and demand grows quickly, you might not be able to
# increase the capacity quickly enough. This can store up lots of problems ranging from poor performance to an actual
# outage.
