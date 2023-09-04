"""Getting Started with Monitoring"""
# As we called out in an earlier video, once we have our service running in the Cloud, we want to make sure that our
# service keeps running, and not just that. We want to make sure it keeps behaving as expected, returning the right
# results quickly and reliably. The key to ensuring all of this, is to set up good Monitoring and Alerting rules.

# To understand how our service is performing, we need to monitor it. Monitoring lets us look into the history and
# current status of a system.

# How can we know what the status is? We'll check out a bunch of different metrics. These metrics tell us if the service
# is behaving as expected or not. Well, some metrics are generic, like how much memory an instance is using. Other
# metrics are specific to the service we want to monitor.

# Say your company is running a website, and you want to check if it's working correctly. When a web server responds to
# an HTTP request, it starts by sending a response code, followed by the content of the response. You might know, for
# example, that a 404 code means that the page wasn't found, or that a 500 response means that there was an internal
# server error.
# In general, response codes in the 500 range, like 501 or 503, tells us that something bad happened on the server while
# generating a response. Well, response codes in the 400 range means there was a client-side problem in the request.

# When monitoring your web service, you want to check both the count of response codes and their types to know if
# everything's okay. If you're running an e-commerce site, you'll care about how many purchases were made successfully
# and how many failed to complete. If you're running a mail server, you want to know how many emails were sent
# and how many got stuck and so on.
# You'll need to think about the service you want to monitor and figure out the metrics you'll need.

# Now, once we've decided what metrics we care about, what do we do with them? - We'll typically store them in the
# monitoring system.

# There's a bunch of different monitoring systems out there. Some systems like AWS Cloudwatch, Google Stack Driver, or
# Azure Metrics are offered directly by the Cloud providers.
# Other systems like Prometheus, Datadog, or Nagios can be used across vendors.

# There's two ways of getting our metrics into the monitoring system.
# Some systems use a 'Pull model', which means that the monitoring infrastructure periodically queries our service to
# get the metrics. Other monitoring systems use a 'Push model', which means that our service needs to periodically
# connect to the system to send the metrics.

# No matter how we get the metrics into the system, we can create dashboards based on the collected data.
# This dashboard show the progression of the metrics over time. We can look at the history of one specific metric to
# compare the current state to how it was last week or last month. Or we can look at the progression of two or more
# metrics together to check out how the change in one metrics effects another.

# Imagine it's Monday morning, and you notice that your service is receiving a lot less traffic than usual. You can look
# at the data from past weeks and see if you always get less traffic on Monday mornings or if there's something
# broken causing your service to be unresponsive. Or if you see that in the past couple days, the memory used by your
# instances has been going up, you can check if this growth follows a similar increase in another metric, like the
# amount of requests received or the amount of data being transmitted. This can help you decide if there's been a memory
# leak that needs to be fixed or if it's just an expected consequences of a growth in popularity.

# Pro tip: you only want to store the metrics that you care about, since storing all of these metrics in the system
# takes space, and storage space costs money.

# When we collect metrics from inside a system, like how much storage space the service is currently using or how long
# it takes to process a request, this is called 'Whitebox Monitoring'.

# Whitebox monitoring checks the behavior of the system from the inside. We know the information we want to track,
# and we're in charge of making it possible to track.
# For example, if we want to track how many queries we're making to the database, we might need to add a variable to
# count this.

# On the flip side, 'Blackbox Monitoring' checks the behavior of the system from the outside.
# This is typically done by making a request to the service and then checking that the actual response matches the
# expected response.
# We can use this to do a very simple check to know if the service is up and to verify if the service is responding from
# outside your network. Or we could use it to see how long it takes for a client in a different part of the world to get
# a response from the system.

# Okay, monitoring is really cool, but who wants to stare at dashboards all day trying to figure out if something's wrong?
# Fortunately, we don't have to. Instead, we can set up alerting rules to let us know if something's wrong.

"""Getting Alerts When Things Go Wrong"""
# We expect a lot from our modern IT services. We expect them to be up and running 24/7. We want to be able to get our
# work done whenever and wherever. For that, we need our services to respond day or night, workday or holiday.
# But even if the services are running 24/7, System Administrators can't constantly be in front of their systems.
# Instead, we set up our services so that they work unattended and deal with problems when they happen.

# To do this, we need to detect those problems so that we can deal with them as quickly as possible. If you have no
# automated way of raising an alert, you might only find out about the issue when you get a call from a frustrated user
# telling you that your service is down.

