from flask import Flask, Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from webapp.start.Main1 import process_dataset

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    main = Blueprint('main', __name__)

    @main.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            if 'file' not in request.files:
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename)
                filepath = os.path.join('project_subfolder', 'datasets', filename)
                file.save(filepath)
                x_col = request.form.get('x_col')
                y_col = request.form.get('y_col')
                return redirect(url_for('.results', filename=filename, x_col=x_col, y_col=y_col))
        return render_template('index.html')

    @main.route('/results', methods=['GET'])
    def results():
        filename = request.args.get('filename')
        x_col = request.args.get('x_col')
        y_col = request.args.get('y_col')
        filepath = os.path.join('project_subfolder', 'datasets', filename)
        table, best_model, best_accuracy = process_dataset(filepath, x_col, y_col)
        return render_template('results.html', table=table, best_model=best_model, best_accuracy=best_accuracy)

    app.register_blueprint(main)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
