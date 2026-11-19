# Port Scanner

A simple TCP connect port scanner built with Python 3 and sockets. It checks a list of ports on a host, reports which are open, and grabs the service banner when an open port sends one.

## How to run

```
python3 port_sc.py
```

Enter the IP address, then the ports separated by spaces.

## Example

```
ENTER IP TO SCAN : 127.0.0.1
ENTER PORTS TO SCAN SEPARATED BY SPACE: 2222 8080 2223

[+] SCANNING 127.0.0.1

[+] PORT 2222 OPEN
    SSH-2.0-OpenSSH_9.6
[+] PORT 8080 OPEN
[-] PORT 2223 CLOSED
```

## How it works

- Each port gets its own socket, since a socket can only connect once.
- `connect_ex` returns 0 when the TCP handshake completes, which means the port is open.
- After connecting, it waits up to 3 seconds for a banner. Services that wait for the client to speak first (like HTTP) are still shown as open, just without a banner.
- Ports are validated before scanning (1–65535).

Only scan hosts you own or have permission to test.
