# HADJINOR, Norjane M.

π is a mathematical constant commonly associated with circles, but it can also be defined using infinite series. One such representation is the Leibniz series, given by:

π=4(1−3/1+5/1−7/1+⋯)

This formula expresses π as an alternating infinite series. Although it converges slowly, it provides a useful method for approximating π numerically and analyzing decimal precision. Two commonly used decimal approximations of π are 3.1415 and 3.1416. These values differ at the fourth decimal place, and this experiment investigates whether that difference becomes more significant at higher decimal places.

The computed value of π begins as:

π = 3.141592653589793238462643383279… 

π = 3.141592653589793238462643383279… 

Comparison of the approximations shows:

•	3.1415 underestimates π

•	3.1416 slightly overestimates π

The numerical error of 3.1416 is significantly smaller than that of 3.1415. This relationship remains consistent when examined at the 20th, 40th, 60th, and 100th decimal places. Increasing the number of decimal places does not change the relative accuracy of the approximations. The difference between 3.1415 and 3.1416 is fixed at the fourth decimal place, and higher precision only makes the existing error more visible. Since the true value of π has a fifth decimal digit of 9, rounding to 3.1416 provides a closer approximation than truncating to 3.1415.


<img width="957" height="509" alt="output" src="https://github.com/user-attachments/assets/de68da3f-7c8d-459f-96ac-4edab2131eda" />



To conclude, the experiment demonstrates that π can be computed using non-geometric mathematical formulas such as infinite series. The approximation 3.1416 is consistently more accurate than 3.1415, regardless of the number of decimal places examined. Increasing decimal precision does not introduce new differences between the two values but highlights the accuracy of proper rounding.

Example: Comparing π Approximations at Different Decimal Places
The true value of π begins as:
π=3.141592653589793238462643383279…
π=3.141592653589793238462643383279… 

Two common approximations are:

•	π₁ = 3.1415 (truncated)

•	π₂ = 3.1416 (rounded)


Example at the 20th Decimal Place
True π (20 decimals):
3.141592653589793238463.141592653589793238463.14159265358979323846 
Value	Comparison
3.1415	Missing digits starting from the 5th decimal place
3.1416	Matches π up to the 4th decimal place

Error calculation:

  Error of 3.1415 = 3.1415 – π ≈ − 0.0000926536

  Error of 3.1416 = 3.1416 – π ≈ + 0.0000073464 

Since

  ∣ + 0.0000073464 ∣ < ∣ − 0.0000926536∣

  = 3.1416 is closer to π than 3.1415.

What happens at 40th, 60th, and 100th decimal places?
Even if π is written as:

3.1415926535897932384626433832795028841971…

or extended to 100 decimal places, the difference between 3.1415 and 3.1416 remains exactly 0.0001.

The additional decimals do not change which approximation is better—they only show more digits of π beyond where the approximation already stopped.


References

•	Weisstein, E. W. Leibniz Formula. MathWorld

•	Python Software Foundation. decimal — Decimal fixed-point and floating-point arithmetic

