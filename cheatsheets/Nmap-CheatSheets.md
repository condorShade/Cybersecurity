# Nmap Cheat Sheet

> A comprehensive guide for using Nmap, covering target specification, host discovery, scan techniques, and more.

---

## 🏷️ Target Specification
- `-iL <inputfilename>`: Import targets from a list
- `-iR <num hosts>`: Scan random hosts
- `--exclude <host1[,host2],...>`: Exclude specified hosts/networks
- `--excludefile <filename>`: Exclude hosts from a file

---

## 🌐 Host Discovery
- `-sL`: List scan (only lists targets)
- `-sn`: Ping scan (disable port scan)
- `-Pn`: Skip host discovery (treat all hosts as online)
- `-PS/PA/PU/PY`: TCP SYN/ACK, UDP, or SCTP discovery to given ports
- `-PE/PP/PM`: ICMP echo, timestamp, and netmask requests
- `-PO`: IP protocol ping
- `-n / -R`: Skip/force DNS resolution
- `--dns-servers <server1,...>`: Specify custom DNS servers
- `--system-dns`: Use system DNS resolver
- `--traceroute`: Trace network route to host

---

## 🔍 Scan Techniques
- `-sS / -sT / -sA / -sW / -sM`: Various TCP scans (SYN, Connect, ACK, Window, Maimon)
- `-sU`: UDP scan
- `-sN / -sF / -sX`: TCP Null, FIN, and Xmas scans
- `--scanflags <flags>`: Custom TCP scan flags
- `-sI <zombie host[:probeport]>`: Idle scan
- `-sY / -sZ`: SCTP INIT/COOKIE-ECHO scans
- `-sO`: IP protocol scan
- `-b <FTP relay host>`: FTP bounce scan

---

## 🔢 Port Specification & Scan Order
- `-p <port ranges>`: Scan specified ports
- `--exclude-ports <port ranges>`: Exclude specific ports
- `-F`: Fast mode (fewer ports)
- `-r`: Sequential port scan (no randomization)
- `--top-ports <number>`: Scan the top N most common ports
- `--port-ratio <ratio>`: Scan ports with higher ratio of usage

---

## 📄 Output Options
- `-oN/-oX/-oS/-oG <file>`: Output formats (Normal, XML, s|cript kiddie, Grepable)
- `-oA <basename>`: Output in all three major formats
- `-v / -d`: Increase verbosity/debugging level
- `--reason`: Display reasons for port state
- `--open`: Show only open ports
- `--packet-trace`: Display all sent/received packets
- `--iflist`: Print host interfaces and routes
- `--append-output`: Append to existing output files
- `--resume <filename>`: Resume an aborted scan
- `--stylesheet <path/URL>`: XML stylesheet for HTML conversion
- `--webxml`: Reference Nmap.org’s stylesheet
- `--no-stylesheet`: Disable XSL stylesheet association

---

## 🛡️ Firewall/IDS Evasion & Spoofing
- `-f`: Fragment packets
- `-D <decoy1,decoy2,...>`: Decoy scan
- `-S <IP Address>`: Spoof source address
- `-e <iface>`: Use specified interface
- `--source-port <portnum>`: Use specific source port
- `--proxies <url1,...>`: Proxy connections
- `--data <hex string>`: Append payload to packets
- `--data-string <string>`: Append ASCII string to packets
- `--data-length <num>`: Append random data
- `--ip-options <options>`: Send packets with specified IP options
- `--ttl <val>`: Set IP time-to-live
- `--spoof-mac <mac/prefix/vendor>`: Spoof MAC address
- `--badsum`: Send packets with invalid checksums

---

## ⏲️ Timing & Performance
- `-T<0-5>`: Set timing template (0: slowest, 5: fastest)
- `--min-hostgroup / --max-hostgroup <size>`: Host parallelization
- `--min-parallelism / --max-parallelism <numprobes>`: Probe parallelization
- `--min-rtt-timeout / --max-rtt-timeout / --initial-rtt-timeout <time>`: RTT timeouts
- `--max-retries <tries>`: Retry limit for probes
- `--host-timeout <time>`: Give up on target after specified time
- `--scan-delay / --max-scan-delay <time>`: Adjust delay between probes
- `--min-rate <number>`: Minimum packets per second
- `--max-rate <number>`: Maximum packets per second

---

## 🧬 OS Detection
- `-O`: Enable OS detection
- `--osscan-limit`: Limit OS detection to promising targets
- `--osscan-guess`: Guess OS aggressively

---

## 🔍 Service/Version Detection
- `-sV`: Probe open ports to determine service/version info
- `--version-intensity <level>`: Set probe intensity (0 to 9)
- `--version-light`: Light service version detection
- `--version-all`: Try every probe
- `--version-trace`: Detailed version detection (debugging)

---

## 🔧 Script Scan
- `-sC`: Default set of scripts (`--script=default`)
- `--script <scripts>`: Specify scripts or categories to use
- `--script-args <n1=v1,...>`: Arguments for scripts
- `--script-args-file <filename>`: NSE script args from file
- `--script-trace`: Show all script data sent/received
- `--script-updatedb`: Update the script database
- `--script-help <scripts>`: Show script help information

---
