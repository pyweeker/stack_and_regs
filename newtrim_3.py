import os
import sys
import re
import itertools

"""
oldfile = "./9stars.asm"
#oldfile = "./hello.asm"
#oldfile = "./shuffle.asm"
"""

def trimit(sourcecode_file):

    list_of_lines = list()

    '''\
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text
    after the name before appending the line to the output file.
    '''

    with open(sourcecode_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            line = line.split(";")[0].strip()
            line_lstriped = line.lstrip()
            line_bilatstriped = line_lstriped.rstrip()


            #print(f"--------->   {line_bilatstriped}")
            #if line.startswith(txt):
            notab = line_bilatstriped.replace('\t',',')
            #full = line_bilatstriped.split(',')
            full = notab.split(',')
            #res = res.split(',')
            print(f"\n\n AAAAAA--*****------->   {full}")

            list_of_lines.append(full)

    print(len(list_of_lines))
    print(list_of_lines)


    return list_of_lines




            

            

"""

#returned_list_of_lines = trimit(oldfile)

print(len(returned_list_of_lines))

print(returned_list_of_lines)
"""