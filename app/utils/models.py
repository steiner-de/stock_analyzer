"""
Machine learning models for Stock Analyzer
"""

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from typing import Tuple, Dict, Any
import numpy as np


def create_sklearn_model(model_type: str = "random_forest"):
    """
    Create a scikit-learn model for stock prediction
    
    Args:
        model_type: Type of model ('random_forest' or 'gradient_boosting')
    
    Returns:
        Scikit-learn model instance
    """
    if model_type == "random_forest":
        return RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    elif model_type == "gradient_boosting":
        return GradientBoostingRegressor(n_estimators=100, max_depth=5, random_state=42)
    else:
        raise ValueError(f"Unknown model type: {model_type}")


def create_neural_network(input_shape: int, output_shape: int = 1) -> keras.Model:
    """
    Create a TensorFlow/Keras neural network for stock prediction
    
    Args:
        input_shape: Number of input features
        output_shape: Number of output features
    
    Returns:
        Keras Sequential model
    """
    model = keras.Sequential([
        keras.layers.Dense(128, activation='relu', input_shape=(input_shape,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(output_shape)
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    
    return model


def train_model(X: np.ndarray, y: np.ndarray, model_type: str = "random_forest", 
                test_size: float = 0.2) -> Tuple[Any, Dict[str, Any]]:
    """
    Train a machine learning model
    
    Args:
        X: Feature matrix
        y: Target vector
        model_type: Type of model to train
        test_size: Test set size
    
    Returns:
        Tuple of (trained model, metrics dictionary)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )
    
    if model_type == "neural_network":
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = create_neural_network(X_train_scaled.shape[1])
        model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, verbose=0)
        
        metrics = {
            "train_loss": float(model.evaluate(X_train_scaled, y_train, verbose=0)[0]),
            "test_loss": float(model.evaluate(X_test_scaled, y_test, verbose=0)[0]),
        }
    else:
        model = create_sklearn_model(model_type)
        model.fit(X_train, y_train)
        
        metrics = {
            "train_score": float(model.score(X_train, y_train)),
            "test_score": float(model.score(X_test, y_test)),
        }
    
    return model, metrics


def predict_stock_price(model: Any, features: np.ndarray) -> np.ndarray:
    """
    Make predictions using trained model
    
    Args:
        model: Trained model
        features: Feature matrix for prediction
    
    Returns:
        Predictions array
    """
    return model.predict(features)
