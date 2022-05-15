# Auto cancel btrfs scrubbing before shutdown/reboot

Looking at the code yourself is encouraged if you know basics of Python, no warranty comes with anything in this repository.

## Requrements

1. Python3
2. [psutil](https://pypi.org/project/psutil/) library
3. running Systemd

## Installation

You can use automatic_install.sh if you want quick installation

### Manual installtion

1. Run `python3 main.py` and make sure it doesn't print `can't import psutil, you don't have this installed`

2. Copy this program to your system with

		sudo cp main.py /usr/local/bin/btrfs-cancel-all-scrub
		sudo chmod 700 /usr/local/bin/btrfs-cancel-all-scrub

 You can also copy it to other directory, make sure to edit `btrfs-auto-cancel-scrub.service` to reflect the change.

3. Copy service file and make sure it's registered.

		sudo cp btrfs-auto-cancel-scrub.service /etc/systemd/system
		sudo systemctl daemon-reload

4. Try running this service once

 This will cancel all your scrubbing process!

		sudo systemctl start btrfs-auto-cancel-scrub.service

 It shouldn't print any error messages. (I am 99 percent sure)

5. Enable the service

		sudo systemctl enable btrfs-auto-cancel-scrub.service

Done