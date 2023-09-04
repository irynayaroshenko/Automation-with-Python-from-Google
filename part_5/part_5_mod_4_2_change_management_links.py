"""Change Management"""

# Let's talk about how to keep your service running in the cloud.
# Most of the time when something stops working, it's because something changed. If we want our cloud service to be
# stable, we might be tempted to avoid changes altogether. But change is a fact of cloud life.

# If we want to fix bugs and improve features in our services, we have to make changes.
# But we can make changes in a controlled and safe way. This is called 'Change Management', and it's what lets us keep
# innovating while our services keep running.

# Step one in improving the safety of our changes, we have to make sure they're well-tested. This means running unit
# tests and integration tests, and then running these tests whenever there's a change.

# In an earlier course, we briefly mentioned Continuous Integration, or CI, but here's a refresher.
# CI system will build and test our code every time there's a change. Ideally, the CI system runs even for changes that
# are being reviewed. That way you can catch problems before they're merged into the main branch.

# You can use a common open source CI system like Jenkins, or if you use GitHub, you can use its Travis CI integration.
# Many cloud providers also offer continuous integration as a service.
# Once the change has committed, the CI system will build and test the resulting code.

# Now you can use Continuous Deployment, or CD, to automatically deploy the results of the build or Build Artifacts.
# CD lets you control the deployment with rules. For example, we usually configure our CD system to deploy new builds
# only when all the tests have passed successfully. On top of that, we can configure our CD to push to different
# environments based on some rules. What do we mean by that?

# In an earlier video, we mentioned that when pushing Puppet changes, we should have a Test environment separate from
# the Production environment. Having them separate lets us validate that changes work correctly before they affect
# users.

# Here 'Environment' means everything needed to run the service. It includes the machines and networks used for
# running the service, the deployed code, the configuration management, the application configurations, and the customer
# data.

# Production, usually shortened to Prod, is the real environment, the ones users see and interact with.
# Because of this, we have to protect, love, and nurture a prod. The test environment needs to be similar enough to prod
# that we can use them to check our changes work correctly.

# You could have your CD system configured to push new changes to the test environment. You can then check that the
# service is still working correctly there, and then manually tell your deployment system to push those same changes to
# production.

# If the service is complex and there are a bunch of different developers making changes to it, you might set up
# additional environments where the developers can test their changes in different stages before releasing them.
# For example, you might have your CD system push all new changes to a development or Dev environment, then have a
# separate environment called Pre-Prod, which only gets specific changes after approval.
# And only after a thorough testing, these changes get pushed to Prod.

# Say you're trying to increase the efficiency of your service by 20%, but you don't know if the change you made might
# crash part of your system. You want to deploy it to one of those testing or development environments to make sure it
# works correctly before you ship it to prod. Remember, these environments need to be as similar to prod as possible.
# They should be built and deployed in the same way. And while we don't want them to be breaking all the time, it's
# normal for some changes to break dev or even pre-prod. We're just happy that we can catch them early so that they
# don't break prod.

# Sometimes you might want to experiment with a new service feature. You've tested the code, you know it works, but
# you want to know if it's something that's going to work well for your users. When you have something that you want to
# test in production with real customers, you can experiment using 'A/B testing'.

# In A/B testing, some requests are served using one set of code and configuration (A), and other requests are served
# using a different set of code and configuration (B).

# This is another place where a load balancer and instance groups can help us out. You can deploy one instance group in
# your A configuration and a second instance group in your B configuration. Then by changing the configuration of the
# load balancer, you can direct different percentages of inbound requests to those two configurations.
# If your A configuration is today's production configuration and your B configuration is something experimental,
# you might want to start by only directing 1% of your requests to B. Then you can slowly ramp up the percentage that
# you check out whether the B configuration performs better than A, or not.

# Heads up, make sure you have basic monitoring so that it's easy to tell if A or B is performing better or worse.
# If it's hard to identify the back-end responsible for serving A requests or B requests, then much of the value of
# A/B testing is lost to A/B debugging. So what happens if all the precautions we took aren't enough, and we break
# something in production?

