# Databricks notebook source
from pyspark.sql.functions import lit

# Variaveis
odate = getArgument("odate", "DefaultValue")
#odate = '20240126'
location_raw = 'abfss://raw-data@storagebigdatadev.dfs.core.windows.net/'
location_bronze = 'abfss://bronze@storagebigdatadev.dfs.core.windows.net/'
file_name =  f'EFIN_RETIF_R4010_{odate}.CSV'

# COMMAND ----------

# Leitura do arquivo CSV
df = spark.read.format('csv').options(header='true', delimiter=';').load(f'{location_raw}{file_name}')

# COMMAND ----------

# Acrescentando campo odate
df = df.withColumn('odate', lit(odate))

# COMMAND ----------

# Escrevendo arquivo na camada bronze
df.write.format('delta').mode('overwrite').partitionBy('odate').save(f'{location_bronze}EFIN_RETIF_R4010/')
