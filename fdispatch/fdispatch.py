#!/usr/bin/env python3

import os
import sys
import shutil
from random import shuffle
import argparse

def main():
    parser = argparse.ArgumentParser(description='File dispatcher. For detailled information please refer to the README file')
    parser.add_argument('source_folder', help="Source folder containing the file to dispatch to the target folders")
    parser.add_argument('dispatching', nargs='*', help="Must be a sequence of <percentage target_folder> <percentage target_folder> ... The sum of all percentage must be inferior to 100")
    parser.add_argument('--ext', '-e', dest='extension', default=None, help='Restrain dispatch to file with given extension')
    args = parser.parse_args()

    #Check source folders
    if not os.path.isdir(args.source_folder):
        print("ERROR : Could not find source folder {}".format(args.source_folder))
        exit(-1)

    #check number of argument
    if len(args.dispatching) % 2 != 0:
        print("ERROR : Invalid number of arguments. Try fdispatch.py -h")

    #Check percentage
    percents = [int(percent) for percent in args.dispatching[::2]]
    if sum(percents) > 100:
        print("ERROR : The percentage sum must be <= 100.")
        exit(-1)
    
    #List files
    files = [f for f in os.listdir(args.source_folder) if f.endswith(args.extension if args.extension is not None else '')]
    n_files = len(files)
    print("{} files has been found in source folder.".format(n_files))

    #Dispatch
    n_target_files = [round(percent * 0.01 * n_files) for percent in percents]

    if sum(n_target_files) > n_files:
        n_target_files[-1] -=1
    elif sum(n_target_files) < n_files and sum(percents) == 100:
        n_target_files[0] += 1

    shuffle(files)
    print("Dispatching {} from {}: ".format(n_files, args.source_folder))
    i = 0
    for target_folder, n_file in zip(args.dispatching[1::2], n_target_files):
        if not os.path.isdir(target_folder):
            os.mkdir(target_folder)
        print("-> {} : {} files ({:.2f}%)".format(target_folder, n_file, n_file/n_files*100))
        for i in range(n_file):
            shutil.copy(os.path.join(args.source_folder,files[i]), os.path.join(target_folder, os.path.basename(files[i])))
            i += 1
    print("DONE")
        
if __name__ == '__main__':
    main()