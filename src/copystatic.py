import os
import shutil

def copy_to_public():
    public_path = "public"
    static_path = "static"
    if os.path.exists(public_path): # fix this once testing is done
        shutil.rmtree(public_path)
    os.mkdir(public_path)
    child_files = []
    copy_to_public_r(static_path, child_files)

def copy_to_public_r(current_path, child_files):
    children = os.listdir(current_path)
    for child in children:
        child_path = os.path.join(current_path, child)
        is_file = os.path.isfile(child_path)
        if is_file:
            adjusted_path = child_path.split("static/")[1]
            #print(f"public/{child_path_list}")
            shutil.copy(child_path, f"public/{adjusted_path}")
        else:
            adjusted_path = child_path.split("static/")[1]
            if not os.path.exists(f"public/{adjusted_path}"):
                os.mkdir(f"public/{adjusted_path}")
            copy_to_public_r(child_path, child_files)