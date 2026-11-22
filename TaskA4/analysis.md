# A4 — TLS and Firewall Design

Certificate validation checks the server identity through a trusted chain; TLS negotiates keys, ciphers and authentication. HTTPS encrypts application content, though some metadata and traffic patterns may remain observable.

Original firewall rule allowing any source to TCP 3306 precedes a deny for the same port, so the deny is shadowed. Correct policy: allow TCP 10.5.0.0/16 → database TCP 3306; deny other sources → database TCP 3306; allow HTTPS 443 as needed; permit approved office SSH 22; deny other SSH; permit required DNS; default deny. Restrict database exposure at both perimeter and host. Stateless filters inspect packet headers; stateful firewalls track flows; application proxies inspect protocol requests.

A web application firewall can help filter SQL injection and cross-site scripting attempts, but does not replace secure application code. The example Python program models basic flow tracking, not production firewall behavior.
