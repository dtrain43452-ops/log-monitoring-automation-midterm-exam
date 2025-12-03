import socket
import datetime
import time

def scan_port(host, port):
    """Check if a single port is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        else:
            return False
    except:
        return False
    finally:
        sock.close()

def scan_range(host, start_port, end_port):
    """Scan a range of ports on a host."""
    print(f"\nScanning {host} from {start_port} to {end_port}")
    print("Timestamp:", datetime.datetime.now())
    print("-" * 40)

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
        time.sleep(0.1)  # ethical delay

if __name__ == "__main__":
    try:
        host = input("Enter host to scan (127.0.0.1 or scanme.nmap.org): ")
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("[ERROR] Invalid port range")
        else:
            scan_range(host, start_port, end_port)

    except ValueError:
        print("[ERROR] Ports must be numbers")
import socket
from datetime import datetime

def is_valid_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        result = sock.connect_ex((host, port))
        if result == 0:
            return True
        else:
            return False
    except Exception:
        return False
    finally:
        sock.close()

def main():
    host = input("Enter host to scan (127.0.0.1 or scanme.nmap.org): ").strip()

    if not is_valid_host(host):
        print("\n❌ ERROR: Host unreachable or invalid.\n")
        return

    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("\n❌ ERROR: Invalid port range.\n")
            return

    except ValueError:
        print("\n❌ ERROR: Port numbers must be integers.\n")
        return

    print(f"\nScanning {host} from {start_port} to {end_port}")
    print("Timestamp:", datetime.now())
    print("----------------------------------------")

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

if __name__ == "__main__":
    main()

