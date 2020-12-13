/** @file
*	cf. Sedgewick-Wayne, Intro to Programming in Java, p. 283, ex. 2.3.25:
*	There are 2n discs of increasing size stored on 3 poles.
*	Initially all of the discs with odd size (1, 3, ... 2n-1) are piled
*	on the left pole from top to bottom in increasing order of size;
*	all of the discs with even size (2, 4, ..., 2n) are piled on the right
*	pole. This program should provide instructions for moving the odd 
*	discs to the right pole and the even discs to the left pole,
*	obeying the same rules as for towers of Hanoi.
*	
*	My instructions (as in Sedgewick-Wayne) will view the towers as
*	a cyclic group, where tower 1 is to the right of tower 3
*	@author Marshall Farrier
*	@date 6/7/10
*/

#include <iostream>
using std::cout;
using std::endl;

/**
class towers of Hanoi
@param n
height
@param move_to_left
true iff instructions are to move the tower
to the left
*/
void move_tower(int n, bool move_left);

/**
recursive function giving instructions for interleaving
both towers into 1 correct tower on the empty peg
function makes use of move_tower() function
@param n
height of each tower
note that this is for a total of 2n discs
@param odd_on_right
true iff odd tower is to the right of the even tower
(as is the case in the starting set up with odd on peg 1 and
even on peg 3)
*/
void interleave(int n, bool odd_on_right);

/**
once the 2 towers are consolidated
this function gives instructions for
distributing the odd and even disks
from a single tower
@param n
tower height
@param odd_on_right
whether the instructions should distribute the disks
with the odd disks on the right side (true)
or left side (false) of the originial tower
*/
void distribute(int n, bool odd_on_right);

/**
combines the above functions into instructions
for swapping 2 towers
*/
void swap_towers(int n, bool odd_on_right = true);

int main()
{
	using std::cin;
	int height;

	cout << "Enter height for each tower: ";
	cin >> height;
	//distribute(2 * height, true); // distributes odd tower to right of orig
	// interleave(height, true);
	swap_towers(height, false);
	return 0;
}

void move_tower(int n, bool move_left)
{
	// base case: n == 0
	if (!n) return;
	move_tower(n - 1, !move_left);
	cout << n;
	if (move_left) cout << " left\n";
	else cout << " right\n";
	move_tower(n - 1, !move_left);
}

void interleave(int n, bool odd_on_right)
{
	if (!n) return;
	// interleave for respective tower heights using n - 1
	interleave(n - 1, odd_on_right);
	// move the tower just created onto the base disc of the odd tower
	move_tower(2 * n - 2, odd_on_right);
	// move disc 2n to the empty peg
	cout << 2 * n;
	if (odd_on_right) cout << " left\n";
	else cout << " right\n";
	// move the tower atop the biggest odd disk back to the empty peg
	move_tower(2 * n - 1, !odd_on_right);
}

void distribute(int n, bool odd_on_right)
{
	// <= 0 at least prevents infinite loop in case of incorrect input for n (which is assumed to be even)
	if (n <= 0) return;
	// move the tower, except for bottom even disc, to
	// where we want the bottom odd disk
	// i.e., if odd_on_right (we want odd tower on the right)
	// move_tower should also have its move_left variable set to false
	move_tower(n - 1, !odd_on_right);
	// move the base disk onto the empty peg:
	cout << n;
	if (odd_on_right) cout << " left\n";
	else cout << " right\n";
	// move the n - 2 tower back to the empty peg
	move_tower(n - 2, odd_on_right);
	// run distribute() on n - 2 discs:
	distribute(n - 2, odd_on_right);
}

void swap_towers(int n, bool odd_on_right)
{
	interleave(n, odd_on_right);
	distribute(2 * n, odd_on_right);
}
