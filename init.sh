#!/bin/bash

# Exit on error
set -e

# --- CONFIG ---
ANSIBLE_USER="ansible"
SSH_PASSWORD="password"

sudo apt-get update -y
sudo apt-get install -y sshpass
ssh-keygen -t rsa -b 4096 -f "/home/ansible/.ssh/id_rsa" -N ""
chmod 764 dynamic_inventory.py
export ANSIBLE_HOST_KEY_CHECKING=False
sshpass -p "$SSH_PASSWORD" ansible-playbook -i dynamic_inventory.py setupKeys.yml \
  -u "$ANSIBLE_USER" --ask-pass --extra-vars "ansible_ssh_pass=$SSH_PASSWORD"
