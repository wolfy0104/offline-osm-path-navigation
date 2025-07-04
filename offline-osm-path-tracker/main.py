from map_utils import load_osm_from_pbf, get_map_bounds
from path_drawer import PathDrawer
import sys
import os

def main():
    if len(sys.argv) > 1:
        osm_path = sys.argv[1]
    else:
        osm_path = "maps/your-map.osm.pbf"

    if not os.path.exists(osm_path):
        print(f"OSM file not found: {osm_path}")
        return

    graph = load_osm_from_pbf(osm_path)
    bounds = get_map_bounds(graph)
    minx, miny, maxx, maxy = bounds
    start_center = [(minx + maxx) / 2, (miny + maxy) / 2]

    drawer = PathDrawer(bounds, start_center)
    drawer.start()

if __name__ == "__main__":
    main()
