# Derivation: A Two-Variable Quadratic

The objective is

`f(x,y)=2x^2+xy+y^2-6x-5y`.

Its gradient is

`∇f(x,y) = [4x+y-6, x+2y-5]`.

Setting the gradient to zero gives the linear system (4x+y=6), (x+2y=5). The solution is ((x,y)=(1,2)), and the Hessian

`H = [[4,1],[1,2]]`

is positive definite because its leading principal minors are positive: (4>0) and determinant (8-1=7>0). Therefore the stationary point is the unique global minimum. Substitution gives (f(1,2)=-8).

This analytical answer provides a reference for the numerical methods, but the implementation should still check its stopping conditions.
