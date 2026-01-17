import csv
import pandas as pd

PRODUCTS_PATH = "oliveyoung_products_final.csv"
ING_PATH = "product_ingredient_merged.csv"

OUT_PRODUCTS = "oliveyoung_products_final_reid.csv"
OUT_ING = "product_ingredient_merged_reid.csv"


def read_csv_safely(path: str) -> pd.DataFrame:
    encodings = ["utf-8-sig", "utf-8", "cp949", "euc-kr", "latin1"]
    last_err = None
    for enc in encodings:
        try:
            return pd.read_csv(path, encoding=enc, dtype=str)
        except Exception as e:
            last_err = e
    raise last_err


def main():
    df_prod = read_csv_safely(PRODUCTS_PATH)
    df_ing = read_csv_safely(ING_PATH)

    if "product_id" not in df_prod.columns or "group_id" not in df_prod.columns:
        raise ValueError(f"products 파일에 product_id/group_id가 없어요. columns={df_prod.columns.tolist()}")

    if "product_id" not in df_ing.columns:
        raise ValueError(f"ingredient 파일에 product_id가 없어요. columns={df_ing.columns.tolist()}")

    df_prod = df_prod.copy()
    df_prod["group_id"] = df_prod["group_id"].astype(str)
    df_prod["product_id"] = df_prod["product_id"].astype(str)

    prod_unique = (
        df_prod[["group_id", "product_id"]]
        .dropna()
        .drop_duplicates(subset=["group_id", "product_id"], keep="first")
        .reset_index(drop=True)
    )

    prod_unique["seq"] = prod_unique.groupby("group_id").cumcount() + 1
    prod_unique["new_product_id"] = prod_unique["group_id"] + "_" + prod_unique["seq"].astype(int).astype(str)

    id_map = dict(zip(prod_unique["product_id"], prod_unique["new_product_id"]))
    print("[INFO] 고유 product_id 매핑 개수:", len(id_map))

    df_prod["product_id"] = df_prod["product_id"].map(id_map)
    df_ing = df_ing.copy()
    df_ing["product_id"] = df_ing["product_id"].astype(str).map(id_map)

    unmatched_ing = df_ing["product_id"].isna().sum()
    print("[INFO] ingredient 매핑 실패 row 수:", unmatched_ing)

    df_prod.to_csv(OUT_PRODUCTS, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_ALL)
    df_ing.to_csv(OUT_ING, index=False, encoding="utf-8-sig", quoting=csv.QUOTE_ALL)

    print("[DONE] products 저장 ->", OUT_PRODUCTS)
    print("[DONE] ingredient 저장 ->", OUT_ING)


if __name__ == "__main__":
    main()
