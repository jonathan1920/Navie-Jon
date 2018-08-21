from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session
import os
from google.cloud import datastore
from google.cloud import storage
import g_cloud_key.json
import vision
app = Flask(__name__, static_url_path='')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# client = datastore.Client()
# key = client.key('Person')

# entity = datastore.Entity(key=key)
# entity['name'] = 'Your name'
# entity['age'] = 25
# client.put(entity)

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

client = storage.Client()
bucket = client.get_bucket('first123123123')

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
        translation = vision.generate_t(filename)

if __name__ == '__main__':
    app.debug = True
    app.run()
