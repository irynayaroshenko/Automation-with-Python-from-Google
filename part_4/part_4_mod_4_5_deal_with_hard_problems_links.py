"""Dealing with Hard Problems"""
# Develop code in small, digestible chunks.
# Keep your goal clear.
# If you feel that you're out of ideas, it's better to take your mind off the problem for a while.

# Rubber duck debugging - explain the problem to duck.

"""Proactive Practices"""
# 1. If we're the ones writing the code, one thing we can do is to make sure that our code has good unit tests and
# integration tests.

# 2. Continuous Integration.

# 3. Test environment.

# 4. Deploy software in phases or canaries.
# What this means is that instead of upgrading all computers at the same time and possibly breaking all of them at the
# same time, you upgrade some computers first and check how they behave. If everything goes fine, you can upgrade a few
# more, and so on until you're confident enough to upgrade the remaining part of the fleet. As the saying goes,
# like a canary in a coal mine. To make the best use of this practice, we'll need to be able to easily
# roll back to the previous version.

# 5. Good debug logging in the code.

# 6.Centralized logs collection.
# This means there's a special server that gathers all the logs from all the servers or even all the computers in the
# network. That way, when we have to look at those logs, we don't need to connect to each machine individually,
# we can comb through all the logs together in a centralized server.

# 7. Monitoring system.

# 8. Ticketing system.

# 9. Documentation.


"""Planning Future Resource Usage"""
# If you're dealing with a service that's expected to grow and will acquire more resources in the future, it makes sense
# to spend some time thinking about what that might look like.

# You might opt for buying a network attached storage or NAS that can be attached to your server for additional disk
# space. Migrating to a different type of storage takes time, and can be tricky to do right under pressure.
# So it's important to do this kind of planning in advance and not wait until the disk is completely full.

# If you have a process that's CPU intensive and takes almost all the available CPU on a computer, you can still run
# processes that are IO intensive, reading and writing a lot of data to the hard drive.

# Or if you have a service that requires a lot of RAM, you can pair it with another one that uses very little memory,
# and mostly sends and receives data over the network.

# An alternative for having to deal with all these resources like figuring out when to buy more and how to distribute
# them, is to migrate those systems to the Cloud.

# Setting up your service to run on the cloud will require some initial setup time, as well as an ongoing cost for the
# Cloud resources you're using. But while this is more expensive than what you'd pay when running the service on premise,
# you're basically delegating all your capacity planning needs to your Cloud provider.

# That way, if the initial setup doesn't have enough space, you can simply attach a bigger hard drive. Or if the program
# needs more RAM, you can just deploy the service in a virtual machine with more memory assigned. If you decide that
# moving to the Cloud is a good way to go for your company, remember that you'll also need to plan for that.

"""Preventing Future Problems"""
# Make good use of monitoring
# The short version of it is that you want the computers you care about to send their data to a centralized location
# that aggregates all this information. And then you want to be able to look at both: the information yourself, and
# trigger alerts when the values are not within acceptable range.

# Start with basics:
# - CPU
# - disc
# - memory
# - network usage

# Later you'll add new metrics.

# If it's a web server, you'll want to know the ratio between successful web responses and errors.
# If it's a database server, you'll want to know how many queries that are being served over time.

# Report bugs
# Write tests
# Document solutions

"""More About Preventing Future Breakage"""
# Preventing future breakage is a bit of a dynamic subject. Probably the most useful techniques here are identifying,
# isolating, and managing problem domains and failure domains.

# Problem Domains just describe the complexity of a given problem that one is trying to solve. Let’s look at an example
# below:

# For example: counting the number of occurrences of a specific word in one of Shakespeare’s plays, like Hamlet. This is
# an indexing problem. And its problem domain is fairly limited in scope. It’s a single word, and a single play. A bit
# of BASH could easily solve this problem. So the problem domain is small, and the technical solution is fairly simple.

# However, if the scope is widened slightly to include all of Shakespeare’s plays, the problem domain becomes larger.
# Any software solution used to try and solve this indexing problem has to now handle various logic that it did not have
# to handle before, like consolidating word occurrences in various plays. I.e. the word ‘Brevity’ may occur at least
# once in Hamlet, and N number of times in various other plays. Managing N occurrences of ‘Brevity’ over M works of
# Shakespeare is an order of magnitude more complex in terms of describing the problem domain. A bit of BASH could solve
# this problem, but it might be difficult.

# If the problem becomes slightly more complex, such as finding the occurrences of various synonyms to a given word,
# then the problem domain becomes equally large. Managing original words, their synonyms, and their hit-count across
# multiple works of Shakespeare is even MORE complex.

# So why is any of this useful? Well, if one can easily describe and reason about a problem in a lot of detail, they
# understand the Problem Domain fairly well. Producing a software solution for a given problem becomes easier when the
# Software Engineer understands the problem domain fairly well. Of course, building a good understanding of the Problem
# Domain often requires a lot of experimentation, and iteration. This is why it’s good to make a few initial attempts at
# testing a design before building an entire Production system to solve a problem like indexing Shakespeare.

# Failure Domains

# Like problem domains, failure domains just describe the complexity of a system. Except, instead of describing the
# various problems a system tries to solve, failure domains describe various sub-systems which may fail. Using the
# Shakespeare example again, if one of your systems is responsible for managing the full text of the works of
# Shakespeare (a content server), that might be a single failure domain. If another system is responsible for actually
# searching that content and counting the words (an indexer), that is a separate failure domain. Some failure domains
# can be within other failure domains. For example, if an indexer fails, the content server may not fail. But if a
# content server fails, the indexer will probably also fail.
#
# So why do we care about any of this? Well, Problem Domains drive system complexity. Complex systems often have many
# failure domains. The key to preventing future breakage is to identify, and manage the scope and severity of a failure
# domain. This may mean redesigning the system in a way that has many smaller failure domains, instead of few large ones.
#
# As another example It’s better to have a video streaming service slow down instead of failing entirely. This kind of
# graceful degradation can be attributed to isolated failure domains.
#
# This topic can be a bit complex, but there are several community articles on the idea of identifying and managing
# failure domains. Consolidating and completely eliminating possible failure domains is the key to preventing future
# breakage. If anything, managing failure domains should keep the scope of a break as small as possible.
#
# Check out some more info here:

# https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/
# https://deploy.equinix.com/blog/explaining-failure-domains-sre-lifeblood/
# https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    # data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])

    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        if row_date < start_date:
            continue

        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))

    return min_date, min_date_employees