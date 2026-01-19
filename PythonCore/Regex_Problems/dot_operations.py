import re
pattern = r'^.{3}$'
tests = ['cat', '1234', '@#$']
for t in tests:
    print(t, bool(re.match(pattern, t)))

#pattern2
pattern2 = r'^c.t$'
test = ['cat', 'cut', 'c9t', 'ct']
for t in test:
    print(t, bool(re.match(pattern2, t)))

#pattern start with 'a' and ends with 'b'
pattern3 = r'^a.*b$'
test1 = ['ab', 'axb', 'a123b', 'a123']
for t in test1:
    print(t, bool(re.match(pattern3, t)))

#getting .txt files
pattern = r'^.+\.txt$'
files = ['notes.txt', 'a.txt', 'notes.txt.bak']
for f in files:
    print(f, bool(re.match(pattern, f)))
