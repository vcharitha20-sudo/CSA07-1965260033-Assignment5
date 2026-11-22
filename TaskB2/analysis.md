# B2 — Network Simulation Plan

Model head office, two regional offices, booking server and internet gateway. Suggested scenario matrix: baseline 100 users on 100 Mbps with 20 ms delay; congestion 500 users on 20 Mbps with 100 ms delay; repeat with low-latency priority queuing for voice. Collect voice one-way delay/jitter/loss and booking throughput under each condition. These are experiment settings, not measurements. Apply the same packet sizes and observation duration to compare runs. Priority queuing should protect voice while preserving fair service for booking traffic.
