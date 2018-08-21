import io
import os

from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    
def generate_t(path):
    client = vision.ImageAnnotatorClient()
    des = []
    if path.startswith('http') or path.startswith('gs:'):
        image = types.Image()
        image.source.image_uri = path
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')

        for label in labels:
            print(label.description)
            des.append(label.description)
    print(des)
    return des
generate_t('gs://erg/chocolate_lab_cute_puppies.jpg')


def translation(words):
    # Instantiates a client
    translate_client = translate.Client()
    
    # The text to translate
    # The target language
    target = 'zh-TW'
    
    # Translates some text into Russian
    translation = translate_client.translate(
        words,
        target_language=target)
    
    print(u'Text: {}'.format(words))
    print(u'Translation: {}'.format(translation['translatedText']))
    
    
words = generate_t('gs://erg/chocolate_lab_cute_puppies.jpg')
print words
translation(words[0])