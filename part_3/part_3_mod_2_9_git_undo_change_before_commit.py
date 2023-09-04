"""Undoing Changes Before Committing"""
# If we modified previously added to stage file, and want to revert changes (not to do 'git add'), use 'restore/checkout':

# git restore <file_name>
# or
# git checkout <file_name>  (old version)


# If we staged files but then decided to revert some, use 'restore/reset':

# git restore --staged <file_name>
# or
# git reset HEAD <file_name>  (old version)


# NOTE. If you want to delete staged file:

# git rm <file_name>
# git commit -m "Deleting file <file_name>"

# If you want to delete un-staged file:

# rm <file_name>


# If we want to review all staged and available for reverting file and then decide revert or not. If you need to check
# out individual changes instead of the whole file, you can do that using the dash p flag. This will ask you change by
# change if you want to go back to the previous snapshot or not:

# git restore --staged -p


# Example:

# $ git restore --staged -p
# diff --git a/all_checks_correct.py b/all_checks_correct.py
# index 3463a71..f4555bd 100644
# --- a/all_checks_correct.py
# +++ b/all_checks_correct.py
# @@ -9,7 +9,7 @@ def main():
#    if check_reboot():
#      print("Pending Reboot")
#      sys.exit(1)
# -  print("Everything ok.")
# +  print("Everything ok!")
#    sys.exit(0)
#
#  main()
# (1/1) Unstage this hunk [y,n,q,a,d,e,?]? n





