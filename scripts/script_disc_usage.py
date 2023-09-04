import shutil
import psutil

disk_usage = shutil.disk_usage('/')  # total, used, free number of bites on disc
print(disk_usage)  # usage(total=1999636860928, used=1165968257024, free=833668603904)

# calculate the percentage of free disk space by div the number of bytes free by the total and multiplying that by 100.
free_space_perc = disk_usage.free / disk_usage.total * 100
print(f'{free_space_perc:.2f}%')

# But what about cpu_usage? For this, we can use another module called psutil.
# This includes a cpu_percent function that returns a number showing how much of the CPU is being used.
# The amount of CPU used at each instant can change a lot, since processes are starting and finishing all the time.
# So this function receives an interval of seconds and returns an average percentage of usage in that interval.
cpu_perc = psutil.cpu_percent(0.1)  # call the function with 0.1 sec
print(cpu_perc)
