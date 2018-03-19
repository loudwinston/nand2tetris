// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// initialize sum to zero
	@sum
	M = 0

// set i to R0
	@R0
	D = M	
	@i
	M = D

(LOOP)
	// exit loop if i = 0
		@i 
		D = M
		@END
		D;JEQ

	// subtract 1 from i
		@i
		M = M-1

	// add R1 to sum
		@R1
		D = M
		@sum
		M = M + D // add R1 to @SUM
	
	// repeat loop
		@LOOP
		0;JMP
(END)
@END

// set R2 to sum
	@sum
	D = M
	@R2
	M = D

