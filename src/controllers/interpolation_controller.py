from .http import Http
import numpy as np
from sympy import *

class InterpolationController(Http):
    
    # calculator auxiliary functions
    def stringToArray(self, string): #ex: 1,2;3,4 -> [[1.0, 2.0], [3.0, 4.0]]
      string = string.split(";")
      array = []
      aux = []
      for i in string:
        coordenada = i.split(",") 
        aux = []
        for j in coordenada:
          aux.append(float(j))
        array.append(aux)
      return array      

    def gauss_elimination(self, a,b,n): 
      n = np.size(b)
      for k in range (n-1):
        for i in range(k+1,n):       
          m = a[i, k]/a[k, k]
          a[i,:] = (a[i,:] - m*a[k,:])
          b[i] = b[i] - m*b[k]

      x = np.zeros(n)
      x[-1] = b[-1]/a[-1,-1]

      for i in reversed(range(n-1)):
        s = 0
        for j in range(i+1,n):
            s += a[i,j] * x[j]
        x[i] = (b[i]-s)/a[i,i]
      return x

    def polinomio_string(self, constantes): # retorna uma string do polinomio 
      n = 0
      s = "p(x): "
      for a in constantes:
          a = float('%g' % (a))
          absConstantToString = str(abs(a))
          constantToString = str(a)
          if ((absConstantToString == "1.0") and (n != 0)) : 
            absConstantToString = ""
            constantToString = ""
          
          if a != 0:
            if n == 0: 
              if a < 0:
                  s += "- " + absConstantToString
              else:
                  s += constantToString
          
            elif n == 1:
                if a < 0:
                    s += "- " + absConstantToString + "X"
                else:
                    s += "+ " + constantToString + "X"
            
            else:
                if a < 0:
                    s += "- " + absConstantToString + "X^" + str(n)
                else:
                    s += "+ " + absConstantToString + "X^" + str(n)
            s += " "
          n += 1
      return s

    def polinomio_resultado(self, x, constantes): # resolve o polinomio
      n = 0 
      f = 0
      for a in constantes:
          f += a*x**n 
          n += 1
      return f 

    # the calculation
    def calculation(self, coordinates):
      data = np.array(coordinates)
      n = np.size(data, 0)
      a = np.zeros([n,n]) 
      b = np.zeros(n) 

      for i in range(n):
        b[i] = data[i,1]   
        for j in range(n):  
          a[i,j] = data[i,0]**j
      
      constantes = self.gauss_elimination(a,b,n)

      # Codigo que gerava o grafico
      # x= data[:,0] 
      # y= data[:,1] 
      # xMin= np.min(x) 
      # xMax= np.max(x) 

      # xx= np.linspace(xMin, xMax, 1000) 
      # yy = self.polinomio_resultado(xx, constantes) 

      # # plt.plot(x, y, 'bo') 
      # # plt.plot(xx, yy) 
      # # plt.show() 

      return self.polinomio_string(constantes)
    
    # main
    def interpolation_expression(self, body):
        try:
            coordinates = body["coordinates"]
            array = self.stringToArray(coordinates) 
            result = self.calculation(array)
            return self._return_result(result) 
        except Exception as e:
            if str(e).find("Sympify of expression 'could not parse") != -1:
                return self.bad_request({"expressionError": "The expression is not valid"})
            return self.server_error()

    def _return_result(self, result):
        return self.ok({"result": str(result)})

    