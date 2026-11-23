import unittest

from computational.h10_level5_residual_certificate import (
    FOURIER,
    H4_EXPECTED,
    POLYNOMIAL,
    SOURCE_COMMIT,
    verify,
)


class H10ResidualCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = verify()

    def test_source_reconstruction_and_crt_bound(self):
        result = self.result
        self.assertEqual(result["status"], "SOURCE_RECONSTRUCTED_EXACT_EXTERNAL_CRT_CERTIFICATE")
        self.assertEqual(result["source"]["commit"], SOURCE_COMMIT)
        self.assertEqual(result["source"]["recurrence_theorem"],
                         "defectO10_succ_num_level5_constant_boundary_unconditional")
        self.assertEqual(result["primes"], [10000453, 20000569, 30000769])
        self.assertGreater(result["crt_modulus_product"],
                           2 * result["coefficient_absolute_bound"])
        self.assertEqual(result["polynomial"], POLYNOMIAL)

    def test_h4_controls_and_exact_h10_endpoints(self):
        result = self.result
        self.assertEqual(result["H4_source_controls"],
                         {str(k): v for k, v in H4_EXPECTED.items()})
        self.assertEqual(result["D5_pi"], -2505633280)
        self.assertEqual(result["D6_pi"], -7512392320)
        self.assertEqual(result["C10_pi"], 4507520)
        self.assertEqual(result["D6_pi"] - 3 * result["D5_pi"], result["C10_pi"])

    def test_fourier_form(self):
        self.assertEqual(self.result["fourier"], FOURIER)


if __name__ == "__main__":
    unittest.main()
