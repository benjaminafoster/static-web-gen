import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip()
        else:
            raise Exception("no title in markdown")
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}")
    md = open(from_path)
    temp = open(template_path)
    md_content = md.read()
    temp_content = temp.read()
    md.close()
    temp.close()
    md_to_html_node = markdown_to_html_node(md_content)
    html_string = md_to_html_node.to_html()
    page_title = extract_title(md_content)
    updated_content = temp_content.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)
    dest_dir_path = os.path.dirname(dest_path)
    if os.path.exists(dest_dir_path):
        pass
    else:
        os.makedirs(dest_dir_path)
    out_file = open(dest_path, 'w')
    out_file.write(updated_content)
    out_file.close()

#generate_page("content/index.md", "template.html", "public/index.html")
