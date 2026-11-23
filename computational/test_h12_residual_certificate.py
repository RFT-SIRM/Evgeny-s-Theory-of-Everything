import unittest

from computational.h12_residual_certificate import (
    EXPECTED_C_PI,
    EXPECTED_D_PI,
    EXPECTED_FOURIER,
    EXPECTED_REDUCED,
    TRANSITIONS,
    verify,
)


class H12ResidualCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = verify()

    def test_source_pin_and_crt_uniqueness(self):
        self.assertEqual(self.payload["moment"], 12)
        self.assertEqual(self.payload["source"]["commit"], "4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f")
        self.assertGreater(
            self.payload["crt_modulus_product"],
            self.payload["twice_max_canonical_coefficient_bound"],
        )
        self.assertEqual(self.payload["max_graph_degree"], 4)
        self.assertEqual(self.payload["max_row_coefficient_l1"], 10)
        self.assertEqual(self.payload["canonical_reduction_factor"], 64)
        self.assertEqual(self.payload["crt_uniqueness_margin_ratio"], 595)

    def test_exact_reduced_polynomial_and_fourier_form(self):
        self.assertEqual(
            self.payload["common_reduced_polynomial"],
            {f"c^{a}s^{b}": value for (a, b), value in EXPECTED_REDUCED.items()},
        )
        self.assertEqual(self.payload["common_fourier"], EXPECTED_FOURIER)
        for m in TRANSITIONS:
            self.assertEqual(self.payload["residuals"][str(m)]["at_theta_pi"], EXPECTED_C_PI)
            self.assertEqual(self.payload["residuals"][str(m)]["at_theta_zero"], 0)

    def test_five_finite_transition_polynomials_agree(self):
        self.assertEqual(self.payload["levels_computed"], [3, 4, 5, 6, 7, 8])
        self.assertEqual(self.payload["transitions_compared"], [3, 4, 5, 6, 7])
        self.assertEqual(
            self.payload["comparisons"],
            {
                "C12_3_equals_C12_4": True,
                "C12_4_equals_C12_5": True,
                "C12_5_equals_C12_6": True,
                "C12_6_equals_C12_7": True,
                "all_five_finite_transitions_equal": True,
            },
        )

    def test_level_eight_endpoint_and_all_adjacent_residuals(self):
        self.assertEqual(
            self.payload["D_m_at_theta_pi"],
            {str(k): value for k, value in EXPECTED_D_PI.items()},
        )
        for m in TRANSITIONS:
            values = self.payload["D_m_at_theta_pi"]
            self.assertEqual(values[str(m + 1)] - 3 * values[str(m)], EXPECTED_C_PI)
        self.assertEqual(
            self.payload["independent_integer_endpoint_crosscheck"],
            {
                "level": 7,
                "D7_pi": EXPECTED_D_PI[7],
                "imaginary_part": 0,
                "source": "h12_level7_pi_crosscheck.cpp",
            },
        )


if __name__ == "__main__":
    unittest.main()
