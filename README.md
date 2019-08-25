# minimax
This is Tic Tac Toe game with an AI that uses a minimax algorithm. 

To run this, you will need to be running Python 2.7.10
You can clone this repository, and then run 

```
python main.py
@player: press 1 to go first, 2 to go second: 
```
You will be prompted to choose whether you (the player) want to go first or second. 

A 3x3 grid get displayed after every move. You will initially see an empty grid. 
```
@player: press 1 to go first, 2 to go second: bad_input
@player: ERROR (BAD INPUT) press 1 to go first, 2 to go second: 3
@player: ERROR (BAD INPUT) press 1 to go first, 2 to go second: 1
 | | 
-----
 | | 
-----
 | | 

```
You will then be prompted to enter the position where you would like to play your first move. You will
need to enter a zero indexed row and column (so the center spot corresponds to row 1, column 1)
```
@player: pick row (zero indexed) for your turn: 1
@player: pick column (zero indexed) for your turn: 1
 | | 
-----
 |P| 
-----
 | | 
```

The computer will then automatically come up with it's move. Since the search space is small, it typically
does not take longer than a second for the computer to compute it's move (on my machine). 
```
@computer has selected their move
C| | 
-----
 |P| 
-----
 | | 
```
The once exception is if the computer is allowed to go first. It takes roughly 5 seconds (on my machine) for it to perform it's first move (since it's going through the entire search space). After that each move will be less than second again. Alpha Beta pruning can be used in the future to decrease the search space and improve the speed the algorithm. 

The following represents the remainder of that sample game: 
```
@player: pick row (zero indexed) for your turn: 1
@player: pick column (zero indexed) for your turn: 1
@player: ERROR (BAD INPUT) pick row (zero indexed) for your turn: 0
@player: ERROR (BAD INPUT) pick column (zero indexed) for your turn: 2
C| |P
-----
 |P| 
-----
 | | 


@computer has selected their move
C| |P
-----
 |P| 
-----
C| | 


@player: pick row (zero indexed) for your turn: 1
@player: pick column (zero indexed) for your turn: 0
C| |P
-----
P|P| 
-----
C| | 


@computer has selected their move
C| |P
-----
P|P|C
-----
C| | 


@player: pick row (zero indexed) for your turn: 2
@player: pick column (zero indexed) for your turn: 1
C| |P
-----
P|P|C
-----
C|P| 


@computer has selected their move
C|C|P
-----
P|P|C
-----
C|P| 


@player: pick row (zero indexed) for your turn: 2
@player: pick column (zero indexed) for your turn: 2
The game is over!
C|C|P
-----
P|P|C
-----
C|P|P
```
