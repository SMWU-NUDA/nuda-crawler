import csv
import pandas as pd

PRODUCTS_IN = "oliveyoung_products_final.csv"
ING_IN = "product_ingredient_final.csv"

PRODUCTS_OUT = "oliveyoung_products_final_clean.csv"
ING_OUT = "product_ingredient_final_clean.csv"

REPORT_OUT = "data_validation_report.txt"


def read_csv_safely(path: str) -> pd.DataFrame:
    encodings = ["utf-8-sig", "utf-8", "cp949", "euc-kr", "latin1"]
    last_err = None
    for enc in encodings:
        try:
            return pd.read_csv(path, encoding=enc, dtype=str)
        except Exception as e:
            last_err = e
    raise last_err


def remove_all_spaces(series: pd.Series) -> pd.Series:
    return series.astype(str).str.replace(" ", "", regex=False)


def main():
    df_p = read_csv_safely(PRODUCTS_IN)
    df_i = read_csv_safely(ING_IN)

    report_lines = []

    required_p = ["product_id", "category_code", "group_id"]
    required_i = ["product_id"]

    missing_cols_p = [c for c in required_p if c not in df_p.columns]
    missing_cols_i = [c for c in required_i if c not in df_i.columns]

    if missing_cols_p:
        raise ValueError(f"[ERROR] products에 필수 컬럼 누락: {missing_cols_p}")
    if missing_cols_i:
        raise ValueError(f"[ERROR] ingredient에 필수 컬럼 누락: {missing_cols_i}")

    p_pid_na = df_p["product_id"].isna().sum()
    i_pid_na = df_i["product_id"].isna().sum()

    report_lines.append(f"products rows: {len(df_p)}")
    report_lines.append(f"ingredients rows: {len(df_i)}")
    report_lines.append(f"products product_id NA: {p_pid_na}")
    report_lines.append(f"ingredients product_id NA: {i_pid_na}")

    p_ids = set(df_p["product_id"].dropna().astype(str).unique())
    i_ids = set(df_i["product_id"].dropna().astype(str).unique())

    missing_in_products = sorted(list(i_ids - p_ids))
    report_lines.append(f"unique product_id in products: {len(p_ids)}")
    report_lines.append(f"unique product_id in ingredients: {len(i_ids)}")
    report_lines.append(f"ingredient product_id not found in products: {len(missing_in_products)}")
    if missing_in_products:
        report_lines.append("sample missing product_id (up to 30): " + ", ".join(missing_in_products[:30]))

    p_cat_na = df_p["category_code"].isna().sum()
    report_lines.append(f"products category_code NA: {p_cat_na}")

    if "review_text" in df_p.columns:
        df_p = df_p.drop(columns=["review_text"])
        report_lines.append("dropped products.review_text")


    excluded = set(["name", "group_name"])
    for col in df_p.columns:
        if col in excluded:
            continue

        df_p[col] = df_p[col].fillna("")
        df_p[col] = remove_all_spaces(df_p[col]).replace({"": None})

    cols = df_p.columns.tolist()
    if "product_id" in cols and "category_code" in cols:
        cols.remove("category_code")
        pid_idx = cols.index("product_id")
        cols.insert(pid_idx + 1, "category_code")
        df_p = df_p[cols]
        report_lines.append("moved category_code right after product_id")

    df_p.to_csv(PRODUCTS_OUT, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_MINIMAL)
    df_i.to_csv(ING_OUT, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_MINIMAL)

    report_lines.append(f"saved -> {PRODUCTS_OUT}")
    report_lines.append(f"saved -> {ING_OUT}")

    with open(REPORT_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print("[DONE] Clean + Validate finished.")
    print(f"[DONE] Report saved -> {REPORT_OUT}")


if __name__ == "__main__":
    main()
