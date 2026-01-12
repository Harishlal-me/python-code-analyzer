import ast
import json
import sys

class CodeAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.results = {
            'file': filepath,
            'functions': [],
            'classes': [],
            'imports': [],
            'metrics': {}
        }
    
    def read_file(self):
        """Read the Python file"""
        try:
            with open(self.filepath, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{self.filepath}' not found")
            return None
    
    def analyze(self):
        """Main analysis function"""
        code = self.read_file()
        if code is None:
            return None
        
        # Parse the code
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            print(f"Syntax error in file: {e}")
            return None
        
        # Analyze the tree
        self._extract_functions(tree)
        self._extract_classes(tree)
        self._extract_imports(tree)
        self._calculate_metrics(code, tree)
        
        return self.results
    
    def _extract_functions(self, tree):
        """Extract all function definitions"""
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_info = {
                    'name': node.name,
                    'line_number': node.lineno,
                    'arguments': [arg.arg for arg in node.args.args],
                    'has_docstring': ast.get_docstring(node) is not None
                }
                self.results['functions'].append(func_info)
    
    def _extract_classes(self, tree):
        """Extract all class definitions"""
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Find methods in this class
                methods = []
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        methods.append(item.name)
                
                class_info = {
                    'name': node.name,
                    'line_number': node.lineno,
                    'methods': methods
                }
                self.results['classes'].append(class_info)
    
    def _extract_imports(self, tree):
        """Extract all import statements"""
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    self.results['imports'].append({
                        'module': alias.name,
                        'alias': alias.asname,
                        'line': node.lineno
                    })
            elif isinstance(node, ast.ImportFrom):
                module = node.module if node.module else ''
                for alias in node.names:
                    self.results['imports'].append({
                        'module': f"{module}.{alias.name}" if module else alias.name,
                        'alias': alias.asname,
                        'line': node.lineno
                    })
    
    def _calculate_metrics(self, code, tree):
        """Calculate basic code metrics"""
        lines = code.split('\n')
        
        self.results['metrics'] = {
            'total_lines': len(lines),
            'total_functions': len(self.results['functions']),
            'total_classes': len(self.results['classes']),
            'total_imports': len(self.results['imports'])
        }
    
    def print_results(self):
        """Print results in readable format"""
        print("\n" + "="*50)
        print(f"Analysis Results for: {self.filepath}")
        print("="*50 + "\n")
        
        print("📊 METRICS:")
        for key, value in self.results['metrics'].items():
            print(f"  {key}: {value}")
        
        print("\n📦 IMPORTS:")
        for imp in self.results['imports']:
            alias_info = f" as {imp['alias']}" if imp['alias'] else ""
            print(f"  Line {imp['line']}: {imp['module']}{alias_info}")
        
        print("\n🏛️ CLASSES:")
        for cls in self.results['classes']:
            print(f"  {cls['name']} (Line {cls['line_number']})")
            print(f"    Methods: {', '.join(cls['methods'])}")
        
        print("\n🔧 FUNCTIONS:")
        for func in self.results['functions']:
            args = ', '.join(func['arguments']) if func['arguments'] else 'none'
            docstring = "✓" if func['has_docstring'] else "✗"
            print(f"  {func['name']}({args}) - Line {func['line_number']} [Docs: {docstring}]")
        
        print("\n" + "="*50 + "\n")
    
    def save_json(self, output_file='output/results.json'):
        """Save results to JSON file"""
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"✅ Results saved to: {output_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <path_to_python_file>")
        print("Example: python analyzer.py examples/sample.py")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    print(f"\n🔍 Analyzing: {filepath}\n")
    
    analyzer = CodeAnalyzer(filepath)
    results = analyzer.analyze()
    
    if results:
        analyzer.print_results()
        analyzer.save_json()
    else:
        print("❌ Analysis failed")


if __name__ == "__main__":
    main()