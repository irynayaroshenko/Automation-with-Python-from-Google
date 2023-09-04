"""Evaluating the Cloud"""
# If you've always worked in a traditional IT environment with servers that are physically owned by your company,
# the idea of migrating to the cloud can be pretty scary. When you're running the service yourself, if something breaks,
# you can either physically walk up to the server to fix it or SSH into it from inside the same network.
# You can apply a quick fix and have your users back to being productive in no time.

# As part of the IT team, you own the hardware, software, the network connections, and anything in between,
# which lets you have a lot of control over what's going on in the whole system.

# In the case of cloud solutions, we need to give up some of this control to the cloud provider. We have different
# levels of control depending on the service model that we choose, whether that's software, platform, or infrastructure
# as a service.

# When choosing to use software as a service, we're basically giving the provider complete control of how the
# application runs. We have a limited amount of settings that we can change, but we don't need to worry about making the
# system work. This can be a great option when the software provided fulfills all of our needs, and we'd rather just
# focus on using the software instead. But as we called out, there's only a limited amount of applications being
# offered in such a prepackaged way.

# If we need to create our own applications, we can use platform as a service.
# With this option, we're in charge of the code, but we aren't in control of running the application.

# Or we can choose infrastructure as a service, where we can still keep a high level of control. We decide the OS that
# runs on the virtual machines, the applications that are installed on it, and so on. We'll still depend on the vendor
# for other aspects of the deployment, like the network configuration or the services' availability. If something does
# break, you might need to get support from the vendor to fix the problem.

# So when choosing a cloud provider, it's important to know what kind of support is available and select the one that
# fits your needs.

# One aspect that might make you hesitant to move to the cloud is that you don't know exactly what security measures are
# being put in place. So when selecting which provider to use, it's important that you check how they're
# keeping your instances and your data secure.

# There are a bunch of certifications like SOC 1, ISO 27001, and other industry recognized credentials that you can look
# for to verify that your provider has invested in security. Once you're sure that your provider is taking the right
# security measures, it might be tempting to just leave security to the professionals and forget about it.

# But as cloud users, we also have a responsibility to follow reasonable security practices.
# Google, Amazon, Microsoft, and other cloud providers invest heavily in security research. But that won't matter if the
# root password of your cloud instance is 'password' or the instance doesn't use a firewall.

# In other words, we should always use reasonable judgment to protect the machines that we deploy, whether that's on
# physical server is running on-premise or on virtual machines in the Cloud.

# It's also important to keep in mind that security systems can be expensive to implement correctly.
# Some highly sensitive deployments might warrant specialized security procedures, like multi-factor authentication,
# encrypted file systems, or public key cryptography. But these processes can also be expensive to implement.
# It's worth considering if using these techniques is necessary for your specific use case.

# If your application stores recent patient health records, that's super important data that needs to be protected.
# You want to apply the most stringent security practices. But if you're dealing with patient health records from the
# 1800s, you'll need less comprehensive security measures, since this data is much less sensitive, given its age.

# There's a bunch of other reasons why you might have doubts about cloud providers. For example, you might be worried of
# where your data is going to be stored. Or you might fear that the support offered won't satisfy your needs.
# No matter the reason, it's important that you carefully read the terms of service to understand the conditions and
# figure out if the service offered will satisfy your needs.

"""Migrating to the Cloud"""
# A lot of companies today are looking into migrating at least part of their IT infrastructure to the Cloud.
# The details of the migration will depend on what your infrastructure currently looks like, and what you're trying to
# achieve by migrating to a Cloud provider.
# In general, we're looking at a trade-off between how much control we have over the computers providing the services
# and how much work we need to do to maintain them.

# We've called out that when we use Infrastructure as a Service or IaaS, we deploy our services using virtual machines
# running on the Cloud providers infrastructure. We have a lot of control over how the infrastructure is designed which
# can be super useful. For example, we can decide which of the many available machine types to use and what kind of
# storage to attach to them. IaaS is especially useful to administrators using a 'lift and shift' strategy.
# So what does that mean?

