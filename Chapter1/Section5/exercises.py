"""
------------------------------------Exercise 1.5.1--------------------------------------------
quick-find
changing all pointing of one id towards another
9-0 3-4 5-8 7-2 2-1 5-7 0-3 4-2.
"""

"""
------------------------------------Solution 1.5.1--------------------------------------------
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 3 4 5 6 7 8 9

on 9-0, 13 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 3 4 5 6 7 8 0

on 3-4, 13 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 4 4 5 6 7 8 0

on 5-8, 13 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 4 4 8 6 7 8 0

on 7-2, 13 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 4 4 8 6 2 8 0

on 2-1, 14 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 1 4 4 8 6 1 8 0

on 5-7, 14 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 1 4 4 1 6 1 1 0

on 0-3, 14 access
index   0 1 2 3 4 5 6 7 8 9
array   4 1 1 4 4 1 6 1 1 4

on 4-2, 16 access
index   0 1 2 3 4 5 6 7 8 9
array   1 1 1 1 1 1 6 1 1 1
"""


"""
------------------------------------Exercise 1.5.2--------------------------------------------
quick-union
changing one id towards another 
9-0 3-4 5-8 7-2 2-1 5-7 0-3 4-2.
"""

"""
------------------------------------Solution 1.5.2--------------------------------------------
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 3 4 5 6 7 8 9

on 9-0, 3 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 3 4 5 6 7 8 0

on 3-4, 3 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 4 4 5 6 7 8 0

on 5-8, 3 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 4 4 8 6 7 8 0

on 7-2, 3 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 4 4 8 6 2 8 0

on 2-1, 3 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 1 4 4 8 6 2 8 0

on 5-7, 9 access
index   0 1 2 3 4 5 6 7 8 9
array   0 1 1 4 4 8 6 2 1 0

on 0-3, 5 access
index   0 1 2 3 4 5 6 7 8 9
array   4 1 1 4 4 8 6 2 1 0

on 4-2, 5 access
index   0 1 2 3 4 5 6 7 8 9
array   4 1 1 4 1 8 6 2 1 0
"""


"""
------------------------------------Exercise 1.5.3--------------------------------------------
weighted quick-union
changing one id towards another but only smaller gets attached to bigger
9-0 3-4 5-8 7-2 2-1 5-7 0-3 4-2.
"""

"""
------------------------------------Solution 1.5.3--------------------------------------------
index   0 1 2 3 4 5 6 7 8 9
array   0 1 2 3 4 5 6 7 8 9
size    1 1 1 1 1 1 1 1 1 1
count   10

on 9-0, 8 access
index   0 1 2 3 4 5 6 7 8 9
array   9 1 2 3 4 5 6 7 8 9
size    1 1 1 1 1 1 1 1 1 2
count   9

on 3-4, 8 access
index   0 1 2 3 4 5 6 7 8 9
array   9 1 2 3 3 5 6 7 8 9
size    1 1 1 2 1 1 1 1 1 2
count   8

on 5-8, 8 access
index   0 1 2 3 4 5 6 7 8 9
array   9 1 2 3 3 5 6 7 5 9
size    1 1 1 2 1 2 1 1 1 2
count   7

on 7-2, 8 access
index   0 1 2 3 4 5 6 7 8 9
array   9 1 7 3 3 5 6 7 5 9
size    1 1 1 2 1 2 1 2 1 2
count   6

on 2-1, 12 access
index   0 1 2 3 4 5 6 7 8 9
array   9 7 7 3 3 5 6 7 5 9
size    1 1 1 2 1 2 1 3 1 2
count   5

on 5-7, 8 access
index   0 1 2 3 4 5 6 7 8 9
array   9 7 7 3 3 7 6 7 5 9
size    1 1 1 2 1 2 1 5 1 2
count   4

on 0-3, 12 access
index   0 1 2 3 4 5 6 7 8 9
array   9 7 7 9 3 7 6 7 5 9
size    1 1 1 2 1 2 1 5 1 4
count   3

on 4-2, 14 access
index   0 1 2 3 4 5 6 7 8 9
array   9 7 7 9 3 7 6 7 5 7
size    1 1 1 2 1 2 1 9 1 4
count   2
"""

"""
------------------------------------Exercise 1.5.5--------------------------------------------
quick-find algorithm on 10^9 sites and 10^6 pairs
on a machine capable of 10^9 instructions per second
"""

"""
------------------------------------Solution 1.5.5--------------------------------------------
quick-find algorithm has constructor n, find complexity 1 and union complexity n
So for each pair, around 10^9 instructions are needed in worst case
So 10^6*(2+10*10^9)/10^9[instructions per second]
i.e. ~1*10^7 seconds which is around 115 days
"""

"""
------------------------------------Exercise 1.5.6--------------------------------------------
Weighted Quick union algorithm on 10^9 sites and 10^6 pairs
on a machine capable of 10^9 instructions per second
"""

"""
------------------------------------Solution 1.5.6--------------------------------------------
Weighted Quick union algorithm has constructor n, find complexity ~1 and union complexity ~1
So for each pair, around 10^9 instructions are needed in worst case
So 10^6*(10+2+1)/10^9[instructions per second]
which is less than a second
"""