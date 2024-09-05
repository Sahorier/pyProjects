import os
# print(os.getcwd())
# os.chdir("E:/")
# print(os.getcwd())
all_folders = []
folder_dict = {}
file_dict = {}
choice = input("What are you searching? input 1 for folder or 2 for files \n>> ")
if choice == "1":
    find_folder = input("Enter the name of folder that you are searching \n>> ")
    for dir_path, dir_names, filenames in (os.walk("C:/")):
        folder_dict[dir_path] = dir_names
        if find_folder in folder_dict[dir_path]:
            print(f"Folder found in {dir_path}!")
        # else:
        #     print("Folder not found! Please enter correct spelling")
    for dir_path, dir_names, filenames in (os.walk("D:/")):
        folder_dict[dir_path] = dir_names
        if find_folder in folder_dict[dir_path]:
            print(f"Folder found in {dir_path}!")

    
    for dir_path, dir_names, filenames in (os.walk("F:/")):
        folder_dict[dir_path] = dir_names
        if find_folder in folder_dict[dir_path]:
            print(f"Folder found in {dir_path}!")


    for dir_path, dir_names, filenames in (os.walk("E:/")):
        folder_dict[dir_path] = dir_names
        if find_folder in folder_dict[dir_path]:
            print(f"Folder found in {dir_path}!")
    
    
elif choice == "2":
    find_file = input("Enter the name of file that you are searching \n>> ")
    for dir_path, dir_names, filenames in os.walk("C:/"):
        file_dict[dir_path] = filenames
        if find_file in file_dict[dir_path]:
            print(f"File found in {dir_path}!")



    for dir_path, dir_names, filenames in os.walk("D:/"):
        file_dict[dir_path] = filenames
        if find_file in file_dict[dir_path]:
            print(f"File found in {dir_path}!")



    for dir_path, dir_names, filenames in os.walk("E:/"):
        file_dict[dir_path] = filenames
        if find_file in file_dict[dir_path]:
            print(f"File found in {dir_path}!")
                    


    for dir_path, dir_names, filenames in os.walk("F:/"):
        file_dict[dir_path] = filenames
        if find_file in file_dict[dir_path]:
            print(f"File found in {dir_path}!")
                    
        # else:
            # print("No file found of such name! Please currect the spelling")
else:
    raise ValueError("Please choice 1 or 2")
