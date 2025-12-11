# ft_linear_regression

Simple linear regression to predict car prices based on mileage.

## How It Works
Uses gradient descent to find the best fit line: `price = θ0 + (θ1 × mileage)`

## Requirements
Python 3.8+ installed on your system, then:
```bash
pip install -r requirements.txt
```

## Usage
Run the single entry point and choose an option:
```bash
python main.py
```
Then select `1` (train) or `2` (predict) when prompted. Training asks for the CSV path and optional learning rate/iterations, saves θ0/θ1 to `thetas.json`, and can show a plot. Predict asks for mileage and prints the estimated price.

## Files
| File | Description |
|------|-------------|
| `main.py` | Interactive entry point (train or predict) |
| `train.py` | Training utilities (no CLI) |
| `predict.py` | Prediction utilities (no CLI) |
| `data.csv` | Dataset (km, price) |
| `requirements.txt` | Dependencies (matplotlib) |
