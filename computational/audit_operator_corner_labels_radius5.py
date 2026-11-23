#!/usr/bin/env python3
"""Finite strict operator-label audit for rooted radius-five corner balls.

This reuses the repository's independent graph recursion and compares all three
outer corners separately against their own level-three reference. It labels
nodes by root/distance/full graph degree and directed edges by face-axis class
and the vertex-order sign that selects U versus U^H. The result is finite
reproducibility evidence; the all-level induction is stated separately in the
H12 boundary-contraction report.
"""
from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path


LEVELS = tuple(range(3, 11))
CORNERS = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
RADIUS = 5


def graph(level: int):
    """Rebuild the deterministic gasket graph using only the standard library."""
    vertices = [(0.0, 0.0), (1.0, 0.0), (0.0, 1.0)]
    edges = [(0, 1), (1, 2), (0, 2)]
    faces = None
    for _ in range(level):
        offsets = ((0.0, 0.0), (0.5, 0.0), (0.0, 0.5))
        new_vertices = []
        index = {}
        new_edges = set()
        maps = []
        for ox, oy in offsets:
            mapping = {}
            for i, (x, y) in enumerate(vertices):
                point = (round(x * 0.5 + ox, 10), round(y * 0.5 + oy, 10))
                if point not in index:
                    index[point] = len(new_vertices)
                    new_vertices.append(point)
                mapping[i] = index[point]
            maps.append(mapping)
        new_faces = []
        for mapping in maps:
            for a, b in edges:
                new_edges.add(tuple(sorted((mapping[a], mapping[b]))))
            if faces is None:
                new_faces.append((mapping[0], mapping[1], mapping[2]))
            else:
                new_faces.extend(tuple(mapping[v] for v in face) for face in faces)
        vertices, edges, faces = new_vertices, list(new_edges), new_faces
    return vertices, edges, faces


def operator_ball(
    level: int, corner: tuple[float, float], commuting: bool
) -> tuple[dict[int, tuple], dict[tuple[int, int], tuple[int, int]]]:
    vertices, edges, faces = graph(level)
    lookup = {xy: i for i, xy in enumerate(vertices)}
    root = lookup[corner]
    adjacency = [set() for _ in vertices]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)

    distances = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        if distances[v] >= RADIUS:
            continue
        for w in adjacency[v]:
            if w not in distances:
                distances[w] = distances[v] + 1
                queue.append(w)

    axes: dict[tuple[int, int], int] = {}
    for k, (a, b, _c) in enumerate(faces):
        axes[tuple(sorted((a, b)))] = 2 if commuting else k % 3

    node_labels = {
        v: (v == root, len(adjacency[v]), distance)
        for v, distance in distances.items()
    }
    edge_labels: dict[tuple[int, int], tuple[int, int]] = {}
    for a, b in edges:
        if a not in distances or b not in distances:
            continue
        axis = axes.get(tuple(sorted((a, b))), -1)
        sign_ab = 1 if a < b else -1
        edge_labels[(a, b)] = (axis, sign_ab)
        edge_labels[(b, a)] = (axis, -sign_ab)
    return node_labels, edge_labels


