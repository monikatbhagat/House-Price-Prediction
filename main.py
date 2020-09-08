from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()

def homePage():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
@cross_origin()

def index():
    if request.method == 'POST':
        try:
            crim = float(request.form['crim'])
            zn = float(request.form['zn'])
            indus = float(request.form['indus'])
            is_charles_river = request.form['chas']
            if(is_charles_river == 'yes'):
                chas = 1
            else:
                chas = 0
            nox = float(request.form['nox'])
            rm = float(request.form['rm'])
            age = float(request.form['age'])
            dis = float(request.form['dis'])
            rad = float(request.form['rad'])
            tax = float(request.form['tax'])
            ptratio = float(request.form['ptratio'])
            b = float(request.form['rad'])
            lstat = float(request.form['lstat'])

            filename = 'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb'))
            prediction = loaded_model.predict(my_pipeline.fit_transform(([[crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat]])))
            print('prediction is:',prediction)
            return render_template('results.html', prediction=prediction)
        except Exception as e:
            print('The Exception message is:', e)
            return 'something is wrong'
    else:
        return render_template('index.html')


my_pipeline = Pipeline([
    #     ..... add as many as you want in your pipeline
    ('std_scaler', StandardScaler())
])

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app













