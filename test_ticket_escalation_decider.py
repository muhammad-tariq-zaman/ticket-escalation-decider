import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import decide


def row(p, age, reopens, status="open"):
    return {"ticket": "T1", "priority": p, "age_hours": str(age),
            "reopen_count": str(reopens), "status": status}


class TestEscalation(unittest.TestCase):
    def test_p1_over_threshold(self):
        self.assertEqual(decide(row("P1", 5, 0))[0], "ESCALATE")

    def test_p1_within_threshold(self):
        self.assertEqual(decide(row("P1", 2, 0))[0], "KEEP")

    def test_reopen_escalates_any_priority(self):
        self.assertEqual(decide(row("P4", 1, 3))[0], "ESCALATE")

    def test_closed_never_escalates(self):
        self.assertEqual(decide(row("P1", 99, 5, "closed"))[0], "KEEP")
