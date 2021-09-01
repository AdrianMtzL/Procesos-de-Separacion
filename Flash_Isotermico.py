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
P_c = np.array([33.98, 50.41, 48.72, 46.0, 42.48, 37.96, 36.4]) #Presion critica [MPa]
P_c = P_c*1000 #Preción crítica, conversión a [kPa]
w = np.array([0.037, 0.087, 0.099, 0.142, 0.152, 0.2, 0.186]) #Factor acentrico
R = 8.314472 #Cte. de los gases [KPa-L/K-mol]
PM = np.array([28.014, 28.054, 30.07, 42.081, 44.097, 58.123, 58.123]) #Peso molecular g/mol
rho = np.array([1.165, 1.26, 1.264, 1.748, 1.882, 2.489, 2.489]) #Densidad del gas a condiciones normales[g/L]

# Parametros para definir la Ec. de SRK
Tr = T/T_c #Temperatura reducida
Pr = P/P_c #Presion reducida
m =  0.48 + 1.574*w - 0.176*w**2 #Parametro del factor acentrico
a =  (0.42748*((R*T_c)**2)/P_c)*((1+m*(1-Tr**0.5)))**2 #Parametro a
b =  0.08664*R*T_c/P_c #Parámetro b
v = PM/rho #Volumen molar [L/mol]
Psat = (R*T/(v-b))-(a/(v*(v+b))) # Ecuación de SRK
Ki = Psat/P #Constante de equilibrio

#Cálculo del Flash Isotérmico
psi = 0.5 #Estimado inicial de la fracción Vapor, psi = V/F
