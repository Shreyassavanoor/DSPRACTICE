'''
shutil copyfile copies only one file. We need to specify exact path with extension in source
'''
import os
import shutil

def copy_file(src, des):
    destination = shutil.copyfile(src, des)
    print(destination)

def main():
    src = 'E:\Prep\GRE.xlsx'
    des = 'E:\prep_temp\GRE.xlsx'
    copy_file(src, des)

if __name__ == '__main__':
    main()