from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parents[1] / "data" / "raw" / "sales.xlsx"
OUT = Path(__file__).resolve().parents[1] / "reports" / "figures"

def main():
    df = pd.read_excel(RAW, engine="openpyxl")
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)

if __name__ == "__main__":
    main()