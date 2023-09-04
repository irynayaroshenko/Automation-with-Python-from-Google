"""Basic Monitoring in GCP"""
# Open video part_5_mod_4_5_Basic-Monitoring-in-GCP.mp4 in current folder

# So far, we've seen how to create virtual machines in the Google Cloud Console. We've kept these virtual machines
# running, and now we want to see how we can use the tools provided by the cloud vendor to monitor them and create
# alerts based on them.

# For this demonstration, we'll use the monitoring tool called Stackdriver, which is part of the overall offering.

# When you first activate this system, it takes a while until it starts collecting on the metrics from all the machines,
# so we've activated in advance. When we first opened the monitoring console, we see an overview of the system.
# At the moment, this is looking pretty empty, but we could configure this dashboard to show the charts that we consider
# the most useful.

# Let's go into the Instances dashboard, we see here the list of our instances, and we can click on each of them to see
# that monitoring information that Stackdriver has collected about them.

# The monitoring system gives us a very simple overview of each of the instances with 3 basic metrics: CPU usage,
# Disk I/O, and network traffic.
# Depending on what surface we want to run on a VM, we can customize these dashboards to show different metrics.
# If the metrics that come baked in aren't enough, you can create your own metrics and also add them here.

# Now we want to check out how to set up an alert to notify us if something isn't behaving correctly. To do this, we'll
# create a new alerting policy. To set up a new alert, we have to configure the condition that triggers the alert.
# After we've done that, we can also configure how we want to be notified of the issue and add any documentation that we
# want the notification to include.

# Let's start by configuring the condition. As we called out, alerting conditions are related to specific metrics.
# We want to be notified when the metric indicates that there's a problem with an instance. For this example, we're
# going to configure an alert that triggers if an instance in CPU utilization is more than 90%.
# We'll start by selecting that we want to monitor GCE, VM instances, which are the instances that we currently have
# running and then select the CPU utilization metric.
# After selecting the metric, we see the graph of the collected values for all the current running instances.
# We can optionally add extra filters and groups for the data for this condition.
# For example, we could choose to only look at some instances, selecting by their zone, region, or name.
# This can be useful if you want to have separate alerts for instances used for production, and those used for testing
# or development.

# On top of that, we can also choose an aggregator for the data, these aggregators are useful when the metrics that
# you're collecting are about the overall system and not just one instance.

# For example, if you're checking the number of error responses that your system generated, you want to sum all the
# errors across instances. Depending on how we filter group and aggregate the data, we'll end up with a bunch of
# different time series, we'll use these values to decide if we should trigger the alert or not.

# The next step is selecting how many of the different time series need to violate the condition for the alert to
# trigger.
# We can trigger the alert when one, some, or all of the different time series violate the condition.
# For this example, we'll configure our alert to trigger if any instance is using more than 90 percent of the CPU.
# So, let's select any time series violates.

# Now, we'll say that we want our alert to trigger if the value is above 90% for 1 min.
# All right. We've set the condition.

# Now, we can select how we want to get the notification and when the alert triggers. Currently, the only type of
# notification that we can use is e-mail. To use the other channel types available, we need to configure them in our
# profile. For this example, e-mail will do. Using e-mails can be just fine when you're getting started with alerting,
# but eventually you'll want to configure additional methods. We've configured our alert to send e-mails.

# Now, we can add extra documentation to our alert. This documentation is intended to help the person that's responding
# to the alert understand what they need to do to fix the problem. Including good documentation here, it can be
# super-important when you've got a bunch of different people working together in a team and not everyone knows
# everything. Alerts that include good documentation are much easier to tend to and help get the service back to a
# healthy state faster. For our example, we'll add a message saying that whoeveris taking care of this alert,
# should "Check the instance with top".

# Finally, we'll need to give a name to our alerting policy, we'll call it 'CPU' and then save it.
# Now, we've set up our alert.

# For the final part of this demo, we want to show what happens when the alert triggers.
# To do that, we'll start a process in one of our instances that uses all the available CPU, by creating infinite loop.
# So we'll go back to the main console, SSH into the VM, called linux-instance and then create a 'while loop' that never
# ends.

# Now, our loop is running and using all the available CPU, we can check this by running the top command that shows us
# the CPU usage. We see that there's a bash command that's using almost 100% of the available CPU, our experiment is
# working. Now, remember that we said that we wanted the condition to be true for a minute before the alert triggers,
# it won't trigger just yet.

# It's common practice to use time windows of 1, 5, or even 10 minutes when dealing with the alerting. We don't want t
# get an alert for a small spike that lasted only a few seconds and then went away. We want to get alerted when there's
# an actual problem that requires our attention.

# The size of the time window we choose depends on the metric we're checking, the length of the expected spikes
# and a bunch of other factors. It's pretty normal to have to tweak how long we want the condition to be true as we try
# our alert out.

# If you're getting notified too often about conditions that go away on their own without you having to do anything,
# you might choose to make the time window larger.

# On the flip side, if you're getting notified too late about conditions that needed attention, you might choose to make
# the time window smaller.

# We've let enough time pass, let's check out what's up with our alert. We see that there's an open incident,
# which is a way of grouping problems. The alerts summary gives us a bunch of info about what's going on.
# We can click on the CPU link to get more information. This page shows us the metric that triggered the alert for the
# incident, it shows the threshold for triggering the alert and the current value of the metric. It also shows us the
# documentation that we entered and lets us create annotations. We can use these annotations to track the work that
# we do during an incident.

# Let's stop the process that's using all of our instances CPU. It's still running the top process from before.
# Let's exit with 'q'. Now, the infinite loop is currently running in the background of our console.
# We can make it run in the foreground by typing 'fg', and then cancel it by pressing CTRL+C. Now, we've stopped the
# process. Let's check with 'top' that it's no longer using all of our CPU.
# Great, the 'bash' process isn't taking all the CPU time anymore. In another minute, the alert that we'd saw
# earlier will stop triggering, nice.

# With that, we've demonstrated how we can monitor a bunch of instances running in the Cloud.
# We've created an alert based on metrics and verify that the alert triggers.

"""More Information on Monitoring and Alerting"""
# https://www.datadoghq.com/blog/monitoring-101-collecting-data/
# https://www.digitalocean.com/community/tutorials/an-introduction-to-metrics-monitoring-and-alerting
# https://en.wikipedia.org/wiki/High_availability
# https://landing.google.com/sre/books/
