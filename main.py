from flask import Flask, render_template, request, url_for, send_file
import os
from app.simulation import SIRModel
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'outputs'

# Ensure output directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Fetch and validate user input
            population = int(request.form.get('population', 1000))
            initial_infected = int(request.form.get('initial_infected', 1))
            beta = float(request.form.get('beta', 0.3))
            gamma = float(request.form.get('gamma', 0.1))
            days = int(request.form.get('days', 160))

            # Run simulation using the enhanced SIRModel class
            model = SIRModel(population, initial_infected, beta, gamma, days)
            t, S, I, R = model.run()

            # Plot the results
            fig, ax = plt.subplots()
            ax.plot(t, S, label='Susceptible', color='blue')
            ax.plot(t, I, label='Infected', color='red')
            ax.plot(t, R, label='Recovered', color='green')
            ax.set_xlabel('Days')
            ax.set_ylabel('Population')
            ax.set_title('SIR Simulation – Infectio')
            ax.legend()

            # Save the plot to a file
            plot_path = os.path.join(app.config['UPLOAD_FOLDER'], 'infection_curve.png')
            plt.savefig(plot_path)
            plt.close()

            # Export CSV data
            df = model.to_dataframe()
            csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'results.csv')
            df.to_csv(csv_path, index=False)

            # Summary stats
            stats = model.get_final_stats()

            return render_template('index.html',
                                   img_path=url_for('static', filename='infection_curve.png'),
                                   csv_available=True,
                                   population=population,
                                   initial_infected=initial_infected,
                                   beta=beta,
                                   gamma=gamma,
                                   days=days,
                                   stats=stats)

        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html')

@app.route('/download-csv')
def download_csv():
    """Download the simulation results as CSV."""
    csv_path = os.path.join(app.config['UPLOAD_FOLDER'], 'results.csv')
    return send_file(csv_path, mimetype='text/csv', as_attachment=True)

@app.route('/plot')
def get_plot():
    """Serve the simulation plot image."""
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'infection_curve.png')
    return send_file(img_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
