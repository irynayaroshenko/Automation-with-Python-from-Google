import locale

import psutil
import shutil


def check_disc_usage(disc):
    d_usage = shutil.disk_usage(disc)
    free = d_usage.free / d_usage.total * 100
    return free > 20


def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage < 75


if not check_disc_usage('/') or not check_cpu_usage():
    print(f'Error! Disc usage: {check_disc_usage("/")}, CPU usage: {check_cpu_usage()}.')
else:
    print("Health check PASS.")
