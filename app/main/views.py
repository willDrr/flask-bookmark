from datetime import datetime
from flask import render_template, session, redirect, url_for, jsonify, make_response
from . import main
from .forms import NameForm
from .. import db
from ..models import User

from ..bookmark_controller import BookMarkProcessor


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    # if form.validate_on_submit():
    #     # some logic later
    #     return redirect(url_for('.index'))
    return render_template('index.html',
            form=form, name=session.get('name'),
            known=session.get('known', False),
            current_time=datetime.utcnow())


@main.route('/bookmarks', methods=['GET', 'POST'])
def bookmarks():
    file_bookmark = "c:\\users\\personal\\desktop\\python-bookmark\\app\\" \
       "static\\Bookmarks.json"
    lista = BookMarkProcessor(file_bookmark).process_list_of_childrens()
    return render_template('bookmarks.html', file_data=lista)
