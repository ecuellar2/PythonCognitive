pip install --upgrade azureml-sdk

import azureml.core
import os
from azureml.core import Workspace, Datastore, Dataset
print("SDK version:", azureml.core.VERSION)

subscription_id = ""
resource_group = "rg"
workspace_name = "ml"
workspace_region = "South Central US"
auth = None

from azureml.core import Workspace
ws = Workspace(workspace_name = workspace_name,
               subscription_id = subscription_id,
               resource_group = resource_group,
               auth = auth)

https://microsoft.com/devicelogin > will ask for login

print('Workspace name: ' + ws.name, 
      'Azure region: ' + ws.location, 
      'Subscription id: ' + ws.subscription_id, 
      'Resource group: ' + ws.resource_group, sep = '\n')

import azureml.core
from azureml.core import Workspace, Datastore
ws = Workspace.from_config()

#spn for adls
datastore = Datastore.register_azure_data_lake_gen2(workspace=ws, datastore_name='adls', filesystem='container', account_name='xx', tenant_id='xx', client_id='xx',
 client_secret='x', resource_url=None, authority_url=None, protocol=None, endpoint=None, overwrite=False )

datastores = ws.datastores
for name, datastore in datastores.items():
    print(name, datastore.datastore_type)

datastore = Datastore.get(ws, datastore_name='adls')
print("Registered adls datastore with name: %s" % datastore)

file_name = '/lake/filepath/Data1.csv'
datastore_paths = [(datastore, file_name)]
dataset = Dataset.Tabular.from_delimited_files(datastore_paths, validate=False, infer_column_types=False)
dataset.take(3).to_pandas_dataframe()

#############
# on prem use case  below 
sql_datastore_name="onprem"
server_name="sernamewithoutsuffix"  #domain suffix will go in endpoint parameter
database_name="db"
username="user"
password="x"

sql_datastore = Datastore.register_azure_sql_database(workspace=ws,datastore_name=sql_datastore_name,server_name=server_name,endpoint='blah.blah.com',database_name=database_name,username=username,password=password,skip_validation=True)
sql_datastore = Datastore.get(ws, 'onprem')
dataset = Dataset.Tabular.from_sql_query((sql_datastore, 'select blah from blah'), validate=False)
df = dataset.take(3).to_pandas_dataframe()
df = dataset.to_pandas_dataframe()
print(df)

############################################
# azure sql example below but can use UI in portal
sql_datastore_name="sql"
server_name="xx.database.windows.net"
database_name="db"
username="user"
password="x"

sql_datastore = 
Datastore.register_azure_sql_database(workspace=ws,datastore_name=sql_datastore_name,server_name=server_name,database_name=database_name,username=username,password=password)

from azureml.core import Dataset, Datastore
# create tabular dataset from a SQL database in datastore
sql_datastore = Datastore.get(ws, 'sql')
sql_ds = Dataset.Tabular.from_sql_query((sql_datastore, 'SELECT * FROM dbo.delete_me'))
sql_ds.take(3).to_pandas_dataframe()

