# A1 — Delay and Performance Targets

Packet size = 1,200 bytes = 9,600 bits. Per-link transmission delay = 9,600/50,000,000 = 0.192 ms. Assuming four routers and five links, transmission = 0.960 ms; queuing = 4 × 0.8 = 3.2 ms; processing = 4 × 0.05 = 0.2 ms. Propagation depends on medium: assuming 2×10^8 m/s, 1,800 km / speed = 9.0 ms. Total = 13.36 ms (one-way, without other overhead). With 500 Mbps links, transmission becomes 0.096 ms total; total ~12.50 ms. Propagation dominates.

Bandwidth–delay product: 10 Gbps × 0.040 s = 400 Mb = 50 MB. 128 KiB TCP window limits throughput to 128×1024×8/0.040 = 26.21 Mbps.

Proposed service objectives: booking and payment page p95 response <2 s; voice one-way delay <150 ms, jitter <30 ms, loss <1%; help video throughput ≥5 Mbps and low buffering; e-mail delivery <60 s; nightly sync ≥100 Mbps where provisioned. Use browser developer tools for page phases, ping/traceroute for RTT/path, iperf3 for throughput, Wireshark for packet timing and SNMPv3 for interface counters. Active probes inject traffic; passive monitoring observes existing traffic.
