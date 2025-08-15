import shutil

path = "/"

total, used, free = shutil.disk_usage(path)

total_gb = round(total / (1024**3), 2)
used_gb = round(used / (1024**3), 2)
free_gb = round(free / (1024**3), 2)

print(f"Disk used for path: {path}")
print(f"Total space: {total_gb} GB")
print(f"Used space: {used_gb} GB")
print(f"Free space: {free_gb} GB")
