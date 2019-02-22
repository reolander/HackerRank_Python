def is_leap(year):
    leap = False
    if not year % 4:
        if not year % 100:
            if not year % 400:
                leap = True
                return leap
        else:
            leap = True
            return leap
    return leap

year = int(raw_input())
print is_leap(year)