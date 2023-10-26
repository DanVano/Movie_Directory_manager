        ### Scan library. Check if in folder or not.
        ### If in folder
        ### Check inside folder for movie file and subtitles

        ### If not in folder
            ### Make a folder in current directory with the name of the movie and place the file inside.

        ### Place the movie folder in based alphabetically for easier search. A-D E-H
        ### Perhaps T in it's own folder.

        ### If A to D folder exists place file inside.
        ### Else creat folder then move file over

import os
import shutil

Movies_Dirs = ('C:\\Users\\vanov\\PythonPrograms\\Movies_Files\\films')
Movie_type = ('.avi', '.mp4', '.mkv')
subtitles = ('.srt')

print('Movie file program begins')
print('The acceptable Movie file types are .avi, .mp4, and .mkv')
print('The acceptable Subtiles file type is .srt')
print('')
print('')
print('-------------------------------------------------------')

for root, dirs, files in os.walk(Movies_Dirs):
    print('')
    print('Inside Folder(s):', root.lstrip('C:\\Users\\vanov\\PythonPrograms\\Movies_Files'))
    files.sort(key=lambda f: os.path.splitext(f)[1])
    files_ext = [ext[-4:] for ext in files]
    if root == Movies_Dirs:
        for file in files:
            print('')
            print('File found:', file)
            if file.endswith(Movie_type):
                print('Movie in main folder and needs to be moved.')
    elif root != Movies_Dirs and dirs == []:
        print('')
        print('File(s) found: ', end="")
        print(*files, sep=", ")
        if any(Target_file in files_ext for Target_file in Movie_type) and subtitles in files_ext:
            print('Movie file exists with subtitles in the folder.')
        elif any(xTarget_file in files_ext for Target_file in Movie_type) and not subtitles in files_ext:
            print('Movie in folder with no subtitles.')
        elif subtitles in files_ext and not any(Target_file in files_ext for Target_file in Movie_type):
            print('Subtitles found without a Movie file.')
        else:
            print('No Movie file or Subtitles found.')    
    elif root != Movies_Dirs and dirs != []:
        print('')
        print('File(s) found: ', end="")
        print(*files, sep=", ")
        if any(Target_file in files_ext for Target_file in Movie_type) and subtitles in files_ext:
            print('Movie file exists with subtitles in the folder.')
            print('Another subs folder named', dirs, 'was found. Please delete.')
            dirs[:] = []
        if any(Target_file in files_ext for Target_file in Movie_type) and not subtitles in files_ext:
            files = os.listdir(root + '\\' + dirs[0])
            if subtitles in [x[-4:] for x in files]:
                print('Subtitles found within a seperate folder:', files)
                dirs[:] = []
            else:
                print('No subs found.')
                dirs[:] = []
    print('')
    print('-------------------------------------------------------')
print('')
print('End of program')

#NMFp = root + '\\' + file[:-4]
#MFilep = NMFp + '\\' + file
#os.mkdir(NMFp)
#shutil.move(NMFp, MFilep