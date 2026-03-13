## Soulution
I'll only give the proof to question `d` as `c` and `d` are essentially the same.

As we know, the `HAD` process doesn't matter with the order of the qubits being changed, so let's assume that we do the `HAD x_j` as the last `HAD`

If we operate the `HAD x_k` as the first `HAD`, then we are putting the average of the amp of the qubit of `x_k=0` and `x_k=1` on the qubit `x_k=0`,(actually multiplied by some constant), then if we do the had on another bit, it's equivalent to another average based on the average that `HAD x_k` gave, and so on...(here I'm just explaining the intuitive proof that prof gave on his class). At last, when we have `|00..010...0>` and `|00..000...0>` with the amplitude of the average of the qubits with the j th bit being `|1>` and `|0>`, when we do the final `HAD`, we got the ExpectationGain(j) on qubit `|00..010...0>`(I think it's actally 1/2 of that...)

I didn't use the hint given by prof, i don't know what to do with the hint...

Wait I just realised that the hint is exactly what i said here...