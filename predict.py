#!/usr/bin/env python3
import json
import os

def load_thetas():
    """Load theta0 and theta1 from file, default to 0 if not found."""
    try:
        with open("thetas.json", "r") as f:
            data = json.load(f)
            return data.get("theta0", 0), data.get("theta1", 0)
    except FileNotFoundError:
        return 0, 0

def estimate_price(mileage, theta0, theta1):
    """Calculate estimated price using the linear hypothesis."""
    return theta0 + (theta1 * mileage)

def main():
    theta0, theta1 = load_thetas()
    
    try:
        mileage = float(input("Enter mileage (km): "))
        if mileage < 0:
            print("Error: Mileage cannot be negative")
            return
        
        price = estimate_price(mileage, theta0, theta1)
        print(f"Estimated price: {max(0, price):.2f}")
        
    except ValueError:
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    main()
