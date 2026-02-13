import pandas as pd
import subprocess

def collect_logs():
    print("[+] Collecting logs from journalctl...")
    
    try:
        # Get last 500 log lines
        result = subprocess.run(
            ["journalctl", "-n", "500", "--no-pager"],
            capture_output=True,
            text=True
        )

        logs = result.stdout.strip().split("\n")
        print(f"[+] Collected {len(logs)} log entries")
        return logs

    except Exception as e:
        print("Error collecting logs:", e)
        return []


def save_to_csv(logs):
    df = pd.DataFrame(logs, columns=["raw_log"])
    df.to_csv("data/raw_logs.csv", index=False)
    print("[+] Logs saved to data/raw_logs.csv")


if __name__ == "__main__":
    logs = collect_logs()
    if logs:
        save_to_csv(logs)
