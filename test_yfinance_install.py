# Simple check for yfinance
try:
    import yfinance as yf
    print("yfinance imported successfully, version:", getattr(yf, "__version__", "unknown"))
except Exception as e:
    print("Failed to import yfinance:", e)
    raise
