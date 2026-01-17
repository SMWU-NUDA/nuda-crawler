import pandas as pd

FILE1 = "oliveyoung_products_jihyo_final.csv"
FILE2 = "oliveyoung_products_jimin_final.csv"
OUT_PATH = "oliveyoung_products_merged.csv"

# product_id를 group_id + 번호로 만들 때, 구분자(원하면 "_"로 바꾸기)
SEP = "_"  # 예: "" -> 10001, 10002 / "_" -> 1000_1, 1000_2

def read_csv_safely(path: str) -> pd.DataFrame:
    encodings_to_try = ["utf-8", "utf-8-sig", "cp949", "euc-kr", "latin1"]
    for enc in encodings_to_try:
        try:
            return pd.read_csv(path, encoding=enc)
        except UnicodeDecodeError:
            continue
    return pd.read_csv(path, encoding="cp949", encoding_errors="replace")

# 1) 파일 로드
df1 = read_csv_safely(FILE1)
df2 = read_csv_safely(FILE2)

print("[INFO] file1 rows:", len(df1))
print("[INFO] file2 rows:", len(df2))

# 2) 합치기
df = pd.concat([df1, df2], ignore_index=True)
print("[INFO] merged rows:", len(df))

# 3) org_price 제거
if "org_price" in df.columns:
    df = df.drop(columns=["org_price"])
    print("[OK] org_price 컬럼 제거 완료")
else:
    print("[SKIP] org_price 컬럼이 원래 없어요")

# 4) group_id 컬럼 찾기 (이름이 다를 수 있어서 후보 탐색)
group_candidates = ["group_id", "groupId", "groupID", "group", "group_no", "groupNo"]
group_col = next((c for c in group_candidates if c in df.columns), None)
if group_col is None:
    raise ValueError(f"group_id 컬럼을 찾지 못했어요. 현재 컬럼: {df.columns.tolist()}")

print(f"[INFO] Using group column = {group_col}")

# 5) 같은 group 내에서 product_id를 group_id+1,2,3... 으로 재부여
# - 현재 행 순서를 유지한 채로 cumcount로 번호를 매김
df[group_col] = df[group_col].astype(str)
seq = df.groupby(group_col).cumcount() + 1

# product_id가 숫자로만 이루어지길 원하면 아래 방식(문자열 연결)
df["product_id"] = df[group_col] + SEP + seq.astype(str)

print("[OK] product_id 재부여 완료 (group 기준 연번)")

# 6) category_code를 product_id 바로 뒤로 이동 (컬럼 순서 정리)
cols = df.columns.tolist()
if "category_code" in cols and "product_id" in cols:
    cols.remove("category_code")
    pid_idx = cols.index("product_id")
    cols.insert(pid_idx + 1, "category_code")
    df = df[cols]
    print("[OK] category_code 위치 이동 완료 (product_id 다음)")
else:
    print("[WARN] product_id 또는 category_code 컬럼이 없어서 순서 변경 못했어요")

# 7) 저장
df.to_csv(OUT_PATH, index=False, encoding="utf-8-sig")
print(f"[DONE] 저장 완료 -> {OUT_PATH}")
