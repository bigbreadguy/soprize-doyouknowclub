import os
import glob
import json
import tqdm
import shutil
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

if __name__ == "__main__":
    cwd = os.getcwd()
    result_dir = os.path.join(cwd, "result")
    repr_dir = os.path.join(result_dir, "represent")
    anlz_dir = os.path.join(result_dir, "analyzed")
    dump_dir = os.path.join(result_dir, ".dump")
    info_dir = os.path.join(result_dir, "video_url")
    plot_dir = os.path.join(result_dir, "figures")
    if not os.path.exists(plot_dir):
        os.mkdir(plot_dir)
    
    repr_array = np.load(os.path.join(repr_dir, "representation.npy"))
    print("Representational Array Loaded!")

    dbscan = DBSCAN(min_samples = 1000)

    labels = dbscan.fit_predict(repr_array)

    plt.hist(labels, bins=1000)
    #plt.show()
    plt.savefig(os.path.join(plot_dir, "dbscan_histogram.png"), dpi=300)

    print("Done")