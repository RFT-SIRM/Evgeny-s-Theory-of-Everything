import unittest

from computational.h10_level5_residual_certificate import verify


class H10ResidualCertificateTests(unittest.TestCase):
    def test_exact_polynomial_fourier_identity_and_endpoints(self):
        result = verify()
        self.assertEqual(
            result["identity"], "verified in Z[c,s]/(c^2+s^2-1)"
        )
        self.assertEqual(result["source_residual_equality"], "NOT_CHECKED")
        self.assertEqual(result["C10_zero_from_polynomial"], 0)
        self.assertEqual(result["C10_pi_from_polynomial"], 4507520)
        self.assertEqual(result["D5_pi"], -2505633280)
        self.assertEqual(result["D6_pi"], -7512392320)
        self.assertEqual(result["C10_pi_from_traces"], 4507520)


if __name__ == "__main__":
    unittest.main()
