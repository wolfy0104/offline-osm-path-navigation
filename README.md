Offline OSM Path Tracker

This project provides an offline system to visualize simulated 2D movement (such as odometry or GPS paths) over OpenStreetMap data. It uses a `.osm.pbf` file as the base map and overlays a real-time moving path line.

Overview

The program performs the following steps:

1. Loads an OpenStreetMap `.osm.pbf` file using `osmnx`
2. Extracts the map’s geographical boundaries (longitude/latitude)
3. Starts at the center of the map
4. Simulates a small movement at each time step
5. Draws a path line connecting each movement point on the map

This can be extended later for real GPS or visual odometry input.

#How it Works

Map Loading

The `.osm.pbf` file is parsed using `osmnx.graph_from_file()`. This constructs a walkable road network graph from the file and enables extraction of map bounds.

```python
graph = ox.graph_from_file("maps/mumbai.osm.pbf", network_type="walk")
```

Map Bounds

The spatial extent of the loaded map is obtained to define the visible plotting region:

```python
(minx, miny, maxx, maxy) = ox.utils_geo.graph_to_gdfs(graph, nodes=False).total_bounds
```

These represent:

* minx: minimum longitude
* miny: minimum latitude
* maxx: maximum longitude
* maxy: maximum latitude

The center point is calculated as:

```python
center_x = (minx + maxx) / 2
center_y = (miny + maxy) / 2
```

### Simulated Movement

At each frame, a small delta is applied to the current position:

```python
delta = np.random.uniform(-0.0001, 0.0001, size=2)
current_position += delta
```

Each new position is appended to a list representing the path.

Path Drawing

The path is drawn using `matplotlib`:

* A red line connects all previous positions
* A blue dot shows the current position
* The x-axis shows longitude, y-axis shows latitude

The axes limits are fixed to the map bounds to maintain scale.

Visualization

Live updates are handled using `matplotlib.animation.FuncAnimation`. The simulation updates every 500 milliseconds.

Requirements

This project requires the following Python libraries:

* osmnx
* matplotlib
* numpy

Install them using pip:

```bash
pip install osmnx matplotlib numpy
```

Directory Structure

```
offline-osm-path-tracker/
├── main.py
├── map_utils.py
├── path_drawer.py
├── README.md
└── maps/
    └── your-map.osm.pbf
```

How to Use

1. Download a `.osm.pbf` map file from:
   [https://download.geofabrik.de/](https://download.geofabrik.de/)

2. Place the file inside the `maps/` folder.

3. Run the program by providing the file path:

```bash
python main.py maps/your-map.osm.pbf
```

This will open a window showing the map area with a live simulation of movement as a red path.

Customization

You can replace the `simulate_move()` function inside `path_drawer.py` to use:

* GPS input
* SLAM/odometry data
* Manual keyboard control
* Pre-recorded path coordinates

The system is structured to be modular and extensible.

Notes

* The simulation assumes a small delta movement in geographic coordinates.
* No geographic projection is applied. It uses raw latitude and longitude values.
* This is suitable for small-scale tracking (e.g., pedestrian or indoor scale).

License

MIT License. See `LICENSE` file if added.
