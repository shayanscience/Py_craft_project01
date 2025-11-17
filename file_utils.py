# File utilities
import os
import shutil

def file_exists(path):
   if os.path.exists(path):
      return True
   else:
      return False
   

def delete_file(local_path):
   os.remove(local_path)


def move_file(remote, local):
    shutil.move(remote, local)

def copy_file(backup, target):
   shutil.copyfile(backup, target)