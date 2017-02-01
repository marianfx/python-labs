# . All characters except new line
# ^ Matches at the start of the string
# $ Matches at the end of the string
# * >=0 repetition(s)
# ? 0 or 1 occurrence
# + >=1 repetition(s)
# {x} Matches <x> times
# {x,y} Matches between <x> and <y> times
# [] Group of characters
# | Or condition

# \d Decimal characters 0,1,2,3,…9
# \D All except decimal characters
# \s Space, tab, new line (CR/LF) characters
# \S All except characters designated by \s
# \w Word characters a-z, A-Z, 0-9 and _
# \W All except characters designated by \w
# \ Escape character
# [^…] Not specified group of characters
# (…) Grouping
# [ ..-..] ‘-’ interval for a group of characters.

# THE USE OF RE
 # 1 import
import re

# 2. compile (may not be needed => will give as first param)
# Obs: to not use double slash to mark backslash, use r""
r = re.compile(r"\d+")

# 3. Match (from the beginning!)
# obj = None => no match. Else, an RegexObj is returned
obj = r.match("1234")

# 4. Search (in the whole string). Works the same way, but searches the whole string
# Use ^ + $ ti check string start - end
obj = r.search("3")

# 4.1 Find all (searches for all matches)
stringlist = r.findall("12 13  14")
# using groups in findall returns tuplelist insstead of stringlist

# 4.2 Split - splits the string using the matches. for groups, splits between groups (keeps  groups)
stringlist = re.split("(\d)(\d)", "12 12") # => 1 2 1 2

# 4.3 Substitution - replaces match with pattern (can use matched groups in patters)
# re.sub(pattern, replacewith, string, maxoccurs = 0)
# sub can use a func(str) method instead of replacewith


# 5. Groups
# - the groups are usually nested, and come in order (take one, enumerate all inner groups, then next, do the same etc.)
# uncaptured groups:  '(?: ... )' (will not be indexed)
#      - named groups: (?P<name_here>...)

wholematch = obj.group(0)
wholematch = obj.group(1)
# on r"\d+([A-Z]+)" will return the ([A-Z]+) part
# use r"(\d+).+?(\1)"
#       - \1 means match the same as the first group
#       - .+? means non-greedy behavior () (at the first encounter from the next match (eg A-Z), will stop expanding)
