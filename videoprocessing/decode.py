import os

# judge whether the file is a video
def is_vide(file_name):
    all_suffix = (".flv",".f4v",".f4p",".f4a",".f4b",".nsv"
                  ,".roq",".mxf",".3g2",".3gp",".svi",".m4v"
                  ,".mpg",".mpeg",".m2v",".mp2",".mpe",".mpv"
                  ,".mp4",".m4p",".amv",".asf",".rmvb",".rm"
                  ,".yuv",".wmv",".mov",".qt",".avi",".mng"
                  ,".gifv",".gif",".drv",".ogv",".ogg",".vob"
                  ,".flv",".webm",".mkv")
    suffix = os.path.splitext(file_name)[1]
    if suffix in all_suffix:
        return True
    else:
        return False

