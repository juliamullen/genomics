import json
import gzip
import os
import datetime

from biothings import config
logger = config.logger

def load_annotations(data_folder):
    json_path = os.path.join(data_folder, "api_data.json.gz")
    with gzip.open(json_path) as f:
        data = json.loads(f.read().decode('utf-8'))
    for datum in data:
        datum['_id'] = datum['accession_id']
        yield datum

def release():
    return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
