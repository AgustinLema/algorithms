
# Python algorithms

## Ideas for sorting algorithms

- Generate random sequences and find best, average and worst input for each algorithm
  - Calculate run time for algorithm run
  - For too fast algorithm, run multiple times and then divide
- Compare algorithms times for same input

## First pomodoro

- Installed vscode extensions for readme and python
- Wrote some ideas of what I wanted to do
- Created venv
- Installed linter
- Learned some shortcuts in vscode
- Started writing main idea

## Second pomodoro

- Wrote structure of functions to generate random number, call algorithm and print results
- Read about how to write constants in a separate file and import them
- Troubleshoot problems since the numbers generated were int. Now the generated inputs are lists of numbers
- Wrote the timing function
- Made a simple running version using just builint sort

## Thid pomodoro

- Wrote iterative function that guarantees a certain run count to reach some sensible time
- Print max and min time and input
- Working on median time

## Fourth pomodoro

- Write a number generator to generate all number combinations to use as input

## Non-pomodoro

- Refactor code
- Write multiple algorithms:
  - Bubble sort and its improvement
  - Insertion sort and its improvement
  - Searching algorithm to find position where a number would fit
- Reduce peak run times by running algorithms less times in a loop and by looking the shortest result from 20

## Fifth-pomodoro

- Wrote a way to write results into a CSV to compare algorithms and used an vscode extension to show them and sort them. Also analyzed the results.
- Started writing selection sort, should be done but not tested.

## Sixth-pomodoro

- Tested and compared selection sort
- Wrote merge sort and tested it

## Backlog

- Write improved merge sort (No new list creation)
- Write quick sort
- Write improved merge sort? https://en.wikipedia.org/wiki/Merge_sort#Variants AND natural merge sort
- Write function to get median time to get a sample input that would get average runtime

## Bugs

- Remove peak times from algorithm runs: If one run takes too long, this card it.
  - I'll need to track individual run time and get median
  - Maybe it can be a mix, get 10 group of runs using old method (avg) and then get median of that
  - I care about minimum time, but when values are too small, that doesn't work. Maybe I can run the algorithm multiple times until I get a sensible runtime and do it multiple time and keep the lowest so that I reduce peaks
  - Min allowed time should be configurable
  