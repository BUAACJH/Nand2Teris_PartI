// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
//
//pseudo code:
//    while(true)){
//        if(KBD=0):  white
//        else:       black
//    }
//
//addr = SCREEN
//n = 8192
//i = 0
//LOOP:
//    if KBD=0: goto WHITE
//    goto BLACK
//WHITE:
//    if i >= n goto LOOP
//    RAM[addr] = 0
//    addr = addr + 1
//    i = i + 1
//    goto WHITE
//BLACK:
//    if i >= n goto LOOP
//    RAM[addr] = -1
//    addr = addr + 1
//    i = i + 1
//    goto BLACK
//

(LOOP)
    @SCREEN
    D=A
    @addr
    M=D // addr=SCREEN

    @8192
    D=A
    @n
    M=D // n=8192

    @i
    M=0 // i=0
    
    @KBD
    D=M
    @WHITE
    D;JEQ   //  if KBD=0: goto WHITE
    @BLACK
    0;JMP   // goto BLACK

(WHITE)
    @i
    D=M
    @n
    D=D-M
    @LOOP
    D;JGE   // if i >= n goto LOOP

    @addr
    A=M    
    M=0     //  RAM[addr] = 0

    @addr
    M=M+1   //  addr = addr + 1

    @i
    M=M+1   // i = i + 1

    @WHITE
    0;JMP   // goto WHITE

(BLACK)
    @i
    D=M
    @n
    D=D-M
    @LOOP
    D;JGE   // if i >= n goto LOOP

    @addr
    A=M    
    M=-1     //  RAM[addr] = -1

    @addr
    M=M+1   //  addr = addr + 1

    @i
    M=M+1   // i = i + 1

    @BLACK
    0;JMP   // goto WHITE