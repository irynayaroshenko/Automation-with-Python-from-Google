"""The Code Review Workflow"""
# Nit
# Sometimes, your reviewer might point out something small, that's not really critical. And the comment is mostly a
# suggestion for making the code better. These comments are usually prefixed, saying that it's a Nit.

# It's a good idea to refer to a style guide that explains the preferred coding style for the project (PEP8, etc.).

"""How to Use Code Reviews in GitHub"""

# Comments for code review are in 'Conversations' tab

# 'View changes' button to see all changes

# We've addressed all the comments in our code review.
# Let's save our file and then commit the changes.
# Since we want this change to
# be a part of the previous commit, we'll call
#
# git commit -a --amend

# which will edit the original commit.

# git status

# Just like before, we see that our change has diverged from the origin/main branch.
# You might remember that 'git commit --amend' modifies commits.
# So it's not safe to do with commits that have been pushed to the repo.

# Using amend is pretty much the same as creating a new commit, and then using an interactive rebase ('rebase -i')
# to 'fixup' a change. So, the commit gets replaced by a completely new commit with a completely different commit ID.
# This means that to push it, we'll need to use the -f flag again ('git push -f').

# Remember that 'git push -f' is fine for pull request branches because nobody else should have cloned it.
# But this isn't something that we want to do with public repos.

# On GitHub click 'Resolve conversation' under comments you resolved.

# Then you can comment to all reviewers and close conversation or just comment and ask check changes you made.

"""More Information on Code Reviews"""
# http://google.github.io/styleguide/
#
# https://help.github.com/en/articles/about-pull-request-reviews
#
# https://medium.com/osedea/the-perfect-code-review-process-845e6ba5c31
#
# https://smartbear.com/learn/code-review/what-is-code-review/
