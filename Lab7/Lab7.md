##Lab7 - Samuel Deslandes

####WordLadder problem
Output:  
![WordLadderOutput](http://puu.sh/o2d8O/40160f3a12.png)  

My implementation of this problem is built upon Eric Hagberg's solution which can be found [here](https://github.com/networkx/networkx/blob/master/examples/graph/words.py).
My modifications include allowing for 4 letter word input and an alternative solving method in which all permutations of a word with a one letter difference are considered adjacent. 
Doing this dramatically increased runtime, but reduced the number of steps required to get from the starting to ending word.

![Alternative method output](http://puu.sh/o2dzs/bb308391f2.png)

My code can be found here.
