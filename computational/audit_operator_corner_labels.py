#!/usr/bin/env python3
"""Audit whether rooted corner graph balls preserve directed operator block types.

For each undirected edge {a,b}, independent_sparse_level7.operator stores
U = cos(theta/2) I - i sin(theta/2) P_axis at the (min(a,b),max(a,b)) block
and U* in the reverse block. Thus the directed block type includes both the
face-index Pauli axis and the sign induced by vertex-index ordering.

The test is deliberately diagnostic: if isomorphism fails, that means this
particular strict label is not preserved by a rooted graph isomorphism. It does
not rule out a gauge-equivalent operator isomorphism. Finite levels only.
"""
import argparse
import json
from collections import deque
from pathlib import Path

import networkx as nx

from independent_sparse_level7 import graph

LEVELS = (3, 4, 5, 6)
CORNERS = ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))
RADIUS = 4


def operator_ball(level, corner, commuting):
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

    axes = {}
    for k, (a, b, _c) in enumerate(faces):
        axes[tuple(sorted((a, b)))] = 2 if commuting else k % 3

    result = nx.DiGraph()
    for v, distance in distances.items():
        result.add_node(v, root=(v == root), degree=len(adjacency[v]), distance=distance)

    for a, b in edges:
        if a not in distances or b not in distances:
            continue
        axis = axes.get(tuple(sorted((a, b))), -1)
        # Sign of the imaginary Pauli term in H[a,b] for generic theta.
        sign_ab = 1 if a < b else -1
        result.add_edge(a, b, axis=axis, sign=sign_ab)
        result.add_edge(b, a, axis=axis, sign=-sign_ab)
    return result


def node_match(a, b):
    return a["root"] == b["root"] and a["degree"] == b["degree"] and a["distance"] == b["distance"]


def edge_match(a, b):
    return a["axis"] == b["axis"] and a["sign"] == b["sign"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/operator_corner_label_audit.json")
    args = parser.parse_args()
    result = {
        "status": "finite strict directed-block-label audit; diagnostic only",
        "radius": RADIUS,
        "levels": list(LEVELS),
        "corners": [list(c) for c in CORNERS],
        "models": {},
        "checks": {},
        "interpretation": "A false isomorphism check means the strict directed labels are not preserved; gauge-equivalent operator maps may still exist. A true check is finite evidence only.",
    }
    for commuting, model in ((False, "noncommuting_SU2"), (True, "commuting_control")):
        model_data = {}
        for ci, corner in enumerate(CORNERS):
            reference = operator_ball(LEVELS[0], corner, commuting)
            levels = {}
            for level in LEVELS:
                candidate = operator_ball(level, corner, commuting)
                levels[str(level)] = {
                    "isomorphic_to_level_3": nx.is_isomorphic(
                        reference, candidate, node_match=node_match, edge_match=edge_match
                    ),
                    "vertices_in_ball": candidate.number_of_nodes(),
                    "directed_edges_in_ball": candidate.number_of_edges(),
                }
            model_data[str(ci)] = {"corner": list(corner), "levels": levels}
        result["models"][model] = model_data
        result["checks"][f"{model}_all_corners_levels_3_to_6_match"] = all(
            result["models"][model][str(ci)]["levels"][str(level)]["isomorphic_to_level_3"]
            for ci in range(3) for level in LEVELS
        )
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["checks"], indent=2))
    print("Wrote", output)


if __name__ == "__main__":
    main()
