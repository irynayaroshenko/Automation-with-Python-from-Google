"""Using Threads to Make Things Go Faster"""
# Our company has an e-commerce website that includes a bunch of images of the products that are up for sale.
# There's a rebranding coming up, which means that all of these images will need to be replaced with new ones.
# This includes both the full-size images and the thumbnails.

# We have a script that creates the thumbnails based on the full-size images. But there's a lot of files to process, and
# our script is taking a long time to finish.

# We'll start by trying out the current script as-is using a set of 1,000 test images.
# There's more images to convert, but it'll be easier to test the speed of our script with a smaller batch.

# We'll execute our program using 'time' command to see how long it takes. It took about two seconds for 1,000 images.

# time ./thumbnail_generator.py


# open thumbnail_generator_1.png
# This doesn't seem too slow, but there's tons of thousands of images that need converting, and we want to make sure
# that the process is as fast as possible.

# Let's try making this go faster by having it process the images in parallel.
# We'll start by importing the 'futures' submodule, which is part of the 'concurrent' module.
# This gives us a very simple way of using Python threads.

# To be able to run things in parallel, we'll need to create an 'executor' - process that's in charge of distributing
# the work among the different workers.

# The 'futures' module provides a couple of different executors, one for using threads and another for using processes.
# We'll go with the ThreadPoolExecutor for now.

# Now the function that does most of the work in this loop is process_file().
# Instead of calling it directly in the loop, we'll submit a new task to the executor with the name of the function
# and its parameters. Our for loop now creates a bunch of tasks that are all scheduled in the executor. The executor
# will run them in parallel using threads.

# An interesting thing that happens when we use threads is that the loop will finish as soon as all tasks are scheduled.
# But it will still take a while until the tasks complete.

# So we'll add a message saying that we're waiting for all threads to finish, and then call the shutdown function on
# the executor. This function waits until all the workers in the pool are done, and only then shuts down the executor.
# Open thumbnail_generator.py

# All right, we've made the change, let's save our script and test it out. Our script now takes 1.2 seconds.
# open thumbnail_generator_2.png

# time ./thumbnail_generator.py


# That's a nice improvement over the 2 sec we saw before.

# See how the user time is higher than the real time?
# By using multiple threads, our script is making use of the different processors available in the computer.
# And this value shows the time used on all processors combined.

# What do you think will happen if we try to use processes instead of threads? Let's try this out by changing executor
# that we're using. By changing the executor to the ProcessPoolExecutor, we tell the futures module that we want to use
# processes instead of threads for the parallel operations.

# Save and check again.

# time ./thumbnail_generator.py

# Open thumbnail_generator_3.png
# This is now taking less than a second to finish, and the user time has gone up even more.
# This is because, by using processes, we're making even more use of the CPU. The difference is caused by the way
# threads and processes work in Python. Threads use a bunch of safety features to avoid having two threads that try to
# write to the same variable. And this means that when using threads, they may end up waiting for their turn to write to
# variables for a few milliseconds, adding up to the small difference between the two approaches.

"""More About Complex Slow Systems"""
# https://realpython.com/python-concurrency/
# https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32
