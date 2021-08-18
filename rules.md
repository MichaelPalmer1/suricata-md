| Action | Protocol | Direction | Source IP | Source Port | Destination IP | Destination Port | Description | Options |
|--------|----------|-----------|-----------|-------------|----------------|------------------|-------------|---------|
| pass | tcp | Forward | 10.0.0.0/8 | 0-65535 | 10.0.0.0/24 | 80 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 10.0.0.0/8 | 0-65535 | 10.0.0.0/24 | 443 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 10.0.0.0/8 | 0-65535 | 10.0.0.0/24 | 22 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 10.0.0.0/8 | 0-65535 | 10.1.0.0/24 | 80 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 10.0.0.0/8 | 0-65535 | 10.1.0.0/24 | 443 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 10.0.0.0/8 | 0-65535 | 10.1.0.0/24 | 22 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 192.168.0.0/16 | 0-65535 | 10.0.0.0/24 | 80 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 192.168.0.0/16 | 0-65535 | 10.0.0.0/24 | 443 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 192.168.0.0/16 | 0-65535 | 10.0.0.0/24 | 22 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 192.168.0.0/16 | 0-65535 | 10.1.0.0/24 | 80 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 192.168.0.0/16 | 0-65535 | 10.1.0.0/24 | 443 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 192.168.0.0/16 | 0-65535 | 10.1.0.0/24 | 22 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 172.16.0.0/12 | 0-65535 | 10.0.0.0/24 | 80 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 172.16.0.0/12 | 0-65535 | 10.0.0.0/24 | 443 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 172.16.0.0/12 | 0-65535 | 10.0.0.0/24 | 22 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 172.16.0.0/12 | 0-65535 | 10.1.0.0/24 | 80 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 172.16.0.0/12 | 0-65535 | 10.1.0.0/24 | 443 | Allow GitHub | priority=1, sid=1 |
| pass | tcp | Forward | 172.16.0.0/12 | 0-65535 | 10.1.0.0/24 | 22 | Allow GitHub | priority=1, sid=1 |
