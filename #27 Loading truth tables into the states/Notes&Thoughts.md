I can't tell it's the best solution, but it's the best I can get and offer. It took me a long time to come up with this solution.


Lese first take a look at those gates:

binary:

$$
\begin{pmatrix} 1 & 0 &0&0 \\ 0 & 1&0&0\\0&0&0&1\\0&0&1&0 \end{pmatrix},\begin{pmatrix} 0&1 &0&0 \\ 1&0&0&0\\0&0&1&0\\0&0&0&1 \end{pmatrix}
$$

none-binary

$$
\begin{pmatrix} 1 & 0 &0&0 \\ 0 & 1&0&0\\0&0&1&0\\0&0&0&1 \end{pmatrix},\begin{pmatrix} 0&1 &0&0 \\ 1&0&0&0\\0&0&0&1\\0&0&1&0 \end{pmatrix}
$$

we consider to construct a state of this (we ignore the constant at the beginning):

$$
\begin{pmatrix} 1 \\ -1\\1\\-1\end{pmatrix}
$$

after binary transform, the state should be $\begin{pmatrix} c \\ -c\\-c\\c\end{pmatrix}$, while after the none-binary state, the qubit should be $\begin{pmatrix} -c \\ c\\-c\\c\end{pmatrix}$, then, we can do the Hadamard A. Then, for none-binary transform, we get $\begin{pmatrix} -b \\ b\\0\\0\end{pmatrix}$, for binary transform, we get $\begin{pmatrix} 0 \\ 0\\-b\\b\end{pmatrix}$. Last, we extract all and focus on the state of qubit A. If it's zero, then Enigma is none-binary, if it's one, then Enigma is binary. (The b and c are just some appopriate constants because i don't want to mess up with the square-sum-equaling-one thing)

The last thing we focus on is that how do we get the qubit $
\begin{pmatrix} 1 \\ -1\\1\\-1\end{pmatrix}
$. Remember the `#21&22`, we had `Had ,toggle, Had`? We can utilize it to get minus signs.

So here's the final code:

```aiignore

new qubit A,B
HAD A
toggle B
HAD B
# adding 2 Had B before the toggle, then it is just HAD ALL, HAD B toggle B and stuff...
Enigma(A,B)
HAD A
EXTRACT ALL
```
