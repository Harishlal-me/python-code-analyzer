# Python Code Analyzer 🐍

A command-line tool that analyzes Python code files and extracts useful information about their structure.

## Features

✨ **What it analyzes:**
- Function definitions (name, parameters, line numbers, docstrings)
- Class definitions (name, methods, line numbers)
- Import statements (modules, aliases)
- Code metrics (total lines, counts)

📊 **Output formats:**
- Colored console output
- JSON file with complete analysis
- Text summary report

🔄 **Bonus:** Compare two Python files side-by-side

## Quick Start

### 1. Analyze a single file:
```bash
python analyzer.py examples/sample.py
```

### 2. Compare two files:
```bash
python analyzer.py examples/sample.py examples/complex_example.py
```

### 3. Check output files:
- `output/results.json` - Complete analysis in JSON
- `output/summary.txt` - Human-readable summary

## Example Output