from flask import Flask,render_template,request
import pickle
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        estimatedsalary = request.form['estimatedsalary']

        model = pickle.load(open('model.pkl','rb'))
        prediction= model11.predict([[gender,age,estimatedsalary]])
        target=prediction[0]
        print(target)
        
    return render_template('prediction.html',target=target)


if __name__ =='__main__':

   app.run()