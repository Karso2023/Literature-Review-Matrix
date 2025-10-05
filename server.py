from flask import Flask, render_template, request, redirect, url_for
import json
from models.db import get_connection


app = Flask(__name__)


@app.route('/', methods=["GET"])
def main():
    return render_template('main.html')

# https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application
@app.route('/submit_info', methods=["POST"])
def submit_info():
    title = request.form['title']
    authors = request.form['authors']
    journal = request.form['journal']
    doi = request.form['doi']
    year = int(request.form['year'])
    category = request.form['category']
    context = request.form['context']
    correctness = request.form['correctness']
    contributions = request.form['contributions']
    clarity = request.form['clarity']
    rationale = request.form['rationale']
    aims = request.form['aims']
    hypothesis = request.form['hypothesis']
    participants = request.form['participants']
    method = request.form['method']
    findings = request.form['findings']
    implications = request.form['implications']
    falsifiable = request.form['falsifiable']
    limitations = request.form['limitations']
    assumptions = request.form['assumptions']
    errors = request.form['errors']
    missing_citations = request.form['missing_citations']
    presentation = request.form['presentation']
    support = request.form['support']
    efficacy = request.form['efficacy']
    
    basic_info={
        "Title":title,
        "Authors":authors,
        "Journal":journal,
        "doi":doi,
        "Year":year
    }
    
    first_pass={ 
        "Category":category,
        "Context":context,
        "Correctness":correctness,
        "Contributions":contributions,
        "Clarity":clarity
    }
    
    second_pass={
        "Rationale":rationale,
        "Aims":aims,
        "Hypothesis":hypothesis,
        "Participants":participants,
        "Method":method,
        "Findings":findings,
        "Implications":implications,
        "Falsifiable":falsifiable,
        "Limitations":limitations
    }
    
    third_pass={  
        "Assumptions":assumptions,
        "Errors":errors,
        "Missing Citations":missing_citations,
        "Presentation":presentation,
        "Support":support,
        "Efficacy":efficacy
    }
    
    total = {
        "Basic info": basic_info, 
        "First_pass": first_pass, 
        "Second_pass": second_pass, 
        "Third_pass": third_pass
    }
    
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO review_matrix (data) VALUES (%s)", [json.dumps(total)])
    conn.commit()
    cur.close()
    conn.close()


    return redirect(url_for('saved_matrix'))

# Delete saved matrix
@app.route('/delete', methods=["POST"])
def delete():
    data = request.get_json()
    matrix_id = data.get("id")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM review_matrix WHERE id = %s", (matrix_id,))
    conn.commit()
    cur.close()
    conn.close()
    
    print(f"Deleted matrix {matrix_id}")
    return '', 204

# For saving my review matrix 
@app.route('/saved_matrix')
def saved_matrix():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, data FROM review_matrix")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    matrices = [{"id": row[0], "data": row[1]} for row in rows]

    return render_template("saved_matrix.html", matrices=matrices)



@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)