# 🧮 Disk Usage Report Generator

A simple Python script to scan disk or partition usage and generate a human-readable report saved to a text file.  
Designed as a beginner-friendly project using only Python's standard libraries: `os`, `platform`, `shutil`, and `time`.

---

## 📌 Features

- Detects all available disks or partitions (cross-platform support).
- Allows user to select which disk to scan.
- Shows disk usage in the terminal (total, used, and free space in GB).
- Appends each report to `report.txt`, preserving previous records.
- Option to scan multiple disks in one session.

---

## 🛠️ Technologies Used

- Python 3
- No external libraries required

---

## 📂 File Structure

```

disk_report_generator/
│
├── disk_report.py
├── report.txt
└── README.md

```

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal and navigate to the folder containing `disk_report.py`.
3. Run the script:

```bash
python disk_report.py
```

4. Follow the instructions to select a disk or partition.

5. Check report.txt to see the saved report.

## 🧑‍💻 Sample Output (Terminal)

```
Available disks/partitions:
1: C:\
2: D:\

Select the number of the disk you want to scan: 1

Disk usage for path: C:\
Total space: 465.76 GB
Used space: 300.12 GB
Free space: 165.64 GB

Report appended to 'report.txt'

```

## 📝 Example report.txt

```
=== Disk Usage Report ===
Generated at: 2025-08-15 18:30:10
Path: C:\
Total space: 465.76 GB
Used space: 300.12 GB
Free space: 165.64 GB

```
