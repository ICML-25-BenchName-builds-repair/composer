# Test script to verify our fix for the transformers import

# Let's just check if the file has the correct imports
with open('composer/datasets/in_context_learning_evaluation.py', 'r') as f:
    content = f.read()

# Check if the direct import of transformers is removed
if 'import torch\nimport transformers' in content:
    print("Direct import of transformers found - this is bad!")
else:
    print("No direct import of transformers found - good!")

# Check if there are try/except blocks for transformers
if 'try:\n            import transformers' in content:
    print("Found try/except block for transformers import - good!")
else:
    print("No try/except block for transformers import found")

# Check if there are MissingConditionalImportError for transformers
if 'raise MissingConditionalImportError(extra_deps_group=\'nlp\',\n                                                conda_package=\'transformers\'' in content:
    print("Found MissingConditionalImportError for transformers - good!")
else:
    print("No MissingConditionalImportError for transformers found")

print("Test completed")