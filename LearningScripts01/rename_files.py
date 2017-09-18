import os

def rename_files():
        #(1) get file names from a folder
        file_list = os.listdir("/home/dhiraj/Python/Repositories/Python/LearningScripts01/prank")
        print(file_list)
        saved_path = os.getcwd()
        print("Current directory is "+ saved_path)
        os.chdir("/home/dhiraj/Python/Repositories/Python/LearningScripts01/prank")

        for file_name in file_list:
                print("old file name"+file_name)
                print("new file name"+file_name.translate(None,"0123456789"))
                os.rename(file_name,file_name.translate(None,"0123456789"))
               
        os.chdir(saved_path)

rename_files()
