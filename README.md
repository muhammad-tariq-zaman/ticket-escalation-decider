# ticket-escalation-decider

Decide ticket escalations from age, priority and reopen count, with a plain reason per ticket so the handover is auditable.

## How to run

```sh
python3 main.py tickets.csv
```

## Example output

```
T-101: ESCALATE (P1 older than 4h)
T-102: KEEP (within SLA window)
1 ticket(s) to escalate.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
