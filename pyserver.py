from flask import Flask, request 
import json 
import pickle 
import sys
     
app = Flask(__name__) 
     
@app.route('/') 
def index(): 
    return "Flask server" 
     
@app.route('/postdata', methods = ['POST']) 
def postdata(): 
    data = request.get_json() 
    # data1 = json.loads(data)
    print(data['data3']+100) 
    

    # Here we run the neural network file which does the denoising
    import usr_in
    
    #we select the latest file in the output folder where the denoised image is saved
    import glob
    import os
    list_of_files = glob.glob('./public/images/output/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file = latest_file.replace("./public", "")

    # print(latest_file)
    return json.dumps({"newdata": latest_file}) 
     
if __name__ == "__main__": 
    app.run(port=5000) 