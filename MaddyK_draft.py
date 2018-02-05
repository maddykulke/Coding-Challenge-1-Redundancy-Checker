import os 


def redundancy_checker(dir_path):
    match_lst = []

    all_files = os.listdir(dir_path)
    num_files = len(all_files)
    for i in range(num_files):
        for n in range(i+1,num_files):
                file1 = open(str(dir_path+"/"+all_files[i]),"r") 
                file2 = open(str(dir_path+"/"+all_files[i]),"r") 
                file1_lines = file1.readlines()
                file2_lines = file2.readlines()
                for l in range(len(file1_lines)):
                    for t in range(len(file2_lines)):
                        if (file1_lines[l] != '\n' and file1_lines[l] == file2_lines[t]): 
                            match_lst.append([file1_lines[l], file2_lines[t]])
                print("file 1: ", all_files[i], "file 2: ", all_files[n])
                print("matches: ")
                for match in match_lst:
                    print(match)
                match_lst = []
                   
def main():

    dir_path = raw_input("enter directory  name: ")

    if not (os.path.exists(dir_path)):
        print("The path you enetered does not exist")
    redundancy_checker(dir_path)



main()
