from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
print data

for t,marker,c in zip(xrange(3),">ox","rgb"):
    plt.scatter(features[target == t,0],
                features[target == t,1],
                marker=marker,
                c=c)

#plt.show()

# based on first observation we can see that iris setosa is
# different there clearly lies a separation from the other 2 datasets

plength = features[:,2]   # features = [pwidth,plength,swidth,slength]

# use numpy indexing
labels = target_names[target]

is_setosa = (labels == 'setosa')

max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

# following gives us a good threshold to separate sentosa from the others
print 'Maximum of setosa:', max_setosa
print 'Minimum of others:', min_non_setosa


# In order to separate versicolor and verginica we need something more
