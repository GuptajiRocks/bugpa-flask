from flask import Flask, request, jsonify, render_template
import getmac as gt

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main_page():
    return render_template("main.html")

@app.route('/marks', methods=['POST', 'GET'])
def marks():
    selected_subjects = request.form.getlist('subjects') 
    subject_values = {}
    cgl = []
    credit_sum = 0
    for subject in selected_subjects:
        if subject == "cpp":
            value = request.form.get(f"{subject}_value")
            if value == "A+":
                cgl.append(10)
            elif value == "A":
                cgl.append(9)
            elif value == "B+":
                cgl.append(8)
            elif value == "B":
                cgl.append(7)
            elif value == "C":
                cgl.append(6)
            else:
                cgl.append(0)
            credit_sum += 7
            subject_values["Data Structures using C++"] = value
        elif subject == "ims":
            value = request.form.get(f"{subject}_value")
            if value == "A+":
                cgl.append(10)
            elif value == "A":
                cgl.append(9)
            elif value == "B+":
                cgl.append(8)
            elif value == "B":
                cgl.append(7)
            elif value == "C":
                cgl.append(6)
            else:
                cgl.append(0)
            credit_sum += 4
            subject_values["Information Management Systems"] = value
        elif subject == "spec":
            value = request.form.get(f"{subject}_value")
            if value == "A+":
                cgl.append(10)
            elif value == "A":
                cgl.append(9)
            elif value == "B+":
                cgl.append(8)
            elif value == "B":
                cgl.append(7)
            elif value == "C":
                cgl.append(6)
            else:
                cgl.append(0)
            credit_sum += 4
            subject_values["Specialization"] = value
        elif subject == "prob":
            value = request.form.get(f"{subject}_value")
            if value == "A+":
                cgl.append(10)
            elif value == "A":
                cgl.append(9)
            elif value == "B+":
                cgl.append(8)
            elif value == "B":
                cgl.append(7)
            elif value == "C":
                cgl.append(6)
            else:
                cgl.append(0)
            credit_sum += 4
            subject_values["Probability and Statistics"] = value
        elif subject == "swe":
            value = request.form.get(f"{subject}_value")
            if value == "A+":
                cgl.append(10)
            elif value == "A":
                cgl.append(9)
            elif value == "B+":
                cgl.append(8)
            elif value == "B":
                cgl.append(7)
            elif value == "C":
                cgl.append(6)
            else:
                cgl.append(0)
            credit_sum += 4
            subject_values["Software Engineering"] = value
        else:
            pass
    
    
    based = 0
    for i in range(len(cgl)):
        if i == 0:
            based = based + int(cgl[i])*7
        else:
            based = based + int(cgl[i])*4
    
    try:
        finalcg = round(based/23,2)
    except ZeroDivisionError:
        finalcg = 0
    
    return render_template('output.html', data=subject_values, specific_data=finalcg)


@app.route("/getmac")
def get_mac_add():
    add = gt.get_mac_address()
    return render_template("final.html", mac_add = add)

@app.route("/pgone")
def sgpa():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
