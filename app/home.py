from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, json
)

from app.data import get_api_data

bp = Blueprint('home', __name__)

@bp.route('/', methods=('POST', 'GET'))
def home_display():
    output = ''
    if request.method == 'POST':
        entry = request.form['entry']
        error = None

        if not entry:
            error = "Whoops...Please enter something"
        else:
            result = get_api_data(entry)
            if result:
                output = result
            else:
                error = "No entries found. Sad!"
                output = None
        if error:
            flash(error)

    return render_template('home/index.html', output=output)