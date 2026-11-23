import random
import unittest

from computational.h12_boundary_diagonal_contraction import (
    LEVEL3_CORNER_DISTANCE,
    POWER,
    build_inventory,
    compositions,
    even_pairing_safe_gaps,
    independent_safe_gap_set,
)


def mat2_mul(a, b):
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0],
         a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0],
         a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]


def mat2_trace(a):
    return a[0][0] + a[1][1]


def mat2_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def zero2():
    return [[0, 0], [0, 0]]


def eye2():
    return [[1, 0], [0, 1]]


def make_block_data(seed=20261123):
    """Six glued states, three copies, and noncommuting integer spin blocks."""
    rng = random.Random(seed)
    points = [(copy, end) for copy in range(3) for end in range(2)]
    sigma = {
        (0, 0): (1, 0), (1, 0): (0, 0),
        (0, 1): (2, 0), (2, 0): (0, 1),
        (1, 1): (2, 1), (2, 1): (1, 1),
    }
    data = {}
    for power in range(1, 13):
        blocks = {}
        for x in points:
            for y in points:
                if x[0] != y[0]:
                    continue  # K^j is block diagonal across copies.
                if x != y and power < LEVEL3_CORNER_DISTANCE:
                    continue  # Short powers cannot connect distinct glued points.
                blocks[(x, y)] = [
                    [rng.randint(-3, 3), rng.randint(-3, 3)],
                    [rng.randint(-3, 3), rng.randint(-3, 3)],
                ]
        data[power] = blocks
    return points, sigma, data


def direct_trace_word(word, points, sigma, data):
    """Evaluate Tr(K^a1 N ... K^ar N) by exact boundary-state paths."""
    answer = 0
    for start in points:
        # Each path state is (current boundary point, ordered 2x2 product).
        paths = [(start, eye2())]
        for exponent in word:
            next_paths = []
            for current, product in paths:
                targets = [y for y in points if y[0] == current[0]
                          and (y == current or exponent >= LEVEL3_CORNER_DISTANCE)]
                for target in targets:
                    block = data[exponent].get((current, target), zero2())
                    if block == zero2():
                        continue
                    next_paths.append((sigma[target], mat2_mul(product, block)))
            paths = next_paths
        answer += sum(mat2_trace(product) for current, product in paths if current == start)
    return answer


def diagonal_boundary_word(word, points, sigma, data):
    """The proposed ordered product of alternating diagonal corner blocks."""
    answer = 0
    for start in points:
        product = eye2()
        for i, exponent in enumerate(word):
            point = sigma[start] if i % 2 == 0 else start
            product = mat2_mul(product, data[exponent][(point, point)])
        answer += mat2_trace(product)
    return answer


class H12BoundaryDiagonalContractionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.payload = build_inventory()

    def test_composition_and_raw_long_gap_counts(self):
        payload = self.payload
        self.assertEqual(payload["ordered_compositions_total"], 2048)
        self.assertEqual(payload["raw_compositions_with_a_part_at_least_8"], 48)
        self.assertEqual(payload["raw_long_gap_split"], {"odd_r": 24, "even_r": 24})
        for r in range(1, POWER + 1):
            self.assertEqual(len(compositions(POWER, r)), 1 if r == 1 else __import__("math").comb(11, r - 1))
            for word in compositions(POWER, r):
                self.assertLessEqual(sum(x >= 8 for x in word), 1)

    def test_odd_strata_have_safe_nonadjacent_pairings(self):
        for r in range(3, POWER + 1, 2):
            for word in compositions(POWER, r):
                chosen = independent_safe_gap_set(word, 8)
                self.assertEqual(len(chosen), (r - 1) // 2)
                self.assertTrue(all(word[i] < 8 for i in chosen))
                selected = set(chosen)
                self.assertTrue(all((i + 1) % r not in selected for i in selected))

    def test_even_strata_have_an_alternating_safe_pairing(self):
        for r in range(2, POWER + 1, 2):
            for word in compositions(POWER, r):
                chosen = even_pairing_safe_gaps(word, 8)
                self.assertEqual(len(chosen), r // 2)
                self.assertTrue(all(word[i] < 8 for i in chosen))

    def test_exact_noncommuting_block_contraction_for_all_words(self):
        # Three independent integer block samples; every spin block is full and
        # noncommuting, and every long power may have arbitrary spatial offdiag.
        for seed in (20261123, 20261124, 20261125):
            points, sigma, data = make_block_data(seed)
            # r=1 is Tr(K^12 N), zero because K^12 is copy block-diagonal.
            self.assertEqual(direct_trace_word((12,), points, sigma, data), 0)
            even_checks = odd_checks = 0
            for r in range(2, POWER + 1):
                for word in compositions(POWER, r):
                    direct = direct_trace_word(word, points, sigma, data)
                    if r % 2:
                        self.assertEqual(direct, 0, msg=f"seed {seed}, odd word {word}")
                        odd_checks += 1
                    else:
                        reduced = diagonal_boundary_word(word, points, sigma, data)
                        self.assertEqual(direct, reduced, msg=f"seed {seed}, even word {word}")
                        even_checks += 1
            self.assertEqual(odd_checks, 1023)
            self.assertEqual(even_checks, 1024)

    def test_cyclic_orbit_reduction_and_integer_weights(self):
        reduction = self.payload["cyclic_even_r_reduction"]
        self.assertEqual(reduction["representative_count"], 179)
        self.assertEqual(reduction["even_r_composition_weight_sum"], "2047")
        self.assertEqual(reduction["all_word_weight_sum"], "4095")
        self.assertEqual(
            [x["cyclic_orbit_count"] for x in reduction["by_r"]],
            [6, 43, 80, 43, 6, 1],
        )
        for row in reduction["by_r"]:
            self.assertEqual(
                sum(item["coefficient"] for item in row["representatives"]),
                int(row["cyclic_weight_sum"]),
            )

    def test_boundary_formula_is_cyclically_invariant_for_every_even_word(self):
        from computational.h12_boundary_diagonal_contraction import rotations

        points, sigma, data = make_block_data()
        for r in range(2, POWER + 1, 2):
            for word in compositions(POWER, r):
                expected = diagonal_boundary_word(word, points, sigma, data)
                for rotated in rotations(word):
                    self.assertEqual(
                        diagonal_boundary_word(rotated, points, sigma, data),
                        expected,
                        msg=f"cyclic boundary value changed for {word} -> {rotated}",
                    )

    def test_no_offdiagonal_corner_data_is_needed_after_pairing(self):
        after = self.payload["after_pairing_reduction"]
        self.assertEqual(after["odd_r_compositions_vanish"], 1024)
        self.assertEqual(after["even_r_compositions_reduce_to_boundary_products"], 1024)
        self.assertEqual(after["genuine_off_diagonal_corner_terms_required"], 0)


if __name__ == "__main__":
    unittest.main()
