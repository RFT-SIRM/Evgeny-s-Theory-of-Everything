#!/usr/bin/env python3
"""Exact finite audit of rooted labelled corner neighbourhoods.

This checks graph isomorphism of radius-4 corner balls for levels 3..6.
Node labels preserve degree and root identity; edge labels reproduce the
SU(2)-label index used by independent_sparse_level7.operator (or the
commuting control label). This is finite evidence only, not an all-level proof.
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


def rooted_ball(level, corner, commuting):
    vertices, edges, faces = graph(level)
    index = {xy: i for i, xy in enumerate(vertices)}
    root = index[corner]
    adjacency = [set() for _ in vertices]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)

    distances = {root: 0}
    queue = deque([root])
    while queue:
        v = queue.popleft()
        if distances[v] == RADIUS:
            continue
        for w in adjacency[v]:
            if w not in distances:
                distances[w] = distances[v] + 1
                queue.append(w)

    # Match operator(): each face contributes a labelled edge (a,b);
    # later faces overwrite earlier labels for shared (a,b) edges.
    labels = {}
    for k, (a, b, _c) in enumerate(faces):
        labels[tuple(sorted((a, b)))] = 2 if commuting else k % 3

    result = nx.Graph()
    for v, distance in distances.items():
        result.add_node(
            v, root=(v == root), degree=len(adjacency[v]), distance=distance
        )
    for a, b in edges:
        if a in distances and b in distances:
            result.add_edge(
                a, b, label=labels.get(tuple(sorted((a, b))), -1)
            )
    return result


def node_match(a, b):
    return (
        a["root"] == b["root"]
        and a["degree"] == b["degree"]
        and a["distance"] == b["distance"]
    )


def edge_match(a, b):
    return a["label"] == b["label"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/corner_neighbourhood_audit.json")
    args = parser.parse_args()

    result = {
        "status": "finite exact labelled-graph isomorphism audit; not an all-level proof",
        "radius": RADIUS,
        "levels": list(LEVELS),
        "corners": [list(c) for c in CORNERS],
        "models": {},
        "checks": {},
    }
    for commuting, model in ((False, "noncommuting_SU2"), (True, "commuting_control")):
        model_result = {}
        all_match = True
        for corner_index, corner in enumerate(CORNERS):
            reference = rooted_ball(LEVELS[0], corner, commuting)
            per_level = {}
            for level in LEVELS:
                candidate = rooted_ball(level, corner, commuting)
                same = nx.is_isomorphic(
                    reference, candidate,
                    node_match=node_match, edge_match=edge_match
                )
                per_level[str(level)] = {
                    "isomorphic_to_level_3": same,
                    "vertices_in_radius_ball": candidate.number_of_nodes(),
                    "edges_in_induced_ball": candidate.number_of_edges(),
                }
                all_match = all_match and same
            model_result[str(corner_index)] = {
                "corner": list(corner),
                "levels": per_level,
            }
        result["models"][model] = model_result
        result["checks"][f"{model}_radius4_neighbourhoods_match_levels_3_to_6"] = all_match

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["checks"], indent=2))
    print("Wrote", output)
    if not all(result["checks"].values()):
        raise SystemExit("labelled corner-neighbourhood isomorphism check failed")


if __name__ == "__main__":
    main()
