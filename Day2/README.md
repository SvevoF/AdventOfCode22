# Day 2

Today it was a bit of a struggle, I didn't want to make some if nesting if it wasn't necessary.
Instead, since both the opponent's and the player's plays where consecutive, I decided to check the difference in ASCII values.

This allows to restrict the number of if statement.
Part one was easy, I simply considered that scissors beats rock (not true, if you didn't know).

Solved that problem, the result was easy.

Part 2 was basically the same, but reversed. Now we have the results and we have to play accordingly. However, the same differences between ASCII characters still hold, meaning we can simply ADD instead of making the difference.

[Reference](https://adventofcode.com/2022/day/2)