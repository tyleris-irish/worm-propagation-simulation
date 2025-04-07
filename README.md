# Worm Propagation Simulation

This project simulates the propagation of computer worms, specifically the Code Red and Code Red II worms, across a network of IP addresses. The simulation tracks the infection process over time and generates reports in CSV format.

## Features

- Simulates the spread of the Code Red and Code Red II worms.
- Tracks the number of infected machines at each time tick.
- Generates CSV reports for infection counts and elapsed times.
- Supports multiple runs for statistical analysis.

## Project Structure

```
.
├── worm_simulation.py       # Main simulation script
└── README.md                # Project documentation
```

## How It Works

1. **Initialization**: The network is initialized with a range of IP addresses. Some IPs are marked as vulnerable, and one IP is initially infected.
2. **Simulation**: The worm scans the network and infects vulnerable machines. The infection process is repeated until all vulnerable machines are infected.
3. **Reporting**: The simulation generates CSV files with infection counts over time and elapsed times for each simulation.

## Usage

### Prerequisites

- Python 3.x

### Running the Simulation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd worm-propagation-simulation
   ```

2. Run the simulation:
   ```bash
   python worm_simulation.py
   ```

3. View the generated CSV files for infection data and elapsed times.

### Output Files

- **`code_red_X.csv`**: Infection data for Code Red simulations (X = 1, 2, 3).
- **`code_red_II_X.csv`**: Infection data for Code Red II simulations (X = 1, 2, 3).
- **`elapsed_times.csv`**: Elapsed times and total ticks for all simulations.

## Customization

- Modify `IP_RANGE` and `SCAN_RATE` in `worm_simulation.py` to adjust the network size and scanning rate.
- Add visualization tools (e.g., matplotlib) to generate graphs of infection rates.

## Acknowledgments

- Inspired by studies on malware propagation and network security.
- Code Red and Code Red II worms are real-world examples of network-based malware.
