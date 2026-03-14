## Notes
Here, Prof gives us the definition of the correlation function on two functions that outputs a single bit. It's defined by the fractions of all input bits where two function are them same, minus the fraction that they are not. the value of $\text{Corr}(f,g)\in[-1,1]$, where $1$ meaning that they have the same output for every input bit strings and $-1$ meaning that their output is different for every single input.

Here's a theorem involving the correlation function: If you do the `HAD` on a $\pm1$ truth table of a one-bit-output function, then the amp on every bit is equal to $\text{Corr}(f,\text{XOR}_\text{This Bit})$

## Solutions
Well, the question is actually pretty great. The proof that Prof O'Deneell gives definitely worked, but frankly it's very indirect and feels like cheating LOL. So the goal here is a straightforward proof to satisfy the curiosity of some students(and me!).

After some attempts, I find it's pretty hard to give a straightforward solution and express it with fluent sentences, but anyway, I'll try my best.

Let's say the control bits(or mask bits) are $s_1,...,s_n$ and $y_1,...,y_n$, and the variable bits are $x_1,...,x_n$. If $s_k=y_k$, nothing happens. If $s_k \neq y_k$, then the difference of the output only happens when $x_k=1$, and as the bits are unrelated to each other, it's safe to say that unless the two mask bits are equal, there are always half of the input bits that makes the same output and half of the bits don't, a.k.a. the correlation function becomes zero.