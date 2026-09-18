import subprocess

def get_diff():
    result = subprocess.run(['git', 'diff', '--cached'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Could not get staged files ")
        return None

    return result.stdout