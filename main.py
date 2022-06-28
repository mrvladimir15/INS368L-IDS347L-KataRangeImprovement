def getFI(interval):
    a=interval.strip()
    fi=a[0]
    return fi

def getFN(interval):
    a=interval.strip()
    fn=a[1: a.find(",")]
    return int(fn)

def getLN(interval):
    a=interval.strip()
    ln = a[a.find(",") +1 : -1]
    return int(ln)

def getLI(interval):
    a=interval.strip()
    li=a[-1]
    return li
class Range:
    def __init__(self, interval):
        self.interval = interval
    def getEquals(self, interval2):
        fi1 = getFI(self.interval)
        fn1 = getFI(self.interval)
        ln1 = getFI(self.interval)
        li1 = getFI(self.interval)

        fi2 = getFI(self.interval)
        fn2 = getFI(self.interval)
        ln2 = getFI(self.interval)
        li2 = getFI(self.interval)
    # getting first interval
        if fi1 == "(":
            fn1 += 1
        elif  fi1 == "[":
            pass
        else:
            return "Ivalid first interval opening symbol"  
    # getting final interval
        if li1 == "(":
            ln1 -= 1
        elif  li1 == "[":
            pass
        else:
            return "Ivalid Last interval opening symbol"  
