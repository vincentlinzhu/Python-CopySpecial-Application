#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def Special_Files_List_Prime(directories):
    response = []
    filenames = os.listdir(directories)
    for filename in filenames:
        checkmark = re.search(r'__(\w+)__', filename)
        if checkmark:
            tmp_path = os.path.join(directories, filename)
            print os.path.abspath(tmp_path)

def Special_Files_List(directories):
    #print 'in SFL'
    response = []
    filenames = os.listdir(directories)
    for filename in filenames:
        checkmark = re.search(r'__(\w+)__', filename)
        if checkmark:
            tmp_path = os.path.join(directories, filename)
            response.append(os.path.abspath(tmp_path))
    #print response
    return response

def copy_to(paths, to_dir):
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for path in paths:
        filename = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, filename))

def zip_to(paths, to_zip):
    #cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    #print "I'm going to do this command:" + cmd
    #(status, output) = commands.getstatusoutput(cmd)
    #if status:
        #sys.stderr.write(output)
        #sys.exit(1)
    #copy_to(paths, to_dir)
    shutil.make_archive(paths, 'zip', to_zip)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[0:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
    todir = ''
    if args[1] == '--todir':
        todir = args[3]
        #del args[0:2]

    tozip = ''
    if args[1] == '--tozip':
        tozip = args[3]
        #del args[0:2]
        
    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

  # +++your code here+++
  # Call your functions
    
    if len(args) == 2:
        Special_Files_List_Prime(args[1])
        sys.exit(1)
   
    paths = []
    paths.extend(Special_Files_List(args[2]))
    
    if todir:
        copy_to(paths, todir)
    elif tozip:
        #print 'in zipto'
        zip_to(args[4], tozip)
    #else:
        #print '\n'.join(paths)
  
 
if __name__ == '__main__':
    main()