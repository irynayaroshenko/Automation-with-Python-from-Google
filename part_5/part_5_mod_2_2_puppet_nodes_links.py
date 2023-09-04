"""Puppet Nodes"""
# When managing fleets of computers, we usually want some rules to apply to every computer, and other rules to apply
# only to a subset of systems. Let's say you're managing all your servers with Puppet. You might want to install a
# basic set of tools on all of them, but only install the packages for serving web pages in your web servers.
# And only install the packages for sending and receiving email in your mail servers.
# There's a bunch of different ways that we can do this.

# In an earlier video, we saw how to conditionally apply some rules using facts from the machines.
# Another way to apply different rules to different systems is to use separate 'Node definitions'.

# In Puppet terminology, a node is any system where we can run a Puppet agent.
# It could be a physical workstation, a server, a virtual machine, or even a network router, as long as it has a Puppet
# agent and can apply the given rules. So we can set up Puppet to give some basic rules to all the nodes, but
# then apply some specific rules to the nodes that we want to be different.

# When setting up Puppet, we usually have a default node definition that lists the classes that should be included for
# all the nodes. For example, it could look something like this:

# node default {
#     class { 'sudo': }
#     class { 'ntp':
#         servers => ['ntp1.example.com', 'ntp2.example.com']
#     }
# }

# Here, the default node is including two classes: sudo and ntp.
# For ntp class, we're setting an additional servers parameter that lists servers we can use to get the network time.
# As you can see here, when defining a node, you can include a class by just using its name if there's no additional
# settings, or include the class and set additional parameters if necessary.

# That's the default node, so it will apply to computers in the fleet by default.
# What if you want some settings to only apply to some specific nodes?
# You can do that by adding more node definitions that list the classes that you want them to include, like this:

# node webserver.example.com {
#     class { 'sudo': }
#     class { 'ntp':
#         servers => ['ntp1.example.com', 'ntp2.example.com']
#     }
#     class { 'apache': }
# }

# We can see here that specific nodes in the fleet are identified by their FQDNs - fully qualified domain names.
# In this case, we have the node definition for a host called webserver.example.com. For this node, we're including the
# same sudo and ntp classes as before, and we're adding the apache class on top.

# We're listing the same classes because the classes included in the default node definition are only applied to the
# nodes that don't have an explicit entry. In other words, when a node requests which rules it should apply,
# Puppet will look at the node definitions, figure out which one matches the node's FQDN, and then give only those rules

# To avoid repeating the inclusion of all the common classes, we might define a base class that does the work of
# including all the classes that are common to all node types.

# Now, where's this information stored?
# The node definitions are typically stored in a file called 'site.pp', which isn't part of any module. Instead, it just
# defines what classes will be included for what nodes. This is another step towards helping us organize our code in a
# way that makes it easier to maintain.

"""Puppet's Certificate Infrastructure"""
# We've called that a few times that in typical Puppet deployments, all managed machines in the fleet connect to a
# Puppet server. The client send their facts to the server, and the server then processes the manifests, generates the
# corresponding catalog, and sends it back to the clients who apply it locally. In our last video, we mentioned that we
# can apply different rules to different nodes depending on their names. The clients send their name to the server when
# they connect, but how can the server trust that a client is really who he claims to be?

# Puppet uses Public Key Infrastructure, or PKI, to establish secure connections between the server and the clients.
# There's a bunch of different types of public key technologies. The one used by Puppet is Secure Sockets Layer or SSL.
# This is the same technology used for encrypting transmissions over HTTPS.

# The clients use this infrastructure to check the server's identity, and the server uses it to check the client's
# identity, and all communication is done over an encrypted channel that uses these identities, so it can't be
# intercepted by other parties.
# So how does this work?

# Each machine involved has a pair of keys related to each other, a private key and a public key.
# The private key is secret, only known to that specific machine, the public key is shared with other machines involved.
# Machines can then use the standardized process to validate the identity of any other machine. The sender signs a
# message using the private key and the receiver validates the signature using the corresponding public key.

# How do machines know which public keys to trust?
# This is where a Certificate Authority, or CA comes in.

# The CA verifies the identity of the machine and then creates a certificate stating that the public key goes with that
# machine. After that, other machines can rely on that certificate to know that they can trust the public key, since it
# means the machine's identity has been verified.

# Puppet comes with its own certificate authority, which can be used to create certificates for each client.
# So you can use that one, or if your company already has a CA that validates the identity of machines in your fleet,
# you can integrate it with Puppet, so you only validate the identities once.

# Now, let's assume you're using the baked-in certificate infrastructure and dive into how this process works.
# When a node checks in to the Puppet master for the first time, it requests the certificate.
# The Puppet master looks at this request and if it can verify node's identity, it creates a certificate for that node.
# The system administrator can check the identity manually or use a process that does this automatically using
# additional information about the machines to verify their identity.

# When the agent node picks up this certificate, it knows it can trust the Puppet master, and node can use the
# certificate from then on to identify itself when requesting a catalog.

# Why do we care so much about the identity of the nodes? There's a bunch of reasons.

# First, Puppet rules can sometimes include confidential information that you don't want to fall in the wrong hands.
# But even if none of the rules hold confidential info, you want to be sure that the machine you're setting up as you
# web server really is your web server and not a rogue machine that just claims to have the same name.

