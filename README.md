# 🧪 Infectio - SIR Disease Spread Simulator

**Infectio** is a web-based simulation app that models how infectious diseases spread using the classic **SIR (Susceptible-Infected-Recovered)** model in epidemiology. It allows users to input parameters like transmission rate, recovery rate, and population size — and then visualizes how an epidemic unfolds over time.

---

## 🚀 Live Demo

> 🔗 Coming Soon on [Render](https://render.com)


---

## 🧠 Features

- 🔢 SIR Model Simulation
- 📈 Infection Curve Plot
- 📊 Final Stats Summary
- 📄 CSV Export of Results
- 🎯 Input validation with error feedback
- 🌐 Deployed using Flask + Gunicorn on Render

---

## ⚙️ How It Works

1. Enter population, initial infections, beta (transmission rate), gamma (recovery rate), and duration.
2. The app runs a daily simulation of the disease spread.
3. A line graph is generated showing the counts of susceptible, infected, and recovered over time.
4. Results are saved and downloadable as a `.csv` file.

---

## 🛠️ Tech Stack

- **Python**
  - Flask (Web Framework)
  - Pandas (Data Handling)
  - NumPy (Calculations)
  - Matplotlib (Graph Plotting)
- **Frontend**
  - HTML5 + CSS3 (Vanilla, Responsive)
  - Jinja2 Templates
- **Deployment**
  - Gunicorn (WSGI)
  - Render.com (Free Hosting)
