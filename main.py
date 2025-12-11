#!/usr/bin/env python3

from train import calculate_precision, load_data, plot_results, save_thetas, train
from predict import estimate_price, load_thetas


def prompt_float(msg, default=None):
    raw = input(msg).strip()
    if raw == "" and default is not None:
        return default
    try:
        return float(raw)
    except ValueError:
        return None


def do_train():
    data_path = input("Data CSV path [data.csv]: ").strip() or "data.csv"
    lr = prompt_float("Learning rate (blank=default 0.1): ", default=0.1)
    iters = prompt_float("Iterations (blank=default 1000): ", default=1000)
    if lr is None or iters is None:
        print("Invalid number. Aborting.")
        return

    mileages, prices = load_data(data_path)
    print(f"Loaded {len(mileages)} rows from {data_path}")

    theta0, theta1 = train(mileages, prices, learning_rate=lr, iterations=int(iters))
    save_thetas(theta0, theta1)
    print(f"Done. theta0={theta0:.4f}, theta1={theta1:.6f} (saved to thetas.json)")

    r2 = calculate_precision(mileages, prices, theta0, theta1)
    print(f"R²: {r2:.4f} ({r2*100:.2f}% accuracy)")

    show_plot = input("Show plot? [y/N]: ").strip().lower()
    if show_plot == "y":
        plot_results(mileages, prices, theta0, theta1)


def do_predict():
    theta0, theta1 = load_thetas()
    mileage = prompt_float("Mileage (km): ")
    if mileage is None or mileage < 0:
        print("Invalid mileage.")
        return
    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price: {max(0, price):.2f}")


def main():
    choice = input("Choose: [1] train  [2] predict: ").strip()
    if choice == "1":
        do_train()
    elif choice == "2":
        do_predict()
    else:
        print("Please type 1 or 2.")


if __name__ == "__main__":
    main()
