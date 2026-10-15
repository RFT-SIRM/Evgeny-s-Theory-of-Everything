import unittest
from decimal import Decimal

from computational.audit_recurrence import REFERENCE, transition_constants


class PublishedReferenceRecurrenceAudit(unittest.TestCase):
    def test_first_transition_is_not_the_later_constant(self):
        for power, values in REFERENCE.items():
            with self.subTest(power=power):
                c12, c23, c34 = transition_constants(values)
                self.assertGreater(abs(c12 - c23), Decimal("1"))

    def test_later_two_transitions_agree_to_published_precision(self):
        # Tolerance is deliberately stated; source values are floating-point
        # regression references rounded to the displayed decimal places.
        relative_tolerance = Decimal("1e-9")
        for power, values in REFERENCE.items():
            with self.subTest(power=power):
                _, c23, c34 = transition_constants(values)
                scale = max(abs(c23), abs(c34), Decimal(1))
                self.assertLessEqual(abs(c23 - c34), relative_tolerance * scale)

    def test_expected_moment_sets_are_present(self):
        self.assertEqual(set(REFERENCE), {"H6", "H8", "H10"})
        self.assertTrue(all(len(values) == 4 for values in REFERENCE.values()))


if __name__ == "__main__":
    unittest.main()
