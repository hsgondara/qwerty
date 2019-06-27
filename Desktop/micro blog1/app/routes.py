from app import app
@app.route('/index')
def variables():
    a=10
    b=20
    c=a+b
    return(str(c))
    
















