from datetime import datetime
from flask import render_template, session, redirect, url_for, jsonify, make_response, request
from . import main
from .forms import NameForm
from .. import db
from ..models import User

from ..bookmark_controller import BookMarkProcessor

from flask_paginate import Pagination, get_page_parameter


FILE_BOOKMARK = "C:\\Users\\PERSONAL\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"

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
    # TODO:: check symlinked file not updating
    # file_bookmark = "c:\\users\\personal\\desktop\\python-bookmark\\app\\" \
    #   "static\\Bookmarks.json"

    bookmarks = BookMarkProcessor(FILE_BOOKMARK).process_list_of_childrens()

    return render_template('bookmarks.html', bookmarks=bookmarks)


@main.route('/links', methods=["GET", "POST"])
def links():
    bookmark = BookMarkProcessor(FILE_BOOKMARK)
    bookmarks = bookmark.get_json_data()
    links = bookmark.get_names(bookmarks)
    return render_template('links.html', links=links)
