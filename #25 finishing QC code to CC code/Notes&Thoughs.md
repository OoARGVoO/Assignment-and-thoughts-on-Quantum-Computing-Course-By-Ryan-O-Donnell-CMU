## Notes:
So here if we get new qubit w1,w2,w3... and then extract w1,w2,w3..., that's equivalent to doing nothing. This can help the get rid of the temp qubits.

## Solutions:
So here we want Bs to be f(B0)s and Cs to be 0s.

Here we can think in a reverse order.

If we want to clear the Cs, the we have to use some sort of $\text{Toggle } f^{-1}(B_{rightnow}) \text{ on to C}$ , so here C must be $B_0$

Then, to get Bs into $f(B_0)$, we would do the $\text{Toggle } f(B_0) \text{ on to B}, so first we should swap Bs and Cs.

So the code follows:

```aiignore
swap Bs and Cs
toggle Bs with f(Cs)
toggle Cs with f-1(Bs)
```

Bt the way, I didn't now that you can swap at first, so i'm confused. It turned out at last that my english need improvement :))