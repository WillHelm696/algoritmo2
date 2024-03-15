from avltree import *

#Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
#Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
#Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad.
def calculateBalance(AVLTree): 
    if AVLTree.root!=None:
        balance_factor(AVLTree.root)
    return AVLTree

def balance_factor(avlnode):
    if avlnode !=None:

        if avlnode.leftnode == avlnode.rightnode :
            avlnode.bf = 0
        elif avlnode.leftnode.bf != None and avlnode.rightnode.bf == None: 
            avlnode.bf = avlnode.leftnode.bf+1
        elif avlnode.leftnode.bf == None and avlnode.rightnode.bf != None: 
            avlnode.bf = avlnode.leftnode.bf+1 
        elif avlnode.leftnode.bf != None and avlnode.rightnode.bf != None: 
            avlnode.fb = haltura(avlnode.leftnode,0) - haltura(rightnode,0)
        balance_factor(avlnode.leftnode)
        balance_factor(avlnode.rightnode)

def haltura(avlnode,num):
    if avlnode!=None:
        haltura(avlnode.leftnode,num+1)
        if avlnode.rightnode!=None:
            return haltura(avltree.rightnode,num+1)
        return num + 1
    return num
