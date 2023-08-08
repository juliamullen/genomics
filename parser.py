import json
import gzip
import os

from biothings import config

from .gisaid_secret import AUTH_TOKEN
import requests

logger = config.logger

def update_not_smaller(new_data_file):
    new_num_lines = sum(1 for line in open(new_data_file))
    current_metadata = requests.get("https://api.outbreak.info/genomics/metadata", headers={'Authorization': secrets.GEN_AUTH})
    old_num_lines = current_metadata.json()['stats']['total']

    if old_num_lines > new_num_lines:
        raise RuntimeError(f"Attempted update with fewer documents failed. Current: {old_num_lines} New: {new_num_lines}")

def load_data_muts(data_folder):
    json_path = os.path.join(data_folder, "data.muts.jsonl.gz")
    with gzip.open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['accession_id']
            yield datum

def load_data_mutless(data_folder):
    json_path = os.path.join(data_folder, "data.mutless.jsonl.gz")
    with gzip.open(json_path) as f:
        for line in f:
            datum = json.loads(line)
            datum['_id'] = datum['accession_id']
            yield datum