# All sorts of things could go wrong if random computers start popping up in your network with the wrong settings.
# If you're creating a test deployment to try out how Puppet rules get applied, and so you're only managing tests
# machines, you can configure Puppet to automatically sign all requests, but you should never do this for
# real computers being used by real users. Remember that it's better to be safe than sorry. So always take the time to
# authenticate your machines.

# When starting out with Puppet, it's common to use the manual signing approach. In this case, when the node connects
# to the master, it will generate a certificate request, which will go into a queue in the Puppet master machine.
# You'll then need to verify that the machine's identity is correct and the baked-in CA will issue the corresponding
# certificate.

# If your fleet is large, this manual approach won't really work. Instead, you'll want to write a script that verifies
# the identity of the machines automatically for you. One way to do this is by copying a unique piece of information
# into the machines when they get provisioned and then use this pre-shared data as part of the certificate request.
# That way, your script can verify that the machines are who they claim to be without involving any humans.

"""Setting up Puppet Clients and Servers"""
# We're now ready to see a Puppet deployment in action. We've already installed the Puppet master package on this
# computer, so we'll use it as the master.
# Since this is a test deployment to demonstrate Puppet, we'll configure it to automatically sign the certificate
# requests of the nodes we add.
# But remember, if we were deploying this to real computers, we'd have to manually sign the requests or implement a
# proper validating script.
# We'll do this by calling the Puppet command with the config parameter, and then saying that in this section master
# we want to set auto sign to true:

# sudo puppet config --section master set autosign true

# With that, we can connect to the client that we want to manage using Puppet.
# We'll connect using SSH to a machine called web server:

# ssh webserver

# On this machine, we'll install the Puppet client which is shipped by the Puppet package

# sudo apt install puppet

# open puppet_setup_1.png
# We have the Puppet agent installed.

# Now we need to configure it to talk to the Puppet server that we're running on the other machine.
# To do that, we'll use Puppet config like before but this time we'll tell it that we want to set the server to
# ubuntu.example.com:

# sudo puppet config set server ubuntu.example.com

# Now that we've configured the server, we can test the connection to the Puppet master by using the Puppet agent
# command passing '-v' as before to get verbose output, and '--test' to do a test run (open puppet_setup_2.png):

# sudo puppet agent -v --test

# As usual, Puppet tells us everything it did.
# It first created an SSL key for the machine. It then read a bunch of information from the machine and used this to
# create a certificate request.
# The agent shows us the fingerprint of the certificate requested.
# If we were using manual signing, we could use this fingerprint to verify that the request and the server matches
# the one generated on the machine. The certificate was then generated on our puppet master. We don't see any entries
# for that because it happened on the other computer. But we see that this computer received a certificate and stored it
# locally.
# Once the certificate exchange completed, the agent retrieved all the information from the machine and sent it to the
# master. In exchange, it got back a catalog and applied it. The catalog applied almost immediately because we
# haven't actually configured any rules to be applied to our clients. We should go ahead and do that now.

# We'll go back to our Puppet master and create a couple of node definitions. As we called out, node definitions are
# stored in a manifest file called site.pp, which is stored at the root of the nodes environment.
# We'll talk more about environments in a later video. For now, we just need to know that our client is trying
# to access the production environment.
# So the file that we need to create will be:

# /etc/puppet/code/environments/production/manifests/site.pp

# In this file, we'll create a couple of node definitions. We want to install Apache in our web server, so we'll create
# a node definition for the web server with the Apache class and node parameters for now, and we'll also add a default
# node definition. We'll keep it empty for now. We can add more classes in the future.

# node webserver.example.com {
#     class { 'apache': }
# }
#
# node default {}

# With that, we have our very basic node definition. We can now save this and run the Puppet agent on our web server
# machine again:

# sudo puppet agent -v --test

# This time, the Puppet agent connected to the Puppet master and got a catalog that told it to install and configure
# Apache package. This included setting up a bunch of different services. open puppet_setup_3.png

# Up to now, we've been doing manual runs of the Puppet agent for testing purposes.
# Now that we know it's working fine, we want to keep Puppet running automatically. That way, if we make changes to the
# configuration, clients will automatically apply those changes without us having to do any manual steps.
# So to do that, we'll use the system CTL command, which lets us control the services that are enabled when
# the machine starts and those that are currently running.

# So we'll first tell the system CTL to enable the puppet service so that the agent gets started whenever the machine
# reboots:

# sudo systemctl enable puppet

# and then we'll tell system CTL to start the puppet service so that it starts running:

# sudo systemctl start puppet

# Last step, we'll ask systems CTL for the status of the Puppet service to check that it's actually running:

# sudo systemctl status puppet

# That worked. open puppet_setup_4.png

# The Puppet agent will keep regularly checking in with the master and ask if there are any changes that need to be
# applied to the machine. With that, you've seen Puppet in action using the server-client model.

# We use the configuration we set in the Puppet master to manage the installation and configuration of software in our
# web server, and we set up the Puppet agent in the web server to keep running so that the configuration stays up to
# date.
# We've only seen the very basics of how to configure Puppet, but this can already give you an idea of
# how powerful configuration management can be.

"""More Information about Deploying Puppet to Clients"""
# http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/
