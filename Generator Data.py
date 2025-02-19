from flask import Flask, render_template_string, request, make_response
import pandas as pd
import random

app = Flask(__name__)

# Topics and their corresponding data generators
def generate_health_data(num_records):
    data = {
        "Patient ID": [i for i in range(1, num_records + 1)],
        "Age": [random.randint(18, 90) for _ in range(num_records)],
        "Blood Pressure": [random.randint(80, 140) for _ in range(num_records)],
        "Cholesterol Level": [random.randint(150, 300) for _ in range(num_records)],
        "Diagnosis": ["Healthy" if random.random() > 0.2 else "Unhealthy" for _ in range(num_records)]
    }
    return pd.DataFrame(data)

def generate_poverty_index_data(num_records):
    data = {
        "Country": [f"Country_{i}" for i in range(1, num_records + 1)],
        "Poverty Index": [round(random.uniform(0, 100), 2) for _ in range(num_records)],
        "Population": [random.randint(1_000_000, 1_000_000_000) for _ in range(num_records)],
        "GDP Per Capita": [round(random.uniform(1000, 50000), 2) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

def generate_population_growth_data(num_records):
    data = {
        "Year": [2000 + i for i in range(num_records)],
        "Country": ["Worldwide" for _ in range(num_records)],
        "Population": [random.randint(6_000_000_000, 8_000_000_000) for _ in range(num_records)],
        "Growth Rate (%)": [round(random.uniform(0.5, 3.0), 2) for _ in range(num_records)]
    }
    return pd.DataFrame(data)

@app.route("/", methods=["GET", "POST"])
def index():
    # HTML template embedded in the Python code
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dummy Data Generator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            label {
                font-weight: bold;
            }
            input, select, button {
                padding: 10px;
                font-size: 16px;
            }
            button {
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Dummy Data Generator</h1>
            <form method="POST" action="/">
                <label for="topic">Select Topic:</label>
                <select name="topic" id="topic" required>
                    <option value="health">Health Data</option>
                    <option value="poverty_index">Poverty Index</option>
                    <option value="population_growth">Population Growth</option>
                </select>

                <label for="num_records">Number of Records:</label>
                <input type="number" name="num_records" id="num_records" min="1" value="10" required>

                <button type="submit">Generate & Download CSV</button>
            </form>
        </div>
    </body>
    </html>
    """

    if request.method == "POST":
        topic = request.form.get("topic")
        num_records = int(request.form.get("num_records", 10))  # Default to 10 records

        # Generate data based on selected topic
        if topic == "health":
            df = generate_health_data(num_records)
        elif topic == "poverty_index":
            df = generate_poverty_index_data(num_records)
        elif topic == "population_growth":
            df = generate_population_growth_data(num_records)
        else:
            return "Invalid topic", 400

        # Convert DataFrame to CSV and send it as a downloadable file
        csv_data = df.to_csv(index=False)
        response = make_response(csv_data)
        response.headers["Content-Disposition"] = f"attachment; filename={topic}_data.csv"
        response.headers["Content-type"] = "text/csv"
        return response

    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)