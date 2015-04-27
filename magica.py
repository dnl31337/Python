import numpy as np

def embaralha(coluna):
    if coluna == 0:
        w = y[:,1][::-1]
        w = np.concatenate((w,y[:,0][::-1]))
        w = np.concatenate((w,y[:,2][::-1]))
    elif coluna == 1:
        w = y[:,2][::-1]
        w = np.concatenate((w,y[:,1][::-1]))
        w = np.concatenate((w,y[:,0][::-1]))
    else:
        w = y[:,0][::-1]
        w = np.concatenate((w,y[:,2][::-1]))
        w = np.concatenate((w,y[:,1][::-1]))
    w = w.reshape((7,3))
    return(w)


x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]])
y = x.copy()
t = 0

print '*******************************************'
print '* Esta eh uma pequena magica usando Numpy *'
print '*                                         *'
print '* Vou advinhar o numero que voce escolheu *'
print '*******************************************'


print '\nEscolha um numero abaixo, e apenas me informe qual coluna ele esta....\n'
print ' Colunas\n\n[0] [1] [2]\n\n'
print(x)
col = int(raw_input('\nDigite o numero da coluna que ele esta (Ex: 0, 1 ou 2): '))

while t <2:
    
    print'\n'
    w = embaralha(col)
    y = w.copy()
    print w
    t+=1
    col = int(raw_input('\nDigite o numero da coluna que ele esta (Ex: 0, 1 ou 2): '))
    

print '\nOpa voce escolheu o numero: %d'%(w[3,col])
print 'Acertei ne?! Magica com python...\n\n'
