Author: Hardkase 
P. Collins

Python 3.x using current cryptography module.
Basic exercise using AES & CFB, trying to determine where and how
to implement different crypto objects and randoms - init vector

Current implementation put cipher object, iv, and key in the class __init__
feels like bad practice, but works. Using iv in __init__ but key as variable
and cipher obj instatiated in encrypt/decrypt functions works. 'Re-rolling' iv
between encr and decr seems to not/partially work. Further research and more play
needed.

PC
