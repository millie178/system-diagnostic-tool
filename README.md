# 🖥️ System Diagnostic Tool

A lightweight Python-based diagnostic tool to collect system information for troubleshooting and IT support use cases.

It gathers system stats like CPU usage, memory, disk space, and network status, then logs them to a file for later review.

## 🔧 Features

- System information: OS, IP address, boot time, processor details
- CPU stats: core count, usage percentage
- Memory usage: total, used, free
- Disk usage: for all partitions
- Network information: interface and IP details
- Ping test: basic connectivity check to `google.com`
- Log output saved to `diagnostic_log.txt`

## 📂 Folder Structure

```
system-diagnostic-tool/
├── syscheck.py
├── diagnostic_log.txt
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/system-diagnostic-tool.git
cd system-diagnostic-tool
```

### 2. Install Dependencies

Only one external dependency:

```bash
pip install psutil
```

### 3. Run the Tool

```bash
python syscheck.py
```

### 4. Check Output

View the diagnostic_log.txt file created in the same folder.

✅ Sample Output (in diagnostic_log.txt)

```yaml
System Information
---
Hostname: Shuleis-MacBook.local
IP Address: 192.168.1.7
System: Darwin 23.3.0
Processor: Apple M1
---
## CPU Info

Physical cores: 4
Total cores: 8
CPU Usage: 9.3%

and more...
```

### 🔒 Notes

1. Compatible with macOS, Windows, and most Linux distros
2. Requires Python 3.x
