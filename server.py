from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key="verySecret"

@app.route( '/', methods=['GET'] )
def displayCount():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] +=1    
    return render_template( "index.html" )


@app.route('/addTwo', methods=['GET'] )
def addTwoCount():
    session["count"] +=1 
    return redirect('/')

@app.route('/reset', methods=['GET'] )
def resetCount():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run( debug = True)