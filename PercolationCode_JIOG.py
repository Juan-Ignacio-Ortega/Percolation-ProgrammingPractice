def graficar(matrix):
  import matplotlib.pyplot as plt
  import matplotlib.colors as cls
  from IPython import display

  fig, ax = plt.subplots()
  colormap = cls.ListedColormap(["black", "red", "white"])
  im = ax.imshow(matrix, cmap = colormap)
  ax.set_xticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5], minor = True)
  ax.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5], minor = True)
  ax.grid(which='minor', color='black', linestyle='-', linewidth = 1)
  fig.tight_layout()
  display.clear_output(wait=True)
  plt.show()

def reiniciar(matrix, longitm):
  import numpy as np

  iterator = 0
  while iterator <= (longitm - 1):
    positions = []
    positions.append(np.where(matrix[iterator] == 1))
    for element in positions:
      matrix[iterator][element] = 2
    iterator += 1

m = 10
n = 10
tot_vent = m * n
prob_tap = 40

import random as rd

cant_ven_tap = ((tot_vent) * prob_tap) / 100
cont = 0
ven_tap = []
while cont <= (cant_ven_tap - 1):
  num_prop = rd.randint(0, (tot_vent - 1))
  if num_prop not in ven_tap:
    ven_tap.append(num_prop)
    cont += 1

import numpy as np
col_ini = []
countm = 0
while countm <= (m - 1):
  fila = []
  countn = 0
  while countn <= (n - 1):
    num_ven = (countm * 10) + countn
    if num_ven in ven_tap:
      num = 0
    else:
      num = 2
    fila.append(num)
    countn += 1
  col_ini.append(fila)
  countm += 1

col = np.array(col_ini)

graficar(col)

reiniciar(col, m)

import matplotlib.pyplot as plt

result = 'Sin probar'
countm = 0
countn = 0
estado = 0
while countm <= (m - 1):
  if (col[countm][countn] == 2) and (estado == 0):
    col[countm][countn] = 1
    countm += 1
    graficar(col)
    if countm == m:
      result = 'Percola'
  elif (col[countm][countn] == 1) and (estado == 0):
    col[countm][countn] = 2
    countn += 1
    if countn == n:
          result = 'No percola'
          countm = m
    graficar(col)
  elif (col[countm][countn] == 0) and (estado == 0) and (countm == 0):
    countn += 1
    if countn == n:
      result = 'No percola'
      countm = m
  elif (col[countm][countn] == 0) and (estado == 0) and (countm != 0):
    countm -= 1
    if countm == 0:
      estado = 0
    else:
      estado = 1
  elif (col[countm][countn] != 0) and (estado == 1):
    countn += 1 
    if countn > (n - 1):
      countn -= 1
      estado = 3
    elif col[countm][countn] == 1:
      countn -= 1
      estado = 3
    elif col[countm][countn] != 1:
      estado = 2  
  elif (col[countm][countn] == 0) and (estado == 2):
    countn -= 1
    estado = 3
    if (countn == (n - 1)) and (countm == 0):
      result = 'No percola'
      countm = m
  elif (col[countm][countn] == 2) and (estado == 2):
    col[countm][countn] = 1
    countm += 1
    estado = 0
    graficar(col)
  elif (col[countm][countn] != 0) and (estado == 3):
    countn -= 1
    if countn < 0:
      countn += 1
      estado = 5
    elif col[countm][countn] == 1:
      countn += 1
      estado = 5
    elif col[countm][countn] != 1:
      estado = 4
  elif (col[countm][countn] == 0) and (estado == 4):
    countn += 1
    estado = 5
  elif (col[countm][countn] == 2) and (estado == 4):
    col[countm][countn] = 1
    countm += 1
    estado = 0
    graficar(col)
  elif (col[countm][countn] != 0) and (estado == 5):
    col[countm][countn] = 2
    if (countn < (n - 1)) and (col[countm][countn + 1] == 1):
      countn += 1
    elif (countn > 0) and (col[countm][countn - 1] == 1):
        countn -= 1
        if col[countm][countn - 1] != 1:
          estado = 6
    elif col[countm - 1][countn] == 1:
      countm -= 1
      estado = 1
      if countm == 0:
        col[countm][countn] = 2
        countn += 1
        estado = 0
        if countn == n:
          result = 'No percola'
          countm = m
    graficar(col)
  elif (col[countm][countn] != 0) and (estado == 6):
    countn -= 1
    estado = 4
    if countn < 0:
      countn += 1
      estado = 5

print(result)

