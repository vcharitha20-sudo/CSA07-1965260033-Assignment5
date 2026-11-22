# A3 — P2P, VoIP and Overlays

Assume 6 GB decimal = 48 Gb. Client–server lower bound max(15×48 Gb/200 Mbps, 48 Gb/100 Mbps) = 3,600 s = 60 min. P2P lower bound max(48 Gb/200 Mbps, 48 Gb/100 Mbps, 15×48 Gb/(200+15×40) Mbps) = max(240,480,900) s = 900 s = 15 min. Real distribution includes startup, peer availability and protocol overhead.

G.729 payload in 20 ms = 8,000×0.020/8 = 20 bytes; plus 40-byte headers = 60 bytes. 50 packets/s ×60×8 = 24 kbps per direction; floor(1,000/24) = 41 simultaneous unidirectional streams (or 41 calls on symmetric 1 Mbps links, ignoring L2). SIP establishes/changes sessions; RTP carries timed media.

A CDN caches video near users; a VPN creates encrypted logical paths between offices. If a 1 Gbps CDN edge independently serves one 6 GB package to a region, a 100 Mbps receiving office still takes at least 480 s; edge availability does not remove the office bottleneck.
