################
# struc
################
# used to pack data into C/C++ structure (including alignment)
# bytelist => C/C++ STruct

#  struct.pack(format, v1, v2 ...) = pack values
# struct.unpack(format, bugger) = returns list of tuples from BufferError

# format: firstchar + 

# FIRSTCHAR:
# - '@' = default encoding (with compiler alignment) (USED AS DEFAULT)
# - '=' = native, without alignment??
# - '<' / '>' = little, big endian (or '!' for network big endian)

# REST OF CHARS:
# - 'c' = char (1)
# - 'b' = signed char
# - '?' = bool (1)
# - 'h' = short (2)
# - 'i' = int (4)
# - 'l' = long
# - 'f' = float
# - 'd' = double (8)
# - 'x' = padding byte

# LAST POINTER DATA
# - 'N' = size_t
# - 'P' = void*
# - 's' = char[n]

# ints
import struct
data = struct.pack("@iii", 1, 2, 3)
print(len(data)) # 4 (lenofint) * 3 = 12 bytes
# one object will always start at multiple of its size (eg int starts at 4, 8, etc)
# char char int => cc??iiii => size = 8
data = struct.pack("@cci", b'x', b'y', 4) # do not forget it needs bytes
# Obs: they are aligned in memory in the given order from the string (so length may be different for different alignments)


# length will always be multiple of the greatest size (padding occures)
# To specify this, tell them specifically to padd up to an given size with '0x' x = i/d - works only with @ at the beginning (in other modes, add padding manually - eg. xxxx or 4x)
data = struct.pack("@chic0i", b'A', 1, 2, b'B') # => size = 12 (multiple of int)

# = instead of  @ disables alignment
data = struct.pack ("@3i10sf", 1, 2, 3, b"Python", 1.5)
 # 3 ints, 10 chars, float
 # not specifying 10s but only s, it takes only the first letter



##########
# ctype
##########
# module provides wrappers around C++ basic types + loading of libraries / pointers etc
