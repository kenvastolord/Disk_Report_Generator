import shutil
import time

path = "/"

total, used, free = shutil.disk_usage(path)

total_gb = round(total / (1024**3), 2)
used_gb = round(used / (1024**3), 2)
free_gb = round(free / (1024**3), 2)

print(f"Disk used for path: {path}")
print(f"Total space: {total_gb} GB")
print(f"Used space: {used_gb} GB")
print(f"Free space: {free_gb} GB")

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

with open("report.txt", "w") as file:
    file.write(f"Disk Usaged Report\n")
    file.write(f"Generated at: {timestamp}\n")
    file.write(f"Path: {path}\n")
    file.write(f"Total space: {total_gb} GB\n")
    file.write(f"Used space: {used_gb} GB\n")
    file.write(f"Free space: {free_gb} GB\n")

print(f"Report saved at report.txt")
