#!/usr/bin/python

'''
Python Chaocipher implementation.
Copyright 2010 Joel Martin
Licensed under LGPLv3 (see LICENSE.txt)
'''

import sys, optparse, re

class Chaocipher:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    def __init__(self, left, right):
        self.orig_left = left
        self.orig_right = right

        self.reset()
        self.check()

    def reset(self):
        self.left = list(self.orig_left.upper())
        self.right = list(self.orig_right.upper())

    def check (self):
        left = self.left
        right = self.right

        if len(left) != 26:
            raise Exception("Left side must contain 26 characters");
        if len(right) != 26:
            raise Exception("Left side must contain 26 characters");

        for i in range(26):
            char = self.alphabet[i]
            if left.count(char) != 1:
                raise Exception("Left side missing '%s'" % char)
            if right.count(char) != 1:
                raise Exception("Right side missing '%s'" % char)

    def permute(self, idx):
        # Permute the left

        # Step 1: Rotate idx to zenith
        for cnt2 in range(idx):
            self.left.append(self.left.pop(0))
        # Step 2 and 3: extract zenith +1
        char = self.left.pop(1)
        # Step 4: Insert at nadir
        self.left.insert(13, char);

        # Permute the right

        # Step 1 and 2: rotate idx to zenith-1
        for cnt2 in range(idx+1):
            self.right.append(self.right.pop(0))
        # Step 3 and 4: remove zenith + 2
        char = self.right.pop(2)
        # Step 5: insert at nadir
        self.right.insert(13, char)

    def crypt (self, text, mode):
        src = list(text)
        dest = []

        for cnt in range(len(src)):
            char = src[cnt]
            if self.alphabet.find(char) < 0:
                #print "Ignoring character '%s'" % char
                continue

            if mode == "decrypt":
                idx = self.left.index(char)
                dest.append(self.right[idx])
            else:
                idx = self.right.index(char)
                dest.append(self.left[idx])

            if cnt + 1 == len(src):
                break

            self.permute(idx)

        return ''.join(dest)


if __name__ == '__main__':
    usage = "%prog [--left LEFT] [--right RIGHT] [--encrypt|--decrypt]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("--left", help="left alphabet",
            default="HXUCZVAMDSLKPEFJRIGTWOBNYQ")
    parser.add_option("--right", help="right alphabet",
            default="PTLNBQDEOYSFAVZKGJRIHWXUMC")
    parser.add_option("--encrypt", help="perform encryption",
            action="store_const", const="encrypt", dest="mode",
            default="encrypt")
    parser.add_option("--decrypt", help="perform decryption",
            action="store_const", const="decrypt", dest="mode")
    (options, args) = parser.parse_args()

    print "Using left: %s" % options.left
    print "Using right: %s" % options.right
    if sys.stdin.isatty():
        if options.mode == "encrypt":
            print "Enter plaintext (Ctrl-D to finish):"
        else:
            print "Enter ciphertext (Ctrl-D to finish):"
    text = sys.stdin.read()

    C = Chaocipher(options.left, options.right)
    result = C.crypt(text, options.mode)
    print "%sed result:\n%s" % (options.mode, result)

    #result = C.crypt("WELLDONEISBETTERTHANWELLSAID", "encrypt")
    #print "encrypted:", result
    #C.reset()
    #result = C.crypt("OAHQHCNYNXTSZJRRHJBYHQKSOUJY", "decrypt")
    #print "decrypted:", result

