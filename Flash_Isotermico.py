# Flash Isotermico multicomponente
# Equipo 2: Gabriela, Saul y Adrian
# Modelo Termodinamico: SRK
import numpy as np

# Propiedades de los compuestos puros
Componentes = ['Nitrogeno','Etileno','Etano','Propileno','Propano','n-butano','i-butano']
T_c = np.array([126.2, 282.34, 305.32, 364.9, 369.83, 425.12, 407.85]) #Temperatura critica [K]
P_c = np.array([33.98, 50.41, 48.72, 46.0, 42.48, 37.96, 36.4]) #Presion critica [MPa]
w = np.array([0.037, 0.087, 0.099, 0.142, 0.152, 0.2, 0.186]) #Factor acentrico
PM = np.array([28.014, 28.054, 30.07, 42.081, 44.097, 58.123, 58.123]) #Peso molecular lb/lbmol

# Condiciones del flash y la corriente de Alimentación
P = 2.62 #[MPa]
T = 281.25 #[K]
F = 100 #[lbmol/h]
z = np.array([0.0016, 0.193, 0.1363, 0.2515, 0.2742, 0.091, 0.0524])# Composición de entrada

# Parámetros para definir la Ec. de SRK
R = 8.314472 #Cte. de los gases [KPa-L/K-mol]
