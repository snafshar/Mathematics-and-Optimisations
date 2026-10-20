# Armijo Backtracking

For descent direction p, the directional derivative satisfies grad(f(x)) dot p < 0. Backtracking shrinks a positive step until f(x+alpha*p) <= f(x)+c*alpha*grad(f(x)) dot p for c in (0,1).

A non-descent direction should be rejected. A minimum step and iteration budget prevent endless search caused by numerical issues or violated assumptions.