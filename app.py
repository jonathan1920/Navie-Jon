from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session
import os
from google.cloud import datastore
from google.cloud import storage
import g_cloud_key.json

app = Flask(__name__, static_url_path='')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


client = datastore.Client()
key = client.key('Person')

entity = datastore.Entity(key=key)
entity['name'] = 'Your name'
entity['age'] = 25
client.put(entity)


#!/usr/bin/python

import boto
import gcs_oauth2_boto_plugin
import os
import shutil
import StringIO
import tempfile
import time

# URI scheme for Cloud Storage.
GOOGLE_STORAGE = 'gs'
# URI scheme for accessing local files.
LOCAL_FILE = 'file'

# Fallback logic. In https://console.cloud.google.com/
# under Credentials, create a new client ID for an installed application.
# Required only if you have not configured client ID/secret in
# the .boto file or as environment variables.


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)


        
client = storage.Client()
bucket = client.create_bucket('first')


def generate_t(linktoimage):
    


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        filename = file.filename
        dst_uri = boto.storage_uri(
        'first' + '/' + filename, GOOGLE_STORAGE)
        dst_uri.new_key().set_contents_from_file(file)
        flash('Successfully Uploaded Image', 'success')
        linktoimage = 'gs://first/'+filename
        translation = generate_t(filename)
        return render_template('uploaded.html', {linktoimage, translation})
    return render_template('upload.html')


    


if __name__ == '__main__':
    app.debug = True
    app.run()
