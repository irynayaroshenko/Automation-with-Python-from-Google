"""Managing Collaboration"""
# 1. Documentation (what you do and why you do)
#
# The most basic form of this is writing clear code with good comments and documentation for those functions in the
# code. On top of that, you'll want to create documentation files to let others know how they can interact with your
# project like the readme.md, etc.

# 2. If you're a project maintainer, it's important that you are reply promptly to pull requests and don't let them
# stagnate. The more time that passes until a pull request gets reviewed, the more likely it is that there's a new
# commit that causes a conflict when you try to merge in the change.

# 3. It's important that you understand any changes you accept.

# 4. Follow (create and share) style guides

# 5. Use issue tracker

# 6. Use communication channels (slack, telegram, discord, etc.)

"""Tracking Issues"""
# 1. Issue tracker
# 2. Bug tracker (GitHub has built-in tracker, 'Issues' tab)

# Before start working on issue, "Assign to yourself" issue.

# To close automatically issues, add "Closes #<issue number>" in your commit message or as a part of the description
# of your pull request. Once the code gets merged into the main tree, GitHub will automatically close the issue with
# a message linking it to the new commit. (Open closing_issues_automatically.png)

"""Continuous Integration"""
# CI
# If we have continuous integration configured for our project, we can automatically run our tests using the code in a
# pull request.

# CD
# Once we have our code automatically built and teste the next automation step is continuous deployment which is
# sometimes called continuous delivery or CD.
# Continuous deployment means the new code is deployed often. The goal is to avoid roll-outs with a lot of changes
# between two versions of a project and instead do incremental updates with only a few changes at a time.
# This allows errors to be caught and fixed early. Typical configurations include deploying a new version whenever
# a commit is merged into the main tree or whenever a branch is tagged for release.

# Jenkins, GitLab, Travis (which communicates with GitHub and can access the information from GitHub projects to know
# which integrations to run.). GitHub Actions is a CI/CD platform available through GitHub.

# Concepts to deal with when creating CI/CD:
# 1. Pipelines.
# For a simple Python Project, the pipeline could be to just run the automated tests.
# For a web service written in Go, the pipeline could be to compile the program, run the unit and integration tests
# and finally deploy the code to a test instance.

# 2. Artifacts
# This is the name used to describe any files that are generated as part of the pipeline. This typically includes the
# compiled versions of the code but can include other generated files like PDFs for the documentation or OS specific
# packages for easy installation. On top of this, you might want to keep the logs of the pipelines build and
# test stages to review if things fail.

# 3. Secrets/security
# If our pipeline includes deploying a new version of the software to a test server, we need to somehow give the
# software that's running the pipeline access to our test server. There are a bunch of different strategies to do this,
# like exchanging 'SSH keys' or using application specific 'API tokens'.
# For some pipelines, it might be unavoidable to use one of these methods but be aware that you're giving access to
# your test servers to the owner of the service that's running the pipeline for you.
# 2 things to remember:
# 1) make sure the authorized entities for the test servers are not the same entities authorized to deploy on the
# production servers. Cause, if there's any kind of compromise in the pipeline, your production server is not affected.
# 2) always have a plan to recover your access in case your pipeline gets compromised.

# Travis website at www.travis-ci.com using your GitHub account then enable the projects that you want to continuously
# integrate. After that, you'll need to add a configuration file to your project written in YAML format that states the
# language your project is in, in which steps to take for the pipeline.
# This file can be very simple if your project files are typical configuration for the language you're using but can
# also become very complex if you want to run a complicated pipeline with lots of stages and steps outside the defaults.

# CI works in 3 simple stages: push, test, and fix.


"""Additional Tools"""
# https://arp242.net/diy.html
# https://help.github.com/en/articles/closing-issues-using-keywords
# https://help.github.com/en/articles/setting-guidelines-for-repository-contributors
# https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html
# https://stackify.com/what-is-cicd-whats-important-and-how-to-get-it-right/
# https://docs.travis-ci.com/user/tutorial/
# https://docs.travis-ci.com/user/build-stages/


