import unittest

from computational.h12_residual_certificate import (
    EXPECTED_C_PI,
    EXPECTED_D_PI,
    EXPECTED_FOURIER,
    EXPECTED_REDUCED,
    verify,
)


class H12ResidualCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = verify()

    def test_source_pin_and_crt_uniqueness(self):
        self.assertEqual(self.payload["moment"], 12)
        self.assertEqual(
            self.payload["source"]["commit"],
            "4ccfae17ae8d1ed8c9f1c1488ecec87fe9c97d9f",
        )
        self.assertGreater(
            self.payload["crt_modulus_product"],
            self.payload["twice_max_coefficient_bound"],
        )
        self.assertEqual(self.payload["max_graph_degree"], 4)
        self.assertEqual(self.payload["max_row_coefficient_l1"], 10)

    def test_exact_reduced_polynomial_and_fourier_form(self):
        self.assertEqual(
            self.payload["common_reduced_polynomial"],
            {f"c^{a}s^{b}": value for (a, b), value in EXPECTED_REDUCED.items()},
        )
        self.assertEqual(self.payload["common_fourier"], EXPECTED_FOURIER)
        self.assertEqual(self.payload["residuals"]["3"]["at_theta_pi"], EXPECTED_C_PI)
        self.assertEqual(self.payload["residuals"]["3"]["at_theta_zero"], 0)

    def test_three_finite_transitions_agree(self):
        self.assertEqual(
            self.payload["comparisons"],
            {
                "C12_3_equals_C12_4": True,
                "C12_4_equals_C12_5": True,
                "C12_3_equals_C12_5": True,
            },
        )
        self.assertEqual(
            self.payload["D_m_at_theta_pi"],
            {str(k): value for k, value in EXPECTED_D_PI.items()},
        )
        for m in (3, 4, 5):
            self.assertEqual(
                self.payload["D_m_at_theta_pi"][str(m + 1)]
                - 3 * self.payload["D_m_at_theta_pi"][str(m)],
                EXPECTED_C_PI,
            )


if __name__ == "__main__":
    unittest.main()