def PruebaDePercolacion(Min, Nin, Prob):
  m = Min
  n = Nin
  tot_vent = m * n
  prob_tap = Prob

  import random as rd

  cant_ven_tap = ((tot_vent) * prob_tap) / 100
  cont = 0
  ven_tap = []
  while cont <= (cant_ven_tap - 1):
    num_prop = rd.randint(0, (tot_vent - 1))
    if num_prop not in ven_tap:
      ven_tap.append(num_prop)
      cont += 1

  import numpy as np
  col_ini = []
  countm = 0
  while countm <= (m - 1):
    fila = []
    countn = 0
    while countn <= (n - 1):
      num_ven = (countm * 10) + countn
      if num_ven in ven_tap:
        num = 0
      else:
        num = 2
      fila.append(num)
      countn += 1
    col_ini.append(fila)
    countm += 1

  col = np.array(col_ini)

  import matplotlib.pyplot as plt

  result = 'Sin probar'
  countm = 0
  countn = 0
  estado = 0
  while countm <= (m - 1):
    if (col[countm][countn] == 2) and (estado == 0):
      col[countm][countn] = 1
      countm += 1
      #graficar(col)
      if countm == m:
        result = 'Percola'
    elif (col[countm][countn] == 1) and (estado == 0):
      col[countm][countn] = 2
      countn += 1
      if countn == n:
            result = 'No percola'
            countm = m
      #graficar(col)
    elif (col[countm][countn] == 0) and (estado == 0) and (countm == 0):
      countn += 1
      if countn == n:
        result = 'No percola'
        countm = m
    elif (col[countm][countn] == 0) and (estado == 0) and (countm != 0):
      countm -= 1
      if countm == 0:
        estado = 0
      else:
        estado = 1
    elif (col[countm][countn] != 0) and (estado == 1):
      countn += 1 
      if countn > (n - 1):
        countn -= 1
        estado = 3
      elif col[countm][countn] == 1:
        countn -= 1
        estado = 3
      elif col[countm][countn] != 1:
        estado = 2  
    elif (col[countm][countn] == 0) and (estado == 2):
      countn -= 1
      estado = 3
      if (countn == (n - 1)) and (countm == 0):
        result = 'No percola'
        countm = m
    elif (col[countm][countn] == 2) and (estado == 2):
      col[countm][countn] = 1
      countm += 1
      estado = 0
      #graficar(col)
    elif (col[countm][countn] != 0) and (estado == 3):
      countn -= 1
      if countn < 0:
        countn += 1
        estado = 5
      elif col[countm][countn] == 1:
        countn += 1
        estado = 5
      elif col[countm][countn] != 1:
        estado = 4
    elif (col[countm][countn] == 0) and (estado == 4):
      countn += 1
      estado = 5
    elif (col[countm][countn] == 2) and (estado == 4):
      col[countm][countn] = 1
      countm += 1
      estado = 0
      #graficar(col)
    elif (col[countm][countn] != 0) and (estado == 5):
      col[countm][countn] = 2
      if (countn < (n - 1)) and (col[countm][countn + 1] == 1):
        countn += 1
      elif (countn > 0) and (col[countm][countn - 1] == 1):
          countn -= 1
          if col[countm][countn - 1] != 1:
            estado = 6
      elif col[countm - 1][countn] == 1:
        countm -= 1
        estado = 1
        if countm == 0:
          col[countm][countn] = 2
          countn += 1
          estado = 0
          if countn == n:
            result = 'No percola'
            countm = m
      #graficar(col)
    elif (col[countm][countn] != 0) and (estado == 6):
      countn -= 1
      estado = 4
      if countn < 0:
        countn += 1
        estado = 5

  return(result)

Porcentaje = 0
porce_efect = 100
while (Porcentaje <= 100) and (porce_efect >= 80):
  NdP = 0
  results = []
  while NdP <= 99:
    temporal_result = PruebaDePercolacion(10, 10, Porcentaje)
    if temporal_result == 'No percola':
      results.append(0)
    else:
      results.append(1)
    NdP += 1
  
  porce_efect = sum(results)

  Porcentaje_parcial = str(Porcentaje)
  Porcentaje_efect_parcial = str(porce_efect)
  print('Con un porcentaje de obstrucción del', Porcentaje_parcial + '%, nos da un porcentaje de efectividad del', Porcentaje_efect_parcial + '%.')

  Porcentaje += 1

Porcentaje_fin = str(Porcentaje - 2)

print('La percolación crítica es igual a', Porcentaje_fin + '%.')