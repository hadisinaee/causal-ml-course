import pandas as pd 
from os import path
import networkx as nx
from graphical_model_learning import pcalg, gsp
from graphical_models.rand import directed_erdos, rand_weights
from conditional_independence import MemoizedCI_Tester
from conditional_independence import partial_correlation_suffstat, partial_correlation_test
import numpy as np
import matplotlib.pyplot as plt
import ges
import pandas as pd

def get_data():
    dir_path = "./"

    all_files = [path.join(dir_path, f) for f in ["fennel_output.csv"]]

    # make sure they exists
    assert all([path.exists(f) for f in all_files]), "some files are missing"

    # read them into pd 
    fennel_df = [pd.read_csv(f) for f in all_files][0]

    # remove spaces from column names
    fennel_df.columns = [c.strip() for c in fennel_df.columns]

    print("length of fennel: {0}".format(len(fennel_df)))

    columns = ["num_parts", "num_vertices", "num_edges", "part_time", "comm_vol", "edge_cut"]
    print("selecting only these columns: {0}".format(columns))

    # get the columns we want
    fennel_df = fennel_df[columns]

    print("num_rows: fennel={0}".format(len(fennel_df)))
    print(fennel_df.head(n=2))

    return fennel_df


def run_ges(data_np, names, title):
    # normalize data
    data_np = (data_np - data_np.mean(axis=0)) / data_np.std(axis=0)

    # number of nodes
    nnodes = 6 

    suffstat = partial_correlation_suffstat(data_np)
    ci_tester = MemoizedCI_Tester(partial_correlation_test, suffstat, alpha=0.01)

    # PC
    estimated_graph_pc = pcalg(set(range(nnodes)), ci_tester).to_amat()[0]
    estimated_graph_pc_nx = nx.from_numpy_matrix(estimated_graph_pc, create_using=nx.DiGraph)
    
    # GSP
    estimated_graph_gsp = gsp(set(range(nnodes)), ci_tester).to_amat()[0]
    estimated_graph_gsp_nx = nx.from_numpy_matrix(estimated_graph_gsp, create_using=nx.DiGraph)

    # GES
    estimated_graph_ges, score = ges.fit_bic(data_np)
    estimated_graph_ges_nx = nx.from_numpy_matrix(estimated_graph_ges, create_using=nx.DiGraph)

    fig, axes = plt.subplots(1, 3, figsize=(55, 10))
    fig.suptitle(title, fontsize=20)

    titles = ["PC Output", "GSP Output", "GES Output"]
    dic_name = {i: names[i] for i in range(len(names))}
    node_labels = { i: dic_name[i] for i in range(len(dic_name))}
    i = 0
    for ax, graph in zip(axes, [estimated_graph_pc_nx, estimated_graph_ges_nx, estimated_graph_gsp_nx]):
        pos = nx.shell_layout(graph)
        nx.draw(graph, ax=ax, with_labels=True, node_size=12000, node_color="tab:blue", pos=pos, font_size=16, labels=node_labels,  width=4, edge_color="grey",arrowsize=30, font_color="white")
        ax.grid(False)
        ax.margins(0.3)           
        ax.set_title(titles[i%3], fontsize=20)
        i += 1

    plt.show()

fennel_df = get_data()

print("number of columns: {0}".format(len(fennel_df.columns)))
fennel_np = fennel_df.to_numpy()

print("fennel_np[:2]: {0}".format(fennel_np[:2]))
run_ges(fennel_np, names=fennel_df.columns, title="Fennel")