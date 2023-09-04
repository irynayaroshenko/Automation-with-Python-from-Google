"""Modifying and Testing Manifests"""
# It's pretty common for IT specialist working on configuration management to test out new rules on their
# machines by simply forcing the machine to apply the manifest they want to test. We've done this in some of our
# examples where we applied the rules locally before applying them to remote machines, this approach can backfire though

# Say you're trying to use puppet to change the permissions of some files on the node locking down some paths that you
# don't think that your users will need. Now imagine you try out the rules on your computer and discover you made a
# mistake and locked yourself out. So what can you do instead?

# There's a bunch of things to consider.

# A simple first step is to use 'puppet parser validate' command that checks that the syntax of the manifests is
# correct.
# On top of that we can also run the rules using '--noop' parameter. Name comes from 'no operations' and makes
# puppet simulate what it would do without actually doing it. You can look at the list of actions that it would take and
# check that they're exactly what you wanted puppet to do.
# But if the change is complex, it's likely that we'll miss something important when looking at the planned actions.

# Another option you could use is having test machines that are used only for testing out changes.
# You can apply the rules there and after a puppet has run, check that everything's working correctly.
# But again, this is a manual process, and we might forget to verify something important.

# How can we automate it? Kind of like the python automatic tests that we checked out in an earlier course, Puppet also
# lets us test our manifests automatically by using 'rspec tests'.
# In these tests we can set the facts involved different values and check that the catalog ends up stating what we
# wanted it to. Let's check out an example:

# describe 'gksu', :type => :class do
#     let (:facts) { { 'is_virtual' => 'false '} }
#     it { should contain_package('gksu').with_ensure('latest')}
# end

# Here we're setting the 'is_virtual' fact to 'false'.
# And then we asked the test infrastructure to verify that the 'gksu' package is included 'with_ensure' parameter
# set to 'latest'.

# Test like this one can be a useful way to check that our catalog is written correctly. And they can be super helpful
# when a rule is used a lot of facts that interact with each other, and we want to check that the result is actually
# what we intended.

# We can write a bunch of these tests and run them automatically whenever there is a change to the rules. This way we
# can be sure that the rules stay valid and know that the new changes didn't break the old rules. But that's just checks
# that the catalog contains the rules that we set should contain.
# How can we verify that these rules actually have the effects we want, like enabling the corporate website or setting
# up a strict firewall?
# We need to apply the rules on the nodes and check that the result is correct. We can automate this process too. To do
# this we can use the set of test machines where we first apply the catalog and then use scripts to check that the
# machines are behaving correctly.

"""Safely Rolling out Changes and Validating Them"""
# Once you've prepared and tested the changes that you want to make, it's time to roll them out, but not so fast.
# Even if you've tested the change on your computer or on a test computer, and it worked just fine, it doesn't mean that
# the change will work correctly on all machines running in production.

# In an infrastructure context, 'Production' is the part of the infrastructure where a service is executed and served to
# its users. If you host a website, the servers that deliver the website content to the users are the production servers
# Inside your company, the servers that validate users passwords are the production authentication servers, etc.

# Making changes to the production servers can be tricky because if something goes wrong, the service can go down.
# So how can we roll out changes safely?

# The key is to always run them through a 'Test environment' first.
# The test environment should have one or more machines running the exact same configuration as the production
# environment. But these machines aren't actually serving any users of the service.

# This way, there's a problem when deploying the changes should be able to fix it without any actual users seeing it.
# As we briefly touched on in an earlier video, Puppet has environments built in. Each environment has its own directory
# with its own set of manifests and modules. Puppet environments let us fully isolate the configurations that agent see
# depending on what environment they're running.
# This isn't just what nodes install which modules, it's also the whole contents of the modules.

# For example, we can use this to try out a whole new version of the Apache module for the machines in the test
# environment while still using the old version for the production environments.

# You can define as many environments as you need.
# For example, you could have a development environment for IT specialists to try out new Puppet rules before they
# even reach the test environment, or say you're developing a very tricky new feature for your system and don't know
# when it'll be ready. You could have an environment for testing just that specific feature.

# Now, let's assume that you have a bunch of changes ready to roll out.
# You'll usually push them to the machines in the test environment first and check that everything works well there.
# This can include both manual verification and automated checking. Say the changes worked fine in the test environment,
# how do you roll them out to the other machines in your fleets?

# You might be tempted to just apply the changes to all the machines and be done with it. But pushing changes to every
# machine at the same time is usually not a great idea. It's always possible that we missed some special case when
# preparing the change which wasn't part of our test environment and suddenly, half our fleet is offline.
# So instead of pushing the changes to all nodes, we usually do it in batches.

# There's a bunch of ways you can do this depending on how your fleet is arranged.
# You could have some machines with the fact that marks them as early adopters or 'Canaries'.
# Like the canaries that coal miners used to detect toxic gases in the mines, these nodes detect potential issues
# before they reach the other computers.

# So you could push the changes to the canaries on one day, check that everything's working fine, and then deploy them
# to the rest of the fleet on the next day. That way, if there's an issue with the changes that wasn't caught in testing,
# only a subset of the users might see it.

# As soon as you get notified of the problem, you can roll it back and avoid it hitting the rest of the fleet.

# Now, we've been talking about changes without going into detail on what those changes are.
# It's a good idea for these changes to be small and self-contained. That way, if something breaks,
# it's much easier to figure out where the problem was.

# Imagine you're trying to push six months work of changes to your fleet of computers. When you push this to machines
# in the test environment, you discover that they stop responding all together. You now need to come through
# all the changes that were bundled together to try to find out which one is causing the problem X.

# Instead, you could aim to roll out your changes every one or two weeks. This would mean that whenever a problem is
# detected, there's only a small list of changes to go through to figure out the problem.

# Of course, there's a lot more to say about testing and releasing changes safely. But you don't need to put
# all the best practices in place to get started. You could start small and make improvements as you go.
# As your manifests get more complex, you want to improve the automated testing of all the pieces.
# And as the fleet you manage with your configuration management system grows in size, you want to increase the size
# of your testing environment, move some nodes to canaries and so on.
