import os

"""
This module is used to divide video. After the process that video is decoded
into frames, we will judge the length of video. If the video is too large, we
have to segment it to make it easy for following processing. Notice that we
divide it in a overlap way.
"""


# segment frames according to fps
def segment_video(folder, video_fps):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    image_list = os.listdir(folder)
    frame_list = segment_list(image_list, video_fps * 30, video_fps * 2)
    return frame_list


def segment_list(long_list, seg_len, overlap):
    if len(long_list) < seg_len:
        return long_list
    else:
        if len(long_list)%seg_len == 0:
            dimension = len(long_list)/seg_len
        else:
            dimension = len(long_list) / seg_len + 1
        new_list = create_multi_list(dimension,seg_len)
        new_list[0][0:] = long_list[0:seg_len + overlap]
        new_list[dimension - 1][0:] = long_list[(dimension - 1) * seg_len - overlap :]
        for i in range(1, dimension - 1):
            new_list[i][0:] = long_list[i * seg_len - overlap : (i + 1) * seg_len + overlap]
        return new_list


def create_multi_list(dimension, length):
    new_list = [[0 for x in range(length)] for y in range(dimension)]
    return new_list
