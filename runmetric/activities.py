from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from runmetric.auth import login_required
from runmetric.models.database.run import Run


bp = Blueprint('activities', __name__, url_prefix='/activities')



@bp.route('/create', methods=('POST','GET'))
@login_required
def create():
    if request.method == 'POST':
        flash('Hello POST')
    elif request.method == 'GET':
        return 'HELLO GET'