# app.py
from flask import Flask, render_template, request, make_response
from backend.f1_telemetry import get_telemetry_plot  # Import the function

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# About route with GET and POST methods
@app.route('/about', methods=['GET', 'POST'])
def about():
    result = ''
    if request.method == 'POST':
        # Get the string from the form input
        user_input = request.form['user_input']
        
        # Modify the string (custom logic here, for example: reversing the string)
        result = f"Modified string: {user_input[::-1]}"
        
    return render_template('about.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/f1', methods=['GET','POST'])
def f1_telemetry():
    if request.method == 'POST':
        year = int(request.form['year'])
        driver = request.form['driver'].upper()
        race = request.form['race']

        # Render f1_plot.html with the inputs
        return render_template('f1_plot.html', year=year, driver=driver, race=race)

    return render_template('f1_form.html')

@app.route('/f1_plot.png')
def plot_png():
    # Get the inputs from the query parameters
    year = int(request.args.get('year'))
    driver = request.args.get('driver')
    race = request.args.get('race')

    # Use the function from f1_telemetry.py to get the plot
    plot_output = get_telemetry_plot(year, driver, race)

    # Return the image as a response
    return make_response(plot_output.read(), 200, {'Content-Type': 'image/png'})

if __name__ == '__main__':
    app.run(debug=True)
