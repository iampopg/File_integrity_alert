# File Integrity Monitor

## Description

This program monitors the integrity of specified files and alerts the user if any changes are detected. It calculates the SHA-256 hash of a file and continuously compares it to the previously calculated hash.

## Features

- Check file integrity in every 10s
- Print alerts for detected changes
- Play alert sound when a change is detected

## Getting Started

### Prerequisites

- Python 3.11
- Required Python packages (can be installed using `pip` or `pip install -r requirements.txt`):
  - `colorama`
  - `playsound`
  - `pyfiglet`

### Installation

```bash
git clone https://github.com/iampopg/File_integrity_alert/
pip install -r requirements.txt
python main.py #to run
```

### Support OS
It can work on all OS
