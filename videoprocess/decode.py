import os

# judge whether the file is a video
def is_vide(file_name):
    all_suffix = (".avi",".mov")
    suffix = os.path.splitext(file_name)[1]
    if suffix in all_suffix:
        return True
    else:
        return False


