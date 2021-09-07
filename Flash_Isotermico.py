# coding=utf-8
# Flash Isotermico multicomponente
# Equipo 2: Gabriela, Saul y Adrian
# Modelo Termodinamico: SRK
import numpy as np

# Condiciones del flash y la corriente de Alimentacion
P = 2620 #[kPa]
T = 281.25 #[K]
F = 100 #[lbmol/h]
z = np.array([0.0016, 0.193, 0.1363, 0.2515, 0.2742, 0.091, 0.0524])# Composicion de entrada

# Propiedades de los compuestos puros
Componentes = ['Nitrogeno','Etileno','Etano','Propileno','Propano','n-butano','i-butano']
T_c = np.array([126.2, 282.34, 305.32, 364.9, 369.83, 425.12, 407.85]) #Temperatura critica [K]
P_c = np.array([3.398, 5.041, 4.872, 4.60, 4.248, 3.796, 3.64]) #Presion critica [MPa]
P_c = P_c*1000 #Preción crítica, conversión a [kPa]
w = np.array([0.037, 0.087, 0.099, 0.142, 0.152, 0.2, 0.186]) #Factor acentrico
R = 8.314472 #Cte. de los gases [KPa-L/K-mol]
PM = np.array([28.014, 28.054, 30.07, 42.081, 44.097, 58.123, 58.123]) #Peso molecular g/mol
rho = np.array([1.165, 1.26, 1.264, 1.748, 1.882, 2.489, 2.489]) #Densidad del gas a condiciones normales[g/L]

# Parametros para definir la Ec. de SRK
Tr = T/T_c #Temperatura reducida
Pr = P/P_c #Presion reducida
m =  0.48 + 1.574*w - 0.176*(w**2) #Parametro del factor acentrico
a =  (0.42748*((R*T_c)**2)/P_c)*(((1+m*(1-Tr**0.5)))**2) #Parametro a
b =  0.08664*R*T_c/P_c #Parámetro b
v = PM/rho #Volumen molar [L/mol]
Psat = (R*T/(v-b))-(a/(v*(v+b))) # Ecuación de SRK
Ki = Psat/P #Constante de equilibrio


#Cálculo del Flash Isotérmico
psi = 0.5 #Estimado inicial de la fracción Vapor, psi = V/F
suma = 0
suma2 = 0
RR = (z*(1-Ki))/(1+psi*(Ki-1)) #Ecuacion de Rachford-Rice
dRR = (z*(1-Ki)**2)/((1+psi*(Ki-1)))**2 #Derivada d(RR)/d(psi)

#Estos dos ciclos for, sirven para sumar cada elemento de la ec. de RR y de d(RR)/d(psi)
for num in RR:
	
	suma = suma + num
	 #Sumatoria de la Ec. de RR
	def RR(psi):
		return suma

for num in dRR:
	
	suma2 = suma2 + num
	def dRR(psi):
		return suma2

def MetodoNewton(psi,tolerancia=0.001):
	while True:
		psi1 = psi - suma/suma2
		tol = abs((psi1-psi)/psi1)
		if tol<tolerancia:
			break
		psi=psi1
	return psi

psi0 = MetodoNewton(psi)
print('psi: ', psi0)

#Teniendo ambas sumatorias se puede empezar a buscar la raiz:
#Método de Newton para 1 variable
#for i in range(100):
#	psinva = psi - float(RR(psi)/dRR(psi))
#	if abs (psi-psinva)<0.001: break
#	psi = psinva


		


