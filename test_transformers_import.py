#!/usr/bin/env python3
"""
Test script to reproduce the transformers import issue.
This script should fail before the fix and pass after the fix.
"""

import sys
import subprocess

def test_transformers_not_installed():
    """Test that transformers is not installed."""
    try:
        import transformers
        print("ERROR: transformers is installed, but it should not be for this test")
        return False
    except ImportError:
        print("✓ transformers is not installed (as expected)")
        return True

def test_direct_import():
    """Test importing the problematic module directly."""
    try:
        import sys
        import os
        sys.path.insert(0, os.path.join(os.getcwd(), 'composer', 'datasets'))
        import in_context_learning_evaluation
        print("✓ Direct import of in_context_learning_evaluation succeeded")
        return True
    except ImportError as e:
        print(f"✗ Direct import failed: {e}")
        return False

def test_smoketest_import():
    """Test the smoketest import that was failing."""
    try:
        from composer import (algorithms, callbacks, core, datasets, devices, functional, 
                             loggers, loss, metrics, models, optim, profiler, trainer, utils)
        print("✓ Smoketest imports succeeded")
        return True
    except ImportError as e:
        print(f"✗ Smoketest imports failed: {e}")
        return False

def main():
    print("Testing transformers import issue...")
    
    # First check that transformers is not installed
    if not test_transformers_not_installed():
        sys.exit(1)
    
    # Test direct import
    success1 = test_direct_import()
    
    # Test smoketest import
    success2 = test_smoketest_import()
    
    if success1 and success2:
        print("\n✓ All tests passed!")
        return 0
    else:
        print("\n✗ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())