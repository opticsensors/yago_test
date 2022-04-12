import numpy as np

paths=np.array([[0.1,0.8,0.8,0.3,0.5,0.4],
                [0.7,0.8,0.1,0.0,0.8,0.4],
                [0.8,0.0,0.4,0.7,0.2,0.9],
                [0.9,0.0,0.0,0.5,0.9,0.4],
                [0.2,0.4,0.0,0.2,0.4,0.5],
                [0.2,0.4,0.2,0.5,0.3,0.0],
                ])

init_cell = 3
a,b = paths.shape
l_izq = init_cell
l_der = b-(init_cell+1)

for f in range(a):
    for c in range(b):
        if f+c < l_izq or (f<l_der and c-init_cell>f) :
            paths[f,c] = np.inf
        else:
            pass
        
def select_options(array,f,c):
    if c==0:
        return list(np.append(np.array([np.inf]),array[f-1,c:c+2]))
    elif c==b-1:
        return list(np.append(array[f-1,c-1:c+1],np.array([np.inf])))
    else:
        return list(array[f-1,c-1:c+2])

PATH = {}

for c in range(b):
    print('Vamos por la columna '+str(c))
    f=a-1
    path = [paths[a-1,c]]
    while f != 1:
        print('  Vamos por la fila '+str(f))########
        f-=1
        opts = select_options(paths,f,c)
        c += opts.index(min(opts))-1
        print('>> Así está el path interno:')######################
        path.append(paths[f,c])
        print(path)##########################
    PATH[str(f)+str(c)] = path
    print(PATH)
    print('Añadido interno a base de paths')#####

a = 1