def labelled_digraph_isomorphic(
    left: tuple[dict[int, tuple], dict[tuple[int, int], tuple[int, int]]],
    right: tuple[dict[int, tuple], dict[tuple[int, int], tuple[int, int]]],
) -> bool:
    """Exact small-graph isomorphism, preserving every node and directed-edge label."""
    left_nodes, left_edges = left
    right_nodes, right_edges = right
    if len(left_nodes) != len(right_nodes) or len(left_edges) != len(right_edges):
        return False

    def color_ids(signatures_by_graph):
        unique = sorted({sig for signatures in signatures_by_graph for sig in signatures.values()}, key=repr)
        ids = {sig: i for i, sig in enumerate(unique)}
        return [{node: ids[sig] for node, sig in signatures.items()} for signatures in signatures_by_graph]

    colors_left, colors_right = color_ids((left_nodes, right_nodes))
    for _ in range(len(left_nodes) + 1):
        def refine(nodes, edges, colors):
            outgoing = {node: [] for node in nodes}
            incoming = {node: [] for node in nodes}
            for (a, b), (axis, sign) in edges.items():
                outgoing[a].append((axis, sign, colors[b]))
                incoming[b].append((axis, sign, colors[a]))
            return {
                node: (
                    nodes[node],
                    tuple(sorted(outgoing[node])),
                    tuple(sorted(incoming[node])),
                )
                for node in nodes
            }
        sig_left = refine(left_nodes, left_edges, colors_left)
        sig_right = refine(right_nodes, right_edges, colors_right)
        next_left, next_right = color_ids((sig_left, sig_right))
        if next_left == colors_left and next_right == colors_right:
            break
        colors_left, colors_right = next_left, next_right

    classes_left = {}
    classes_right = {}
    for node, color in colors_left.items():
        classes_left.setdefault(color, []).append(node)
    for node, color in colors_right.items():
        classes_right.setdefault(color, []).append(node)
    if {c: len(v) for c, v in classes_left.items()} != {c: len(v) for c, v in classes_right.items()}:
        return False

    mapping: dict[int, int] = {}

    def compatible(a: int, b: int) -> bool:
        if colors_left[a] != colors_right[b] or left_nodes[a] != right_nodes[b]:
            return False
        for old_a, old_b in mapping.items():
            if left_edges.get((a, old_a)) != right_edges.get((b, old_b)):
                return False
            if left_edges.get((old_a, a)) != right_edges.get((old_b, b)):
                return False
        return True

    def search() -> bool:
        if len(mapping) == len(left_nodes):
            return True
        best_a = None
        best_candidates = None
        for a in left_nodes:
            if a in mapping:
                continue
            candidates = [
                b for b in classes_right[colors_left[a]]
                if b not in mapping.values() and compatible(a, b)
            ]
            if not candidates:
                return False
            if best_candidates is None or len(candidates) < len(best_candidates):
                best_a, best_candidates = a, candidates
                if len(candidates) == 1:
                    break
        for b in best_candidates:
            mapping[best_a] = b
            if search():
                return True
            del mapping[best_a]
        return False

    return search()

def build_audit() -> dict:
    report = {
        "status": "finite exact strict directed operator-label audit; not an all-level proof",
        "radius": RADIUS,
        "levels": list(LEVELS),
        "corners": [list(c) for c in CORNERS],
        "models": {},
        "checks": {},
        "expected_reference_ball": {
            "vertices": 19,
            "directed_edges": 66,
        },
        "labels": [
            "root identity",
            "distance from root",
            "full-graph vertex degree (onsite coefficient)",
            "face-index Pauli-axis class modulo 3 (or constant Z control)",
            "directed vertex-order sign selecting U versus U^H",
        ],
        "interpretation": (
            "Every tested radius-five ball matches its own level-three reference. "
            "This is finite exact graph-label evidence; the recursive induction in "
            "H12_BOUNDARY_DIAGONAL_CONTRACTION_2026-11-23.md supplies the universal argument."
        ),
    }

    for commuting, model in ((False, "noncommuting_SU2"), (True, "commuting_control")):
        model_data = {}
        all_match = True
        for corner_index, corner in enumerate(CORNERS):
            reference = operator_ball(LEVELS[0], corner, commuting)
            per_level = {}
            for level in LEVELS:
                candidate = operator_ball(level, corner, commuting)
                same = labelled_digraph_isomorphic(reference, candidate)
                per_level[str(level)] = {
                    "isomorphic_to_same_corner_at_level_3": same,
                    "vertices_in_ball": len(candidate[0]),
                    "directed_edges_in_induced_ball": len(candidate[1]),
                }
                all_match = all_match and same
                if len(candidate[0]) != 19 or len(candidate[1]) != 66:
                    all_match = False
            model_data[str(corner_index)] = {
                "corner": list(corner),
                "levels": per_level,
            }
        report["models"][model] = model_data
        report["checks"][f"{model}_all_corners_levels_3_to_10_match"] = all_match

    if not all(report["checks"].values()):
        raise AssertionError("radius-five directed operator-label audit failed")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", default="computational/data/h12_operator_corner_label_radius5_audit.json"
    )
    args = parser.parse_args()
    payload = build_audit()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload["checks"], indent=2))
    print("Wrote", output)


if __name__ == "__main__":
    main()