# Say you work at a small organization that's expanding.
# As the company grows, physical space for employees, desks, ping pong tables, and printers becomes scarce.
# Eventually, the whole office might need to move to a larger space. This means moving not just the desks and printers,
# but also any servers running on-premise. If physical servers need to be moved, you might need to take a server from
# the old office, turn it off during a maintenance window, load it onto a truck, and physically drive it to the new
# location. This could be the new office or maybe even a small data center. So you're literally lifting the server and
# moving it to a new location, that's where the lift in 'lift and shift' comes from.

# When migrating to the Cloud, the process is somewhat similar. But instead of moving the physical server in the back
# of a truck, you migrate your physical servers running on-premise to a virtual machine running in the Cloud.
# In this case, you're shifting from one way of running your servers to another.

# The key thing to note with both approaches, is that the servers core configurations stay the same.
# It's the same software that needs to be installed on the machine to provide its functionality, no matter if the server
# is hosted physically on-site or virtually in the Cloud.

# If you've already been using configuration management to deploy and configure your physical servers, moving to a Cloud
# setup can be pretty easy. You just have to apply the same configuration to the VMs that are running in the Cloud, and
# you'll have replicated the setup.

# On the flip side, using this strategy means that you still have to install and configure the applications yourself.
# You need to make sure that both the OS and the software stay up to date, that no functionality breaks when they get
# updated, and a bunch of other things depending on which specific application the server is running.

# One alternative in this case is using Platform as a Service or PaaS.
# This is well-suited for when you have a specific infrastructure requirement, but you don't want to be involved in
# the day-to-day management of the platform. In an earlier video, we mentioned the example of an SQL database that could
# be used in this way. By leaving the management of the database to the Cloud provider, you don't need to worry about
# having the right disks attached to the computer, configuring the database or any other task related to machine setup.
# Instead, you can focus on just using the database.

# Another example of Platform as a Service are managed web applications.
# When using this service, you only have to care about writing the code for the web app. You don't need to care about
# framework for running it. This can accelerate development because developers don't have to spend time managing the
# platform and can just focus on writing code.

# Some popular managed web application platforms include Amazon Elastic Beanstalk, Microsoft App Service, and Google App
# Engine. While these platforms are very similar, they aren't fully compatible.
# So migrating from an on-premise framework and switching between vendors will require some code changes.

# Another related concept that you might have heard of is 'containers'.
# Containers are applications that are packaged together with their configuration and dependencies.
# This allows the applications to run in the same way no matter the environment used to run them. In other words, if
# you have a container running an application, you can deploy it to your on-premise server, to a Cloud provider,
# or a different Cloud provider. Whichever you choose, it will always run in the same way.
# This makes migrating from one platform to the other super easy.

# When talking about migrating to the Cloud, you may also hear about public Clouds, private Clouds, hybrid Clouds
# and multi-Clouds.

# We call public Cloud the Cloud services provided to you by a third party. It's called public because Cloud providers
# offer services to the public.

# A private Cloud is when your company owns the services and the rest of your infrastructure, whether that's on-site or
# in a remote data center. It's private because it's just for your company, like having your own Cloud in the sky.

# A hybrid Cloud is a mixture of both public and private Clouds.
# In this scenario, some workloads are run on servers owned by your company, while others are run on servers owned by a
# third party. The trick to making the most of the hybrid Cloud is ensuring that everything is integrated smoothly.
# This way, you can access, migrate, and manage data seamlessly no matter where it's hosted.

# Finally, multi-Cloud is a mixture of public and/or private Clouds across vendors.
# For example, a multi-Cloud deployment may include servers hosted with Google, Amazon, Microsoft, and on-premise.
# A hybrid Cloud is simply a type of multi-Cloud, but the key difference is that multi-Clouds will use several vendors,
# sometimes in addition to on-site services. Using multi-Clouds can be expensive, but it gives you extra protection.
# If one of your providers has a problem, your service can keep running on the infrastructure provided by a different
# provider.
