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
        fn1 = getFN(self.interval)
        ln1 = getLN(self.interval)
        li1 = getLI(self.interval)

        fi2 = getFI(self.interval)
        fn2 = getFN(self.interval)
        ln2 = getLN(self.interval)
        li2 = getLI(self.interval)
    # getting first interval
        if fi1 == "(":
            fn1 += 1
        elif  fi1 == "[":
            pass
        else:
            return "Ivalid first interval opening symbol"  
    # getting final interval
        if li1 == ")":
            ln1 -= 1
        elif  li1 == "]":
            pass
        else:
            return "Ivalid Last interval opening symbol"  
    # getting second part of interval
        if fi2 == "(":
            fn2 += 1
        elif fi2 == "[":
            pass
        else:
            return "Invalid second interval opening symbol"
    # getting last part of interval
        if li2 == ")":
            ln2 -= 1
        elif li2 == "]":
            pass
        else:
            return "Invalid second interval closing symbol"
        
        aR = range(fn1, ln1)
        bR = range(fn2, ln2)
        
        if aR == bR:
            return True
        else:
            return False
        

    def getAllpoints(self):
        fi1 = getFI(self.interval)
        fn1 = getFN(self.interval)
        ln1 = getLN(self.interval)
        li1 = getLI(self.interval)
    #getting first interval
        if fi1 == "(":
            fn1 += 1
        elif fi1 == "[":
            pass
        else:
            return "Invalid first interval opening symbol"
    #Getting last interval
        if li1 == ")":
            ln1 -= 1
        elif li1 == "]":
            pass
        else:
            return "Invalid final interval closing symbol"

        while fn1 <= ln1:
            print(fn1)
            fn1 += 1

    def containsRange(self, interval2):
        fi1 = getFI(self.interval)
        fn1 = getFN(self.interval)
        ln1 = getLN(self.interval)
        li1 = getLI(self.interval)

        fi2 = getFI(self.interval)
        fn2 = getFN(self.interval)
        ln2 = getLN(self.interval)
        li2 = getLI(self.interval)
        
        # getting first interval
        if fi1 == "(":
            fn1 += 1
        elif  fi1 == "[":
            pass
        else:
            return "Ivalid first interval opening symbol"  
    # getting final interval
        if li1 == ")":
            ln1 -= 1
        elif  li1 == "]":
            pass
        else:
            return "Ivalid Last interval opening symbol"  
    # getting second part of interval
        if fi2 == "(":
            fn2 += 1
        elif fi2 == "[":
            pass
        else:
            return "Invalid second interval opening symbol"
    # getting last part of interval
        if li2 == ")":
            ln2 -= 1
        elif li2 == "]":
            pass
        else:
            return "Invalid second interval closing symbol"
        
        if fn1 <= fn2 and ln1 >= ln2:
            return True
        else:
            return False
    
    def endPoints(self):
        fi1 = getFI(self.interval)
        fn1 = getFN(self.interval)
        ln1 = getLN(self.interval)
        li1 = getLI(self.interval)
    #getting first interval
        if fi1 == "(":
            fn1 += 1
        elif fi1 == "[":
            pass
        else:
            return "Invalid first interval opening symbol"
    #Getting last interval
        if li1 == ")":
            ln1 -= 1
        elif li1 == "]":
            pass
        else:
            return "Invalid final interval closing symbol"
        
        return fn1, ln1
            
a=Range("(2,7]")
b=Range("[3,8)")

# print(a.getEquals(b.interval))
# print(a.getAllpoints())
# print(a.containsRange(b.interval))
print(a.endPoints())