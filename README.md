# RSAalgo_efficient_encrypt
RSA Encryption Algorithm with complexity of O(log (n))

This algo requires encryption and decryption and applies formula :

Encytption = M^e % n Decryption = C^e % n

The exponentiation can be very expensive if the numbers are huge.

So the technique used here applies, #Fast modular exponentiation for reducing the complexity to logn.
