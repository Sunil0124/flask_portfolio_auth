from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import User

admin = Blueprint('admin', __name__)

@admin.route('/admin/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        return "Unauthorized", 403
    users = User.query.all()
    return render_template('admin/dashboard.html', users=users)
