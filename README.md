# causal-ml-course

This repository contains code and data for experimentation with causal machine learning techniques. It includes synthetic and real-world datasets as well as code for running experiments.

## Prerequisites

To use this repository, you will need:
- Python 3
- The virtual environment module for Python
- R libraries as required by the [Causal Discovery Toolbox][cdt]

## Available Data

There are two `tar.gz` files in this repository:
1. `results_20perc_n15.tar.gz`: This file contains the results of a sparse experiment with 15 nodes and 5 trials.
2. `results_70perc_n15.tar.gz`: This file contains the results of a dense experiment with 15 nodes and 5 trials.

## Installation and Usage

To set up the necessary packages and environment, follow these steps:

1. Create a virtual environment: 
```bash
python3 -m venv venv
pip install -r requirements.txt
```

You can then use `15_Nodes.ipynb` file to run all the experiments. This is a python notebook that includes all of our experiments. You can change the variables, such as number of node `nnode`, number of trials or many other variables.

## Graph Partitioning Data

The file partitioning_data.py contains code for running experiments on graph partitioning data. This file loads the required data from the `fennel_output.csv` file. To run this experiment, simply run: `python3 ./partitioning_data.py`

