import sys
import os

# Add the repository to the Python path
sys.path.insert(0, os.path.abspath('/lca-workspace/repos/mosaicml__composer'))

try:
    # Try to import transformers
    import transformers
    print("Successfully imported transformers")
except ImportError as e:
    print(f"Import error: {e}")
    
# Now try to import the module with a mock transformers module
if 'transformers' not in sys.modules:
    # Create a mock transformers module
    import types
    transformers_mock = types.ModuleType('transformers')
    sys.modules['transformers'] = transformers_mock
    
    try:
        # Now try to import the module
        from composer.datasets.in_context_learning_evaluation import InContextLearningCodeEvalDataset
        print("Successfully imported InContextLearningCodeEvalDataset with mock transformers")
    except ImportError as e:
        print(f"Import error with mock transformers: {e}")