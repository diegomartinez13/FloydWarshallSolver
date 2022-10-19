#! /usr/bin/env python

from sys import argv
import ast

def FloydWarshall(graf, k_value):
    A = graf
    n = len(graf)
    for k in range(0, k_value):
        for i in range(0,n):
            for j in range(0,n):
                if A[i][j] == 'inf':
                    A[i][j] = float('inf')
                A[i][j] = min( A[i][j], A[i][k]+ A[k][j])
    return A

#condition if no arguments are passed
if len(argv) > 1:

    graf = ast.literal_eval( argv[1].replace("inf","'inf'"))

    if len(argv) > 2:
        k_value = int(argv[2])
        print(FloydWarshall(graf, k_value))

    else: print(FloydWarshall(graf, len(graf)))


