# ft_linear_regression

Simple linear regression to predict car prices based on mileage.

## How It Works
Uses gradient descent to find the best fit line: `price = θ0 + (θ1 × mileage)`

## Requirements
```bash
pip install matplotlib
```

## Usage
1. **Train the model:**
   ```bash
   python train.py
   ```
   Reads `data.csv`, trains the model, saves θ0/θ1 to `thetas.json`, and displays a plot.

2. **Predict a price:**
   ```bash
   python predict.py
   ```
   Enter a mileage → get estimated price.

## Files
| File | Description |
|------|-------------|
| `train.py` | Trains model using gradient descent |
| `predict.py` | Predicts price for given mileage |
| `data.csv` | Dataset (km, price) |
