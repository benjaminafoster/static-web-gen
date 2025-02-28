import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip()
        else:
            raise Exception("no title in markdown")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    child_dirs = os.listdir(dir_path_content)
    for child in child_dirs:
        if os.path.isfile(f"content/{child}"):
            print(f"Generating a page from {dir_path_content} to {dest_dir_path} using {template_path}")
            md = open(f"{dir_path_content}{child}")
            temp = open(template_path)
            md_content = md.read()
            temp_content = temp.read()
            md.close()
            temp.close()
            md_to_html_node = markdown_to_html_node(md_content)
            html_string = md_to_html_node.to_html()
            page_title = extract_title(md_content)
            updated_content = temp_content.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)
            dest_dir_path = os.path.dirname(dest_dir_path)
            if os.path.exists(dest_dir_path):
                pass
            else:
                os.makedirs(dest_dir_path)
            out_file = open(f"{dest_dir_path}/index.html", 'w')
            out_file.write(updated_content)
            out_file.close()
        else:
            current_dir_path_content = f"{os.path.join(dir_path_content, child)}/"
            current_dest_path = f"{os.path.join(dest_dir_path,child)}/"
            generate_pages_recursive(current_dir_path_content, template_path, current_dest_path)
