"""Decide which open tickets to escalate, with a reason for each.

Usage: python3 main.py tickets.csv
CSV columns: ticket,priority,age_hours,reopen_count,status
Rules: P1 older than 4h, P2 older than 24h, P3 older than 72h, or any
ticket reopened 2+ times is escalated. Closed tickets are never escalated.
"""
import argparse, csv, sys

THRESHOLDS = {"P1": 4, "P2": 24, "P3": 72, "P4": 168}


def decide(row):
    if row["status"].strip().lower() == "closed":
        return "KEEP", "closed"
    priority = row["priority"].strip()
    age = float(row["age_hours"])
    reopens = int(row["reopen_count"])
    if reopens >= 2:
        return "ESCALATE", f"reopened {reopens} times"
    if age > THRESHOLDS.get(priority, 168):
        return "ESCALATE", f"{priority} older than {THRESHOLDS.get(priority, 168)}h"
    return "KEEP", "within SLA window"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    escalated = 0
    with open(args.path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            verdict, reason = decide(row)
            if verdict == "ESCALATE":
                escalated += 1
            print(f"{row['ticket']}: {verdict} ({reason})")
    print(f"{escalated} ticket(s) to escalate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
