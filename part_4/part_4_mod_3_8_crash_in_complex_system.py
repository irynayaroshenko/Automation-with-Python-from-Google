"""Crashes in Complex Systems"""
# Up to now we've talked about how to diagnose and fix errors that are confined to one computer.
# That's a common case for computers that are used by a single user.
# But once we start going into complex systems that involve many different services, we'll need to take a look at the
# bigger picture and have different computers interact with each other.

# Say you're in charge of the e-commerce site for your company.
# The page, seen by the users, recently started responding with 'Internal server error' to about 20% of all requests.
# How do you figure out what's going on?

# You want to apply the same principles that we saw for troubleshooting a problem on one computer, but this time at a
# larger scale. So you'll want to check the log messages in the servers providing the service, and see if you find any
# additional information pointing to what's causing the issue.

# You'll want to find any log specific to the service that's failing, and also look at the general system logs to see
# if there's a problem affecting the server in general.

# For this example, let's say you find a bunch of entries in the logs that say, 'Invalid response from server'.
# That's not a great error message. You don't know what the request was or what the response was, but it's at least a
# clue that whatever happening, it's related to some other service in the overall system.

# We said that this started failing recently, so it might make sense to figure out what changed between, when it was
# working correctly and when it started to fail.

# Was there a new version of the system deployed?
# Were there any relevant changes regarding the requests?

# Let's say this is happening on a Tuesday morning, and the latest release of this service was the previous week.
# Things were working fine until today, and the requests seemed normal, nothing out of the ordinary.
# So the service itself is probably okay, but what about the other services involved in the system?

# Was there a new version of one of the underlying systems, like the database, the authentication service, or some
# other back-end server like the inventory, billing, or procurement systems?

# Looking at recent changes, you see that there were a bunch of changes made earlier in the day to the load balancer
# used between the front-end and the back-end services. Since the only clue you have is that the response from the
# service was invalid, you're not sure that these changes are at fault, but they sure seem suspicious.

# Whenever possible, the best strategy is to roll back the changes that you suspect are causing the issue, even if you
# aren't 100% sure if this is the actual cause. If your infrastructure allows easy rollbacks, try that before doing any
# further investigation.

# Why? Because that way, you'll restore the service back to health if it was the cause, or you'll eliminate this change
# as a possible cause if doing the rollback doesn't help.

# Whether you do the rollback or not, when coming across unhelpful error messages, it's a good idea to improve them.
# Instead of the error just saying that the response is invalid, change it to include what the request and the response
# were, and why the response was invalid. That way, the next time you're trying to debug a similar issue you already
# have more information to work with.

# For this example, if error had included this information you'd have seen that the invalid response was a 404 error.
# This was caused by having a server added to the pool as part of the inventory system, but the server actually belonged
# to the procurement system.

# Now, say a couple of weeks later you see that again, there are a bunch of internal server errors in the same service.
# It might be tempting to assume that it's the load balancer's fault once again, but by now you know that you should
# always look at the logs first and see what you find.

# There's no reason why the error should be the same this time. When looking at the logs you may notice, for example,
# that only one of the front-end servers is actually affected by the problem. All the other machines are serving their
# content successfully.

# In a case like this, you'd start by first removing the machine from the pool of servers that can provide this service.
# That way, you avoid users getting any more errors. Well, you can investigate what's going on with the broken machine.

# As you've probably realized by now, when dealing with complex systems like these having good logs is essential to
# understanding what's going on. On top of that, you'll want to have good monitoring of what the service is doing and
# use version control for all changes so that you can quickly check what's changed and roll back when needed.

# It's also important that you can very quickly deploy new machines when necessary.
# This could be achieved by either keeping standby servers, in case you need to use them, or by having a tested pipeline
# that allows you to deploy new servers on demand.

# A lot of companies today have automated processes for deploying services to virtual machines running in the cloud.
# This can take a bit of time to set up, but once you've done that you can very easily increase or reduce the amount of
# servers you're using. This can help a lot when investigating and solving problems.

