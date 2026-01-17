import pandas as pd

PRODUCTS_PATH = "oliveyoung_products_expanded_JIMIN.csv"
INGREDIENT_PATH = "product_ingredient_composition_starter_JIMIN.csv"

OUT_PATH = "oliveyoung_products_fixed.csv"
FAIL_PATH = "category_code_match_failed.csv"

def read_csv_safely(path: str) -> pd.DataFrame:
    encodings_to_try = ["utf-8", "utf-8-sig", "cp949", "euc-kr", "latin1"]
    last_err = None
    for enc in encodings_to_try:
        try:
            return pd.read_csv(path, encoding=enc)
        except UnicodeDecodeError as e:
            last_err = e
    return pd.read_csv(path, encoding="cp949", encoding_errors="replace")

df_products = read_csv_safely(PRODUCTS_PATH)
df_ing = read_csv_safely(INGREDIENT_PATH)

print("[INFO] products columns:", df_products.columns.tolist())
print("[INFO] ingredient columns:", df_ing.columns.tolist())

if "product_id" not in df_products.columns:
    raise ValueError("oliveyoung_products 파일에 product_id 컬럼이 없어요.")
if "product_id" not in df_ing.columns or "category_code" not in df_ing.columns:
    raise ValueError("product_ingredient 파일에 product_id 또는 category_code 컬럼이 없어요.")

if "variant" in df_products.columns:
    df_products = df_products.drop(columns=["variant"])
    print("[OK] variant 컬럼 삭제 완료")
else:
    print("[SKIP] variant 컬럼 없음")

df_map = df_ing[["product_id", "category_code"]].dropna()
df_map = (
    df_map.groupby("product_id")["category_code"]
    .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else x.iloc[0])
    .reset_index()
)

df_products = df_products.merge(df_map, on="product_id", how="left")

df_failed = df_products[df_products["category_code"].isna()].copy()

print(f"\n[INFO] category_code 매칭 실패 row 수: {len(df_failed)}")
failed_ids = df_failed["product_id"].dropna().unique().tolist()
print(f"[INFO] 매칭 실패 product_id 개수(중복 제거): {len(failed_ids)}")
print("\n[FAILED product_id 샘플 30개]")
print(failed_ids[:30])

df_failed.to_csv(FAIL_PATH, index=False, encoding="utf-8-sig")
print(f"\n[DONE] 실패 목록 저장 완료 -> {FAIL_PATH}")

df_products.to_csv(OUT_PATH, index=False, encoding="utf-8-sig")
print(f"[DONE] 최종 products 저장 완료 -> {OUT_PATH}")
