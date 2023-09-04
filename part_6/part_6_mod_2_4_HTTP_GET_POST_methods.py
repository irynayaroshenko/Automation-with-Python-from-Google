"""HTTP GET and POST Methods"""
# HTTP supports several HTTP methods https://tools.ietf.org/html/rfc7231#section-4.3
# like GET, POST, PUT, and DELETE. We're going to spend time on the two most common HTTP requests: GET and POST.

# The HTTP GET method https://tools.ietf.org/html/rfc7231#section-4.3.1
# , of course, retrieves or gets the resource specified in the URL. By sending a GET request to the web server, you’re
# asking for the server to GET the resource for you. When you’re browsing the web, most of what you’re doing is using
# your web browser to issue a bunch of GET requests for the text, images, videos, and so forth that your browser
# will display to you.

# A GET request can have parameters. Have you ever seen a URL that looked like this?

# https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15

# The question mark separates the URL resource from the resource's parameters. These parameters are one or more
# key-value pairs, formatted as a query string https://en.wikipedia.org/wiki/Query_string
# In the example above, the search parameter is set to "grey+kitten", and the max_results parameter is set to 15.
#
# But you don't have to write your own code to create URL like that one. With requests.get()
# https://requests.readthedocs.io/en/master/api/#requests.get
# you can provide a dictionary of parameters, and the Requests module will construct the correct URL for you!

# >>> p = {"search": "grey kitten",
# ...      "max_results": 15}
# >>> response = requests.get("https://example.com/path/to/api", params=p)
# >>> response.request.url
# 'https://example.com/path/to/api?search=grey+kitten&max_results=15'

# You might notice that using parameters in Requests is yet another form of data serialization. Query strings are handy
# when we want to send small bits of information, but as our data becomes more complex, it can get hard to represent it
# using query strings.

# An alternative in that case is using the HTTP POST method https://tools.ietf.org/html/rfc7231#section-4.3.3

# This method sends, or posts, data to a web service. Whenever you fill a web form and press a button to submit, you're
# using the POST method to send that data back to the web server. This method tends to be used when there's a bunch of
# data to transmit.

# In our scripts, a POST request looks very similar to a GET request. Instead of setting the params attribute, which
# gets turned into a query string and appended to the URL, we use the data attribute, which contains the data that will
# be sent as part of the POST request.

# >>> p = {"description": "white kitten",
# ...      "name": "Snowball",
# ...      "age_months": 6}
# >>> response = requests.post("https://example.com/path/to/api", data=p)

# Let's check out the generated URL for this request:

# >>> response.request.url
# 'https://example.com/path/to/api'

# See how much simpler the URL is on this POST now? Where did all the parameters go? They’re part of the body of the
# HTTP message. We can see them by checking out the body attribute.

# 3 >>> response.request.body
# 'description=white+kitten&name=Snowball&age_months=6'

# Ah, ha! There they are!

# So, if we need to send and receive data from a web service, we can turn our data into dictionaries and then pass that
# as the data attribute of a POST request.

# Today, it's super common to send and receive data specifically in JSON format, so the Requests module can do the
# conversion directly for us, using the json parameter.

# >>> response = requests.post("https://example.com/path/to/api", json=p)
# >>> response.request.url
# 'https://example.com/path/to/api'
# >>> response.request.body
# b'{"description": "white kitten", "name": "Snowball", "age_months": 6}'

# And that's it for our brief introduction to the Requests module. If you want to learn more, feel free to work through
# the Requests Quickstart https://requests.readthedocs.io/en/master/user/quickstart/

"""What is Django?"""
# The lab project at the end of this module will feature a very simple web application created using Django
# https://djangoproject.com/

# Django is a full-stack web framework written in Python. For this project, you'll only need to interact with it through
# HTTP requests, but it's still a good idea to understand what it is, and when it would be a good tool for you to use.

# A full-stack web framework handles a bunch of different components that are typical when creating a web application.
# It contains libraries that help you handle each of the pieces: writing your application's code, storing and retrieving
# data, receiving web requests, and responding to them. If you need to build an application that has a web frontend,
# using a web framework like Django can save you a lot of time and effort, because a lot of challenges are already
# solved for you.

# Web frameworks are commonly split into three basic components: (1) the application code, where you'll add all of your
# application's logic; (2) the data storage, where you'll configure what data you want to store and how you're storing
# it; and (3) the web server, where you'll state which pages are served by which logic.

# Splitting your code like that helps you write more modular code, promotes code reuse, and allows for flexibility when
# viewing and accessing data. For example, you could have a simple web page where users of the system can access the
# information already stored in it, and a separate programmatic interface that can be used by other scripts or
# applications to transmit data to the system.

# When you’re writing a web application, there's a ton of little decisions to make. Relying on a framework like Django
# is similar to using external libraries for your code. There are a lot of features, which you can use very easily,
# instead of writing everything from scratch and re-making all of the same mistakes that we all make when writing a web
# application for the first time.

# Django has a ton of useful components for building websites. In the lab project, Django will be used for serving the
# company website, including customer reviews. It does this by taking the request for a URL and parsing it using the
# urlresolver module. This is a core module in Django that interprets URL requests and matches them against a list of
# defined patterns. If a URL matches a pattern, the request is passed to the associated function, called a view. This
# allows you to serve different pages depending on what URL is being requested. You can even build complex logic into
# the function handling the request to make more dynamic, interactive, and exciting pages.

# Django can also handle reading and writing data from a database, letting you store and retrieve data used by your
# application. In the lab, the database holds the customer reviews for the company. When a user loads the website, the
# logic will ask the database for all available customer reviews. These are retrieved and formatted into a web page,
# which is served as a response to the URL request. Django makes it easy to interact with data stored in a database by
# using an object-relational mapper, or ORM. This tool provides an easy mapping between data models defined as Python
# classes and an underlying database that stores the data in question.

# On top of this, the Django application running in the lab includes an endpoint that can be used to add new customer
# reviews to the database. This endpoint is configured to receive data in JSON format, sent through an HTTP POST
# request. The data transmitted will then be stored in the database and added to the list of all reviews. The framework
# even generates an interactive web form, that lets us directly interact with the endpoint using our browser, which can
# be really handy for testing and debugging.

# Django is one of many popular web frameworks. Alternative Python-based web frameworks similar to Django include:
# Flask https://www.fullstackpython.com/flask.html
# Bottle https://bottlepy.org/docs/dev/
# CherryPy https://cherrypy.org/
# CubicWeb https://www.cubicweb.org/
# There are a host of other frameworks written in other languages too, not just Python.
