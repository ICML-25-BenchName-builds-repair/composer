# Test script to verify the transformers import issue

import sys
print(f"Python version: {sys.version}")

# Check if transformers is installed
try:
    import transformers
    print(f"transformers is installed: {transformers.__version__}")
except ImportError:
    print("transformers is not installed")

# Look at the specific lines in the files
import inspect
import os

def print_file_snippet(file_path, start_line, num_lines=10):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    end_line = min(start_line + num_lines, len(lines))
    print(f"File: {file_path}, Lines {start_line}-{end_line}:")
    for i in range(start_line - 1, end_line):
        print(f"{i+1}: {lines[i].rstrip()}")
    print()

# Print the relevant sections of the files
print_file_snippet('composer/datasets/in_context_learning_evaluation.py', 10, 15)
print_file_snippet('composer/callbacks/eval_output_logging_callback.py', 10, 15)