#!/usr/bin/env python3
import json

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

# Module-only; interactive flow lives in main.py
