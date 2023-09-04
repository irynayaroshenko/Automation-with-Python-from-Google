"""Building Software for the Cloud
Storing Data in the Cloud"""

# Almost all IT systems need to store some data. Sometimes, it's a lot of data, sometimes, it's only bits and pieces of
# information. Cloud providers give us a lot of storage options. Picking the right solution for data storage will depend
# on what service you're building. You'll need to consider a bunch of factors, like:
# - how much data you want to store,
# - what kind of data that is,
# - what geographical locations you'll be using it in,
# - whether you're mostly writing or reading the data,
# - how often the data changes,
# - what your budget is.

# When choosing a storage solution in the Cloud, you might want to go with the traditional storage technologies,
# like 'Block storage', or you can choose newer technologies, like Object or Blob storage.
# Let's check out what each of these mean.

# As we saw in an earlier video, when we create a VM running in the Cloud, it has a local disk attached to it.
# These local disks are an example of 'block storage'. This type of storage closely resembles the physical storage that
# you have on physical machines using physical hard drives.
# Block storage in the Cloud acts almost exactly like a hard drive.
# The OS of the VM will create and manage a file system on top of the block storage just as if it were a physical drive.
# There's a pretty cool difference though.

# These are virtual disks, so we can easily move the data around.
# For example, we can migrate the information on the disk to a different location, attach the same disk image to other
# machines, or create snapshots of the current state. All of this without having to ship a physical device from place to
# place. Our block storage can be either 'persistent' or 'ephemeral'.

# Persistent storage is used for instances that are long-lived, and need to keep data across reboots and upgrades.

# Ephemeral storage is used for instances that are only temporary, and only need to keep local data while they're running.

# Ephemeral storage is great for temporary files that your service needs to create while it's running, but you don't
# need to keep. This type of storage is especially common when using containers, but it can also be useful when dealing
# with virtual machines that only need to store data while they're running.

# In typical Cloud setups, each VM has one or more disks attached to the machine. The data on these disks is managed by
# the OS and can't be easily shared with other VMs. If you're looking to share data across instances, you might want to
# look into some shared file system solutions, that Cloud providers offer using the 'Platform as a service' model.

# When using these solutions, the data can be accessed through network file system protocols like NFS or CIFS.
# This lets you connect many instances or containers to the same file system with no programming required.

# Block storage and shared file systems work fine when you're managing servers that need to access files.
# But if you're trying to deploy a Cloud app that needs to store application data, you'll probably need to look into
# other solutions like 'Objects storage', which is also known as 'Blob storage'.

# Object storage lets you place and retrieve objects in a storage bucket. These objects are just generic files
# like photos or cat videos, encoded and stored on disk as binary data. These files are commonly called blobs,
# which comes from 'binary large object', and these blobs are stored in locations known as buckets.

# Everything that you put into a storage bucket has a unique name. There's no file system. You place an object into
# storage with a name, and if you want that object back, you simply ask for it by name.
# To interact with an object store, you need to use an API or special utilities that can interact with the specific
# object store that you're using.

# On top of this, we've called out in earlier videos that most Cloud providers offer databases as a service.
# These come in two basic flavors, SQL and NoSQL.

# SQL databases, also known as relational, use the traditional database format and query language.
# Data is stored in tables with columns and rows that can be indexed, and we retrieve the data by writing SQL queries.
# A lot of existing applications already use this model, so it's typically chosen when migrating an existing app
# to the Cloud.

# NoSQL databases offer a lot of advantages related to scale.
# They're designed to be distributed across tons of machines and are superfast when retrieving results.
# But instead of a unified query language, we need to use a specific API provided by the database.
# This means that we might need to rewrite the portion of the application that accesses the DB.

# When deciding how to store your data, you'll also have to choose a storage class.
# Cloud providers typically offer different classes of storage at different prices. Variables like performance,
# availability, or how often the data is accessed will affect the monthly price.

# The performance of a storage solution is influenced by a number of factors, including throughput, IOPS, and latency.

# Throughput is the amount of data that you can read and write in a given amount of time.
# The throughput for reading and writing can be pretty different. For example, you could have a throughput of 1 Gb per
# second for reading and 100 Mb per second for writing.

# IOPS or input/output operations per second measures how many reads or writes you can do in one second, no matter how
# much data you're accessing. Each read or write operation has some overhead. So there's a limit on how many
# you can do in a given second, and latency is the amount of time it takes to complete a read or write operation.
# This will take into account the impact of IOPS, throughput and the particulars of the specific service.

# 'Read latency' is sometimes reported as the time it takes a storage system to start delivering data after read request
# has been made, also known as 'time to first byte'.
# While 'write latency' is typically measured as the amount of time it takes for a write operation to complete.

