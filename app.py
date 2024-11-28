from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main_page():
    return render_template("index.html")

@app.route('/marks', methods=['POST', 'GET'])
def marks():
    selected_subjects = request.form.getlist('subjects') 
    subject_values = {}
    cgl = []
    for subject in selected_subjects:
        if subject == "cpp":
            value = request.form.get(f"{subject}_value")
            cgl.append(value)
            subject_values["Data Structures using C++"] = value
        elif subject == "ims":
            value = request.form.get(f"{subject}_value")
            cgl.append(value)
            subject_values["Information Management Systems"] = value
        elif subject == "spec":
            value = request.form.get(f"{subject}_value")
            cgl.append(value)
            subject_values["Specialization"] = value
        elif subject == "prob":
            value = request.form.get(f"{subject}_value")
            cgl.append(value)
            subject_values["Probability and Statistics"] = value
        elif subject == "swe":
            value = request.form.get(f"{subject}_value")
            cgl.append(value)
            subject_values["Software Engineering"] = value
        else:
            pass
    
    credit_sum = 23
    based = 0
    for i in range(len(cgl)):
        if i == 0:
            based = based + int(cgl[i])*7
        else:
            based = based + int(cgl[i])*4
    
    finalcg = round(based/credit_sum,2)
    
    return render_template('output.html', data=subject_values, specific_data=finalcg)

if __name__ == "__main__":
    app.run(debug=True)
