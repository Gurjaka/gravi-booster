# Gravi-Booster

## Overview

Gravi-Booster is a simulation tool that models the trajectory of a sphere under the influence of gravity and air drag. The simulation takes into account various materials, allowing users to see how different densities affect the motion of the sphere as it falls from a specified height.

## Features

- Simulates the fall of a sphere with adjustable mass and material density.
- Calculates the effects of drag based on the sphere's speed and cross-sectional area.
- Visualizes the trajectory of the sphere with time stamps at one-second intervals.
- Supports various materials such as rubber, steel, and copper, or allows users to input custom densities.

## Getting Started

### Prerequisites

- Python 3.x
- Required libraries:
  - `numpy`
  - `matplotlib`

You can install the required libraries using pip:

```bash
pip install numpy matplotlib
```

Or activate nix development shell:
```bash
nix-shell
```

## How to Use
1) Clone the repository:

```bash
git clone https://github.com/Gurjaka/gravi-booster.git
cd gravi-booster
```

2) Run the simulation:

```bash
python main.py
```

3) Follow the prompts to input the material of the sphere, its mass, the plane's speed, wind speed, and the initial height above the ground.

4) After the simulation runs, a plot will be displayed showing the trajectory of the sphere.