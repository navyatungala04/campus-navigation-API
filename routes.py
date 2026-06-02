import json
from graph import shortest_path

with open("data/campus_map.json") as f:
    campus_graph = json.load(f)


def get_route(start, destination):

    result = shortest_path(
        campus_graph,
        start,
        destination
    )

    return result