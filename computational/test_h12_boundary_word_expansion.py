import unittest
from fractions import Fraction

from computational.h12_boundary_word_expansion import (
    compositions,
    degree12_report_data,
    inventory,
)


class H12BoundaryWordExpansionTests(unittest.TestCase):
    def test_compositions_are_exactly_all_ordered_positive_words(self):
        for p in range(1, 13):
            all_words = [word for r in range(1, p + 1) for word in compositions(p, r)]
            self.assertEqual(len(all_words), 2 ** (p - 1))
            self.assertTrue(all(sum(word) == p for word in all_words))
            self.assertTrue(all(all(x >= 1 for x in word) for word in all_words))

    def test_degree_twelve_level_three_exception_inventory(self):
        data = inventory(12, 8)
        self.assertEqual(data["ordered_compositions_total"], 2048)
        self.assertEqual(
            data["ordered_compositions_with_possible_off_diagonal_corner_factor"], 48
        )
        self.assertEqual(data["ordered_compositions_diagonal_only_by_distance_cutoff"], 2000)
        self.assertEqual(data["exceptional_odd_r_count"], 24)
        self.assertEqual(data["exceptional_even_r_count"], 24)
        self.assertEqual(
            [row["possible_off_diagonal_count"] for row in data["by_number_of_gluing_factors"]],
            [1, 8, 18, 16, 5, 0, 0, 0, 0, 0, 0, 0],
        )

    def test_no_off_diagonal_corner_factor_from_level_four_onward(self):
        data = inventory(12, 16)
        self.assertEqual(data["ordered_compositions_total"], 2048)
        self.assertEqual(
            data["ordered_compositions_with_possible_off_diagonal_corner_factor"], 0
        )
        self.assertEqual(data["ordered_compositions_diagonal_only_by_distance_cutoff"], 2048)

    def test_trace_composition_weights(self):
        data = inventory(12, 8)
        self.assertEqual(data["weighted_composition_count"], "4095")
        self.assertEqual(data["weighted_exceptional_count"], "192")
        # The 48 possible cross-corner words have exact aggregate cyclic weight 192.
        self.assertEqual(
            sum(Fraction(12, row["r"]) * row["possible_off_diagonal_count"]
                for row in data["by_number_of_gluing_factors"]),
            Fraction(192, 1),
        )

    def test_even_odd_strata_for_generic_pair_swap(self):
        data = degree12_report_data()
        self.assertEqual(data["even_r_composition_count"], 1024)
        self.assertEqual(data["odd_r_composition_count"], 1024)
        # Odd r vanishes only after verifying that N is a disjoint union of
        # involutive pairings; this test checks counts, not that graph hypothesis.


if __name__ == "__main__":
    unittest.main()
