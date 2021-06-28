def get_release(self):
    import requests
    res = requests.get('http://storage.googleapis.com/andersen-lab_temp/outbreak_genomics/new_api_metadata.json')
    try:
        return res.json()['date_modified']
    except AttributeError:
        import datetime
        return datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')
