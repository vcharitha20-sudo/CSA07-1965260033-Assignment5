# B1 — Network Measurement and RTP Trace

Measurement plan: collect 100 ping samples to local, national and overseas endpoints in morning, afternoon and evening; calculate RTT min/mean/max, jitter (mean absolute successive RTT difference) and packet loss; use traceroute for path. For iperf3 compare TCP/UDP, single stream and four parallel streams on wired and wireless links. Record actual interfaces and test conditions.

The included Python trace exercise uses the assignment's provided RTP data, not a capture from the student's network. Packet loss = 2/12 = 16.7%. Mean one-way delay and RFC 3550 jitter are computed in the executable script. Compare model-derived MOS to listening quality with caution; burst loss and codecs affect perceived quality.
