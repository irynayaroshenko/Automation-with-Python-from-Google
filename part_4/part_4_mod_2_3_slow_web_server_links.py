"""Slow Web Server"""
# A user has alerted us that one of the web servers in our company is being slow, and we need to figure out what's going
# on. Let's start by navigating to the website and loading the page.

# (Opens site.example.com) We see that the page loads. It seems to be a little slow, but it's hard to measure this on
# our own.
# Let's use a tool called 'ab' which stands for Apache Benchmark tool to figure out how slow it is.

# ab -n 500 site.example.com/


# get the average timing of 500 requests for site.example.com for the measurement.
# This tool is super useful for checking if a website is behaving as expected or not. It will make a bunch of requests
# and summarize the results once it's done.

# Here, were asking for it to do 500 requests to our website. There are a lot more options that we could pass like how
# many requests we want the program to do at the same time, or if the test should finish after timeout, even if not all
# requests completed, we're making 500 requests so that we can get an average of how long things are taking.

# Once the test finishes, we can look at the data and decide if it's actually slow or not.

# The tool has finished running the 500 requests. We see that the mean time per requests was 155 milliseconds. Open
# slow_web_server_1.png. While this is not a super huge number, it's definitely more than what we'd expect for such a
# simple website. It seems that something is going on with the web server, and we need to investigate further.

# Let's connect to the WebServer and check out what's going on.

# ssh webserver

# We'll start by looking at the output of 'top' and see if there's anything suspicious there.


# top    (open slow_web_server_2.png)


# We see that there's a bunch of 'ffmpeg' processes running, which are basically using all the available CPU.
# See those load numbers? 30 is definitely not normal. (Open slow_web_server_2.png)

# Remember that the load average on Linux shows how much time the processor is busy at a given minute with one meaning
# it was busy for the whole minute.
# This computer has 2 processors. So any number above 2 means that it's overloaded. During each minute, there were more
# processes waiting for processor time than the processor had to give.

# This ffmpeg program is used for video transcoding which means converting files from one video format to another.
# This is a CPU intensive process and seems like the likely culprit for our server being overloaded. So what can we do?
# One thing we can try is to change the processes priorities so that the web server takes precedence.

# The process priorities in Linux are so that the lower the number, the higher the priority.
# Typical numbers go from 0 to 19. By default, processes start with a priority of zero.
# But we can change that using 'nice' and 'renice' commands.

# We use 'nice' for starting a process with a different priority and 'renice' for changing the priority of a process
# that's already running.

# Exit 'top' with 'q' and change the priorities.

# We want to run 'renice' for all the ffmpeg processes that are running right now.
# We could do this one by one, but it would be manual, error-prone, and super boring.
# Instead, we can use a quick line of shell script to do this for us.

# For that, we'll use the 'pidof' command that receives the process name and returns all the process IDs that have that
# name. We'll iterate over the output of the 'pidof' command with 'for loop' and then call 'renice' for each of the
# process IDs. 'renice' takes the new priority as the first argument, and the process ID to change as the second one.
# In our case, we'll want the lowest possible priority which is 19. (Open slow_web_server_3.png)


# for pid in $(pidof ffmpeg); do renice 19 $pid; done


# We see that the priorities for those processes were updated.
# Let's run our benchmarking software again and check out if it made any difference.

# ab -n 500 site.example.com/


# This time, the meantime is 153 milliseconds. (open slow_web_server_4.png)
# It doesn't seem like our renice helped. Apparently, the OS is still giving these ffmpeg processes way too much
# processor time. Our website is still slow. What else can we do?

# These transcoding processes are CPU intensive, and running them in parallel is overloading the computer.
# So one thing we could do is, modify whatever is triggering them to run one after the other instead of all at the same
# time.

# To do that, we'll need to find out how these processes got started. Use 'ps' to get some more information about
# the processes. Use 'ps ax' to see all the running processes on the computer, connect the output of the command to
# 'less' to be able to scroll through it.

# ps ax | less


# Now we'll look for the ffmpeg process using slash which is the search key when using 'less'.

#  /ffmpeg


# Open slow_web_server_5.png. We see that there are a bunch of ffmpeg processes that are converting videos from the
# .webm format to the .mp4 format.
# We don't know where these videos are on the hard drive. We can try using 'locate' command to see if we can find them.

# locate static/001.webm      (open slow_web_server_6.png)

# Exit 'less' interface with 'q' and then call:

# locate static/001.webm


# We see that the static directory is located in the srv/deploy_videos directory.

# cd /srv/deploy_videos/
# ls -l

# open slow_web_server_7.png There's a bunch of files here. We could check them all one-by-one to see if one of them
# contained a call to ffmpeg. But that sounds like a lot of manual work.
# Instead, let's use 'grep' to check if any of these files contains a call to ffmpeg.

# grep ffmpeg *

# So we see that there's a couple of mentions in the deploy.sh file (open slow_web_server_8.png).
# Let's take a look at that one. Since we're connecting to the server remotely, we can't open the file using a graphical
# editor. We need to use a command line editor instead. We'll use 'vim' in this case.

# vim deploy.sh

# open slow_web_server_9.png We see that this script is starting the ffmpeg processes in parallel using a tool called
# Daemonize that runs each program separately as if it were a daemon. This might be okay if we only need to convert
# a couple of videos but launching one separate process for each of the videos in the static directory is overloading
# our server.
# So we want to change this to run only one video conversion process at a time.

# We'll do that by simply deleting the daemonized part and keeping the part that calls ffmpeg, then save and exit.
# open slow_web_server_10.png

# We've modified the file. But this won't change the processes that are already running.
# We want to stop these processes but not cancel them completely, as doing so would mean that the videos being
# converted right now will be incomplete.

# So we'll use the 'killall' command with the '-STOP' flag which sends a stop signal but doesn't kill the processes
# completely.

# killall -STOP ffmpeg

# We now want to run these processes one at a time. How can we do that? We could send the 'CONT' signal to one of them,
# wait till it's done, and then send it to the next one. But that's a lot of manual work.
# We can automate this, but it's a little tricky.

# We can iterate through the list of processes using the same for loop with the 'pidof' command that we used earlier.
# Inside the for loop, we want to send the 'CONT' signal and then wait until the process is done.
# Unfortunately, there's no command to wait until the process finishes. But we can create 'while' loop that sends 'cont'
# signal to the process. This will succeed as long as the process exists, and fails once the process goes away.
# Inside this while loop, we'll simply add a call to sleep 1, to wait one second until the next check.

# for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done

# Now our server is running one ffmpeg process at a time.
# Let's turn our benchmark once more.

# ab -n 500 site.example.com/

# open slow_web_server_11.png The mean time is now 33 ms. That's much lower than before.


# Monitoring Tools:

# https://docs.microsoft.com/en-us/sysinternals/downloads/procmon
# http://www.brendangregg.com/linuxperf.html
# http://brendangregg.com/usemethod.html
# For Mac: https://support.apple.com/en-us/HT201464
# Performance Monitor on Windows: https://www.windowscentral.com/how-use-performance-monitor-windows-10
# https://www.digitalcitizen.life/how-use-resource-monitor-windows-7
# https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer
# https://en.wikipedia.org/wiki/Cache_(computing)
# https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/

# Lesson video: https://www.youtube.com/watch?v=g7_3CT6qvJg&list=PLP8aFdeDk9g4ImMVv0PwgTl7ztwBZryi0&index=19
