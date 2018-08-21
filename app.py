from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, session
import os

app = Flask(__name__, static_url_path='')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        name = request.form.get('breed')
        file = request.files['file']
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
        try:
            picture = Image(
                idcode=idcode,
                breed=Breed.query.filter_by(name=name).first(),
                fullpath=destination
            )
            db.session.add(picture)
            db.session.commit()
        except:
            flash('Not added to Database', 'error')
        flash('Successfully Uploaded Image', 'success')
        return redirect(url_for('upload'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
