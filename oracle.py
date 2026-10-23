import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def crates(n, c):
    k = -(-n//c)
    return f"The {pl(n,' item',' items')} at {pl(c,' item',' items')} a crate {v(n,'makes','make')} {pl(k,' crate',' crates')}, the last crate covering {pl(n-(k-1)*c,' item',' items')}."
def weight(k, w, tr):
    t = k*w; trips = -(-t//tr)
    return f"The {pl(k,' crate',' crates')} at {pl(w,' kilogram',' kilograms')} a crate {v(k,'weighs','weigh')} {pl(t,' kilogram',' kilograms')}, {pl(trips,' trip',' trips')} at {pl(tr,' kilogram',' kilograms')} a trip, the last trip carrying {pl(t-(trips-1)*tr,' kilogram',' kilograms')}."
def cost(k, pc, n):
    cc = k*pc
    pi = (2*cc + n)//(2*n)
    return f"The {pl(k,' crate',' crates')} at ${m(pc)} a crate {v(k,'comes','come')} to ${m(cc)}, ${m(pi)} an item."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' item',' items')} at {pl(pm,' item',' items')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(776)
R = random.randint
cases = [
 dict(fn="crates", args=["5000","48"], expect=crates(5000,48)),
 dict(fn="weight", args=["105","12","500"], expect=weight(105,12,500)),
 dict(fn="cost", args=["105","14.50","5000"], expect=cost(105,1450,5000)),
 dict(fn="time", args=["5000","41"], expect=time_(5000,41)),
 dict(fn="crates", args=["1","1"], expect=crates(1,1)),
 dict(fn="crates", args=["4800","48"], expect=crates(4800,48)),
 dict(fn="crates", args=["1000000","10000"], expect=crates(1000000,10000)),
 dict(fn="weight", args=["1","1","1"], expect=weight(1,1,1)),
 dict(fn="weight", args=["10","10","500"], expect=weight(10,10,500)),
 dict(fn="weight", args=["100000","1000","100000"], expect=weight(100000,1000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","1000"], expect=time_(1000000,1000)),
]
for _ in range(20):
    n,c=R(1,1000000),R(1,10000); cases.append(dict(fn="crates", args=[str(n),str(c)], expect=crates(n,c)))
for _ in range(20):
    k,w,tr=R(1,100000),R(1,1000),R(1,100000); cases.append(dict(fn="weight", args=[str(k),str(w),str(tr)], expect=weight(k,w,tr)))
for _ in range(25):
    k,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(k),dec(p),str(n)], expect=cost(k,p,n)))
for _ in range(19):
    n,pm=R(1,1000000),R(1,1000); cases.append(dict(fn="time", args=[str(n),str(pm)], expect=time_(n,pm)))
errs=[["crates",["0","48"]],["crates",["1000001","48"]],["crates",["2.5","48"]],["crates",["5000","0"]],["crates",["5000","10001"]],
 ["weight",["0","12","500"]],["weight",["100001","12","500"]],["weight",["105","0","500"]],["weight",["105","1001","500"]],["weight",["105","12","0"]],
 ["cost",["0","14.50","5000"]],["cost",["105","0","5000"]],["cost",["105","1000","5000"]],["cost",["105","14.505","5000"]],["cost",["105","14.50","0"]],
 ["time",["0","41"]],["time",["5000","0"]],["time",["5000","1001"]],["time",["5000","41.5"]],["weight",["105","1.5","500"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
