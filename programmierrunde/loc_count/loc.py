# -*- coding: utf-8 -*-

import os, sys

def function_loc(name):

    with open(name) as f:
        lines = f.readlines()

    c_lines = len(lines)

    # remove whitespaces and comment one liners
    lines = [line for line in lines if _determine(line)]
    # remove block comments
    lines = _repl_block_comments(lines)

    c_loc = len(lines)

    return {
        'lines' : c_lines,
        'loc' : c_loc
    }

def _determine(line):
    result = True
    result = result and not line.isspace()
    line = line.strip()
    result = result and not line.startswith('#')
    result = result and not (line.startswith(("'")) and line.endswith(("'")) and line.count("'") == 2)
    result = result and not (line.startswith(('"')) and line.endswith(('"')) and line.count('"') == 2)
    return result

def _repl_block_comments(lines):
    result = []
    for line in lines:
        check = False
        if check:
            if '"""' in line:
                check = False
                if line.endswith('"""'):
                    pass
                else:
                    result.append(line)
        elif line.startswith('"""'):
            if line.count('"""') > 1:
                pass
            else:
                check = True
        else:
            result.append(line)
    return result

def _files_from_dir(path):
    result = []
    dir_items = os.listdir(path)
    for item in dir_items:
        if os.path.isfile(path+'/'+item):
            result.append(path+'/'+item)
        else:
            result += _files_from_dir(path+'/'+item)
    return result

# Start of Programm
#
# Input pathname

path = len(sys.argv) > 1 and sys.argv[1]
#path = raw_input('Name of Path: ')
if path:
    if os.path.exists(path):
        # files from path
        files = _files_from_dir(path)

        # count lines and line of code for python-files
        for file in files:
            # python-file?
            if file.endswith('.py'):
                # count lines
                result = function_loc(file)
                print file + ';' + str(result['lines']) + ';' + str(result['loc'])