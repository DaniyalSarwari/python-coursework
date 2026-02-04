"""
Docstring for projects.bulk_file_renamer

    The goal of this project is to build a Bulk File Renamer application that allows users to rename multiple files at once based on a defined naming pattern. \
    The program should enable users to select a directory, place files in it and automatically rename all files using rules such as adding a prefix or suffix, numbering files sequentially.
    Location: ./Files  (Files folder in a current working directory)
"""
import os
from pathlib import Path

def bulk_renamer(location: Path, prefix: str) -> int:
    total: int = 0
    files_list: list[str] = os.listdir(location)
    # print(files_list)
    for file in files_list:
        new_file_name: str
        file_item: list = file.split(sep='.')
        file_item[0] = prefix + str(total)
        new_file_name = '.'.join(file_item)

        source_path: Path = location/file
        # print(source_path)
        dest_path: Path = location/new_file_name
        # print(dest_path)

        source_path.rename(dest_path)
        total += 1
    
    return total
        

def main():
    print("===BULK FILE RENAMER===",end='\n\n')

    current: Path = Path.cwd()
    location: Path = Path(current)/"Files"  # create a folder with name "Files" for files to be placed in it
    location.mkdir(exist_ok=True)

    status: str = '' 
    while status != "done":
        status: str = input(f"Please place your all files at ( {location} ) and write 'done': ").lower()

    input_word: str = input("Please Enter prefix word: ")

    if status == "done":
        count: int = bulk_renamer(location, input_word)
        print(f"Total {count} file renamed successfully")
    

if __name__ == "__main__":
    main()