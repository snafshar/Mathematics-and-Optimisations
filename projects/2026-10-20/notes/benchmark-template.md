# Optimization Benchmark Protocol

1. Fix objectives and starting points.
2. Verify correctness against known solutions when possible.
3. Use identical stopping rules or explain differences.
4. Measure objective evaluations as well as iterations.
5. Repeat timing runs and report a robust statistic.
6. Include failure-to-converge cases.
7. Record environment and parameters.

Do not rank methods solely by iteration count: one method may perform expensive evaluations or linear solves per iteration.