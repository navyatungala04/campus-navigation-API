import json
import os
from graph import shortest_path

_DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "campus_map.json")

with open(_DATA_FILE) as f:
    campus_graph = json.load(f)


def get_route(start, destination):

    result = shortest_path(
        campus_graph,
        start,
        destination
    )

    return result