# Remember what we discussed in an earlier course about post-mortems? We learn from failure and build the new knowledge
# into our change management. Ask yourself, what did I have to do to catch the problem? Can I have one of my change
# management systems look for problems like that in the future? Can I add a test or a rule to my unit tests, my CI/CD
# system, or my service health checks to prevent this kind of failure in the future?

# Sometimes in IT these things happen, no matter how careful you are. And as you use and refine your change management
# systems and skills, you'll gain the confidence to make changes to your service more quickly and safely.

"""Understanding Limitations"""
# We've spent a while talking about how to make your service runs smoothly in the Cloud. Now let's take a moment to
# talk about some of the problems that you might come across. Personally, I find that when writing software to run on
# the Cloud, it's important to keep in mind how my application will be deployed. The software I'm creating needs to be
# 'fault tolerant' and capable of handling unexpected events. Instances might be added or removed from the pool as
# needed and if an individual machine crashes, my service needs to breeze along without introducing problems.
# And not every problem results in a crash, sometimes we run into quotas or limits, meaning that you can only perform a
# certain number of operations within a certain time period.

# For example, when using Blob Storage there might be a limit of 1,000 writes to the same blob in a given seconds.
# If your service performs a lot of these operations routinely, it might get blocked by these limits.
# In that case, you'll need to see if you can change the way you're doing the operations, for example, by grouping all
# the calls into one batch. Switching to a different service is sometimes an option too.

# Some API calls used in Cloud services can be expensive to perform, so most Cloud providers will enforce 'Rate limits'
# on these calls to prevent one service from overloading the whole system.

# For example, there might be a rate limit of one call per second for an expensive API call.
# On top of that, there are also 'Utilization limits', which cap the total amount of a certain resource that you can
# provision. These quotas are there to help you avoid unintentionally allocating more resources than you wanted.

# Imagine you've configured your service to use autoscaling, and it suddenly receives a huge spike in traffic.
# This could mean a lot of new instances getting deployed which can cost a lot of money. For some of these limits, you
# can ask for a 'Quota increase' from the Cloud provider if you want additional capacity, and you can also set a smaller
# quota in the default to avoid overspending. This can be a great idea when you're running a service on a tight budget.

# If your service performance expensive operations routinely, you should make sure you understand the limitations of
# the solution that you choose. A lot of platform as a service and infrastructure as a service offerings have costs
# directly related to how much they're used.

# They also have usage quotas. If the service you've built suddenly becomes very popular, you can run out of quota or
# run out of budget. By imposing a quota on an auto-scaling system, the system will grow to meet user demand until it
# reaches the configured limit. The trick here is to have good monitoring and alerting around behavior like this.

# If your system runs out of quota but there's an increased demand for a puppy videos, the system may have problems,
# degraded performance or worse yet an outage. So you want to be notified as soon as it happens that you can decide
# whether to increase your quota or not.

# Finally, let's talk about dependencies. When your service depends on a Platform as a Service offering like a hosted
# database or CI/CD system, you're handing the responsibility for maintenance and upgrades of that service off to your
# Cloud provider, that's great, fewer things to worry about and maintain, but it also means that you don't always get
# to choose what version of that software you're using. You might find yourself on either side of the upgrade cycle,
# either wanting to stay at a version that's working well for you or wanting the Cloud provider to hurry up and upgrade
# to resolve a bug that's affecting your service. Your Cloud provider has a strong incentive to keep its service
# software fairly up-to-date. Keeping software as a service solutions up to date ensures that customers aren't
# vulnerable to security flaws, that bugs are promptly fixed and that new features get released early.

# At the same time, the Cloud provider has to move carefully and test changes to keep destruction of its service to a
# minimum. They will communicate proactively about changes to the services that you use and in some cases,
# Cloud providers might give you access to early versions of these services.

# For example, you can set up a test environment for your service that uses the Beta or Pre-release version of
# a given software as a service solution, letting you test it before it impacts production.

"""More About Cloud Providers"""
# https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas
# https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html
# https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits
