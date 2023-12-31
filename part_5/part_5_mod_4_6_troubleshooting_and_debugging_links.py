"""What to Do When You Can't Be Physically There"""
# If you're used to troubleshooting problems on physical computers, it can take a bit of a mindset shift to get used to
# fixing problems with virtual machines running in the cloud. There's a bunch of things that you can't do like you can't
# walk up to a server and check out what's wrong with it. But there's also other things that are a lot simpler when
# troubleshooting VMs in the cloud. Like adding more memory or moving the machine to a different data center.

# Let's say that after the latest upgrade, a bunch of your cloud VMs have stopped booting. Something went wrong, but you
# don't know exactly what. You can't connect to the instances or boot them in rescue mode, so what can you do?
# There's a bunch of options, if you're following the infrastructure as code practices that we've talked about.

# You could deploy new VMs with the previous version of the system. This would help us get back to a healthy state as
# quickly as possible. On top of this, you want to understand the problem and how to fix it. To do that, you can create
# a snapshot of the disk image for one of the failing VMs. And then mount that disk image on a healthy machine.
# That way you can analyze the contents of the image and figure out what's causing the failures.
# And it's not always easy to know which piece of the system is causing a failure.
# Especially if the system is complex with many services interacting with each other.

# If you're trying to figure out what's causing your complex servers to respond with a ton of 500s, you need to look at
# different pieces individually until you find the culprit.
# - Does the problem happen if you run the service and a test VM without any load balancers or caching servers in
# between?
# - Does it happen if you run the service locally on your workstation?
# The more you can isolate the faulty behavior, the easier it is to fix it.

# You should remember that problems will happen, it makes sense to spend some time getting ready for them. Setting up a
# testing environment might take time and effort, so it's a good idea to do this in advance before any problem actually
# happens. That way you don't need to do it under pressure when your users are complaining that the system's down.

# Say you're using a database service that's only reachable from inside your cloud network. This means you can't
# interact with it directly from the outside, only from instances within your cloud infrastructure. If your service
# starts acting up, you might want to check the responses from the database directly rather than going through any of
# the other back-end servers. To do this, you'll need to have a debugging machine in the network, and you'll need to use
# tools to interact with the database directly.

# Again, setting the machine up, and learning how to use the tools takes time. So get ahead of the game and do it in
# advance before any problems come up. You might remember from the troubleshooting and debugging course, that
# understanding logs is super important for being able to solve problems in IT. When you run your service in the cloud,
# you need to learn where to find the logs that the provider keeps and what info is available in which logs.
# Some cloud providers offer centralized log solutions to collect all your logs in one place. You can have all your
# notes, send info, warning and error messages to the log collection point.
# Then, when you're trying to debug a problem, you can easily see everything that was going on when the error occurred.

"""Identifying Where the Failure Is Coming From"""
# When we host our services in the cloud, we need to give up part of the control over the infrastructure that we're
# using. This might be especially noticeable when we're trying to find the root cause of a problem in our service, and
# we don't know if the failure is caused by an error on our side or on the provider side.
# So what can we do in that case?

# Problems on the provider side tend to be isolated to geographical regions. If you're seeing weird problems, and you
# have no idea what could be going on, you can try bringing up your service in a different region and checking if the
# failure happens there too. If it works fine there, it's likely that there's an issue with the cloud infrastructure,
# and you should bring it up with your provider. If it fails in the other regions too, it's likely that it's a problem
# with your system.

# Similarly, if you're seeing problems related to resource usage, you can try running the same system in a different
# machine type and checking how it behaves there. This could help out, for example, if your service takes too much time
# to process incoming requests. By changing your service to more powerful machines, you might improve the overall
# performance.

# Another option that we've mentioned is doing rollbacks for the pieces that have recently changed. Having all your
# infrastructure stored as code in a version control system will let you access the history of the changes to each
# component in the system. When setting up your service, you should make sure that you can deploy and roll back each
# individual piece.

