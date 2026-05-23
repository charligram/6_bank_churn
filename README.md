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
![Porcentaje de Exited por edad](outputs/figures/churn_by_ageGroup.png)

- El tenure no es un buen indicador de Exited, aunque de todas formas, dentro de los clientes que se han ido, lo datos son un poco más variados.
![Distribución de tenure por Exited](outputs/figures/tenure_distribution_by_exited.png)

- Dentro de este dataset casi todos los clientes tienen un Balance de 0, aunque existe una tendencia de tener un Balance de al rededor de los 125000
![Distribución de Balance](outputs/figures/balance_distribution.png)

-