# When choosing the storage class to use, you might come across terms like 'hot' and 'cold'.
# Hot data is accessed frequently and stored in hot storage while cold data is accessed infrequently, and stored in
# cold storage.

# These two storage types have different performance characteristics. For example, hot storage backends are usually
# built using solid state disks, which are generally faster than the traditional spinning hard disks.
# So how do you choose between one and the other?

# Say you want to keep all the data your service produces for five years, but you don't expect to regularly
# access data older than one year. You might choose to keep the last one year of data in hot storage, so you have fast
# access to it, and after a year, you can move your data to cold storage where you can still get to it,
# but it will be slower and possibly costs more to access.

"""Load Balancing"""
# In earlier videos, we saw a bunch of different reasons why we might want more than one machine or container running
# our service. For example, we might want to horizontally scale our service to handle more work, distribute instances
# geographically to get closer to our users. Or have backup instances to keep the service running if one or more of the
# instances fail. No matter the reason, we use orchestration tools and techniques to make sure that the instances are
# repeatable. And once we've set up replicated machines, we'll want to distribute the requests across instances.

# This is where load balancing comes into play. Let's take a closer look at the different load balancing methods.
# A pretty common load balancing technique is 'Round-robin DNS'.

# 'Round robin' is a really common method for distributing tasks.
# Imagine you're giving out treats at a party. First, you make sure that each of your friends gets one cookie.
# Then you give everyone a second serving and so on until all of the treats are gone or your guests say: "Thank you,
# we're full". That's the round-robin approach to eating all the cookies.

# Now, if we want to translate URL like 'myservice.example.com' into an IP address, we use the DNS protocol or
# 'Domain Name System'. In the simplest configuration, the URL always gets translated into exactly the same IP address.
# But when we configure our DNS to use 'round robin', it'll give each client asking for the translation a group of IP
# addresses in a different order. The clients will then pick one of the addresses to try to reach the service.
# If an attempt fails, the client will jump to another address on the list. This load balancing method is super easy to
# set up. You just need to make sure that the IPs of all machines in the pool are configured in your DNS server, but it
# has some limitations.

# First, you can't control which addresses get picked by the clients. Even if a server is overloaded, you can't stop
# the clients from reaching out to it. On top of that, DNS records are cached by the clients and other servers.
# So if you need to change the list of addresses for the instances, you'll have to wait until all of the DNS records,
# that were cached by the clients, expire.

# To have more control over how the load's distributed and to make faster changes, we can set up a server as a
# 'Dedicated load balancer'. This is a machine that acts as a proxy between the clients and the servers.
# It receives the requests and based on the rules that we provide, it directs them to the selected back-end server.

# Load balances can be super simple or super complex depending on the service needs.
# Say your service needs to keep track of the actions that a user has taken up till now. In this case, you'll want your
# load balancer to use 'sticky' sessions. Using sticky sessions means all requests from the same client always go to the
# same backend server. This can be really useful for services than need it but can also cause headaches when migrating
# or maintaining your service. So you need to use it only if you really need it.

# Another cool feature of load balancers is that you can configure them to check the health of the backend servers.
# Typically, we do this by making a simple query to the servers and checking that the reply matches the expected reply.
# If a back-end server is unhealthy, the load balancer will stop sending new requests to it to keep only healthy servers
# in the pool.

# As we've called out a few times already, a cool feature of cloud infrastructure is how easily we can add or
# remove machines from a pool of servers providing a service. If we have a load balancer controlling the load of the
# machines, adding a new machine to the pool is as easy as creating the instance. And then letting the load balancer
# know that it can now route traffic to it. We can do this by manually creating and adding the instance or
# when our services under heavy load, we can just let the autoscaling feature do it.

# Okay, so imagine that you've built out your service with load balancers, and you're receiving requests from all over
# the world. How do you make sure that clients connect to the servers that are closest to them?

# You can use GeoDNS and GeoIP.

# These are DNS configurations that will direct your clients to the closest geographical load balancer. The mechanism
# used to route the traffic relies on how the DNS servers respond to requests.
# For example, from machines hosted in North America, a DNS server in North America might be configured to respond with
# the IPs in North America.

# It can be tricky to set this up on your own but most Cloud providers offer it as part of their services making
# it much easier to have a geographically distributed service.

# There are some providers dedicated to bringing the contents of your services as close to the user as possible.
# These are the 'Content Delivery Networks' or CDNs.

# They make up a network of physical hosts that are geographically located as close to the end user as possible.
# This means that CDN servers are often in the same data center as the users Internet service provider.
# CDNs work by caching content super close to the user. When a user requests say, a cute cat video, it's stored in the
# closest CDN server. That way, when a second user in the same region requests the same cat video, it's
# already cached in a server that's pretty close, and it can be downloaded extra fast.
