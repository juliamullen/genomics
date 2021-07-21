import json
import gzip
import os

from biothings import config
logger = config.logger

def load_annotations(data_folder):
    json_path = os.path.join(data_folder, "new_api_data_fix.json.gz")
    with gzip.open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['accession_id']
            yield datum
