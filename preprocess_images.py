import os
import glob
import json
import shutil
import tqdm
import numpy as np
from deepface import DeepFace

if __name__ == "__main__":
    cwd = os.getcwd()
    result_dir = os.path.join(cwd, "result")
    load_dir = os.path.join(result_dir, "face_crop")
    save_dir = os.path.join(result_dir, "analyzed")
    dump_dir = os.path.join(result_dir, ".dump")

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    if not os.path.exists(dump_dir):
        os.mkdir(dump_dir)
    
    images_unfiltered = glob.glob(os.path.join(load_dir, "*.png"))

    print("Filtering Images not Including Face Instance")
    for unf in tqdm.tqdm(images_unfiltered):
        try:
            detected = DeepFace.detectFace(unf, detector_backend = "dlib")
            shutil.copy(unf, dump_dir)
        except:
            base = os.path.basename(unf)
            print(f"\nGiven Image does not Include Face Instance, ({base})")

    images_filtered = glob.glob(os.path.join(dump_dir, "*.png"))

    repr_dir = os.path.join(result_dir, "represent")
    if not os.path.exists(repr_dir):
        os.mkdir(repr_dir)

    print("Generate Representational Vectors for each Image")
    rep_list2d = []
    for fil in tqdm.tqdm(images_filtered):
        embedded = DeepFace.represent(fil, detector_backend = "dlib")
        rep_list2d.append(embedded)
    
    rep_array = np.asarray(rep_list2d)

    with open(os.path.join(repr_dir, "representation.npy"), "wb") as file_out:
        np.save(file_out, rep_array)
    print("Representational Array for the Dataset has been Saved!")

    print("Analyze Filtered Images using DeepFace")
    res_dict = {}
    for fil in tqdm.tqdm(images_filtered):
        key = os.path.basename(fil).split(".")[0]
        resp_obj = DeepFace.represent(fil, detector_backend = "dlib")
        res_dict[key] = resp_obj

    with open(os.path.join(save_dir, "analysis_result.json"), "w", encoding = "UTF-8-SIG") as file_out:
        json.dump(res_dict, file_out, ensure_ascii=False)
        print("\nAnalysis Result Saved!")
