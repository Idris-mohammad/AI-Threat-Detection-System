import subprocess
import re

def clean_log(log):
    # Remove timestamps
    log = re.sub(r"^[A-Za-z]{3}.*?\s", "", log)

    # Remove process tags like sshd[1234]:
    log = re.sub(r"\w+\[\d+\]:", "", log)

    return log.strip()


def stream_logs():
    process = subprocess.Popen(
        ["journalctl", "-f", "-n", "0"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    while True:
        line = process.stdout.readline()
        if line:
            yield clean_log(line.strip())
