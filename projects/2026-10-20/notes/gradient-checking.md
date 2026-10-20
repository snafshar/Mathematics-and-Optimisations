# Finite-Difference Gradient Checking

For coordinate i, a central-difference estimate is (f(x+h e_i)-f(x-h e_i))/(2h). Compare with the analytic gradient using absolute and relative tolerances. Very small h increases cancellation; very large h increases truncation error.

Use a smooth function and representative point away from singularities. Gradient checking is diagnostic, not proof; nonsmooth objectives need different treatment.