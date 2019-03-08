if __name__ == '__main__':
    N = int(raw_input())
    l = []
    while N > 0:
        s = raw_input().strip().split()
        command = s[0]
        args = s[1:]
        if command != 'print':
            command += '(' + ','.join(args) + ')'
            eval("l."+command)
        else:
            print l
        N -= 1
