import os
import glob
import json
    
if __name__ == "__main__":
    cwd = os.getcwd()
    down_dir = os.path.join(cwd, "downloads")
    result_dir = os.path.join(cwd, "result")
    info_dir = os.path.join(result_dir, "video_url")
    if not os.path.exists(info_dir):
        os.mkdir(info_dir)

    video_list = glob.glob(os.path.join(down_dir, '*.mp4'))
    
    idx_to_video = dict()
    for idx, video in enumerate(video_list):
        video_name = os.path.basename(video).split(".")[0]
        print(f"{idx} : {video_name}\n")
        idx_to_video[idx] = video_name
    
    with open(os.path.join(info_dir, "index_to_video.json"), 'w', encoding = "UTF-8-SIG") as file_out:
        json.dump(idx_to_video, file_out, ensure_ascii=False)