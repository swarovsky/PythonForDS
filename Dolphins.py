
# coding: utf-8
#Version Networkx 1.9.1 needed for dolphins.gml file
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.linalg import eigh

file_name='dolphins.gml'
class graphe_dauphins:
    def __init__(self):
        G = nx.Graph()
    
    def get_graph(self,file_name):
        G = nx.read_gml(file_name)
        return G
    def plot_mygraph(self,G):
        return nx.draw_networkx(G)
       
    def bissection(self,v,g):
        communaute1=[]
        communaute2=[]
        
        tab=np.array(v[:,1])
        
        for i in range(len(tab)):
            if tab[i]<0:
                communaute1.append(i)                
            else:
                communaute2.append(i)
        pos=nx.spring_layout(g)
        nx.draw_networkx(g,pos,nodelist=communaute1)
        nx.draw_networkx(g,pos,nodelist=communaute2)   
        
    
    
#Question1
mygraph = graphe_dauphins()
g = mygraph.get_graph(file_name) 
print(g)
print(mygraph.plot_mygraph(g))

#Question2
L=nx.laplacian_matrix(G)
L=L.todense()

hermitian = L.getH()
np.linalg.eigh(hermitian)

w, v = eigh(L)
x = v[:,1] 
y = v[:,2]
spectral_coordinates = {i : (x[i], y[i]) for i in range(62)}
print(spectral_coordinates)

#Question3
fig=plt.figure(1)
plt.plot(x,y)
#Question4
liste = [(w[0],v[0]),(w[1],v[1]),(w[2],v[2])]
print(liste)
#Question5
mygraph.bissection(v,g)

