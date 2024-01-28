# Databricks notebook source
# Python code to mount and access Azure Data Lake Storage Gen2 Account to Azure Databricks with Service Principal and OAuth
# Author: Dhyanendra Singh Rathore

# Define the variables used for creating connection strings
adlsAccountName = "storagebigdatadev"
adlsContainerName = "bronze"
mountPoint = "/mnt/bronze"

# Application (Client) ID
applicationId = dbutils.secrets.get(scope="ProjectAKV",key="ClienteId")
# Application (Client) Secret Key
authenticationKey = dbutils.secrets.get(scope="ProjectAKV",key="ClientSecret")
# Directory (Tenant) ID
tenandId = dbutils.secrets.get(scope="ProjectAKV",key="TenantId")

endpoint = "https://login.microsoftonline.com/" + tenandId + "/oauth2/token"
source = "abfss://" + adlsContainerName + "@" + adlsAccountName + ".dfs.core.windows.net/"

# Connecting using Service Principal secrets and OAuth
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": applicationId,
           "fs.azure.account.oauth2.client.secret": authenticationKey,
           "fs.azure.account.oauth2.client.endpoint": endpoint}

# Mounting ADLS Storage to DBFS
dbutils.fs.mount(
    source = source,
    mount_point = mountPoint,
    extra_configs = configs)

# COMMAND ----------

# Python code to mount and access Azure Data Lake Storage Gen2 Account to Azure Databricks with Service Principal and OAuth
# Author: Dhyanendra Singh Rathore

# Define the variables used for creating connection strings
adlsAccountName = "storagebigdatadev"
adlsContainerName = "raw-data"
mountPoint = "/mnt/raw-data"

# Application (Client) ID
applicationId = dbutils.secrets.get(scope="ProjectAKV",key="ClienteId")
# Application (Client) Secret Key
authenticationKey = dbutils.secrets.get(scope="ProjectAKV",key="ClientSecret")
# Directory (Tenant) ID
tenandId = dbutils.secrets.get(scope="ProjectAKV",key="TenantId")

endpoint = "https://login.microsoftonline.com/" + tenandId + "/oauth2/token"
source = "abfss://" + adlsContainerName + "@" + adlsAccountName + ".dfs.core.windows.net/"

# Connecting using Service Principal secrets and OAuth
configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": applicationId,
           "fs.azure.account.oauth2.client.secret": authenticationKey,
           "fs.azure.account.oauth2.client.endpoint": endpoint}

# Mounting ADLS Storage to DBFS
dbutils.fs.mount(
    source = source,
    mount_point = mountPoint,
    extra_configs = configs)
