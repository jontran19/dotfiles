#!/usr/bin/env python3

import os
import shutil

from datetime import date

def copy_or_symlink_dotfile(src_file, dst_file, symlink):
    src_path = os.path.join(os.getcwd(), src_file)
    dst_path = os.path.join(os.path.expanduser('~'), dst_file)

    if os.path.isfile(dst_path) or os.path.islink(dst_path):
        choice = input(f"{dst_file} already exists. Do you want to create a backup of the old file? (y/n, default=n): ")
        if choice.lower() == 'y':
            # Create a backup directory with a timestamp in the name
            backup_dir = os.path.join(os.path.expanduser('~'), f'config_{date.today().strftime("%Y%m%d")}')
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

            # Backup the old file by moving it to the backup directory
            backup_path = os.path.join(backup_dir, dst_file)
            os.rename(dst_path, backup_path)
            print(f"Created backup of {dst_file} in {backup_path}")

    if os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path)
        print(f"Created directory: {dst_file}")
    else:
        if symlink:
            os.symlink(src_path, dst_path)
            print(f"Created symlink: {dst_file}")
        else:
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {dst_file}")
    return True

def prompt_for_copy_or_symlink(src_file, dst_file, symlink=True):
    while True:
        choice = input(f"Do you want to copy or symlink {src_file} to {dst_file}? (c/s, default=s): ")
        if choice.lower() == 'c':
            return False
        elif choice.lower() == 's' or choice == '':
            return symlink
        else:
            print("Invalid choice, please enter 'c' for copy or 's' for symlink.")

def prompt_for_all_files(symlink):
    files = [
        ('bash/bashrc', '.bashrc'),
        ('tmux/tmux.conf', '.tmux.conf'),
        ('vim/vimrc', '.vimrc'),
        ('vim/colors', '.vim/colors'),
        ('git/gitconfig', '.gitconfig'),
        ('emacs/spacemacs', '.spacemacs')
    ]
    for src_file, dst_file in files:
        if prompt_for_copy_or_symlink(src_file, dst_file, symlink):
            copy_or_symlink_dotfile(src_file, dst_file, symlink)

if __name__ == '__main__':
    symlink = input("Do you want to create symbolic links instead of copying files? (y/n): ").lower() == 'y'
    prompt_for_all_files(symlink=symlink)
