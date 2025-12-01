# Stock Analyzer Development Guide

## Setup

### 1. Clone and Create Virtual Environment

```bash
cd stock_analyzer
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
pip install -e ".[dev]"  # Install in development mode with dev dependencies
```

### 3. TA-lib Windows Installation

If you encounter issues installing TA-lib on Windows:

1. Download the pre-built wheel from: https://github.com/cgohlke/talib-onefile
2. Install it directly:
   ```bash
   pip install ta_lib-0.4.28-cp311-cp311-win_amd64.whl
   ```

### 4. Setup Pre-commit Hooks (Optional but Recommended)

```bash
pre-commit install
pre-commit run --all-files  # Run on all files first time
```

## Running the Application

```bash
shiny run app/main.py
```

The app will be available at `http://localhost:8000`

## Running Tests

```bash
pytest tests/
pytest tests/ --cov=app  # With coverage
```

## Code Quality & Linting

### Format and Lint Code (All-in-one with Ruff)

```bash
# Format code (Black-compatible)
ruff format app/ tests/

# Lint and auto-fix issues
ruff check --fix app/ tests/

# Type checking with MyPy
mypy app/

# Security checks with Bandit
bandit -r app/
```

### Pre-commit Hooks

Run all checks automatically before committing:

```bash
# Install hooks
pre-commit install

# Run on all files (first time)
pre-commit run --all-files

# Run on staged files (automatic on commit)
pre-commit run
```

### Ruff Configuration

- **Line length**: 100 characters
- **Python target**: 3.9+
- **Enabled rules**:
  - `E`, `W`: pycodestyle errors/warnings
  - `F`: Pyflakes
  - `I`: isort (import sorting)
  - `N`: pep8-naming
  - `UP`: pyupgrade
  - `B`: flake8-bugbear
  - `C4`: comprehensions
  - `S`: security (bandit)
- **Config file**: `pyproject.toml` `[tool.ruff]` section

## Project Structure

```
stock_analyzer/
├── app/                    # Main application
│   ├── main.py            # Entry point
│   ├── ui/                # UI components
│   ├── server/            # Server logic
│   └── utils/             # Utility modules
├── data/                  # Data storage
│   ├── raw/               # Raw data
│   ├── processed/         # Processed data (Parquet)
│   └── cache/             # Cached data
├── models/                # ML models
│   ├── trained/           # Trained models
│   └── configs/           # Model configurations
├── tests/                 # Test suite
├── notebooks/             # Jupyter notebooks
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── pyproject.toml         # Modern Python packaging
└── README.md              # Documentation
```

## Key Modules

### Data Loading (`app/utils/data_loader.py`)
- `fetch_stock_data()`: Get historical data from yfinance
- `fetch_fundamental_data()`: Get fundamental metrics
- `load_parquet()` / `save_parquet()`: Parquet file I/O

### Analysis (`app/utils/analysis.py`)
- `analyze_fundamentals()`: Calculate key metrics
- `calculate_financial_ratios()`: Compute financial ratios
- `screen_stocks()`: Filter stocks by criteria

### Models (`app/utils/models.py`)
- `create_sklearn_model()`: Create ML models
- `create_neural_network()`: Create TensorFlow models
- `train_model()`: Train and evaluate
- `predict_stock_price()`: Make predictions

### Visualization (`app/utils/visualization.py`)
- `plot_price_history()`: Interactive historical price charts (Plotly)
- `plot_returns_distribution()`: Interactive returns distribution (Plotly)
- `plot_technical_indicators()`: Interactive technical analysis charts (Plotly)
- `plot_model_performance()`: Interactive training metrics (Plotly)
- `plot_candlestick()`: Interactive candlestick charts (Plotly)

### Technical Analysis (`app/utils/technical_analysis.py`)
- `add_moving_averages()`: SMA and EMA calculation
- `add_rsi()`: Relative Strength Index
- `add_macd()`: MACD indicator
- `add_bollinger_bands()`: Bollinger Bands
- `add_atr()`: Average True Range
- `add_stochastic()`: Stochastic Oscillator
- `calculate_all_indicators()`: Calculate all indicators at once
- `get_signal_summary()`: Generate trading signals

## Adding New Features

1. Create utility functions in `app/utils/`
2. Add corresponding tests in `tests/`
3. Integrate with Shiny UI in `app/ui/pages.py`
4. Add server handlers in `app/server/handlers.py`

## Debugging

Enable debug mode in config:
```python
SHINY_DEBUG = True
```

Check logs:
```bash
shiny run app/main.py --reload
```

## Future Enhancements

### Large Dataset Training
For future features that handle large historical datasets:
- Consider using **Polars** for speed (5-10x faster than Pandas)
- Consider using **Apache Spark** for distributed processing
- These would be optional optimizations for specific training pipelines

## Resources

- [Shiny for Python](https://shiny.posit.co/py/)
- [Plotly](https://plotly.com/python/)
- [pandas_ta](https://github.com/twopirllc/pandas-ta)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [TensorFlow/Keras](https://www.tensorflow.org/)
- [Zipline](https://zipline.ml4trading.io/)

1. Create a feature branch
2. Make changes with tests
3. Run tests and linting
4. Submit a pull request
