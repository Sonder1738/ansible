#!/usr/bin/python3

import socket
import json
import re

base_ip = "172.18.0."
start_ip = 1
end_ip = 10

hostvars = {}
groups = {
    "ubuntu": [],
    "centos": [],
    # Add more groups here if needed
}

# Track count for naming
host_counters = {key: 1 for key in groups}

for i in range(start_ip, end_ip + 1):
    ip = f"{base_ip}{i}"
    try:
        full_hostname = socket.gethostbyaddr(ip)[0]
        short_hostname = full_hostname.split('.')[0]

        # Determine group based on prefix
        matched = False
        for group in groups:
            if short_hostname.startswith(group):
                name = f"{group}{host_counters[group]}"
                hostvars[name] = {"ansible_host": ip}
                groups[group].append(name)
                host_counters[group] += 1
                matched = True
                break

        if not matched:
            # Unmatched hosts could go in 'ungrouped' or be ignored
            continue

    except socket.herror:
        continue

# Build inventory structure
inventory = {
    "_meta": {"hostvars": hostvars},
    "all": {
        "children": ["ungrouped"] + [group for group in groups if groups[group]]
    }
}

# Add group-specific data
for group, hosts in groups.items():
    if hosts:
        inventory[group] = {
            "hosts": hosts,
            "vars": {
                "ansible_port": 22,
                "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
                "ansible_user": "ansible"
            }
        }

print(json.dumps(inventory, indent=4))
