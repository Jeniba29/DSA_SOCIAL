from flask import Flask,render_template,request
import pickle
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        estimatedsalary =request.form['estimatedsalary']
        
        from sklearn.preprocessing import StandardScaler
        scaler=StandardScaler()
        X_train_scale=scaler.fit_transform(X_train)
        X_test_scale=scaler.fit_transform(X_test)

        model = pickle.load(open('model.pkl','rb'))
        prediction= model.predict([[int(gender,age,estimatedsalary)]])
        print(prediction[0])
        
        return render_template('prediction.html',target=prediction[0])
    
if __name__ =='__main__':

   app.run(port=5001,debug=True)