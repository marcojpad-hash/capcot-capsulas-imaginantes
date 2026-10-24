#!/bin/sh
# Natural Earth (dominio público) para capas de mapa
mkdir -p assets/geo && curl -sfL -o assets/geo/ne_110m_land.geojson https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_land.geojson
