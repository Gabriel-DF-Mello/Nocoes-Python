import csv

class glicemia:
  def __init__(self,dia_semana, data, ad_comer, resultado, dose_insulina, kcal, carb, sono):
    self.dia_semana = dia_semana
    self.ad_comer = ad_comer
    self.data = data
    self.resultado = resultado
    self.dose_insulina = dose_insulina
    self.kcal = kcal
    self.carb = carb
    self.sono = sono

  def __str__(self):
    return f"Glicemia({self.dia_semana}, {self.data}, {self.ad_comer}, {self.resultado}, {self.dose_insulina}, {self.kcal}, {self.carb}, {self.sono})"

def extract_data(filename):
  file = open(filename)

  csvreader = csv.reader(file)
  header = []
  header = next(csvreader)

  result = []
  rows = []
  for row in csvreader:
    rows.append(row)

  for row in rows:
    result.append(glicemia(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

  return result

def media(list):
  sum = 0
  count = 0
  if len(list) > 0:
    for value in list:
      sum += value
      count += 1
    return sum/count
  return 0

def bubble(arr):
  n = len(arr)
  for i in range(n-1):
    swapped = False
    for j in range(0, n-i-1):
      if arr[j] > arr[j + 1]:
        swapped = True
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    if not swapped:
      return

def mediana(list):
  bubble(list)
  n = int(len(list)/2)
  if((len(list))%2 == 0):
    return (list[n]+list[n-1])/2
  return list[n]

def moda(list):
  bubble(list)
  h_count = 0
  h_value = []
  count = 0
  current = -1
  for value in list:
    if(value != current):
      current = value
      count = 1
    else:
      count += 1
    if(count == h_count):
      h_value.append(value)
    if count > h_count:
        h_count = count
        h_value = [value]
  return {"moda": h_value,
          "contagem": h_count}

def medias(list):
  #glicemia, kcal, carb
  glic_l = []
  kcal_l = []
  carb_l = []
  for val in list:
    if(val.kcal == ''):
      val.kcal = 0
    if(val.carb == ''):
      val.carb = 0
    glic_l.append(int(val.resultado))
    kcal_l.append(int(val.kcal))
    carb_l.append(int(val.carb))

  print(f"Média glicemia: {media(glic_l):.2f}\nMédia kcal: {media(kcal_l):.2f}\nMédia carb: {media(carb_l):.2f}\n")
  return

def medianas(list):
  #glicemia, kcal, carb
  glic_l = []
  kcal_l = []
  carb_l = []
  for val in list:
    if(val.kcal == ''):
      val.kcal = 0
    if(val.carb == ''):
      val.carb = 0
    glic_l.append(int(val.resultado))
    kcal_l.append(int(val.kcal))
    carb_l.append(int(val.carb))

  print(f"Mediana glicemia: {mediana(glic_l)}\nMediana kcal: {mediana(kcal_l)}\nMediana carb: {mediana(carb_l)}\n")
  return

def modas(list):
  #glicemia, kcal, carb
  glic_l = []
  kcal_l = []
  carb_l = []
  for val in list:
    if(val.kcal == ''):
      val.kcal = 0
    if(val.carb == ''):
      val.carb = 0
    glic_l.append(int(val.resultado))
    kcal_l.append(int(val.kcal))
    carb_l.append(int(val.carb))

  print(f"Moda glicemia: {moda(glic_l)}\nModa kcal: {moda(kcal_l)}\nModa carb: {moda(carb_l)}\n")
  return

glicemia_list = extract_data('glicose_data_suja.csv')

medias(glicemia_list)
medianas(glicemia_list)
modas(glicemia_list)

