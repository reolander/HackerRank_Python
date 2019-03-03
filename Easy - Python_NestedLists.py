n = int(raw_input())
l = [[raw_input(), float(raw_input())] for _ in range(n)]
s = sorted(set(marks for name, marks in l))[1]
print '\n'.join(sorted([name for name, marks in l if marks == s]))


        

