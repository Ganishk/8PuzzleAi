# 8-Puzzle Problem
Solution to 8-puzzle problem using variations of Hill-Climbing Algorithm (First-Choice and Random-Restart).

It was done as a project of CSMI17 - Artificial Intelligence (July 2024)

### Execution
1. Open the *Jupyter Notebook* in a suitable environment of your choice.
2. Set the goal state of your choice.
3. Run all the cells

#### Additionals
- Python script is also provided to execute in minimal python environment.
- Edit the python file with the desired goal state.
- Run `python <path_to_solution.py_file>`.
- In linux, one can give executable permissions to the file using `chmod +x <path_to_solution.py_file>` to run it directly.

### Novelty
Goal state can be changed as per users wish and the best solution for that also will be obtained.

## Issues
- Based on the initial state, the solution may vary.
- Hill-Climbing method is not the best choice for 8-puzzles problem which was clearly mentioned by George F. Luger in his book.

## Advancements
- This can be extended to include symmetrical solutions as mentioned by George F. Luger in his book.
- It can also be extended with reversal of adjacent tiles heuristics to get better solutions for random-restart variation which is also mentioned in the same book as mentioned above.

## References
- F, G. and Luger, W.A. (1998). Artificial intelligence : structures and strategies for complex problem solving. Harlow, England; Reading, Mass. Addison-Wesley.
- Russel, S. and Norvig, P. (2021). Artificial intelligence: A Modern approach. 4th ed. Prentice Hall.
- Wikipedia. (2019). Hill climbing. [online] Available at: https://en.wikipedia.org/wiki/Hill_climbing.
- Fundamentals of Artificial Intelligence Local Search Algorithms. (n.d.). Available at: https://web.cs.hacettepe.edu.tr/~ilyas/Courses/VBM688/lec05_localsearch.pdf.