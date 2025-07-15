



import os

def print_file_tree(start_path):
    for dirpath, dirnames, filenames in os.walk(start_path):
        level = dirpath.replace(start_path, '').count(os.sep)
        indent = '  ' * level
        print(f"{indent}- {os.path.basename(dirpath)}/")
        subindent = '  ' * (level + 1)
        for f in filenames:
            print(f"{subindent}- {f}")

print_file_tree(".")  # or "." if everything is in root