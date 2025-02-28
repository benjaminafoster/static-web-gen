import os
import shutil
from textnode import TextNode, TextType
from copystatic import copy_to_public
from generate_page import generate_pages_recursive


def main():
    copy_to_public()
    generate_pages_recursive("content/", "template.html", "public/")
    return 0

main()