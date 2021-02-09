Why are numerical values returned as strings?
===============================================
If you have gone through the documentation or used this Buycoins SDK package in some capacity,
you have probably already noticed that most, if not all, decimal values are returned in a string format. Why is this so?

Since this package deals with many decimals and numbers that are important as they most represent prices and money, it
is essential to avoid any insignificant errors resulting from issues with floating points, precision, etc.
Therefore, it was decided that all decimals will be returned as strings leaving the responsibility of representing these
operations however they want entirely up to the user
of the SDK.

