import numpy as np
import pandas as pd

class SIRModel:
    def __init__(self, population, initial_infected, beta, gamma, days):
        # Validate inputs
        if population <= 0 or initial_infected < 0 or beta < 0 or gamma < 0 or days <= 0:
            raise ValueError("Invalid simulation parameters")

        self.N = population
        self.I0 = initial_infected
        self.S0 = population - initial_infected
        self.R0 = 0
        self.beta = beta
        self.gamma = gamma
        self.days = days

    def run(self):
        S = np.zeros(self.days + 1)
        I = np.zeros(self.days + 1)
        R = np.zeros(self.days + 1)
        t = np.arange(self.days + 1)

        # Initial values
        S[0] = self.S0
        I[0] = self.I0
        R[0] = self.R0

        for day in range(1, self.days + 1):
            new_infections = (self.beta * S[day-1] * I[day-1]) / self.N
            new_recoveries = self.gamma * I[day-1]

            S[day] = S[day-1] - new_infections
            I[day] = I[day-1] + new_infections - new_recoveries
            R[day] = R[day-1] + new_recoveries

        return t, S, I, R

    def to_dataframe(self):
        t, S, I, R = self.run()
        return pd.DataFrame({
            "Day": t,
            "Susceptible": S,
            "Infected": I,
            "Recovered": R
        })

    def get_peak_infection(self):
        _, _, I, _ = self.run()
        return max(I)

    def get_final_stats(self):
        _, S, I, R = self.run()
        return {
            "Final Susceptible": S[-1],
            "Final Infected": I[-1],
            "Final Recovered": R[-1]
        }
