#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM, timeout as SocketTimeout


def grab_banner(sock):
    """Return the first bytes a service sends, or None if it stays silent."""
    try:
        data = sock.recv(1024)
    except (SocketTimeout, OSError):
        return None
    return data.decode(errors="replace").strip() or None


def port_scanner(host, ports, timeout=3):
    print(f"[+] SCANNING {host}\n")
    for port in ports:
        # A new socket for every port: a socket can only connect once.
        with socket(AF_INET, SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((host, port)) != 0:
                print(f"[-] PORT {port} CLOSED")
                continue
            print(f"[+] PORT {port} OPEN")
            banner = grab_banner(s)
            if banner:
                print(f"    {banner}")


def parse_ports(text):
    ports = []
    for item in text.split():
        if not item.isdigit() or not 1 <= int(item) <= 65535:
            raise ValueError(f"'{item}' is not a valid port (1-65535)")
        ports.append(int(item))
    if not ports:
        raise ValueError("no ports given")
    return ports


if __name__ == "__main__":
    host = input("ENTER IP TO SCAN : ").strip()
    try:
        ports = parse_ports(input("ENTER PORTS TO SCAN SEPARATED BY SPACE: "))
    except ValueError as e:
        raise SystemExit(f"[!] {e}")
    print()
    port_scanner(host, ports)
