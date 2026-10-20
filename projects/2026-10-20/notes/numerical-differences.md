# Numerical Differentiation

Forward differences use one-sided samples and typically have first-order truncation error; central differences use samples on both sides and typically have second-order error for smooth functions.

Both suffer cancellation when the step is too small. Scale the step relative to input magnitude and verify against an analytic derivative when possible. Complex-step differentiation can help for functions supporting complex arithmetic and analyticity.