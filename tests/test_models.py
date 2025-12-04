"""
Tests for machine learning models
"""

import pytest
import numpy as np
from sklearn.datasets import make_regression
from app.utils.models import create_sklearn_model, create_neural_network, train_model, predict_stock_price


def test_create_sklearn_model():
    """Test scikit-learn model creation"""
    model = create_sklearn_model("random_forest")
    assert model is not None
    
    model = create_sklearn_model("gradient_boosting")
    assert model is not None


def test_create_neural_network():
    """Test neural network creation"""
    model = create_neural_network(input_shape=10)
    assert model is not None
    assert len(model.layers) > 0


def test_train_model():
    """Test model training"""
    X, y = make_regression(n_samples=100, n_features=10, random_state=42) # type: ignore
    
    model, metrics = train_model(X, y, model_type="random_forest")
    
    assert model is not None
    assert "train_score" in metrics
    assert "test_score" in metrics


def test_predict_stock_price():
    """Test stock price prediction"""
    X, y = make_regression(n_samples=100, n_features=10, random_state=42) # type: ignore
    
    model, _ = train_model(X, y, model_type="random_forest")
    
    predictions = predict_stock_price(model, X[:5])
    assert len(predictions) == 5
