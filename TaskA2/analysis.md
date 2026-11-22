# A2 — Application Protocols

Example SMTP exchange: EHLO client.example (250), MAIL FROM:<confirm@example.in> (250), RCPT TO:<customer@example.in> (250), DATA (354), message followed by a single dot (250), QUIT (221). MX selects the recipient's mail exchangers; authenticated submission on 587 with STARTTLS protects credentials in transit. SPF authorizes sending hosts, DKIM signs mail, and DMARC specifies alignment and receiver policy.

SFTP uses one encrypted SSH connection on port 22, unlike FTP control/data channel complexity. rsync over SSH transfers changed blocks efficiently. SNMPv3 provides authentication and encryption. Interface counter delta = 175,000,000 octets × 8 / 60 s = 23.33 Mbps, or 23.33% of a 100 Mbps link. Browser timing separates DNS, TCP connect, TLS negotiation, waiting/TTFB and download. 3xx redirect; 4xx client-side request issue; 5xx server-side failure.

20 GB (decimal) at effective 95 Mbps takes 20×8×10^9 / (95×10^6) = 1,684.2 s ≈28.1 min, ignoring retransmission and storage processing. SFTP and HTTPS object storage both support encrypted transport; resumability and cost depend on implementation.
