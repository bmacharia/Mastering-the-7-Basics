# Plus Minus

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the `decimal value` of each fraction ono a new line with 6 places after the decimal.

_Note:_ This problme introduces precision problems. The test cases are scaled to six decimal places, though answers with absolutee error up to 10 to the -4 power are acceptable

## Example

arr = [1,1,0,-1,-1]

There are n = 5 elements, two positive integers, two negative integers, and one zero.
Their ratios are 2/5 = 0.40000, 2/5 = 0.40000m and 1/5 = 0.200000. The results are printed as

```python
0.400000
0.400000
0.200000

```

## Function Descriotion

Complete the plusMinus function
The plusMinus function has the following input parameters

- `int arr[n]: an array of integers`

## Print

Print the ratios of positive, negative, and zero values in the array. Each value shuld be printes on a separate line with `6` digits after the decimal. The function should not return a value

## Input Format

The first line contains an integer, `n`, the size of the array.
The second line contains `n` spaced-separated integers that describe
`arr[n]`

## Constraints

- The number of elements is greater than 0 and less then or equal to 100

  The constraints of the elements in the input are are less than or equal to -100 and
  less than or equal to 100

  ## Output format

  _Print_ the following `3` lines, each `6` decimals:

  - proportion of positive values
  - proportion of negative values
  - proportion of zeros

## Sample Input

```bash

   STDIN              Function
  -------             ---------
   6                 arr[] size n = 6
  -4 3 -9 0 4 1      arr = [-4,3,-9,0,4,1]


```

## Sample Output

```bash
  0.500000
  0.333333
  0.166667
```

## Explanation

There are `3` positive numbers, `2` negative numbers, and `1` zero in the array.

The proportions of occurences are positive: `3/6 = 0.500000`
negative: `2/6 = 0.333333` and zeros `1/6 = 0.166667
