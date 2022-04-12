# Sudoko-Pair-solver
Given a sudoku puzzle pair S1, S2 (both of dimension k) as input, your job is to write a program to fill the empty cells of both sudokus such that it satisfies the following constraints, Individual sudoku properties should hold. For each empty cell S1[i, j] ≠ S2[i, j], where i is row and j is column.

Input: Parameter k, single CSV file containing two sudokus. The first k*k rows are for the first sudoku and the rest are for the second sudoku. Each row has k*k cells. Each cell contains a number from 1 to k*k. Cell with 0 specifies an empty cell.

Output: If the sudoku puzzle pair doesn't have any solution, it returns None otherwise return the filled sudoku pair.

Modulesused: {time,random,csv,math,argparse,pysat}
from pysat.solvers import Solver
from pysat.card import *
import math
import numpy as np
import csv
import time
