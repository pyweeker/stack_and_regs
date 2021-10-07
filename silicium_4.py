#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("https://stackoverflow.com/questions/9147455/what-is-default-register-state-when-program-launches-asm-linux")

print("https://serverfault.com/questions/163487/how-to-tell-if-a-linux-system-is-big-endian-or-little-endian")

#sourcecode_file = "test/9stars.asm"   ORIGINAL
sourcecode_file = "test/_9stars.asm"   #     EAX EBX ECX EDX  become   RAX RBX RCX RDX


import sys
endian = sys.byteorder
print("your endianness is ", endian)

import bitstring
from bitstring import BitArray, BitStream


import newtrim_3
from newtrim_3 import *

import time

#INSTRUCTIONS_CATALOG = ["mov","push","call","cmp","add","pop", "lea", "test", "je", "xor","jmp","jne","ret", "inc", "sub", "fld", "and", "fstp", "shl", "or"]
INSTRUCTIONS_CATALOG = ["debug","mov","push","call","cmp","add","pop", "lea", "test", "je", "xor","jmp","jne","ret", "inc", "sub", "fld", "and", "fstp", "shl", "or"] # DEBUG

# risks  add  pop ; fld ?

class Silicium():
    def __init__(self):

        self.sourcecode_lines = list()
        self.task_lines = list()
        self.first_args = list()
        self.sec_args = list()

        self.vars = dict()

        self.dico_tasks = dict()

        self.RAX = BitArray(intle=1, length=64) # signed integer litlle endian
        self.RBX = BitArray(intle=-1, length=64)
        self.RCX = 0x0
        self.RDX = 0x0
        self.RBP = 0x0 # None ?
        self.RSP = 0x0 # None ?
        self.RSI = 0x0
        self.RDI = 0x0
        self.RIP = 0x0 # None ?


    def setup(self):

        #self.dico_tasks = self.prepare_dico_tasks()   ????

        self.dico_tasks.update({"mov":self.mov})
        self.dico_tasks.update({"debug":self.debug})



        #---

        self.vars.update({"msg":"Displaying 9 stars"})
        self.vars.update({"len":len(self.vars["msg"])})
        self.vars.update({"s2":"*********"})

        #---

        self.sourcecode_lines = trimit(sourcecode_file)

        for line_number in range(0, len(self.sourcecode_lines)):
            if self.sourcecode_lines[line_number][0] in INSTRUCTIONS_CATALOG:

                self.task_lines.append(self.sourcecode_lines[line_number][0])
                self.first_args.append(self.sourcecode_lines[line_number][1])
                self.sec_args.append(self.sourcecode_lines[line_number][2])

        #for task in self.task_lines:
        #    print("! ", task, "   ",)

        for task in range(0, len(self.task_lines)):
            print("! ", self.task_lines[task], "   ",self.first_args[task],"    ",self.sec_args[task])


        for bidul in self.sec_args:
            try:
                intbidul = int(bidul)
                self.sec_args = intbidul
            except Exception as e:
                print(e)
                self.sec_args = self.vars[bidul]



    def prepare_dico_tasks(self):
        pass


    def mov(self, task_n):

        print(f"mov  method  with task_n = {task_n}  type {type(task_n)}   ")
        print(f" {self.sec_args}  in  {self.first_args} ")
        #print(f"moving  {self.sec_args[task_n]}  in  {self.first_args[task_n]}  ")   # INTEL archi
        print(f"moving  {self.sec_args}  in  {self.first_args[task_n]}  ")   # INTEL archi


    def debug(self, task_n):
        print(f"debug method called from task_lines {task_n}")


    def do_task(self, task_n, task_kind):
        #self.

        print(f"  ******>>>>> task_n   {task_n}   type   {type(task_n)}     kind {task_kind} ")
        print("start doing task  n°  ",task_n)

        #task_n = int(task_n)

        #self.dico_tasks[self.task_lines[task_n]]()  # str -> method execution
        self.dico_tasks[task_kind](task_n)

        print("end doing task  n°  ",task_n)

    def work(self):

        #for task in self.task_lines:
        for task_n in range(0, len(self.task_lines)):
            #self.do_task(self.task_lines.index(task))
            self.do_task(task_n, self.task_lines[task_n])
            time.sleep(2)





    
"""

Another option when using pack, as well as other methods such as read and byteswap, is to use a format
specifier similar to those used in the struct and array modules. These consist of a character to give the
endianness, followed by more single characters to give the format.
The endianness character must start the format string and unlike in the struct module it is not optional (except
when used with byteswap):
> Big-endian
< Little-endian
@ Native-endian
For ‘network’ endianness use > as network and big-endian are equivalent. This is followed by at least one of these
format characters:
b 8 bit signed integer
B 8 bit unsigned integer
h 16 bit signed integer
H 16 bit unsigned integer
l 32 bit signed integer
L 32 bit unsigned integer
q 64 bit signed integer
Q 64 bit unsigned integer
f 32 bit floating point number
d 64 bit floating point number
The exact type is determined by combining the endianness character with the format character, but rather than
give an exhaustive list a single example should explain:
>h Big-endian 16 bit signed integer intbe:16
<h Little-endian 16 bit signed integer intle:16
@h Native-endian 16 bit signed integer intne:16
As you can see all three are signed integers in 16 bits, the only difference is the endianness. The native-endian @h
will equal the big-endian >h on big-endian systems, and equal the little-endian <h on little-endian systems. For
the single byte codes b and B the endianness doesn’t make any difference, but you still need to specify one so that
the format string can be parsed correctly.
An example:
s = bitstring.pack('>qqqq', 10, 11, 12, 13)

is equivalent to

s = bitstring.pack('intbe:64, intbe:64, intbe:64, intbe:64', 10, 11, 12, 13)
Just as in the struct module you can also give a multiplicative factor before the format character, so the previous
example could be written even more concisely as
s = bitstring.pack('>4q', 10, 11, 12, 13)
You can of course combine these format strings with other initialisers, even mixing endiannesses (although I’m
not sure why you’d want to):
s = bitstring.pack('>6h3b, 0b1, <9L', *range(18))
This rather contrived example takes the numbers 0 to 17 and packs the first 6 as signed big-endian 2-byte integers,
the next 3 as single bytes, then inserts a single 1 bit, before packing the remaining 9 as little-endian 4-byte unsigned
integers.
"""