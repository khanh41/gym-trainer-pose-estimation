from google.cloud import storage

_storage_client = storage.Client()
_bucket = _storage_client.get_bucket("aift-b7b2c.appspot.com")


def upload_file_google_storage(file, save_path):
    blob = _bucket.blob(save_path)
    blob.upload_from_file(file)