# But one thing to take into account when the servers are running as virtual machines, especially if they're running in
# the cloud, is that there might be external limits apply to these services. Resources, like the available CPU time,
# RAM, or network bandwidth, might be artificially capped.

# And not only that, the use of certain external services can also be limited, like how many database connections you
# can have at the same time or how much data you can store. If these limits are causing problems with your application,
# you might need to rethink how you use your resources.


"""Communication and Documentation During Incidents"""
# Until now, we've discussed how we can troubleshoot
# computers or systems with a specific issue.
# We've covered how we can get
# enough information so we can identify the root cause,
# and then apply the necessary remediation.
# There's another aspect to all of this.
# What is related to how we handle
# the communication with those affected by
# the issue and how we distribute
# tasks when addressing large issues as a team.
# Armed with what you've learned so
# far and your past experience,
# you might do a great job troubleshooting a problem.
# But if you drop the ball when it
# comes to communicating what you're doing,
# you could end up with a bunch of
# frustrated users calling you to find out what's going on.
# If you don't write down what you've
# tried or how you fix the problem,
# you risk for getting some important details and wasting
# a lot of valuable time when you need to revisit an issue.
# When working on a problem,
# it's always a good idea to document
# what you're doing in a bug or ticket.
# If there's no such system at
# your company, then use a doc,
# a text file, or Wiki,
# or whatever you have access to.
# Documenting what you do,
# lets you keep track of what you've
# tried and what the results were.
# This might seem unnecessary.
# But after a whole day of troubleshooting a problem,
# it's pretty common for us to forget what we've
# tried or what was the outcome of a specific action.
# On top of that,
# having all this info available
# in some electronic forum lets
# you easily share all the data
# you've collected with other team members.
# If for example, you brought something
# back which turned out to be unrelated.
# Having the whole process document it,
# helps you remember to roll forward again.
# While you're working on a problem,
# it's important to communicate
# clearly with those affected by the issue.
# They want to know what you figured out about the problem,
# what the available workarounds are,
# and when they can expect the next update.
# If you don't know what the problem is,
# it's hard to give an estimation
# of when you'll have it fixed.
# But you can still provide
# timely updates about the work you're doing.
# This kind of regular communication is
# helpful no matter the size of the incident.
# But the more people affected,
# the more you'll want to provide
# regular updates with clear instructions
# of what users can do
# and what they can expect as a solution.
# That way, they can better plan and organize their time.
# If access to the Internet is down,
# you want to let people know if they can expect to fix in
# one or two hours or if it's going to take the whole day.
# This info can make a difference between
# people choosing to discuss issues
# in person for a couple of
# hours or deciding to work from home.
# If the issue is big enough that you're
# involving more people in finding a solution,
# you should agree on who's going to work on which tasks.
# For example, you could have someone working
# on finding out a temporary workaround,
# while someone else is in
# charge of understanding the root cause
# of the problem and finding the long-term remediation.
# Or if there are lots of possible causes for the issue,
# you could divide the causes among
# the team members and have them work on those in parallel.
# On top of people looking for
# the root cause and a solution,
# you want to have a person in charge of
# communicating with the people affected.
# This lets the team avoid forgetting to update
# the tracking issue or even
# worse providing contradictory information.
# This communications lead needs
# to know what's going on and
# provide timely updates on
# the current state and how
# long until the problem's resolved.
# They can act as a shield for questions from users
# letting the rest of the team focus on the actual problem.
# Similarly, there should be one person in
# charge of delegating the different tasks
# to the team members.
# This person sometimes called
# the Incident Commander or Incident
# Controller needs to look at the big picture and
# decide what's the best use of the available resources.
# They can make sure that there's
# no duplication of work among
# team members and that
# only one person is
# modifying the production system at a time.
# Having multiple people make overlapping changes to
# the system could lead to confusing results,
# making the outage even longer.
# Of course, this division of
# roles makes the most sense when there's
# a large incident and there's
# a big team working on figuring out the solution.
# If it's only two or three people working on the problem,
# it's still important to agree who
# will work on what but you
# probably don't need to use
# any special role names to do that.
# Once the issue has been resolved,
# it's super-important to sum
# up the information that was helpful.
# The most important information that you'll
# want to include are the root cause,
# how you diagnose the problem and found that root cause,
# what you did to fix the issue and what
# needs to be done to prevent
# the problem from happening again.
# Depending on the size of
# the issue and the number of people affected,
# this summary could just be the last update to
# the bug or ticket that you
# use to keep track of your work,
# or it could be a full postmortem.

