from thecsv import storyData
from wordGenisis import genStory
import os



from flask import Flask, render_template, request
app = Flask(__name__)

@global result

# os.getenv() gets pin variables in setting, and replaces them with protected pin.
config{
    "SB": os.getenv('paypalPIN')
}
'''@app.route('/')
def student():
   return render_template('student.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)'''

@app.route('/approved',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      storyData.result.email[1] = 1
      return render_template("home.html")
 
@app.route('/home',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      if dataStory.result.email[0] == psw]:
          [return render_template("result.html" 
      else: dataStory[result.email]:[result.psw,0,result.yourname]
      return render_template("result.html", name = dataStory[result.email][2])



@app.route('/story',methods = ['POST', 'GET'])
def story():
   if request.method == 'POST':
      result = request.form
      #predict story
      storyTime = genStory(result.story, result.numberST)
      #model.predict()
      return render_template("result.html",results = storyTime, name = storyData[result.email][2])


@app.route('/login',methods = ['POST', 'GET'])

def login():
     if request.method == 'POST':
      result = request.form
   #dict = {'phy':50,'che':60,'maths':70}
if storyData[result.email] :
    storyData.result.email[0] = result.psw
   return render_template('home.html')
   else: return render_template('front.html')

if __name__ == '__main__':
   app.run(debug = True)