import os
import glob
import tqdm
import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

  cwd = os.getcwd()
  sort_dir = os.path.join(cwd, "result", "sorted")

  lighter_skin = [0, 5, 7, 9, 10, 11, 13, 15, 16, 21, 22, 23, 24, 25, 26, 28, 33, 34, 36, 37, 39, 41, 42, 43, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 60, 63, 66, 68, 71, 72, 73, 74, 75, 76, 77, 78, 82, 83, 86, 87, 88, 90, 91, 92, 93, 94, 97, 98, 99, 102]
  darker_skin = [14, 20, 32, 57, 58, 62, 67, 79, 80, 96, 106, 107]

  ls_array = np.zeros(0)
  for idx in tqdm.tqdm(lighter_skin):
      targ_dir = os.path.join(sort_dir, f"{idx}", "*.jpg")
      img_dirs = glob.glob(targ_dir)
      for img_dir in img_dirs:
          img = cv2.imread(img_dir)
          img_gscale = np.sum(img, axis=2)
          ls_array = np.append(ls_array, img_gscale.ravel())
   
  print(ls_array.shape)
  
  plt.hist(ls_array, density=True)
  plt.title("Brightness Spectrum for Lighter Skinned Faces")
  plt.show()
  
  ds_array = np.zeros(0)
  for idx in tqdm.tqdm(darker_skin):
      targ_dir = os.path.join(sort_dir, f"{idx}", "*.jpg")
      img_dirs = glob.glob(targ_dir)
      for img_dir in img_dirs:
          img = cv2.imread(img_dir)
          img_gscale = np.sum(img, axis=2)
          ds_array = np.append(ds_array, img_gscale.ravel())
          
  
  print(ds_array.shape)
  
  plt.hist(ds_array, density=True)
  plt.title("Brightness Spectrum for Darker Skinned Faces")
  plt.show()
