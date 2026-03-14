### Part a

It's quite easy through martix multiplication:

$$
\frac{1}{2}\cdot\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}\cdot\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\cdot\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

It's one of a Pauli matrixs. It puts a minus sign on the `|1>` state.

### Part b

We can just put the `If` thing at the begging, so it acts like:
$$
\text{If A then do this on B:}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}
$$

Or:
$$
\begin{pmatrix} 1 & 0 &0&0 \\ 0 & 1&0&0\\0&0&1&0\\0&0&0&-1 \end{pmatrix}
$$

### Part c

It is a swap of A and B. It's just put a minus sign on `|11>` state, so it's kinda same as (b).

### Part d

We use the fact that (b) and (c) are the same to alter the middle 3 lines the the (d) to those in (c). And the Hadamards cancels out.

## Thoughts

I realized that it can be used to proof the _Mystery Toggle_. The

```
Hadamard all
(If x1 toggle ans)
(If x2 toggle ans)
...
(If xn toggle ans)
Hadamard all
```

is equivalant to 
```
If ans toggle (x1)
If ans toggle (x2)
...
If ans toggle (xn)
```

Also this is helpful when we are doing if f then minus

Dude this is cool.