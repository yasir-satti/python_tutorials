import brief
import os


def getDirectoryContents(path):
    directoryListing = os.listdir(path)
    return directoryListing


def getFilesListing(path, list):
    filesList = [file for file in list if os.path.isfile(path + '/' + file)]
    return filesList


def getDirectoriesListing(path, list):
    directoryList = [directory for directory in list if os.path.isdir(path)]
    return directoryList


# prompt user for directory path
directoryPath = input(r'Enter the directory path: ')


# get directory listing from path
directoryListing = getDirectoryContents(directoryPath)
# print(f'Contents in the directory {directoryPath}: {directoryListing}')
for item in directoryListing:
    if os.path.isfile(directoryPath + '/' + item):
        print(f'{directoryPath}/{item} is file ')
    elif os.path.isdir(directoryPath + '/' + item):
        print(f'{directoryPath}/{item} is directory ')
    else:
        print('unknown')



# # get files listing from path
# files = getFilesListing(directoryPath, directoryListing)
# print(f'Files in {directoryPath}: ')


# # get directories listing from path
# directories = getDirectoriesListing(directoryPath, directoryListing)
# print(f'Directories in {directoryPath}: {directories}')


# for (root, dirs, files) in os.walk('./03_intermmediate', topdown=True):
#     # print(root)
#     # print('----------------------------------------------------')
#     # print(dirs)
#     # print('----------------------------------------------------')
#     print(files)