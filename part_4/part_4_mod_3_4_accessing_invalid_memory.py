"""Accessing Invalid Memory"""
# In our earlier videos, we looked into a bunch of different things that can make software crash and what we can
# do about them when we can't fix the code. If we're able to make the application behave correctly though,
# we'll have a lot more options for dealing with the crash. Of course to apply these fixes, we'll need to understand why
# the crash is even happening.

# One common reason a program crashes is it's trying to access invalid memory.
# To understand what this means, let's quickly explain how using the memory works on modern operating systems.

# Each process running on our computer asks the OS for a chunk of memory. This is the memory used to store values and
# do operations on them during the program's execution. The OS keeps a mapping table of which process is assigned which
# portion of the memory. Processes aren't allowed to read or write outside the portions of memory they were assigned.
# So accessing invalid memory means that the process tried to access a portion of the system's memory that wasn't
# assigned to it.

# Now, how does this even happen?
# During normal working conditions, applications will request a portion of the memory and then use the space at the OS
# assigned to them. But programming errors might lead to a process trying to read or write to a memory address outside
# the valid range. When this happens, the OS will raise an error like 'Segmentation fault' or 'General protection fault'

# What kind of programming error is this?
# It typically happens with low-level languages like C or C++ where the programmer needs to take care of requesting
# the memory that the program is going to use and then giving that memory back once it's not needed anymore.
# In these languages, the variables that store memory addresses are called pointers.

# Pointers just like any other variable and code that can be modified as needed. So if a pointer is set to a value
# outside the valid memory range for that process, it will point to invalid memory. If the code then tries to
# access the memory the pointer points to, the application will crash.

# Common programming errors that lead to 'Segmentation faults' or 'segfaults' include forgetting to initialize variable,
# trying to access a list element outside the valid range, trying to use a portion of memory after having given it back,
# and trying to write more data than the requested portion of memory can hold.

# So what can you do if you have a program that's said vaulting?
# The best way to understand what's going on is to attach a debugger to the faulty program. This way when the program
# crashes, you'll get information about the function where the fault happened. You'll know the parameters that the
# function received and find out the address that was invalid.

# That might already be enough to understand the problem. Maybe a certain variable is being initialized too late or the
# code is trying to read too many items on a list. If that's not enough, the debugger can give you a lot more detail on
# what the application is doing and why the memories invalid.

# For this to be possible, we'll need our program to be compiled with debugging symbols.
# This means that on top of the information that the computer uses to execute the program, the executable binary needs
# to include extra information needed for debugging, like the names of the variables and functions being used.
# These symbols are usually stripped away from the binaries that we run to make them smaller. So we'll need to either
# recompile the binary to include the symbols, or download the debugging symbols from the provider of the software if
# they're available.

# Linux distributions like Debian or Ubuntu ships separate packages with the debugging symbols for all the packages in
# the distribution.
# So to debug application that's segfaulting, we download the debugging symbols for that application.
# Attach a debugger to it, and see where the fault occurs. When doing this, we might find that the crash
# happens inside a call to a library function. This is separate from the application itself, so we need to install
# the debugging symbols for that library. We might need to repeat this cycle a few times before we can identify
# the portion of the code that's buggy.

# Microsoft compilers can also generate debugging symbols in a separate PDB file.
# Some Windows software providers let users download the PDP files that correspond to their binaries to let them
# properly debug failures.

# One of the trickiest things about this invalid memory business is that we're usually dealing with undefined behavior.
# This means that the code is doing something that's not valid in the programming language.
# The actual outcome will depend on the compiler used, how the operating system assigns memory to processes,
# and even the version of the libraries in use.

# A program that runs fine on a computer running Windows trigger a segfault on a computer running Linux and vice versa.
# When trying to understand problems related to handling invalid memory, valgrind can help us a lot.

# Valgrind is a very powerful tool that can tell us if the code is doing any invalid operations no matter if it crashes
# or not. Valgrind lets us know if the code is accessing variables before initializing them. If the code is failing to
# free some memory requested, if the pointers are pointing to an invalid memory address, and a ton more things.

# Valgrind is available on Linux and MacOS, and Dr. Memory is a similar tool that can be used on both Windows and Linux.

# So all of that said, what do we do when we finally discover the cause of the segfaults?
# You'll want to either change the code yourself or get the developers to fix the problem in the next version.
# This might sound scary if you've never programmed in the language used by the application. But when you know what's
# wrong with the code, it's usually not that hard to figure out how to fix it.

# If a variable is initialized too late, fixing the problem can be as easy as moving the initialization to the right
# part of the code, or if a loop is accessing an item outside the length of the list, you might solve the issue by
# checking that there aren't more iterations than needed.

# If the program is part of an open source project, you might find that someone else has already done the work,
# and so you can apply a patch available online. If there's no patch, and you can't figure out the bug out yourself,
# you can always get in touch with the developers and ask if they can fix the issue and create the necessary patch.
# In high-level languages like Python, the interpreter will almost certainly catch these problems itself.
# It will then throw an exception instead of letting the invalid memory access reach the operating system.
# But still those exceptions can be pretty annoying.
