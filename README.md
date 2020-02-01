
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

## Non-pomodoro-2

- Refactor code
- Add array function to find max_subarray in linear and logn time

## Seventh-pomodoro

- Start writing heap datastructure

## Eight-pomodoro

- Wrote most part of heap, need to tune functions
- Wrote a hackish way to print the heap tree

## Non-pomodoro-2

- Made working version of heap
- Made working version of heapsort

## Ninth-pomodoro

- Completed merge sort in place and compared with the extracting one

## Non-pomodoro-3

- Write quicksort
- Write quicksort with center pivoting

## Non-pomodoro-4

- Write count sort
- Write radix sort

## Tenth-pomodoro

- Write array select order index in linear time with middle partitioning
- Move partitioning code to common_algorithms file

## Eleventh-pomodoro

- Add a test and move files. Get coverage

## Twelft-pomodoro

- Write a queue and a stack using an underlying array (list of fixed size)

## Backlog

- Write a deque
- Write a linked list and a double linked list. Implement insert relative to another element and at beginning.
- Implement a queue and a stack using a single linked list
- Write a tree with linked elements and a recursive procedure to print all elements
- Write an algorithm that prints all elements of a tree using a non-recursive algorithm and a stack. Then write it with only constant space.
- Write a hashmap using a linked list
- Write a hashmap with open addressing
- Write a hashmap like python builtin dict that preserves order: https://morepypy.blogspot.com/2015/01/faster-more-memory-efficient-and-more.html
- Write a recursive inorder tree walk algorithm
- Write a iterative inorder tree walk algorithm with a stack
- Write a iterative inorder tree walk algorithm without a stack
- Write a search algorithm for binary search tree iterative and recursive
- Write recursive and iterative tree minimum, maximum, predecessor and successor
- Write a tree walk by calling tree minimum and then successor until we print the whole tree
- Write binary tree insertion
- Write binary tree deletion
- Write randomnized select index (and later the non randomnized one, that uses median of medians to select pivot)
- Write quick sort improvements: make three groups so if values are same as pivot they are not partitioned again (Similar to how hoare partition works)
- Write Block Mergesort
- Write Timsort
- Write counting sort
- Write improved merge sort? https://en.wikipedia.org/wiki/Merge_sort#Variants AND natural merge sort
- Write function to get median time to get a sample input that would get average runtime
- Write bucket sort
- Write priority queue with a min heap
- Write a heap insert value and increase key
- Write iterative quicksort

## Bugs

- Remove peak times from algorithm runs: If one run takes too long, this card it.
  - I'll need to track individual run time and get median
  - Maybe it can be a mix, get 10 group of runs using old method (avg) and then get median of that
  - I care about minimum time, but when values are too small, that doesn't work. Maybe I can run the algorithm multiple times until I get a sensible runtime and do it multiple time and keep the lowest so that I reduce peaks
  - Min allowed time should be configurable
  