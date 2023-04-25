import subprocess

pid_cmd = "lsof -i :65433 | awk '{print $2}' | tail -1"
pid = subprocess.check_output(pid_cmd, shell=True).decode().strip()

kill_cmd = f"kill {pid}"
subprocess.run(kill_cmd, shell=True)