"""Writing Effective Postmortems"""
# In our last video, we talked about the importance of
# communication and documentation
# when troubleshooting incidence.
# We called out that if the issue is big enough,
# we might want to document what happened in a postmortem.
# Postmortems are documents that describe details
# of incidence to help us learn from our mistakes.
# When writing a postmortem,
# the goal isn't to blame whoever caused the incident,
# but to learn from what happened to
# prevent the same issue from happening again.
# To do this, we usually document
# what happened, why it happened,
# how it was diagnosed,
# how it was fixed,
# and finally figure out what we can
# do to avoid the same event happening in the future.
# Remember the main goal is to learn from our mistakes.
# Writing a postmortem isn't about getting someone
# fired but about making sure that next time we do better.
# Writing postmortems after dealing with
# incidence is important because it helps us
# avoid dealing with them again or at
# least learn how to deal with the next incident better.
# While Postmortems are super useful with large incidence,
# you don't need to wait until something huge
# happens to write your first postmortem.
# You can practice riding them for any kind of event
# where there's something to be learned
# no matter how small.
# That way, when you need to write
# a postmortem after a big incident,
# you know how to concentrate on
# the things that matter the most.
# What you can learn from the problem
# and how you can prevent it in the future.
# So what should you write in a postmortem?
# The exact structure might vary depending on
# preference and the type
# of incident that you're dealing with.
# In general, you'll want to include
# the details of what caused the issue,
# what the impact of the issue was,
# how it got diagnosed,
# the short-term remediation you applied,
# and the long-term remediation you recommend.
# If the document is long and
# you're going to share it with a lot of people,
# you want to include a summary
# that highlights the root cause,
# the impact, and what needs to be
# done to prevent the issue from happening again.
# It's useful to include what went well in postmortems too.
# When working on a problem,
# we might realize that it would have been much
# worse if we didn't have
# certain tools or systems available.
# For example, we might
# say that we were able to solve the problem
# quickly by doing a roll back to
# the previous version or that we
# caught the issue before users even noticed
# it because we had good monitoring and alerting.
# Noting the things that went well helps us show that
# our systems are effective
# and justifies keeping those systems running.
# Writing a postmortem can sometimes help
# you understand the services that
# you're working with much better.
# Earlier this year, a service I worked on had
# a large outage and I
# needed to provide information on what happened.
# To do this, I needed to
# parse through hundreds of gigabytes of
# archive logged data to show that
# certain data had never been received by the service.
# Doing this, I realized
# that I needed to improve the data logged
# by our tools to give
# better information and have better reporting.
# You can even practice writing
# postmortems outside of the IT context.
# Like, if you bake cookies and
# they don't turn out as great as you wanted them to,
# document what you did, what went wrong,
# what went right, and how you
# can improve the results in the future.
# You can do this with any hobby that you have.
# Maybe photography, 3D printing or brewing your own beer.
# You don't always need to write the whole thing down.
# Sometimes a mental note is enough,
# like if you bike to work and realize
# wearing your backpack hurts your shoulders,
# make a mental note to add a basket to your bike.
# So you can put your backpack there next time,
# or if on your last trip it was colder
# than expected and you forgot to bring a jacket,
# make a mental note that next
# time you should check the weather before you leave.
# Once again, remember that
# the most important part of
# the postmortem is what we can learn for the future.
# So if instead of writing
# a whole document you're creating
# a one paragraph summary of the incident.
# Remember to focus that
# paragraph on what you can do better,
# not on whatever mistake caused the incident.
