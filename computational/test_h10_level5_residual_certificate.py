import unittest
from computational.h10_level5_residual_certificate import verify

class H10ResidualCertificateTests(unittest.TestCase):
    def test_exact_polynomial_fourier_identity_and_endpoint(self):
        result=verify()
        self.assertEqual(result["identity"],"verified in Z[c,s]/(c^2+s^2-1)")
        self.assertEqual(result["C10_pi"],4507520)
        self.assertEqual(result["D5_pi"],-2505633280)
        self.assertEqual(result["D6_pi"],-7512392320)

if __name__=="__main__":
    unittest.main()
