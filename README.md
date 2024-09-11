# Visualizing Conway's Game of Life using Matplot and Numpy

This project simulates Conway's Game of Life using Python. It includes a variety of predefined patterns, visualizes their evolution, and allows interaction with the simulation through `matplotlib`.

## Project Structure

- `patterns.toml`: Contains predefined patterns for Conway's Game of Life.
- `grid.py`: Defines the `LifeGrid` class, which handles the evolution and visualization of patterns.
- `patterns.py`: Provides functionality to load patterns from the `patterns.toml` file.
- `main.py`: Contains the main code to run the simulation and visualize the patterns.

## Patterns

The following patterns are included:

- **Blinker**: A simple oscillator with a period of 2.
- **Toad**: An oscillator with a period of 2.
- **Beacon**: A still life pattern that forms a 2x2 block with a smaller block in the corner.
- **Pulsar**: A large oscillator with a period of 3.
- **Penta Decathlon**: An oscillator with a period of 10.
- **Glider**: A small pattern that moves diagonally.
- **Glider Gun**: A complex pattern that generates gliders.
- **Bunnies**: A random pattern for experimentation.

## Installation

Ensure you have Python 3.11+ installed. Install the required libraries using pip:

```bash
pip install numpy matplotlib 
