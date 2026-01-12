import os
import sys

def manage_environment():
    """Demonstrates using the os module for environment variables and paths."""
    print("--- OS Module Demonstration ---")
    
    # Get current working directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")

    # Access an environment variable (e.g., PATH)
    # Use .get() to avoid errors if the variable isn't set
    os_path_env = os.environ.get('PATH', 'PATH environment variable not found')
    print(f"Snippet of the PATH environment variable: {os_path_env[:50]}...")

    # Join path components securely
    new_path = os.path.join(current_dir, "temp_directory", "file.txt")
    print(f"Safely joined path: {new_path}")

    # List files and directories in the current directory
    # print(f"Files and directories in current location: {os.listdir(current_dir)}")
    
def handle_arguments():
    """Demonstrates using the sys module for command-line arguments and exiting."""
    print("\n--- SYS Module Demonstration ---")

    # Access command-line arguments
    script_name = sys.argv[0]
    arguments = sys.argv[1:]

    print(f"Script name: {script_name}")
    print(f"Arguments provided: {arguments}")

    if not arguments:
        print("No arguments provided. To test this, run the script like: python your_script_name.py arg1 arg2")
    
    # Check Python version information
    print(f"Python version: {sys.version}")

    # Example of exiting the script gracefully with an error code if needed
    # if some_error_condition:
    #     print("An error occurred. Exiting.")
    #     sys.exit(1) # Exits the program

if __name__ == "__main__":
    manage_environment()
    handle_arguments()