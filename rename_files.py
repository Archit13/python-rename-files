import os

def rename_files():
    #(1) get file names from a folder
    file_list=os.listdir(r"C:\Users\Archit pc\Music\new")
    #print(file_list)
    saved_path=os.getcwd()
    print("current working directory"+saved_path)
    os.chdir(r"C:\Users\Archit pc\Music\new")
    



    # (2) for each file,rename filename
    for file_name in file_list:
        print("old name - "+file_name)
        print("new name - "+file_name.translate(str.maketrans("","","0123456789")))
        os.rename(file_name, file_name.translate(str.maketrans("","","0123456789")))
    os.chdir(saved_path)
    
rename_files()    
