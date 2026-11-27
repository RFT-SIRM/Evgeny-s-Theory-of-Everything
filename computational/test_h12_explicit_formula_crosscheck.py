import unittest

from computational.h12_explicit_formula_crosscheck import (
    C_LEVELS,
    D_LEVELS,
    Q3,
    Q12,
    closed_form_at_pi,
    reduce_c_squared,
    times_s2,
    verify,
)


class H12ExplicitFormulaCrosscheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = verify()

    def test_residual_polynomial_equals_minus_64_s2_q12(self):
        self.assertTrue(self.result["residual_polynomial_matches"])
        self.assertEqual(self.result["residual_terms"], 13)

    def test_residual_value_at_pi_for_all_certified_transitions(self):
        self.assertEqual(self.result["residual_at_pi_expected"], -634073536)
        for m in C_LEVELS:
            self.assertTrue(self.result["residual_at_pi_matches"][m], m)

    def test_closed_form_matches_certified_d_at_pi_for_levels_3_to_8(self):
        for m in D_LEVELS:
            self.assertTrue(self.result["d_at_pi_matches"][m], m)
        self.assertEqual(closed_form_at_pi(3), -18026705824)
        self.assertEqual(
            [closed_form_at_pi(m) for m in (3, 4, 5)],
            [-18343742592 * 3 ** (m - 3) + 317036768 for m in (3, 4, 5)],
        )

    def test_reduction_is_exact_and_only_uses_c_exponents_zero_or_one(self):
        reduced = reduce_c_squared(times_s2(Q3, 32))
        self.assertTrue(all(i in (0, 1) for i, _ in reduced))
        self.assertEqual(reduced[(0, 2)] != 0, True)


if __name__ == "__main__":
    unittest.main()
