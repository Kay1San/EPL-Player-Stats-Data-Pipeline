import pyarrow as pa
import pyarrow.parquet as pq
import os

from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/keys/epl-player-stats-597ac10755cc.json"

bucket_name = "epl-player-stats-bucket"
project_id = "epl-player-stats"

root_path = bucket_name



@data_exporter
def export_data(data, *args, **kwargs):
   
   table = pa.Table.from_pandas(data)

   gcs = pa.fs.GcsFileSystem()

   pq.write_to_dataset(
    table,
    root_path=root_path,
    partition_cols=['season'],
    filesystem=gcs
   )
