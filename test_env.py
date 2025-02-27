#!/usr/bin/env python3
# Test script to verify that the environment is set up correctly

import sys
print(f"Python version: {sys.version}")

# Test core packages
import numpy as np
import pandas as pd
import matplotlib
import sklearn
import scipy

print("\nCore packages:")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
print(f"SciPy: {scipy.__version__}")

# Test TensorFlow
try:
    import tensorflow as tf
    print("\nTensorFlow:")
    print(f"TensorFlow: {tf.__version__}")
    # Keras version is now part of TensorFlow version
    print(f"Keras is available: {'keras' in dir(tf)}")
    print("TensorFlow GPU available:", tf.config.list_physical_devices('GPU'))
except ImportError:
    print("\nTensorFlow not installed or not working correctly")

# Test Keras Core
try:
    import keras_core
    print("\nKeras Core:")
    print(f"Keras Core: {keras_core.__version__}")
except ImportError:
    print("\nKeras Core not installed or not working correctly")

# Test other ML packages
try:
    import xgboost
    import transformers
    print("\nOther ML packages:")
    print(f"XGBoost: {xgboost.__version__}")
    print(f"Transformers: {transformers.__version__}")
except ImportError:
    print("\nSome ML packages not installed or not working correctly")

# Test RL packages
try:
    import gymnasium
    print("\nReinforcement Learning:")
    print(f"Gymnasium: {gymnasium.__version__}")
except ImportError:
    print("\nGymnasium not installed or not working correctly")

print("\nEnvironment test completed successfully!") 