import sys

def parse_args():
    """Parse command-line arguments."""
    if len(sys.argv) > 1:
        return sys.argv[1], " ".join(sys.argv[2:])
    return None, None