# Imagine you get an alert saying that the web servers in your application are using a lot more memory than they used to
# do. You don't know why, but you know that a new version was deployed a couple of days ago. By rolling back to the
# previous version, you can verify if that change was at fault or not. If the server's work fine after the rollback,
# you can investigate the specific changes and try to figure out why they're using so much more memory. If the servers
# are still using a lot of memory after the rollback, it means something else is up.

# In an earlier video, we touched briefly upon one popular option when running things on the cloud called 'Containers'.
# Containers are packaged applications that are shipped together with their libraries and dependencies.

# Each application is executed in a separate container, completely independent of any other applications running on the
# same machine. Now, one of the neat characteristics of containerized applications is that you can deploy the same
# container to your local workstation, to a server running on-premise or to cloud infrastructure provided by different
# vendors. This can be really helpful when trying to understand if the failure is in the code or the infrastructure.
# You simply deploy the container somewhere else and check if it behaves the same way.

# When using containers, the typical architecture is to have a lot of small containers that take care of different parts
# of the service. This means that the overall system can get really complex and when something breaks, it can be hard
# to identify where the problem is coming from. The key to solving problems in the container world is to make sure you
# have good logs coming in from all the parts of the system. And, that you can bring up test instances of each of
# the applications to try things out when necessary.

"""Recovering from Failure"""
# When dealing with a complex system, there's a lot of ways it can fail. If we want our service to be reliable,
# we need to make sure that we can get it up and running as quickly as possible when bad things happen.
# We'll need to have good backups and a well-documented recovery plan.

# Backups here doesn't mean just copies of your data. It also means backups for the different pieces of your
# infrastructure, including the instances that are running the service and the network that's used to connect to service

# Backups of the data your service handles are extremely important. If you operate a service that stores any kind of
# data, it's critical that you implement automatic backups and that you periodically check that those backups are
# working correctly by performing restores. This helps make sure that you're backing up the right data and that you have
# well-documented processes for recovering it when things fail.

# What about the rest of the infrastructure?
# If you store all your Infrastructure as code, you already have a backup of what your infrastructure should look like.
# But if your service goes down for some reason, deploying all that infrastructure from scratch might take a while.
# That's why many teams keep backup or a secondary instances of their services already up and running. That way, if
# there's a problem with the primary instance, they can simply point the load balancer or the DNS entries to
# the secondary instance with minimal disruption to the service.

# Alternatively, it's common practice to have enough servers running at any time so that if one of them goes down,
# the others can still handle the traffic, or on a larger scale, have the service running on different data centers
# around the world, so that if one of the data centers has a problem, the service can still be provided by the instances
# running in the other data centers.

# If you're running a service on-premise, you might want to have two different connections to the Internet. This way,
# if the connection offered by one of your ISPs goes down, you can still connect to the Internet through the other one.

# When you're running on Cloud, you can mostly rely on your Cloud provider having enough network redundancy. But if you
# really care about your service staying up no matter what, you might want to run your service on two different Cloud
# vendors so that if one of the providers has a large outage, you can still rely on the other.

# Now, imagine you're running your service in one data center. Unfortunately, that data center has just suffered a
# natural disaster, and all of your instances are down. What do you do?

# You need to recover your service from scratch, deploying it in a different data center and getting all your data from
# backups. As long as the backups are available in other data centers and your Infrastructure is fully stored in VCS,
# this should be possible.

# But figuring out how to successfully bring up the whole system from scratch can take a while. So you don't want to
# have to scramble to do it when disaster hits. Instead, you should have a documented procedure that explains all the
# steps that you need to take. Since systems evolve over time, you need to make sure that this documentation
# stays up-to-date.

# One way to do that is to once in a while pretend that you need to recover your service, follow the documented steps,
# and check if anything is missing or outdated. Systems will fail. 100% availability is simply not an achievable targets,
# but being prepared for a failure will let you recover your service quickly and keep your users happy.


"""Reading: Debugging Problems on the Cloud"""
# https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-instances
# https://docs.microsoft.com/en-us/azure/virtual-machines/troubleshooting/
# https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html
