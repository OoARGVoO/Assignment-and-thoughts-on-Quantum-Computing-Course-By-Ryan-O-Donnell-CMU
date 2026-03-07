## Notes

Here a paradigm (or a Spec) for the boolean function f, which is:

* If f then minus / If f then toggle a1 (for single output f)
* XOR f's output bit by bit with the input (for string output f)

Also, if temp bits are included, we want them to be zero at last, so we kan undo the code that alters the temp bits to make them back to the starting position, which is, zero.



## The Solution to the Assignment:
My solution follows:

```aiignore
IF (a1 xor a2) and (a1 xor a3) toggle ans
IF (a1 xor a3) and (a2 xor a3) toggle ans
IF (a1 xor a2) and (a2 xor a3) toggle ans
toggle ans
```
By some miracle this is correct. But it cannot be correct for any arbitrary n.

The solution to any n should be as follows:

The idea is that we count how many times the `01` or `10` appears in the bit string. If there are more than 1, then we can say for sure that the string is unsorted. The AND OR NOT code follows:

```aiignore
x1 := a1 XOR a2
x2 := a1 XOR a3
x3 := a3 XOR a2

x4 := x1 AND x2
x5 := x1 AND x3
x6 := x3 AND x2

x7 := x4 OR x5
x8 := x7 OR x6
ans := NOT x8
```