"""Keeping Local Results"""
# If we have to parse a file, we do it once before we call the loop instead of doing it for each element of the loop.
# But what if parsing the file is taking a lot of time even when it's done outside the loop?
# Remember that to make our scripts get to their goal faster, we need to avoid having our computer do unnecessary work.

# So how can we avoid expensive operations like parsing a file, downloading data over the network,
# or going through a long list?
# If the script gets executed fairly regularly, it's common to create a local cache.

# So if we're parsing a large file and only keeping a few key pieces of information from it, we can create a cache to
# store only that information, or if we're getting some information over the network, we can keep a local copy of file
# to avoid downloading it over and over again.

# Creating caches can be super useful to save us time and make our programs faster.
# But they're sometimes tricky to get right.

# We need to think about how often we're going to update the cache and what happens if the data in the cache is out of
# date. If we're looking for some long-term stats, we can generate the cache once per day, and it won't be a problem.

# This might be the case for data like how much memory was used on computers across the fleet over the last month?
# How many employees each department in a company has? Or how many units were sold of each product over last quarter?

# But if we're trying to look at data where the value as of right now is super important, we either can't use
# a cache or it has to be very short-lived. This could be the case for monitoring the health of computers to alert when
# something crosses a threshold. Checking the stock levels to see if there's enough of a product to sell or
# seeing if a username already exists in the network when trying to create a new one.

# Sometimes, we can add a check to validate if we need to recalculate the cache or not. For example, if our cache is
# based on a file, we could store the modification date of that file when we calculated the cache. Then only recalculate
# the cache if the modification date of the file is newer than the one we had stored.

# If we don't have a way of checking if our cache is out of date or not, we'll need to add in logic to our program that
# tries to make a sensible decision.

# For that, we'll take into account how often we expect the data to change, how critical it is that the latest data is
# used, and how frequently the program that we're running will be executed. After taking all these factors into account,
# we might decide that the cache needs to be recreated once per day, once per hour, or even once per minute.

# Even once per minute might make sense if you have a script that can get executed several times per minute and
# needs to do an expensive operation that can be cached. That way, only the first execution in a minute will spend time
# on this operation, the rest will be very fast. But the cache is never more than a minute out of date.

# Keep in mind that caches don't always need to be elaborate structures, storing lots of information with a complex
# timeout logic. Sometimes, they can be as simple as having a variable that stores a temporary result instead of
# calculating this result every time we need it.

# For example, say you're generating a report that prints how many users there are in each of the different groups in
# the network. Now, some of these groups may contain other groups in them and some groups may even be part of several
# groups. For example, the Java release engineers group would be part of the release engineers group and the Java
# developers group. How can we avoid counting unique users more than once if they show up in multiple groups?

# We can have a dictionary with the group as the key and the amount of users as the value.
# That way, we only need to count the members of a group once, and after that, just use the value in the dictionary.

# To sum all of this up, remember that you'll want to look for strategies that let you avoid doing expensive operations.
# First, check if these operations are needed at all. If they are, see if you can store the intermediate results to
# avoid repeating the expensive operation more than needed.
