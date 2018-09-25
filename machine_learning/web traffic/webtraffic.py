import scipy as sp
import matplotlib.pyplot as plt

def error(f, x, y):
    return sp.sum((f(x)-y)**2)


data = sp.genfromtxt("web_traffic.tsv", delimiter = "\t")

print(data[:10])

x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x,y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
#plt.show()

'''
Find the real model behind the noisy data
Extrapolate into the future to find the point in time  when
infra needs to be extended
'''

# get a polyfit line of degree 1
fp1, residuals, rank, sv, rcond = sp.polyfit(x,y,1,full=True)
print("Model parameters: %s" % fp1)

# error of approximation
print(residuals)

f1 = sp.poly1d(fp1)
print "Error 1 D model = " , error(f1,x,y)

fx = sp.linspace(0,x[-1],1000)

plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")
#plt.show()

# get a polyfit for degree 2
f2p = sp.polyfit(x,y,2)
f2 = sp.poly1d(f2p)
print "Error 2 D model = " , error(f2,x,y)

# The more complex the data gets the curves capture it better
fx = sp.linspace(0,x[-1],1000)

plt.plot(fx, f2(fx), linewidth=4)
plt.legend(["d=%i" % f2.order], loc="upper left")
#plt.show()

inflection = 3.5*7*24 # approximate the inflection point based on observation
inflection = int(inflection)
#data before inflection
xa = x[:inflection]
ya = y[:inflection]
#data after inflection
xb = x[inflection:]
yb = x[inflection:]


fa = sp.poly1d(sp.polyfit(xa,ya,1))
fb = sp.poly1d(sp.polyfit(xb, yb, 1))

fa_error = error(fa, xa, ya)
fb_error = error(fb, xb, yb)

print "Error in inflection=%f" % (fa_error+fb_error)
