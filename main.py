from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from app.simulation import run_sir_simulation
import matplotlib.pyplot as plt
import io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'outputs'

# Ensure output directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get parameters from form
            population = int(request.form.get('population', 1000))
            initial_infected = int(request.form.get('initial_infected', 1))
            beta = float(request.form.get('beta', 0.3))   # Transmission rate
            gamma = float(request.form.get('gamma', 0.1)) # Recovery rate
            days = int(request.form.get('days', 160))

            # Run simulation
            t, S, I, R = run_sir_simulation(population, initial_infected, beta, gamma, days)

            # Plot results
            fig, ax = plt.subplots()
            ax.plot(t, S, label='Susceptible')
            ax.plot(t, I, label='Infected')
            ax.plot(t, R, label='Recovered')
            ax.set_xlabel('Days')
            ax.set_ylabel('Population')
            ax.set_title('SIR Simulation – Infectio')
            ax.legend()

            # Save plot to buffer
            img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'infection_curve.png')
            plt.savefig(img_path)
            plt.close()

            return render_template('index.html', 
                                   img_path=url_for('static', filename='infection_curve.png'),
                                   population=population,
                                   initial_infected=initial_infected,
                                   beta=beta,
                                   gamma=gamma,
                                   days=days)
        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

@app.route('/plot')
def get_plot():
    """Serve the simulation plot image."""
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'infection_curve.png')
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
