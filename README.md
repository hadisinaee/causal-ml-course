# Requirements
- You need to have `python3` and virtual environment module to run this.
- R libraries required by [Causal Discovery Toolbox][cdt]

# Available Data
There are two `tar.gz` files in this repository. These are the results of our synthetic runs on data. 
1- ./results_20perc_n15.tar.gz : all the results for the sparse experiment where we have 15 nodes and 5 trials
2- ./results_70perc_n15.tar.gz : all the results for the dense experiment where we have 15 nodes and 5 trials

# Steps To Install and Use the Runs
```bash
python3 -m venv venv
pip install -r requirements.txt 
```

# Graph Partitioning Data 

There is a file name `partitioning_data.py` which includes the code for running our test on the graph partitioning case. This file loads the all required data that is inside graph_partitioning.csv file. To run this experiment, simply run `python3 partitioning_data.py`.


[cdt]: https://fentechsolutions.github.io/CausalDiscoveryToolbox/html/index.html
