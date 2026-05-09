# Week 4 Notes — NumPy
**Date started:** 24-04-2026  
**Date completed:**

---

## What I studied
- Why NumPy exists
- Arrays, indexing and slicing
- Fancy and boolean indexing
- Data types, copy vs view, reshape, iterating
- Joining, splitting, searching, sorting and filtering
- repeat, tile, intersect1d, setdiff1d, where, swapaxes, flip
- Random number generation — randint, random, uniform
- Array formatting — suppress, threshold, edgeitems
- Array properties — size, itemsize, nbytes, max, min, mean
- np.nonzero, np.pad, np.nan and its properties
- zip, lambda and map functions
- Structured dtypes — custom dtype, RGBA, field access
- Matrix multiplication — matmul, @, dot and differences
- np.sum with axis — behavior across dimensions
- np.diag, np.indices, np.tile for pattern generation
- Normalisation — z-score, min-max and why it matters
- Namespace pollution and dangers of from numpy import *
- Scalar vs 1D array — np.array(0) vs np.array([0])
- Integer vs float division by zero — nan, IEEE 754, silent corruption
- nan to int conversion — irreversible data corruption
- Bitwise operations — left shift, right shift
- Rounding away from zero — copysign, ceil, floor, abs
- np.seterr and np.errstate — controlling NumPy warnings
- Complex numbers — np.emath, imaginary unit, sqrt(-1)
- datetime64 and timedelta64 — date arithmetic, precision units
- In-place operations — out parameter, memory efficiency
- Extracting integer part — 5 methods and their differences
- Broadcasting — rules, np.newaxis, column vs row vectors
- Generators and yield — lazy evaluation, memory efficiency
- np.fromiter — building arrays from computed sequences
- np.linspace — exact point count vs arange step size
- In-place sort vs np.sort — modifies original vs returns new

## What was clear
- Advantages of NumPy over Python lists
- Boolean indexing
- Always check for nan before converting types
- All numpy ufuncs support out
- datetime64 is a point in time, timedelta64 is an amount of time — adding them gives a new point in time
- fromiter pulls computed values directly into an array — avoids intermediate list, halves peak memory usage
- linspace guarantees exact count and avoids floating point accumulation errors unlike arange

## What confused me
- Strides
- Using axis argument with concatenate and stack

## Questions to follow up

## Code written
- Boolean indexing
- Problems on arrays, indexing, slicing, reshape, view vs copy, filtering and joining
- Problems on join, repeat, tile, intersect1d, setdiff1d, where, swapaxes, flip, random number generation using randint, random, uniform and array formatting
- Problems on array properties — size, itemsize, nbytes, max, min, mean
- Problems on nonzero, pad and nan properties
- Radar signal processor using structured dtype and seeded random generator
- Checkerboard pattern using slicing and np.indices
- Matrix multiplication using @ operator with manual verification
- Diagonal matrix generation using np.diag
- Boolean masking with in-place negation
- Normalisation of random matrix using z-score
- Integer and float division by zero edge cases
- nan to int to float conversion — silent corruption demonstration
- Rounding away from zero using copysign, ceil and np.where
- Bitwise operations on integer arrays
- Date arithmetic using datetime64 and timedelta64
- All dates in a given month using np.arange with datetime64
- In-place computation using out parameter and ufuncs
- Extracting integer part using 5 different methods
- Warning suppression using np.seterr and np.errstate
- 5x5 matrix with row and column values using broadcasting, tile and repeat
- Random vector generation using generators and np.fromiter
- Evenly spaced vector excluding endpoints using np.linspace
- Random vector sorting using in-place sort

## What I can now do

## Final reflection
- Should rely on AI to assess solutions but use the internet for problems
- AI adding unnecessary depth before the core answer strengthened concept understanding but slowed down learning 

## Things to improve