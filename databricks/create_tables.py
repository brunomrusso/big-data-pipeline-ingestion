# Databricks notebook source
# MAGIC %sql
# MAGIC -- Criando Database
# MAGIC CREATE DATABASE IF NOT EXISTS bronze_bmr;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Acessando DB
# MAGIC USE bronze_bmr;
# MAGIC
# MAGIC -- Criando tabela externa
# MAGIC CREATE TABLE IF NOT EXISTS bronze_bmr.EFIN_RETIF_R4010 (
# MAGIC CODIGOISIMP string,
# MAGIC AUTORIZACAO string,
# MAGIC DATAPUBLICACAO string,
# MAGIC RAZAOSOCIAL string,
# MAGIC CNPJ string,
# MAGIC ENDERECO string,
# MAGIC COMPLEMENTO string,
# MAGIC BAIRRO string,
# MAGIC CEP string,
# MAGIC UF string,
# MAGIC MUNICIPIO string,
# MAGIC BANDEIRA string,
# MAGIC DATAVINCULACAO string)
# MAGIC USING DELTA
# MAGIC PARTITIONED BY (odate STRING)
# MAGIC LOCATION 'abfss://bronze@storagebigdatadev.dfs.core.windows.net/EFIN_RETIF_R4010';
# MAGIC

# COMMAND ----------

dbutils.fs.rm('abfss://bronze@storagebigdatadev.dfs.core.windows.net/', True)

# COMMAND ----------

# Leitura do arquivo CSV
df = spark.read.format('csv').options(header='true', delimiter=';').load('abfss://raw-data@storagebigdatadev.dfs.core.windows.net/EFIN_RETIF_R4010_20242601.CSV')
