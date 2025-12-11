#!/usr/bin/env python3
import csv
import json
import matplotlib.pyplot as plt


def load_data(filename):
    """Load dataset from CSV file."""
    mileages = []
    prices = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                mileages.append(float(row["km"]))
                prices.append(float(row["price"]))
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found at: {filename}")
    return mileages, prices


def normalize(data):
    """Normalize data to range [0, 1]."""
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data], min_val, max_val


def estimate_price(mileage, theta0, theta1):
    """Calculate estimated price."""
    return theta0 + (theta1 * mileage)


def train(mileages, prices, learning_rate=0.1, iterations=1000, epsilon=1e-6):
    """Train using gradient descent."""
    m = len(mileages)
    theta0 = 0
    theta1 = 0

    # Normalize data for better convergence
    norm_km, km_min, km_max = normalize(mileages)
    norm_price, price_min, price_max = normalize(prices)

    for iteration in range(iterations):
        old_theta0 = theta0
        old_theta1 = theta1

        # Compute summed errors for bias and slope (loop form of vectorized gradient)
        sum0 = sum(
            estimate_price(norm_km[i], theta0, theta1) - norm_price[i] for i in range(m)
        )
        sum1 = sum(
            (estimate_price(norm_km[i], theta0, theta1) - norm_price[i]) * norm_km[i]
            for i in range(m)
        )

        # Simultaneous update: store deltas before applying them together
        tmp_theta0 = learning_rate * (1 / m) * sum0
        tmp_theta1 = learning_rate * (1 / m) * sum1

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

        # Check convergence: if thetas barely changed, stop training
        if abs(theta0 - old_theta0) < epsilon and abs(theta1 - old_theta1) < epsilon:
            print(f"Converged at iteration {iteration + 1}")
            break

    # Denormalize thetas
    price_range = price_max - price_min
    km_range = km_max - km_min

    real_theta1 = (theta1 * price_range) / km_range
    real_theta0 = (theta0 * price_range) + price_min - (real_theta1 * km_min)

    return real_theta0, real_theta1


def save_thetas(theta0, theta1):
    """Save thetas to JSON file."""
    with open("thetas.json", "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f)


def calculate_precision(mileages, prices, theta0, theta1):
    """Calculate R² score (coefficient of determination)."""
    predictions = [estimate_price(km, theta0, theta1) for km in mileages]
    mean_price = sum(prices) / len(prices)

    ss_res = sum((prices[i] - predictions[i]) ** 2 for i in range(len(prices)))
    ss_tot = sum((p - mean_price) ** 2 for p in prices)

    return 1 - (ss_res / ss_tot)


def plot_results(mileages, prices, theta0, theta1):
    """Plot data points and regression line."""
    plt.figure(figsize=(10, 6))
    plt.scatter(mileages, prices, color="blue", label="Data points")

    # Regression line
    x_line = [min(mileages), max(mileages)]
    y_line = [estimate_price(x, theta0, theta1) for x in x_line]
    plt.plot(x_line, y_line, color="red", label="Regression line")

    plt.xlabel("Mileage (km)")
    plt.ylabel("Price")
    plt.title("Linear Regression: Car Price vs Mileage")
    plt.legend()
    plt.grid(True)
    plt.savefig("plot.png")
    plt.show()
