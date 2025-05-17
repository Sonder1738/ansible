#!/bin/bash

# Exit on error
set -e

# --- CONFIG ---
ANSIBLE_USER="your_ssh_user"
SSH_PASSWORD="your_password_here"

sudo apt-get update -y
sudo apt-get install -y sshpass

export ANSIBLE_HOST_KEY_CHECKING=False

# Run playbook with sshpass providing the password
sshpass -p "$SSH_PASSWORD" ansible-playbook -i hosts_ini setupKeys.yml \
  -u "$ANSIBLE_USER" --ask-pass --extra-vars "ansible_ssh_pass=$SSH_PASSWORD"
