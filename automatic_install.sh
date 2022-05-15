#! /bin/bash
set -e
sudo cp main.py /usr/local/bin/btrfs-cancel-all-scrub
sudo chmod 700 /usr/local/bin/btrfs-cancel-all-scrub
sudo cp btrfs-auto-cancel-scrub.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable btrfs-auto-cancel-scrub.service