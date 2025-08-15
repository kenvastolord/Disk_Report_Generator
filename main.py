import os
import platform
import shutil
import time


def get_available_disks():
    system = platform.system()
    disks = []

    if system == "Windows":
        from string import ascii_uppercase

        for letter in ascii_uppercase:
            drive = f"{letter}:\\"
            if os.path.exists(drive):
                disks.append(drive)
    else:
        try:
            with open("/proc/mounts", "r") as f:
                mounts = [line.split()[1] for line in f.readlines()]
                disks = list(set(mounts))
                disks = [d for d in disks if d.startswith("/") and os.path.exists(d)]
        except FileNotFoundError:
            disks = ["/"]
    return sorted(disks)


def select_disk(disks):
    print("Available disks/partitions: ")
    for idx, disk in enumerate(disks):
        print(f"{idx + 1}. {disk}")

    while True:
        choice = input("\nSelect the number of the disk you want to scan: ")
        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(disks):
                return disks[index]
        print("Invalid choice. Please enter a valid number.")


def generate_report(path):
    total, used, free = shutil.disk_usage(path)

    total_gb = round(total / (1024**3), 2)
    used_gb = round(used / (1024**3), 2)
    free_gb = round(free / (1024**3), 2)

    print(f"Disk usage for path: {path}")
    print(f"Total space: {total_gb} GB")
    print(f"Used space: {used_gb} GB")
    print(f"Free space: {free_gb} GB")

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("report.txt", "a") as file:
        file.write(f"=== Disk Usage Report ===\n")
        file.write(f"Generated at: {timestamp}\n")
        file.write(f"Path: {path}\n")
        file.write(f"Total space: {total_gb} GB\n")
        file.write(f"Used space: {used_gb} GB\n")
        file.write(f"Free space: {free_gb} GB\n")

    print(f"\nReport saved to 'report.txt'")


while True:

    disks = get_available_disks()
    selected_path = select_disk(disks)
    generate_report(selected_path)

    again = input("\nDo you want to scan another disk? (y/n): ").strip().lower()

    if again != "y":
        print("Exiting the program.")
        break