# It's much better to create automation that checks the health of your system and notifies you when things don't behave
# as expected. This can give you advance warning that something's wrong, sometimes even before users notice a problem
# at all.

# The most basic approach is to run a job periodically that checks the health of the system and sends out an email if
# the system isn't healthy. On a Linux system, we could do this using 'cron', which is the tool to schedule periodic
# jobs. We'd pair this with a simple Python script that checks the service and sends any necessary emails.
# This is an extremely simplified version of an alerting system, but it shares the same principles in all alerting
# systems, no matter how complex and advanced.
# We want to periodically check the state of the service and raise alerts if there's a problem.

# When you use a monitoring system like the ones we described in our last video, the metrics you collect represent the
# state of your service. Instead of periodically running a script that connects to the service and checks if it's
# responding, you can configure the system to periodically evaluate the metrics; and based on some conditions, decide if
# an alert should be raised.

# 'Raising an alert' signals that something is broken and a human needs to respond.
# For example, you can set up your system to raise alerts if the application is using more than 10 Gb of RAM, or if it's
# responding with too many 500 errors, or if the queue of requests waiting to get processed gets too long.
# Of course, not all alerts are equally urgent.

# We typically divide useful alerts into two groups: those that need immediate attention and those that need attention
# in the near future. If an alert doesn't need attention, then it shouldn't have been sent at all. It's just noise.

# If your web service is responding with errors to 50% of the requests, you should look at what's going on right away.
# Even if this means waking up in the middle of the night to address whatever is wrong, you'll definitely want to fix
# this kind of critical problem ASAP.

# On the other hand, if the issue is that the attached storage is 80% full, you need to figure out whether to increase
# the disk size or maybe clean up some stored data. But this isn't super urgent, so don't let it get in the way of a
# good night's sleep.

# Since these two types of alerts are different, we typically configure our systems to raise alerts in 2 different ways.
# Those that need immediate attention are called 'Pages', which comes from a device called a 'pager'.
# Before mobile phones became popular, pagers were the device of choice for receiving urgent messages, and they're still
# used in some places around the world. Nowadays, most people receive their pages in other forms like SMS, automated
# phone calls, emails, or through a mobile app, but we still call them 'pages'.

# On the flip side, the non-urgent alerts are usually configured to create bugs or tickets for an IT specialist to take
# care of during their workday. They can also be configured to send email to specific mailing lists or send a message to
# a chat channel that will be seen by the people maintaining the service.

# One thing to highlight is that all alerts should be 'actionable'.
# If you get a bug or a page and there's nothing for you to do, then the alert isn't actionable, and it should be
# hanged or shouldn't be there at all. Otherwise, it's just noise.

# Say you're trying to check if your services database back-end is responsive. If you do this by creating a query that
# returns all rows in a large table, your request might sometimes timeout and raise an alert.
# That would be a noisy alert, not really actionable. You'd need to tweak the query to make the check useful.

# Say you run a cron job that copies files from one location to another every 10 minutes, you want to check that this
# job runs successfully. So you configure your system to alert you if the job fails. After putting this in production,
# you realize there's a bunch of unimportant reasons that can cause this job to temporarily fail.
# Maybe the destination storage is too busy and so sometimes the job times out. Maybe the origin was being rebooted
# right when the job started, so the job couldn't connect to it. No matter why, whenever you go to check out what caused
# a job to fail, you discover that the following run had succeeded and there's nothing for you to do.
# You need to rethink the problem and tweak your alert.

# Since the task is running frequently, you don't care if it fails once or twice, you can change system to only raise
# the alert if the job fails three times in a row. That way when you get a bug, it means that it's failing consistently,
# and you'll actually need to take action to fix it.

# All of this configuring and tweaking can seem like a lot of work. You need to think about which metrics you care about
# Configure your monitoring system to store them, then configure your alerting system to raise alerts when things don't
# behave as expected. The flip side is that once you've set your systems to raise actionable alerts when needed,
# you're going to have peace of mind. If no alerts are firing, you know the service is working fine.
# This lets you concentrate on other tasks without having to worry.

# To set up good alerts, we need to figure out which situations should page, which ones should create bugs, and which
# ones we just don't care about. These decisions aren't always easy and might need some discussion with the rest of your
# team. But it can help make sure that you spend time only on things that actually matter.
