# -*- coding: utf-8 -*-
"""DAI Assigment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sznLRKbzpSMg2wlOzR7UZ8o_1hIIBBGA

Problem 1 .A
"""

import numpy as np

def calculate_speedup_efficiency(n_values, p_values):
    results = []

    for n in n_values:
        for p in p_values:
            T_serial = n**2  # Serial time
            T_parallel = (n**2) / p + np.log2(p)  # Parallel time

            speedup = T_serial / T_parallel  # Calculate speedup
            efficiency = speedup / p  # Calculate efficiency

            results.append((n, p, speedup, efficiency))

    return results

def main():
    n_values = range(10, 321, 10)  # n = 10, 20, ..., 320
    p_values = range(1, 129, 1)    # p = 1, 2, 3, ..., 128

    results = calculate_speedup_efficiency(n_values, p_values)

    for n, p, speedup, efficiency in results:
        print(f"n = {n}, p = {p}: Speedup = {speedup:.2f}, Efficiency = {efficiency:.2f}")

if __name__ == "__main__":
    main()