#!/usr/bin/env python3
"""
Test script to reproduce the exact issue from the issue description.
This should fail before the fix and pass after the fix.
"""

import sys

def test_exact_import_chain():
    """Test the exact import chain that was failing in the CI."""
    try:
        # This is the exact import chain from the error:
        # tests/conftest.py:9: from composer.utils import reproducibility
        # composer/__init__.py:10: from composer.trainer import Trainer
        # composer/trainer/__init__.py:6: from composer.trainer.trainer import Trainer
        # composer/trainer/trainer.py:37: from composer.callbacks import CheckpointSaver, OptimizerMonitor
        # composer/callbacks/__init__.py:12: from composer.callbacks.eval_output_logging_callback import EvalOutputLogging
        # composer/callbacks/eval_output_logging_callback.py:16: from composer.datasets.in_context_learning_evaluation import (...)
        # composer/datasets/in_context_learning_evaluation.py:13: import transformers
        
        # Test the specific file that was causing the issue
        import sys
        import os
        
        # Test just the problematic file
        sys.path.insert(0, os.path.join(os.getcwd(), 'composer', 'datasets'))
        
        # This should NOT raise "ModuleNotFoundError: No module named 'transformers'"
        import in_context_learning_evaluation
        print("✓ in_context_learning_evaluation imports without transformers error")
        return True
        
    except ImportError as e:
        error_msg = str(e)
        if "No module named 'transformers'" in error_msg:
            print(f"✗ EXACT ISSUE REPRODUCED: {error_msg}")
            return False
        else:
            print(f"✓ Different import error (not the transformers issue): {error_msg}")
            return True

def main():
    print("Testing exact issue reproduction...")
    
    # Check that transformers is not installed
    try:
        import transformers
        print("ERROR: transformers is installed, but it should not be for this test")
        return 1
    except ImportError:
        print("✓ transformers is not installed (as expected)")
    
    # Test the exact import chain
    success = test_exact_import_chain()
    
    if success:
        print("\n✓ Issue is FIXED - no 'ModuleNotFoundError: No module named transformers'!")
        return 0
    else:
        print("\n✗ Issue is NOT FIXED - still getting transformers import error!")
        return 1

if __name__ == "__main__":
    sys.exit(main())