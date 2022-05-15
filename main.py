#! /usr/bin/env python3
try:
	import psutil
except:
	print("can't import psutil, you don't have this installed")
	exit(0)
	
import subprocess, shlex #standard library, should be able to import without problem

try:
	for process in psutil.process_iter():
		command = process.cmdline()
		if len(command) == 4 and command[0] == "btrfs" and command[1] == "scrub" and command[2] in ["start", "resume"]:
			cancelCommand = f"btrfs scrub cancel {command[3]}"
			print(f"execute '{cancelCommand}'")
			try:
				subprocess.run(shlex.split(cancelCommand), timeout=60, check=True)
				print("success")
			except subprocess.TimeoutExpired:
				print("Failed to cancel scrub (command timeout)")
			except subprocess.CalledProcessError as error:
				print(f"Failed to cancel scrub (status code {error.returncode})")
			except:
				print(f"Failed to cancel scrub (unknown failure)")
except:
	print("error happened, graceful exit")
	exit(0)
