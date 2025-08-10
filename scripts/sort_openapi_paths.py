#!/usr/bin/env python3
"""
Sort OpenAPI paths alphabetically while preserving all other content.

This script reads the OpenAPI JSON specification file, sorts all endpoint paths
alphabetically, and writes the sorted version back to the file. This ensures
consistent organization and makes the API documentation easier to navigate.

Usage:
    python scripts/sort_openapi_paths.py [path_to_openapi_json]

If no path is provided, it defaults to: api-reference/openapi.json
"""

import json
import sys
import os
from collections import OrderedDict
from pathlib import Path

def sort_openapi_paths(file_path):
    """
    Read OpenAPI JSON file, sort paths alphabetically, and write back to file.
    
    Args:
        file_path (str): Path to the OpenAPI JSON file
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Resolve absolute path
    file_path = os.path.abspath(file_path)
    
    if not os.path.exists(file_path):
        print(f"❌ ERROR: File not found: {file_path}")
        return False
    
    print(f"📖 Reading OpenAPI file: {file_path}")
    
    try:
        # Read the JSON file
        with open(file_path, 'r', encoding='utf-8') as f:
            openapi_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ ERROR: Invalid JSON in file: {e}")
        return False
    except Exception as e:
        print(f"❌ ERROR: Failed to read file: {e}")
        return False
    
    # Check if this is a valid OpenAPI file
    if 'paths' not in openapi_data:
        print("❌ ERROR: No 'paths' section found in the JSON file")
        return False
    
    # Extract the paths section
    paths = openapi_data['paths']
    original_count = len(paths)
    print(f"🔍 Found {original_count} paths to sort")
    
    if original_count == 0:
        print("⚠️  No paths found to sort")
        return True
    
    # Get all path keys and sort them alphabetically
    path_keys = list(paths.keys())
    path_keys.sort()
    
    print("📋 Path sorting order:")
    for i, path in enumerate(path_keys, 1):
        print(f"  {i:2d}. {path}")
    
    # Create a new ordered dictionary with sorted paths
    sorted_paths = OrderedDict()
    for path in path_keys:
        sorted_paths[path] = paths[path]
    
    # Replace the paths section with the sorted version
    openapi_data['paths'] = sorted_paths
    
    try:
        # Write the sorted JSON back to file
        print(f"\n💾 Writing sorted OpenAPI file back to: {file_path}")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(openapi_data, f, indent=2, separators=(',', ': '))
        
        print("✅ Successfully sorted OpenAPI paths alphabetically")
        return True
        
    except Exception as e:
        print(f"❌ ERROR: Failed to write file: {e}")
        return False

def main():
    """Main function to handle command line execution."""
    # Determine the OpenAPI file path
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Default path relative to script location
        script_dir = Path(__file__).parent
        repo_root = script_dir.parent
        file_path = repo_root / "api-reference" / "openapi.json"
    
    print("🚀 OpenAPI Path Sorter")
    print("=" * 50)
    
    try:
        success = sort_openapi_paths(str(file_path))
        if success:
            print("\n🎉 OpenAPI paths have been sorted successfully!")
            print("\n💡 Tip: Run this script after adding new endpoints to maintain alphabetical order.")
        else:
            print("\n❌ Failed to sort OpenAPI paths")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()