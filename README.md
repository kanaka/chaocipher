## Chaocipher: Javascript and Python versions


### Description

[Chaocipher](http://en.wikipedia.org/wiki/Chaocipher) is a method of
encryption invented by John F. Byrne in 1918 that was never publicly
solved.

The algorithm was published in May 2010. These implementations are
based on the
[paper](http://www.mountainvistasoft.com/chaocipher/ActualChaocipher/Chaocipher-Revealed-Algorithm.pdf)
by Moshe Rubin:

### Usage

#### Javascript:

Load the chao.html in a browser. Enter the left and right alphabets.
Enter either the plaintext or the ciphertext and click "Encrypt" or
"Decrypt" respectively.


#### Python:

The python program `chao.py` reads the plaintext or ciphertext from
standard input and writes the result to stdout. The left and right
alphabets are set using the `--left` and `--right` arguments
respectively. The `--encrypt` and `--decrypt` arguments specify the
mode.

An example of encrypting a file:
    cat myfile | ./chao.py --encrypt --left HXUCZVAMDSLKPEFJRIGTWOBNYQ --right PTLNBQDEOYSFAVZKGJRIHWXUMC

An example of decrypting text entered from the terminal:
     ./chao.py --decrypt --left HXUCZVAMDSLKPEFJRIGTWOBNYQ --right PTLNBQDEOYSFAVZKGJRIHWXUMC
