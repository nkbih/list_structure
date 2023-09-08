import os
import sys

def list_directory(path, max_depth, current_depth=0):
    if current_depth > max_depth:
        return
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            print('  ' * current_depth + item)
            if os.path.isdir(full_path):
                list_directory(full_path, max_depth, current_depth + 1)
    except PermissionError:
        pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python script_name.py [путь_к_папке] [максимальная_глубина]")
        sys.exit(1)

    directory_path = sys.argv[1]
    depth = int(sys.argv[2])

    list_directory(directory_path, depth)