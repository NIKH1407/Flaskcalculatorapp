from flask import Flask,render_template,request


app = Flask(__name__)



@app.route('/calculator',methods = ['POST', 'GET' ])
def calculator():
    if request.method == 'POST':
        val1 = float(request.form['field1'])
        val2 = float(request.form['field2'])
        

        if request.form.get('add'):
            res = val1+val2
            return render_template('index.html',val = res)
        
        if request.form.get('sub'):
            res = val1-val2
            return render_template('index.html',val = res)
        
        if request.form.get('div'):
            res = val1 / val2
            return render_template('index.html',val = res)
        
        return render_template('index.html')
    else:
        return render_template('index.html',val = 'na')


if __name__=='__main__':
    app.run(debug = True)