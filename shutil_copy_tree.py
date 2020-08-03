'''
   copytree recursively copies all files and directories from src to des
   here des should not be created initally 
'''
import shutil
def copy_dir(src, des):
    destination = shutil.copytree(src, des)
    print(destination)

def main():
    src = 'E:/Prep'
    des = 'E:/prep_temp'
    copy_dir(src, des)

if __name__ == '__main__':
    main()