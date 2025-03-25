# Learning Exercise: Writing Functions

## 4. Write a function `is_even`

Write a function `is_even` that takes a number as a parameter and returns whether or not it is even. Test that your function works by calling it twice (once with an even number and once with an odd number), and print the results.

---

## 5. Write a function `calculate_total`

Write a function `calculate_total` that takes 3 parameters:

1. **meal**: the cost of the meal
2. **tax_rate**: the percent tax (e.g., NJ tax would be 0.07)
3. **tip_rate**: the percent tip (e.g., a 20% tip rate is 0.20)

Proper tipping technique dictates that the tip should be calculated based on the total cost of the meal **before** tax is applied. Then, return the total.

Test your function with the following call:

```python
calculate_total(53.48, 0.07, 0.18)
```

**Note**: The total for the above meal with tax & tip is \$66.85.

---

## 6. Write a function `hey`

Write a function `hey` that takes a number as a parameter, squares it, and outputs the parameter squared:

**Example calls**:

```
hey(5)   → 25
hey(0)   → 0
hey(-3)  → 9
```

---

## 7. Write a function `there`

Write a function `there` that takes a number `n` as a parameter, and returns `2n` if `n` is positive, and `0` otherwise. Your function should output the following for the given calls:

**Example calls**:

```
there(5)   → 32
there(0)   → 1
there(3)   → 8
there(-2)  → 0
there(-6)  → 0
```

---

## 8. Write a function `are_we`

Write a function `are_we` that takes a number of times to repeat and a phrase to be repeated as parameters. It outputs the phrase in a sentence multiple times. Here is what your function should output for the given calls:

**Example calls**:

```
are_we(2, "there")
```

**Prints**:  
`Are we there yet? Are we there yet?`

```
are_we(3, "50")
```

**Prints**:  
`Are we 50 yet? Are we 50 yet? Are we 50 yet?`

```
are_we(1, "")
```

**Prints**:  
`Are we yet?`

```
are_we(0, "hey!")
```

(No output)

```

```
