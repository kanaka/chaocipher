/*
 * Javascript Chaocipher implementation
 * Copyright (C) 2010 Joel Martin
 * Licensed under LGPL-3 (see LICENSE.txt)
 */

Chaocipher = (function () {

var alphabet, check, permute, crypt;

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

check = function (left, right) {
    var l, r, chr;

    l = left.toUpperCase().split('');
    r = right.toUpperCase().split('');

    // Check left and right for completeness 
    if (l.length != 26) {
        throw("Left side must contain 26 characters");
    }
    if (r.length != 26) {
        throw("Right side must contain 26 characters");
    }
        
    for (i=0; i<26; i++) {
        chr = alphabet.charAt(i);
        if (l.indexOf(chr) < 0) {
            throw("Left side missing '" + chr + "'");
        }
        if (r.indexOf(chr) < 0) {
            throw("Right side missing '" + chr + "'");
        }
    }
    return true;
};

permute = function (l, r, idx) {
    var chr;
    /* Permute the left */

    // Step 1: Rotate chr to zenith
    for (cnt2 = 0; cnt2 < idx; cnt2++) {
        l.push(l.shift());
    }
    // Step 2 and 3: extract zenith + 1
    chr = l.splice(1, 1)[0];
    // Step 4: Insert at nadir
    l.splice(13, 0, chr);


    /* Permute the right */

    // Step 1 and 2: Rotate chr to zenith-1
    for (cnt2 = 0; cnt2 < idx+1; cnt2++) {
        r.push(r.shift());
    }
    // Step 3 and 4: remove zenith + 2
    chr = r.splice(2, 1)[0];
    // Step 5: Insert at nadir
    r.splice(13,0, chr);

};

crypt = function (left, right, text, mode) {
    //console.log(">> crypt [mode: " + mode + "]");
    var l, r, src, dest, chr, cnt;

    check(left, right);

    l = left.toUpperCase().split('');
    r = right.toUpperCase().split('');
    src = text.toUpperCase().split('');
    dest = [];

    for (cnt=0; cnt < src.length; cnt++) {
        chr = src[cnt];
        if (alphabet.indexOf(chr) < 0) {
            //console.log("Skipping character '" + chr + "'");
            continue;
        }

        /* Pick the ciphered letter */
        if (mode === "decrypt") {
            idx = l.indexOf(chr, 0);
            dest.push(r[idx]);
        } else {
            idx = r.indexOf(chr, 0);
            dest.push(l[idx]);
        }

        if (cnt+1 === src.length) {
            break;
        }

        permute(l, r, idx);
    }

    //console.log("<< crypt");
    return dest.join('');
};


// Public functions
return {
    encrypt : function (left, right, plaintext) {
        return crypt(left, right, plaintext, "encrypt");
    },

    decrypt: function (left, right, ciphertext) {
        return crypt(left, right, ciphertext, "decrypt");
    }
};

})();


//This indexOf prototype is provided by the Mozilla foundation and is
// distributed under the MIT license.
//http://www.ibiblio.org/pub/Linux/LICENSES/mit.license
if (!Array.prototype.indexOf)
{
  Array.prototype.indexOf = function(elt /*, from*/)
  {
    var len = this.length;

    var from = Number(arguments[1]) || 0;
    from = (from < 0)
         ? Math.ceil(from)
         : Math.floor(from);
    if (from < 0)
      from += len;

    for (; from < len; from++)
    {
      if (from in this &&
          this[from] === elt)
        return from;
    }
    return -1;
  };
}


