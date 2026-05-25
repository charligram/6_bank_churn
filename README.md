# 🧪 Proyecto churn de servicios del banco

## ❓ Planteamiento del proyecto
En un mundo en donde los dineros se trabajan mediante sistemas bancarios es natural que cada vez existan más organismos de este estilo, generando una gran competencia en donde los clientes tienen distintas opciones a elegir, por lo que es de gran importancia tener en claro cuales son los indicadores más claros que hacen de un cliente fiel al organismo bancario. Este proyecto se ha desarrollado con la intención de realizar un análisis sobre un dataset con datos bancarios de distintos usuarios, de los cuales, algunos han optado por retirarse y dejar de utilizar los productos del banco en cuestion. Con respecto a ello, es necesario identificar características que más influyen en la posibilidad de abandono de este caso. Además de generar modelos de Machine Learning capaces de predecir cuales son los clientes que potencialmente pueden realizar el abandono.

## ℹ️ Dataset
Recurso: Kaggle

Registros: 10000

## 🎯 Objetivo
- Encontrar features con más impacto en el abandono (Exited)
- Generar modelos capaces de identificar cliente potenciales de abandono

## 🧹 Data cleaning
En este dataset en concreto se ha revisado la existencia de datos nulos o textos vacíos, pero no se ha encontrado nada, se considera un dataset limpio.

## 📈 EDA
Insights:

- Este dataset tiene un desbalance importante en el target (Exited), por lo que en el trabajo de ML será necesario ajustar pesos de clases
![Cuenta de clases Exited](/outputs/figures/exited_count.png)

- El CreditScore no es un buen indicador, aunque si se puede ver que los clientes que se van tienen un CreditScore parcialmente más bajo.
![Distribución de CreditScore por Exited](/outputs/figures/creditscore_distribution_by_exited.png)

- La mayor cantidad de clientes del banco son franceses, mientras que en Germany y Spain existe una cantidad muy similar.
![Cuenta de clientes por país](/outputs/figures/exited_by_geography_count.png)

- Germany es el país con más churn de los 3 en relación de su cantidad de clientes.
![Cantidad de Exited por país](/outputs/figures/exited_by_geography_pies.png)

- La mayor cantidad de clientes que han pasado por el banco son personas adultas entre los 35 a 40 años.
![Distribución de edades](/outputs/figures/age_distribution.png)

- Se han separado por grupos etarios los clientes, a lo cual se ha llegado a la conclusión de que los clientes con un abandono notorio son los que tienen entre 45 y 60 años.
![Porcentaje de Exited por grupo de edad](outputs/figures/churn_by_ageGroup.png)

- El tenure no es un buen indicador de Exited, aunque de todas formas, dentro de los clientes que se han ido, lo datos son un poco más variados.
![Distribución de tenure por Exited](outputs/figures/tenure_distribution_by_exited.png)

- Dentro de este dataset casi todos los clientes tienen un Balance de 0, aunque existe una tendencia de tener un Balance de al rededor de los 125000
![Distribución de Balance](outputs/figures/balance_distribution.png)

- Dentro de los clientes que se quedan en el banco, es más común que tengan un balance de 0, mientras que los clientes que se van suelen tener un balance de al rededor de 120000.
![Distribución de Exited en Balance](outputs/figures/balance_distribution_for_exited.png)

- Los que tienen balance se tienden a ir un 10% más que los que no lo tienen.
![Porcentaje de Exited por Balance](outputs/figures/exited_by_balance.png)

- La mejor cantidad de productos que debería tener un cliente, es de 2, ya que con esta cantidad es mucho menos probable que abandone el banco. Además, las peores cantidades de productos son 3 y 4.
![Distribución de Exited por NumOfProducts](outputs/figures/churn_by_NumOfProducts.png)

- No tiene relevancia tener o no tener tarjeta del banco.
![Distribución Exited con Card](outputs/figures/exited_by_HasCrCard_pie.png)

- Los miembros no activos tienden a irse de manera más frecuente.
![Exited en IsActiveMember](outputs/figures/active_members_exited.png)

- El salario estimado no tiene mucha incidencia dentro del abandono.
![Distribución de Salary en Exited](outputs/figures/exited_by_EstimatedSalary.png)

## ⚙️ Feature engineering
- AgeGroup:
Separación de grupos etarios con el fin de proporcionar mejor visión y segmentación, utilizando 4 grupos separados entre 18/29, 30/44, 45/59 y 60 hacia adelante. Obtiendo grupos de adultos jóvenes, adultos, mediana edad y senior.
Gráfico base de esta decisión:
![Porcentaje de Exited por grupo de edad](outputs/figures/churn_by_ageGroup.png)


- HasBalance:
Identifica de forma binaria si el cliente tiene balance =0 o >0.
Gráfico base de esta decisión:
![Distribución de Exited por NumOfProducts](outputs/figures/churn_by_NumOfProducts.png)

- Age_x_NumOfProducts_score:
Genera un puntaje relacionando el grupo al que pertenece y su cantidad de productos. Es el producto de la multiplicación de valores no lineales, por lo que se han estimado valores diferentes para cada grupo y cada cantidad de productos.
Gráficos base de esta decisión:
![Porcentaje de Exited por grupo de edad](outputs/figures/churn_by_ageGroup.png)
![Distribución de Exited por NumOfProducts](outputs/figures/churn_by_NumOfProducts.png)

- BalanceAndActive:
Puntaje indicador de que tanto el cliente utiliza el banco y si tiene balance además de ser activo.
Gráficos base de esta decisión:
![Porcentaje de Exited por Balance](outputs/figures/exited_by_balance.png)
![Exited en IsActiveMember](outputs/figures/active_members_exited.png)

- Score_AgeAndSalaryScore:
Puntaje que sectoriza e identifica potencial financiero, diviendo el salario estimado por la edad.
Gráficos base de esta decisión:
![Porcentaje de Exited por grupo de edad](outputs/figures/churn_by_ageGroup.png)
![Distribución de Salary en Exited](outputs/figures/exited_by_EstimatedSalary.png)





