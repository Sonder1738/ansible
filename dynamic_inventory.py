#!/usr/bin/python3

import json
output = {
    "_meta": {
        "hostvars": {
            "ubuntu1": {
                "ansible_host": "172.18.0.2"
            },
            "ubuntu2": {
                "ansible_host": "172.18.0.4"
            },
            "ubuntu3": {
                "ansible_host": "172.18.0.6"
            }
        }
    },
    "all": {
        "children": [
            "ungrouped",
            "ubuntu"
        ]
    },
    "ubuntu": {
        "hosts": [
            "ubuntu1",
            "ubuntu2",
            "ubuntu3"
        ],
        "vars": {
            "ansible_port": 22,
            "ansible_ssh_private_key_file": "~/.ssh/id_rsa",
            "ansible_user": "ansible"
        }
    }
}
print(json.dumps(output))
