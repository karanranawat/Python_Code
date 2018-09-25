from Percolation import Percolation
import numpy as np
import math as mt
import random as rd

class PercolationStats(object):

    
    def __init__(self, N, T):
        #self.no_of_tries = 0
        self.total_tries = T
        self.monte_carlo_results = range(0,T)

        for i in range(0,T):
            self.p = Percolation(N)
            self.no_of_tries = 0.0

            self.tried_col_pairs = [[0 for x in range(N)] for x in range(N)]
            #print self.tried_col_pairs
            for j in range(0,N*N*2):
                self.row = rd.randrange(N)+1
                self.col = rd.randrange(N)+1

                if self.tried_col_pairs[self.row-1][self.col-1]==1:
                    continue
                else:
                   self.tried_col_pairs[self.row-1][self.col-1] = 1
                   self.no_of_tries += 1
                   self.p.open(self.row,self.col)

                   if self.p.percolates():
                       #print 'System percolates'                
                       self.monte_carlo_results[i] = self.no_of_tries/(N*N)
                       break
            self.p = None
            

    def mean(self):
       return np.mean(self.monte_carlo_results)

    def stdDev(self):
        return np.std(self.monte_carlo_results)

    def confidenceLo(self):
        return self.mean() - ((1.96 * self.stdDev()) / mt.sqrt(self.total_tries))

    def confidenceHi(self):
        return self.mean() + ((1.96 * self.stdDev()) / mt.sqrt(self.total_tries))

if __name__ == '__main__':
    N = 200 # Grid size
    T = 100 # No of tries
    
    pstats = PercolationStats(N,T)
    
    print 'mean \t\t\t= %f' % pstats.mean(),
    print 'stddev \t\t\t= %f' % pstats.stdDev()
    print pstats.confidenceLo()
    print pstats.confidenceHi()
 
            
