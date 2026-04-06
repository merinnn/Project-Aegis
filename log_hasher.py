import hashlib
import json
import os
import sys
from datetime import datetime

LEDGER_FILE  = "ledger.jsson"
def add_to_ledger(log_msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prev_hash = "0"
    if os.path.exists(LEDGER_FILE):
        try:
            with open(LEGER_FILE,'r') as f:
                data = json.load(f)
                if data: prev_hash = data[-1]['current_hash']
        except: prev_hash = "0"
    block_content = f"{timestamp} - {log_msg} - {prev_hash}"
    current_hash = hashlib.sha256(block_content.encode()).hexdigest()
    new_block = {"timestamp": timestamp,"event": log_msg, "previous_hash": prev_hash, "current_hash": current_hash}
    ledger_data = []
    if os.path.exists(LEDGER_FILE):
        try:
            with open(LEDGER_FILE, 'r') as f: ledger_data = json.load(f)
        except: ledger_data = []
    ledger_data.append(new_block)
    with open(LEDGER_FILE, 'w') as f:
        json.dump(ledger_data, f, indent=4)
    print(f"Success! Block added. Hash: {current_hash[:10]}...")
if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else "SIEM_ALERT"
    add_to_ledger(msg)
