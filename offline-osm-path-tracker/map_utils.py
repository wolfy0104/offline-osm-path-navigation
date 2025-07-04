import osmnx as ox
import os

def load_osm_from_pbf(pbf_path):
    if not os.path.exists(pbf_path):
        raise FileNotFoundError(f"OSM file not found at: {pbf_path}")
    print(f"Loading OSM map from: {pbf_path}")
    return ox.graph_from_file(pbf_path, network_type="walk")

def get_map_bounds(graph):
    bounds = ox.utils_geo.graph_to_gdfs(graph, nodes=False).total_bounds
    return bounds
