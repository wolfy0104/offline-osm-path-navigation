# Offline OSM Path Tracker

This project loads an OpenStreetMap .osm.pbf file and simulates 2D path tracking over it using matplotlib.

## Features

- Loads OSM maps from .osm.pbf files
- Fully offline usage
- Live simulation of 2D odometry-style path
- Easy to extend for GPS or visual odometry input

## Requirements

```
pip install osmnx matplotlib numpy
```

## Folder Structure

offline-osm-path-tracker/
├── main.py  
├── map_utils.py  
├── path_drawer.py  
├── README.md  
└── maps/ (put your .osm.pbf file here)

## Usage

Download a map file from https://download.geofabrik.de/  
Example: maps/mumbai.osm.pbf

Then run:

```
python main.py maps/mumbai.osm.pbf
```
