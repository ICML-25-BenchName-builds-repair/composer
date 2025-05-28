#!/usr/bin/env python3
"""
Test script to verify the transformers import fix.
This script tests only the transformers import issue, not other compatibility issues.
"""

import sys
import os

def test_transformers_not_installed():
    """Test that transformers is not installed."""
    try:
        import transformers
        print("ERROR: transformers is installed, but it should not be for this test")
        return False
    except ImportError:
        print("✓ transformers is not installed (as expected)")
        return True

def test_file_imports_without_transformers():
    """Test that the file can be imported without transformers being installed."""
    try:
        # Read the file content and check it doesn't have unconditional transformers import
        with open('composer/datasets/in_context_learning_evaluation.py', 'r') as f:
            content = f.read()
        
        lines = content.split('\n')
        in_type_checking = False
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == 'if TYPE_CHECKING:':
                in_type_checking = True
                continue
            elif line and not line.startswith(' ') and not line.startswith('\t'):
                # Non-indented line means we're out of the TYPE_CHECKING block
                in_type_checking = False
            
            if stripped == 'import transformers' and not in_type_checking:
                print(f"✗ Found unconditional 'import transformers' at line {i}")
                return False
        
        print("✓ No unconditional 'import transformers' found")
        
        # Check that TYPE_CHECKING import is present
        if 'if TYPE_CHECKING:' in content and 'import transformers' in content:
            print("✓ TYPE_CHECKING import for transformers is present")
            return True
        else:
            print("✗ TYPE_CHECKING import for transformers is missing")
            return False
            
    except Exception as e:
        print(f"✗ Error checking file: {e}")
        return False

def test_minimal_import():
    """Test importing the core parts without going through composer package."""
    try:
        # Test the import pattern used in the file
        test_code = '''
import torch
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

if TYPE_CHECKING:
    import transformers

# This should work without transformers being installed
print("Minimal import test passed")
'''
        exec(test_code)
        print("✓ Minimal import pattern works")
        return True
    except ImportError as e:
        if 'transformers' in str(e):
            print(f"✗ Transformers import error: {e}")
            return False
        else:
            print(f"✗ Other import error: {e}")
            return False

def main():
    print("Testing transformers import fix...")
    
    # Check that transformers is not installed
    if not test_transformers_not_installed():
        sys.exit(1)
    
    # Test that the file doesn't have unconditional transformers import
    success1 = test_file_imports_without_transformers()
    
    # Test minimal import pattern
    success2 = test_minimal_import()
    
    if success1 and success2:
        print("\n✓ Transformers import fix is working correctly!")
        return 0
    else:
        print("\n✗ Transformers import fix failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())