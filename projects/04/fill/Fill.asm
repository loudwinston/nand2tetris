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


@24575
D = A
@finalWordAddress
M = D

(FOREVER)
	
	// did the user press the button?
	@24576
	D = M


	@keyPressed
	M = D
	D = M

	//d variable has the actual key that's pressed
	//if d > 0, write 1 to all screen positions
	//else, write zero to all screen positions


	@color
	M = 0
	

	@SETBLACK
	D;JNE

	// This should be setwhite
	@SETWHITE
	D;JEQ



	(SETBLACK)
	@color
	M = -1 // -1 means all ones
	@DRAWSCREEN
	0;JMP

	(SETWHITE)
	@color
	M = 0 // 0 means all zeroes
	@DRAWSCREEN
	0;JMP

	(DRAWSCREEN)
	// set i to SCREEN
		@SCREEN
		D = A	
		@i
		M = D
	
	(DRAWLOOP)
		// exit loop if i > finalWordAddress
			@i 
			D = M

			@finalWordAddress
			D = M - D

			@ENDDRAWLOOP
			D;JLT
	
		// write all ones to the word at i
			@color
			D = M //store the color into D

			@i
			A = M //store the value of i (current screen memory word) into A
			M = D //set M[A] to the current color

		// add 1 to i
			@i
			M = M+1

		// repeat loop
			@DRAWLOOP
			0;JMP
	(ENDDRAWLOOP)
	
@FOREVER
0;JMP
(ENDFOREVER)




