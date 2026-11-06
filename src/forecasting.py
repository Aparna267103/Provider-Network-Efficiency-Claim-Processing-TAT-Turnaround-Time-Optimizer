import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing

BASE_DIR = Path(__file__).resolve().parents[1]
FORECAST_HORIZON = 8

file_path = BASE_DIR / "data" / "processed" / "claims_enriched.csv"

report_dir = BASE_DIR / "reports"
report_dir.mkdir(exist_ok=True)

df = pd.read_csv(file_path)

df["Intake_Date"] = pd.to_datetime(
    df["Intake_Date"]
)

# Weekly claim volume
weekly = (
    df.set_index("Intake_Date")
    .resample("W")["Claim_ID"]
    .count()
    .asfreq("W", fill_value=0)
)


if len(weekly) <= FORECAST_HORIZON:
    raise ValueError(
        f"At least {FORECAST_HORIZON + 1} weekly observations are required "
        "to evaluate the forecast."
    )

# Evaluate on the last eight observed weeks without training on those weeks.
train = weekly.iloc[:-FORECAST_HORIZON]
test = weekly.iloc[-FORECAST_HORIZON:]

evaluation_model = ExponentialSmoothing(
    train,
    trend="add",
    seasonal=None
)

evaluation_fit = evaluation_model.fit()
evaluation_forecast = evaluation_fit.forecast(len(test))

mae = mean_absolute_error(test, evaluation_forecast)
rmse = mean_squared_error(test, evaluation_forecast) ** 0.5

metrics = pd.DataFrame([{
    "Evaluation_Weeks": len(test),
    "Training_Weeks": len(train),
    "MAE": mae,
    "RMSE": rmse
}])
metrics_path = report_dir / "forecast_metrics.csv"
metrics.to_csv(metrics_path, index=False)

print("FORECAST HOLDOUT EVALUATION")
print(f"Training weeks: {len(train)}")
print(f"Evaluation weeks: {len(test)}")
print(f"MAE: {mae:.2f} claims")
print(f"RMSE: {rmse:.2f} claims")
print("Saved:", metrics_path)

# Refit on all observations before forecasting the next eight weeks.
model = ExponentialSmoothing(
    weekly,
    trend="add",
    seasonal=None
)
fitted_model = model.fit()
forecast = fitted_model.forecast(FORECAST_HORIZON)

print("NEXT 8 WEEKS CLAIM FORECAST")

print(forecast.round(0))

# Visualize
plt.figure(figsize=(12, 6))

plt.plot(
    weekly.index,
    weekly.values,
    label="Historical Claims"
)

plt.plot(
    forecast.index,
    forecast.values,
    label="Forecasted Claims",
    linestyle="--"
)

plt.title("Weekly Claims Volume Forecast")

plt.xlabel("Week")
plt.ylabel("Number of Claims")

plt.legend()

plt.tight_layout()

plt.savefig(
    report_dir / "claims_forecast.png",
    dpi=300
)

plt.show()

# Export historical + forecast data

historical = weekly.rename("Actual_Claims").rename_axis(
    "Forecast_Week"
).reset_index()

historical["Predicted_Claims"] = float("nan")

future = forecast.rename("Predicted_Claims").rename_axis(
    "Forecast_Week"
).reset_index()

future["Actual_Claims"] = float("nan")

combined = pd.concat(
    [historical, future],
    ignore_index=True
)

combined = combined[
    ["Forecast_Week", "Actual_Claims", "Predicted_Claims"]
]

output_path = report_dir / "claims_forecast.csv"
combined.to_csv(output_path, index=False)

print("Saved:", output_path)

print("Forecast completed successfully!")
