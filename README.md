# NMKSolver
## A solver for the great puzzle game No More Kings by Decktonic

Requirements:
- Python 3.x installed

Usage:
`python nmksolver.py -x -y`
x is the set (1-3)
y is the level (1-50)

Only levels 1-10 from set 1 are provided with this repo for testing purposes.
You can play set 1 for free here: [http://montoyaindustries.com/nomorekings/]
You really should go buy sets 2 and 3 on the iOS or Android app!

All other levels you can solve by creating a plain-text file with the board and
saving it in the `/src/boards` folder as x-y.txt. Look at the test boards to see
how to save the text file. Then run `python nmksolver.py -x -y'`.