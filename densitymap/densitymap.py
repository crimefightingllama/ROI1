# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:25:54 2023

@author: shuyu
"""
import numpy as np
import scipy.spatial as spatial
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 200

class DM():
    def __init__(self, x,y,r,no_candidates):
        self.x = x
        self.y = y
        self.tree = spatial.KDTree(np.stack((x,y),1))
        self.radius = r
        self.neighbors = self.tree.query_ball_tree(self.tree, self.radius)
    
        self.frequency = np.fromiter(map(len, self.neighbors), dtype = float)
        self.density = self.frequency/self.radius**2
        self.n= no_candidates
        
    def newtree(self,x,y):
        self.nx = x
        self.ny = y
        self.ntree = spatial.KDTree(np.stack((x,y),1))
        self.nneighbors = self.ntree.query_ball_tree(self.ntree, self.radius)
        self.nfrequency = np.fromiter(map(len, self.nneighbors), dtype = float)
        self.ndensity = self.nfrequency/self.radius**2
   
    def plot(self):
        candidates = []
        self.nx = self.x.copy()
        self.ny = self.y.copy()
        while self.n >0 :
            self.newtree(self.nx, self.ny)
            maxi = np.where(self.nfrequency == max(self.nfrequency))[0][0]
            candidates.append([self.nx[maxi],self.ny[maxi]])
            todelete = self.nneighbors[maxi].copy()
            todelete.append(maxi)
            self.nx = np.delete(self.nx, todelete)
            self.ny = np.delete(self.ny, todelete)
            print('annotation n = ',self.n)
            self.n -= 1
        candidates= np.array(candidates)
        print(candidates)
        plt.figure()

        plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        contour = plt.tricontourf(self.x,self.y,self.density,levels = 10)
        plt.xlabel('µm')
        plt.ylabel('µm')
        cbar = plt.colorbar()
        cbar.formatter.set_scientific(True)
        cbar.formatter.set_powerlimits((0,0))
        cbar.update_ticks()
        cbar.ax.set_ylabel(r'cell density $({µm}^{-2})$', rotation=270,labelpad = 25)
        n = 1
        for candidate in candidates:
            cand = plt.Circle(candidate,3*self.radius,color = 'r',linewidth = 5, fill = False)
            plt.text(*candidate, n, color = 'w')
            n+= 1
            plt.gca().add_patch(cand)
        # plt.gca().add_patch(sparsest)
        plt.gca().set_aspect('equal')

