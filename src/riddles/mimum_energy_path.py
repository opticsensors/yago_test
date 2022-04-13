import numpy as np

paths=np.array([[0.1,0.8,0.8,0.3,0.5,0.4],
                [0.7,0.8,0.1,0.0,0.8,0.4],
                [0.8,0.0,0.4,0.7,0.2,0.9],
                [0.9,0.0,0.0,0.5,0.9,0.4],
                [0.2,0.4,0.0,0.2,0.4,0.5],
                [0.2,0.4,0.2,0.5,0.3,0.0],
                ])

pintar_diagramas = False

init_cell = 3 # cell de la primera fila que escogemo
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

for bottom_start in range(b):
    print('Vamos por la columna '+str(bottom_start))
    f, c = a-1, bottom_start
    path = [(paths[f,c],(c+1,a-f))]
    while f != 0:
        print('  Vamos por la fila '+str(f))########
        opts = select_options(paths,f,c)
        c += opts.index(min(opts))-1
        f -= 1
        print('>> Así está el path interno:')######################
        path.append((paths[f,c],(c+1,a-f)))
        print(path)##########################
    PATH[bottom_start] = path
    print(PATH)
    print('Añadido interno a base de paths')#####

resulting_paths = []
for data_path in list(PATH.values()):
    resulting_paths.append([pair[0] for pair in data_path])

resulting_indexed_paths = []
for data_path in list(PATH.values()):
    resulting_indexed_paths.append([pair[1] for pair in data_path])

lengths = [sum(path) for path in resulting_paths]
chosen_index = lengths.index(min(lengths))
minimum_path = resulting_paths[chosen_index]

print('\nCamino mínimo')
print(minimum_path)

import matplotlib.pyplot as plt
from colour import Color

def paint_squares (M,color_cells=[],gradient=False,title=None,iter=None,grid=True,display_nums=True,mgn=0.1) :
    print(color_cells)
    print(M)
    for _ in range(M.shape[0]):
        plt.scatter(0,_+1,c='black',s=1)
    for _ in range(M.shape[1]):
        plt.scatter(_+1,0,c='black',s=1)
    plt.scatter(0,0,c='black',s=1)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            x,y = 1+j, M.shape[0]-i
            if grid == True:
                plt.scatter(x,y,c='black',s=1)
            if display_nums:
                plt.annotate(round(M[i,j],1),(x-0.5,y-0.5))

            if color_cells != []:
                if (x,y) in color_cells:
                    color = '#ffcc00'
                    plt.fill_between([x-1+mgn,x-mgn],[y-1+mgn,y-1+mgn],[y-mgn,y-mgn],color=color)
            if gradient:

                if M[a-y,x-1] != np.inf:
                    color = list(Color('salmon').range_to(Color('red'),1000))[int(M[a-y,x-1]*1000)-1]
                    plt.fill_between([x-1+mgn,x-mgn],[y-1+mgn,y-1+mgn],[y-mgn,y-mgn],color=color.hex)
    plt.title(title)
    plt.show()

if pintar_diagramas:
    paint_squares(paths,resulting_indexed_paths[chosen_index])
    paint_squares(paths,gradient=True)
a = 1