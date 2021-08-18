import os
import glob
import json
import tqdm
import shutil
import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
from soyclustering import SphericalKMeans
from soyclustering import visualize_pairwise_distance
from soyclustering import merge_close_clusters
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
    repr_spars = sparse.csr_matrix(repr_array)

    s_kmeans =  SphericalKMeans(
        n_clusters=1000,
        max_iter=100,
        verbose=1,
        init="similar_cut",
        sparsity="minimum_df",
        minimum_df_factor=0.05
    )

    labels = s_kmeans.fit_predict(repr_spars)

    pca_2d = PCA(n_components=2)

    repr_2d_pjt = pca_2d.fit_transform(repr_array)

    plt.scatter(repr_2d_pjt[:,0], repr_2d_pjt[:,1], c=labels/1000, alpha=0.5)
    plt.show()
    plt.savefig(os.path.join(plot_dir, "skmeans_pca_scatter.png"), dpi=300)

    with open(os.path.join(repr_dir, "repr_clustered.npy"), "wb") as file_out:
        np.save(file_out, labels)

    try:
        labels
    except NameError:
        labels = np.load(os.path.join(repr_dir, "repr_clustered.npy"))

    plt1.hist(labels, bins=1000)
    plt1.show()
    plt1.savefig(os.path.join(plot_dir, "skmeans_histogram.png"), dpi=300)

    sort_dir = os.path.join(result_dir, "sorted")
    if not os.path.exists(sort_dir):
        os.mkdir(sort_dir)

    images_filtered = glob.glob(os.path.join(dump_dir, "*.png"))

    for idx, fil in enumerate(tqdm.tqdm(images_filtered)):
        targ_dir = os.path.join(sort_dir, f"{labels[idx]}")
        if not os.path.exists(targ_dir):
            os.mkdir(targ_dir)
        
        shutil.copy(fil, targ_dir)

    print("Sort Complete!")
    