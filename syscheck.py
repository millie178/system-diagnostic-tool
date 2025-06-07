import platform
import socket
import datetime
import psutil
import subprocess
import sys

def get_system_info():
    print("System Information")
    print("-" * 40)
    print(f"Hostname: {socket.gethostname()}")
    print(f"IP Address: {socket.gethostbyname(socket.gethostname())}")
    print(f"System: {platform.system()} {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {boot_time}\n")

def get_cpu_info():
    print("CPU Info")
    print("-" * 40)
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print()

def get_memory_info():
    print("Memory Info")
    print("-" * 40)
    mem = psutil.virtual_memory()
    print(f"Total: {mem.total // (1024 ** 2)} MB")
    print(f"Available: {mem.available // (1024 ** 2)} MB")
    print(f"Used: {mem.used // (1024 ** 2)} MB")
    print(f"Percentage: {mem.percent}%")
    print()

def get_disk_info():
    print("Disk Info")
    print("-" * 40)
    for partition in psutil.disk_partitions():
        print(f"Device: {partition.device}")
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  Total: {usage.total // (1024 ** 3)} GB")
        print(f"  Used: {usage.used // (1024 ** 3)} GB")
        print(f"  Free: {usage.free // (1024 ** 3)} GB")
        print(f"  Usage: {usage.percent}%\n")

def get_network_info():
    print("Network Info")
    print("-" * 40)
    addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in addrs.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"{interface_name} - IP: {address.address}")
    print()

def ping_test():
    print("Ping Test")
    print("-" * 40)
    try:
        output = subprocess.check_output("ping -c 2 google.com", shell=True)
        print("Ping successful.")
    except subprocess.CalledProcessError:
        print("Ping failed.")
    print()


def log_output():
    with open("diagnostic_log.txt", "w") as f:
        original_stdout = sys.stdout
        sys.stdout = f  # redirect to file

        get_system_info()
        get_cpu_info()
        get_memory_info()
        get_disk_info()
        get_network_info()
        ping_test()

        sys.stdout = original_stdout
        print("System diagnostic saved to diagnostic_log.txt")

log_output()
