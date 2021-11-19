from .http import Http
import math


class CurveFitController(Http):

    def curveFit(self, arrayX, arrayY):

        vectorX = arrayX
        vectorY = arrayY

        pairs = (len(vectorX) + len(vectorY)) / 2  

        def sumX2(vec):
            i = 0
            sum = 0

            while i < len(vec):
                sum += math.pow(vec[i], 2)
                i += 1

            return sum

        def sumY(vec):
            i = 0
            sum = 0

            while i < len(vec):
                sum += vec[i]
                i += 1

            return sum

        def sumX(vet):
            i = 0
            sum = 0

            while i < len(vet):
                sum += vet[i]
                i += 1

            return sum

        def sumXY(vetX, vetY, tam):
            i = 0
            sum = 0

            while i < tam:
                sum += vetX[i] * vetY[i]
                i += 1

            return sum

        def sum2X(vet):
            i = 0
            sum = 0

            while i < len(vet):
                sum += vet[i]
                i += 1

            return math.pow(sum, 2)

        def a1(sumX2, sumY, sumX, sumXxY, pairs):

            a1 = ((sumX2 * sumY) - (sumX * sumXxY)) / ((pairs * (sumX2)) - (math.pow(sumX, 2)))
            return a1

        def a2(sumX2, sumY, sumX, sumXxY, sum2X, pairs):

            a2 = ((pairs * (sumXxY)) - (sumX * sumY)) / ((pairs * (sumX2)) - sum2X)
            return a2

        def generateNewPairs(a1, a2, vet):
            i = 0
            array = []

            while i < len(vet):
                y = a1 + (a2 * vet[i])
                string = f"{vet[i]:.2f}, {y:.2f}"
                array.append(string)
                i += 1
            return array

        newPairs = generateNewPairs(a1(sumX2(vectorX), sumY(vectorY), sumX(vectorX), sumXY(vectorX, vectorY, pairs), pairs), a2(sumX2(vectorX), sumY(vectorY), sumX(vectorX), sumXY(vectorX, vectorY, pairs), sum2X(vectorX), pairs), vectorX)

        stringPairs = ""
        for i in newPairs:
            stringPairs += f"({i}) "
        
        return stringPairs          

    def curveFit_newPairs(self, body):
        if not body["pointsX"] or int(body["pointsX"].isnumeric()) == True or body["pointsY"] or int(body["pointsY"].isnumeric()) == True:
            self.bad_request("Par ordenado inválido!")
        x = body["pointsX"]
        y = body["pointsY"]
        arrayX = x.split(",")
        arrayY = y.split(",")
        arrayFloatX = []
        arrayFloatY = []
        for i in arrayX:
            arrayFloatX.append(float(i))
        for j in arrayY:
            arrayFloatY.append(float(j))
        if len(arrayFloatX) < 2 or len(arrayFloatY) < 2 or len(arrayFloatX) != len(arrayFloatY):
            self.bad_request("Operação inválida")
        try:
            result = self.curveFit(arrayFloatX, arrayFloatY)
            return self._return_result(result)
        except Exception as e:
            if str(e).find("Sympify of expression 'could not parse") != -1:
                return self.bad_request("Pares ordenados inválidos")
            return self.server_error(e)

    def _return_result(self, result):

        return self.ok(
            {"result": "R= " + result}
        )