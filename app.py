from flask import Flask, request, jsonify, render_template
import getmac as gt

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def main_page():
    return render_template("main.html")

# @app.route('/marks', methods=['POST', 'GET'])
# def marks():
#     selected_subjects = request.form.getlist('subjects') 
#     subject_values = {}
#     cgl = []
#     # credit_sum = 0
#     for subject in selected_subjects:
#         if subject == "cpp":
#             value = request.form.get(f"{subject}_value")
#             if value == "A+":
#                 cgl.append(10)
#             elif value == "A":
#                 cgl.append(9)
#             elif value == "B+":
#                 cgl.append(8)
#             elif value == "B":
#                 cgl.append(7)
#             elif value == "C":
#                 cgl.append(6)
#             else:
#                 cgl.append(0)
#             # credit_sum += 7
#             subject_values["Data Structures using C++"] = value
#         elif subject == "ims":
#             value = request.form.get(f"{subject}_value")
#             if value == "A+":
#                 cgl.append(10)
#             elif value == "A":
#                 cgl.append(9)
#             elif value == "B+":
#                 cgl.append(8)
#             elif value == "B":
#                 cgl.append(7)
#             elif value == "C":
#                 cgl.append(6)
#             else:
#                 cgl.append(0)
#             # credit_sum += 4
#             subject_values["Information Management Systems"] = value
#         elif subject == "spec":
#             value = request.form.get(f"{subject}_value")
#             if value == "A+":
#                 cgl.append(10)
#             elif value == "A":
#                 cgl.append(9)
#             elif value == "B+":
#                 cgl.append(8)
#             elif value == "B":
#                 cgl.append(7)
#             elif value == "C":
#                 cgl.append(6)
#             else:
#                 cgl.append(0)
#             # credit_sum += 4
#             subject_values["Specialization"] = value
#         elif subject == "prob":
#             value = request.form.get(f"{subject}_value")
#             if value == "A+":
#                 cgl.append(10)
#             elif value == "A":
#                 cgl.append(9)
#             elif value == "B+":
#                 cgl.append(8)
#             elif value == "B":
#                 cgl.append(7)
#             elif value == "C":
#                 cgl.append(6)
#             else:
#                 cgl.append(0)
#             # credit_sum += 5
#             subject_values["Probability and Statistics"] = value
#         elif subject == "swe":
#             value = request.form.get(f"{subject}_value")
#             if value == "A+":
#                 cgl.append(10)
#             elif value == "A":
#                 cgl.append(9)
#             elif value == "B+":
#                 cgl.append(8)
#             elif value == "B":
#                 cgl.append(7)
#             elif value == "C":
#                 cgl.append(6)
#             else:
#                 cgl.append(0)
#             # credit_sum += 4
#             subject_values["Software Engineering"] = value
#         else:
#             pass
    
    
#     based = 0
#     for i in range(len(cgl)):
#         if i == 0:
#             based = based + int(cgl[i])*7
#         elif i == 3:
#             based = based + int(cgl[i])*5
#         else:
#             based = based + int(cgl[i])*4
    
#     try:
#         finalcg = round(based/24,2)
#     except ZeroDivisionError:
#         finalcg = 0
    
#     return render_template('output.html', data=subject_values, specific_data=finalcg)

@app.route('/marks', methods=['POST', 'GET'])
def marks():
    subject_map = {
        "cpp": {"name": "Data Structures using C++", "credits": 7},
        "ims": {"name": "Information Management Systems", "credits": 4},
        "spec": {"name": "Specialization", "credits": 4},
        "prob": {"name": "Probability and Statistics", "credits": 5},
        "swe": {"name": "Software Engineering", "credits": 4}
    }

    grade_points = {
        "A+": 10,
        "A": 9,
        "B+": 8,
        "B": 7,
        "C": 6
    }

    selected_subjects = request.form.getlist('subjects') 
    subject_values = {}
    total_points = 0
    total_credits = 0

    for subject in selected_subjects:
        value = request.form.get(f"{subject}_value")
        points = grade_points.get(value, 0)
        subject_info = subject_map.get(subject)

        if subject_info:
            credits = subject_info["credits"]
            total_points += points * credits
            total_credits += credits
            subject_values[subject_info["name"]] = value

    try:
        finalcg = round(total_points / total_credits, 2) if total_credits else 0
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
