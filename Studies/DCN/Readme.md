
# Data Communication & Networking (DCN) Lab File

[![C](https://img.shields.io/badge/Language-C-blue.svg)](https://developer.ibm.com/languages/c/)
[![C++](https://img.shields.io/badge/Language-C%2B%2B-00599C.svg?style=flat&logo=c%2B%2B)](https://isocpp.org/)
[![Cisco Packet Tracer](https://img.shields.io/badge/Simulation-Cisco%20Packet%20Tracer-green.svg)](https://www.netacad.com/courses/packet-tracer)
[![Wireshark](https://img.shields.io/badge/Analysis-Wireshark-167EBA.svg?style=flat&logo=wireshark)](https://www.wireshark.org/)
[![Nmap](https://img.shields.io/badge/Security-Nmap-black.svg)](https://nmap.org/)

This repository contains a comprehensive collection of Data Communication & Networking (DCN) Lab Experiments completed as part of the B.Tech Computer Science & Engineering (CSE) curriculum at UPES, Dehradun. 

It spans core networking theories, routing protocols, hands-on Cisco Packet Tracer simulations, packet-level Wireshark analysis, and programmatic C/C++ implementations of error detection and correction algorithms.
---
## Author Profile
| Detail | Description |
| :--- | :--- |
| **Name** | Prabhjeet Singh |
| **Programme** | B.Tech Computer Science & Engineering (CSE) |
| **Semester** | 4th Semester |
| **Institution** | University of Petroleum and Energy Studies (UPES), Dehradun |
---
## Repository Contents

The experiments and implementations are categorized into five core modules:
### 1. Networking Fundamentals
* **Device Familiarization:** Exploration of hardware layers including hubs, switches, routers, gateways, and access points.
* **IP Addressing:** Detailed study of IPv4 addressing structures, classes, and subnet ranges.
* **Subnetting & Supernetting:** Practical design and calculation of VLSM, FLSM, and address aggregation.
* **CLI Diagnostics:** Hand-on exercises using core network commands:
  * `ping`, `traceroute` / `tracert`, `nslookup`, `ipconfig` / `ifconfig`, `netstat`, `arp`

### 2. Programming Experiments
C and C++ implementations simulating Data Link Layer error control and framing techniques:
* **Bit Stuffing & De-Stuffing:** Framing rules to prevent payload-header confusion.
* **Cyclic Redundancy Check (CRC):** Generates and verifies frame check sequences using binary division.
* **Hamming Code:** Error detection and single-bit error correction implementation.

### 3. Cisco Packet Tracer Simulations
Interactive simulations designed to model real-world local and wide area network topologies:
* **Ring Topology:** Setting up and analyzing ring network failovers and packet paths.
* **Router-Switch Integration:** Building hybrid LAN topologies with layer 2 switches and layer 3 routers.
* **Inter-LAN Communication:** Configuring gateways to bridge communication across different logical subnets.

### 4. Routing Protocols
Comparative study and configuration of dynamic routing algorithms:
* **Distance Vector Routing (DVR):** Implementing and understanding RIP (Routing Information Protocol) convergence.
* **Link-State Routing (LSR):** Configuring OSPF (Open Shortest Path First) for shortest-path calculation.
* **DVR vs. LSR:** Comprehensive analysis of routing tables, convergence times, and overhead.

### 5. Network Monitoring & Traffic Analysis
* **Nmap Port Scanning:** Performing host discovery, port scanning, and OS detection.
* **Wireshark Packet Capture:** Live capture and inspection of network packets.
* **Protocol Analysis:** Inspecting header formats and handshake mechanisms of major protocols (TCP, UDP, HTTP, ICMP, DNS).



## Tools & Technologies Used

* **Network Simulation:** Cisco Packet Tracer
* **Packet Analyzer:** Wireshark
* **Security & Auditing:** Nmap
* **Programming Languages:** C & C++
* **Theoretical Foundations:** OSI Model, TCP/IP Suite, CIDR, and Routing Architectures



## Learning Outcomes

Through these practical experiments, I have gained hands-on expertise in:
- [x] Designing, configuring, and troubleshooting network topologies.
- [x] Inspecting and decoding raw network traffic to debug protocol behaviors.
- [x] Implementing error control algorithms programmatically at the system layer.
- [x] Managing and optimizing address space using subnetting techniques.
- [x] Configuring dynamic routing protocols to establish secure inter-LAN communication.



## Notes & Disclaimer
> This repository is maintained strictly for academic and learning purposes. It serves as an archive of coursework submissions and reference implementations for students studying computer networking.
