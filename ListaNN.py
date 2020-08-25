def Lista(nn):#funcao chamamos ela por def, nn é o que vamos passar para essa funcao
  y=[]
  for i in range(nn):
    x=[]
    for j in range(nn):
      x.append(j)
    y.append(x)
  return y 
