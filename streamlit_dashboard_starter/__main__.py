import sys

from streamlit_dashboard_starter.streamlit_dashboard_starter import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
