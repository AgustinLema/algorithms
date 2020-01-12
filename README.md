
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

## Backlog

- Write insertion sort
- Write function to get median time to get a sample input that would get average runtime

## Bugs

- Remove peak times from algorithm runs: If one run takes too long, this card it.
  - I'll need to track individual run time and get median
  - Maybe it can be a mix, get 10 group of runs using old method (avg) and then get median of that
  - I care about minimum time, but when values are too small, that doesn't work. Maybe I can run the algorithm multiple times until I get a sensible runtime and do it multiple time and keep the lowest so that I reduce peaks
  - Min allowed time should be configurable
  