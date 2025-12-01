# Stock Analyzer - Fundamental Analysis Web App

A Shiny web application for performing comprehensive fundamental analysis on stocks using machine learning and financial data processing.

## Features

- **Fundamental Analysis**: Analyze key financial metrics and ratios
- **Machine Learning Models**: 
  - scikit-learn for predictive modeling
  - TensorFlow/Keras for deep learning
- **Data Processing**: Efficient data handling with Pandas and Parquet files
- **Technical Analysis**: pandas_ta integration for 200+ technical indicators
- **Financial Data**: SEC filings via EdgarTools, market data via yfinance
- **Interactive Visualization**: Plotly for interactive charts, Shiny for web framework
- **Backtesting**: Zipline for strategy backtesting

## Project Structure

```
stock_analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Shiny app entry point
│   ├── ui/
│   │   ├── __init__.py
│   │   └── pages.py           # UI components and pages
│   ├── server/
│   │   ├── __init__.py
│   │   └── handlers.py        # Server-side logic
    └── utils/
        ├── __init__.py
        ├── data_loader.py         # Data fetching and loading
        ├── analysis.py            # Fundamental analysis functions
        ├── models.py              # ML model definitions
        ├── technical_analysis.py  # Technical indicators using pandas_ta
        └── visualization.py       # Interactive charts using Plotly
├── data/
│   ├── raw/                   # Raw data from APIs
│   ├── processed/             # Processed Parquet files
│   └── cache/                 # Cached data
├── models/
│   ├── trained/               # Saved trained models
│   └── configs/               # Model configuration files
├── tests/
│   ├── __init__.py
│   ├── test_analysis.py
│   ├── test_models.py
│   └── test_data_loader.py
├── notebooks/
│   └── exploration.ipynb      # Data exploration notebooks
├── requirements.txt           # Python dependencies
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/steiner-de/stock_analyzer.git
cd stock_analyzer
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

```bash
shiny run app/main.py
```

The app will be available at `http://localhost:8000`

## Key Components

### Data Loading (`app/utils/data_loader.py`)
- Fetch data from yfinance and EdgarTools
- Store in Parquet format using Polars

### Analysis (`app/utils/analysis.py`)
- Calculate fundamental metrics
- Perform ratio analysis
- Generate insights

### Models (`app/utils/models.py`)
- Stock price prediction models
- Classification models for buy/sell signals
- Model training and evaluation utilities

### Visualization (`app/utils/visualization.py`)
- Interactive charts with Matplotlib/Seaborn
- Dashboard components

## Development

Run tests:
```bash
pytest tests/
```

## License

MIT

## Authors

- John Steiner
