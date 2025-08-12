import subprocess
import sys
import re

def check_commit_count(min_commits=19):
    try:
        result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True, check=True)
        count = int(result.stdout.strip())
        if count < min_commits:
            print(f"FAIL: Only {count} commits found (need at least {min_commits}).")
            return False
        print(f"PASS: {count} commits found.")
        return True
    except Exception as e:
        print(f"FAIL: Error checking commit count: {e}")
        return False

def check_uppercase_words_longer_than_1_letter(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        words = re.findall(r'\\b[A-Za-z]{2,}\\b', text)
        uppercase_words = [w for w in words if w.isupper()]
        if uppercase_words:
            print(f"FAIL: Found all-uppercase words: {', '.join(uppercase_words)}")
            return False
        print("PASS: No all-uppercase words found.")
        return True
    except Exception as e:
        print(f"FAIL: Error reading file: {e}")
        return False

def main():
    commit_ok = check_commit_count()
    file_ok = check_uppercase_words_longer_than_1_letter('about-us.txt')
    if commit_ok and file_ok:
        print("OVERALL: PASS")
        sys.exit(0)
    else:
        print("OVERALL: FAIL")
        sys.exit(1)

if __name__ == "__main__":
    main()
