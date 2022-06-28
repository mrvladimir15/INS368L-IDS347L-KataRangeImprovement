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