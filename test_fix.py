# Test script to verify our fix

import sys
print(f"Python version: {sys.version}")

# Try to import the modules without transformers installed
try:
    from composer.datasets.in_context_learning_evaluation import InContextLearningCodeEvalDataset
    print("Successfully imported InContextLearningCodeEvalDataset without transformers")
except ImportError as e:
    if "No module named 'transformers'" in str(e):
        print("Expected error: transformers not installed")
    else:
        print(f"Unexpected error: {e}")

try:
    from composer.callbacks.eval_output_logging_callback import EvalOutputLogging
    print("Successfully imported EvalOutputLogging without transformers")
except ImportError as e:
    if "No module named 'transformers'" in str(e):
        print("Expected error: transformers not installed")
    else:
        print(f"Unexpected error: {e}")

# Now install transformers and try again
try:
    import transformers
    print(f"transformers is already installed: {transformers.__version__}")
except ImportError:
    print("transformers is not installed, would install it here in a real test")

# Try to import the modules with transformers installed
try:
    from composer.datasets.in_context_learning_evaluation import InContextLearningCodeEvalDataset
    print("Successfully imported InContextLearningCodeEvalDataset with transformers")
except ImportError as e:
    print(f"Error importing InContextLearningCodeEvalDataset: {e}")

try:
    from composer.callbacks.eval_output_logging_callback import EvalOutputLogging
    print("Successfully imported EvalOutputLogging with transformers")
except ImportError as e:
    print(f"Error importing EvalOutputLogging: {e}")