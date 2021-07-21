def get_release(self):
    import requests
    res = requests.get('https://storage.googleapis.com/andersen-lab_temp/outbreak_genomics/new_genomics_metadata_fix.json')
    try:
        return res.json()['date_modified']
    except AttributeError:
        import datetime
        return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
