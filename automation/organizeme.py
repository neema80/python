import os
from pathlib import Path
# in this file we are making code to creat subfolders based on file types including python scripts
SUBDIRECTORIES = {
    "DOCUMENTS" : ['.pdf','.rtf','.txt'],
    "SCRIPTS" : ['.sh'],
    "AUDIO" : ['.m4a','.m4b','.mp3','.aac'],
    "VIDEOS" : ['.mov','.mp4','.avi'],
    "IMAGES" : ['.jpeg','jpg','.png']
}
# now we make a function to return a category based on file suffix
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return "MISC" # if couldnt find the type in the dictionary
def organizeDirectory():
    for items in os.scandir():
        # cautionary measure, if the it is directory then skip
        if items.is_dir():
            continue
        filepath = Path(items)
        filetype = filepath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # this line allows us to move the file to the directory
        filepath.rename(directoryPath.joinpath(filepath))

organizeDirectory()