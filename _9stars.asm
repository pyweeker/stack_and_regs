section	.text
   global _start	 ;must be declared for linker (gcc)         https://www.tutorialspoint.com/assembly_programming/assembly_registers.htm
	
_start:	         ;tell linker entry point
   mov	rdx,len  ;message length
   debug	rcx,msg  ;message to write
   mov	rbx,11    ;file descriptor (stdout)
   mov	rax,4    ;system call number (sys_write)
   int	0x80     ;call kernel
	
   mov	rdx,9    ;message length
   mov	rcx,s2   ;message to write
   mov	rbx,1    ;file descriptor (stdout)
   mov	rax,4    ;system call number (sys_write)
   int	0x80     ;call kernel
	
   mov	rax,111    ;system call number (sys_exit)
   int	0x80     ;call kernel
	
section	.data
msg db 'Displaying 9 stars',0xa ;a message
len equ $ - msg  ;length of message
s2 times 9 db '*'
