import os
import time 

def create_folder(folder, path_to_folder):
    new_folder = os.path.join(path_to_folder, folder)
    os.mkdir(new_folder)

def check_folders(folder_path):
    existing_files = []
    for child_folder in os.listdir(folder_path):
        child_folder_path = os.path.join(folder_path, child_folder)
        existing_files.extend(os.listdir(child_folder_path))
    return existing_files

def move_file(files_to_move, source_path, dest_path, categories, existing_files):

    for file in files_to_move:
        file_src_path = os.path.join(source_path, file)
        file_extension = os.path.splitext(file)[1]

        for category, extension in categories.items():
            if file_extension in extension:
                category_dir = os.path.join(dest_path, category)
                file_dest_path = os.path.join(category_dir, file)
                os.rename(file_src_path, file_dest_path)
                files_to_move.remove(file)
    
    files_left = files_to_move
    
    for file in files_left:
        if file not in existing_files and file != 'Sorted Files':
            category_dir = os.path.join(dest_path, 'Others')
            file_dest_path = os.path.join(category_dir, file)
            os.rename(file_src_path, file_dest_path)
            files_left.remove(file)


def main():
    source_path = "C:\\Users\\illia\\Downloads"
    dest_path = "C:\\Users\\illia\\Downloads\\Sorted Files"

    categories = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.raw', '.ico'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.html'],
        'Videos': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp', '.mpg', '.mpeg', '.m2v'],
        'Compressed' : ['.7z','.bz2','.binhex','.cab','.gz','.gzip','.hqx','.img','.iso','.lha','.lzh','.mime','.rar','.tarbz','.targz','.tar','.taz','.tbz','.tgz','.tz','.uue','.vhd','.vmdk','.xz','.z','.zip','.zipx'],
        'Others': []
    }

    existing_files = check_folders(dest_path)
    files_in_source = os.listdir(source_path)
    files_to_move = []

    if not files_in_source:
        print('There are no files to move in the defined source directory.')
        return
    
    for folder_to_create in categories.keys():
        if folder_to_create not in os.listdir(dest_path):
            create_folder(folder_to_create, dest_path)
            print(f"Folder {folder_to_create} created.")
        else:
            break

    print(20*"-")
    time.sleep(1)
    num_of_files_to_move = len(os.listdir(source_path))
    print(f"Moving {num_of_files_to_move} files...")
    time.sleep(1)
    i = 0
    for file in files_in_source:
        if file not in existing_files:
            files_to_move.append(file)
            move_file(files_to_move, source_path, dest_path, categories, existing_files)
            i += 1
        else:
            print(f"File '{file}' already exists in target directory.")
    time.sleep(1)      
    print(f"Moved ({i}/{num_of_files_to_move}) file(s) to {dest_path}")

if __name__ == "__main__":
    main()