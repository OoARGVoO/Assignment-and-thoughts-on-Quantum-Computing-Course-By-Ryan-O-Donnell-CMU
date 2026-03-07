
That's the AND OR NOT XOR code
```aiignore
x1 := a1 XOR a2
x2 := a1 XOR a2
x3 := a1 XOR a2

x4 := x1 AND x2
x5 := x1 AND x3
x6 := x3 AND x2

x7 := x4 OR x5
x8 := x7 OR x6
ans := NOT x8
```
The code follows(the idea that is correct for any n)

Oh, and by the way, here we are trying to make the temp qubit zero back again
```aiignore
if a1 XOR a2 toggle x1
if a1 XOR a3 toggle x2
if a3 XOR a2 toggle x3

if x1 AND x2 toggle x4
if x1 AND x3 toggle x5
if x3 AND x2 toggle x6

if x4 OR x5 toggle x7
if x7 OR x6 toggle x8
if NOT x8 toggle ans

#then we make all xs zero

if x7 OR x6 toggle x8
if x4 OR x5 toggle x7
if x3 AND x2 toggle x6
if x1 AND x3 toggle x5
if x1 AND x2 toggle x4
if a3 XOR a2 toggle x3
if a1 XOR a3 toggle x2
if a1 XOR a2 toggle x1

EXTRACT ALL
```