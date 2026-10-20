# Stopping Criteria for Optimization

Common criteria include gradient norm below tolerance, relative objective change below a threshold, step norm below a threshold, or a maximum iteration/evaluation budget.

Each has limitations. A small step can indicate stagnation rather than a good solution, and a small gradient does not guarantee a global minimum for a nonconvex objective. Report which criterion stopped the algorithm and the final objective.