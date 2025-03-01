import os
import shutil
import sys
from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_files_recursive
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
    return 0

main()