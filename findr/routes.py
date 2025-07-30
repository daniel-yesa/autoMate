from flask import render_template

def register_findr_routes(bp):
    @bp.route('/findr')
    def index():
        return render_template('findr_index.html')