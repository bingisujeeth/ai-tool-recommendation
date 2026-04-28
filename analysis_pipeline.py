import pandas as pd


# -------------------------------
# LOAD DATA
# -------------------------------
def load_data(path):
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip()
    print("Data Loaded Successfully\n")
    return df


# -------------------------------
# SHOW COLUMN NAMES
# -------------------------------
def show_columns(df):
    print("ACTUAL COLUMN NAMES:\n")
    for i, col in enumerate(df.columns):
        print(f"{i}: '{col}'")
    print("\n")


# -------------------------------
# CLEAN DATA
# -------------------------------
def clean_data(df):
    df = df.dropna(how='all')
    df = df.fillna("")
    print("Data Cleaned\n")
    return df


# -------------------------------
# HELPER FUNCTIONS
# -------------------------------
def calculate_percentages(series):
    return (series.value_counts(normalize=True) * 100).round(1)


def content_analysis(series, categories):
    series = series.astype(str)
    text = series.str.lower()

    results = {}
    for category, pattern in categories.items():
        results[category] = text.str.contains(pattern).sum()

    return results


def extract_quotes(series):
    series = series.dropna().astype(str)
    return series.sample(min(5, len(series))).tolist()


def get_recommendation(percent_series):
    return percent_series.idxmax()


# -------------------------------
# ANALYSIS FUNCTION (FIXED)
# -------------------------------
def analyze_task(df, tool_col, reason_col, task_name, categories):

    print(f"\n{task_name.upper()} ANALYSIS\n")

    # Handle duplicate column issue
    tool_data = df[tool_col]
    if isinstance(tool_data, pd.DataFrame):
        tool_data = tool_data.iloc[:, 0]

    reason_data = df[reason_col]
    if isinstance(reason_data, pd.DataFrame):
        reason_data = reason_data.iloc[:, 0]

    # Percentages
    tool_percent = calculate_percentages(tool_data)
    print("Tool Preference (%):\n", tool_percent, "\n")

    # Recommendation
    recommended = get_recommendation(tool_percent)
    print("Recommended Tool:", recommended, "\n")

    # Content analysis
    category_counts = content_analysis(reason_data, categories)
    print("Reasons (Grouped):\n", category_counts, "\n")

    # Quotes
    print("Sample Quotes:")
    for q in extract_quotes(reason_data):
        print("-", q)

    print("\n" + "-"*50)


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":

    file_path = "data/survey.xlsx"

    df = load_data(file_path)

    show_columns(df)

    df = clean_data(df)

    # -------------------------------
    # COLUMN INDEX MAPPING (YOUR DATA)
    # -------------------------------

    CONTENT_TOOL = df.columns[9]
    CONTENT_REASON = df.columns[10]

    PROOF_TOOL = df.columns[13]
    PROOF_REASON = df.columns[14]

    IMAGE_TOOL = df.columns[16]
    IMAGE_REASON = df.columns[17]

    INFO_TOOL = df.columns[20]
    INFO_REASON = df.columns[21]

    # -------------------------------
    # CATEGORY DEFINITIONS
    # -------------------------------

    content_categories = {
        "Ease of Use": "easy|simple|user",
        "Quality": "quality|good|better",
        "Speed": "fast|quick",
        "Creativity": "idea|creative"
    }

    proofreading_categories = {
        "Accuracy": "accurate|correct",
        "Grammar": "grammar|spelling",
        "Clarity": "clear|understand",
        "Speed": "fast|quick"
    }

    image_categories = {
        "Quality": "quality|realistic",
        "Creativity": "creative|design",
        "Ease of Use": "easy|simple"
    }

    info_categories = {
        "Accuracy": "accurate|correct",
        "Speed": "fast|quick",
        "Detail": "detailed|explain"
    }

    # -------------------------------
    # RUN ANALYSIS
    # -------------------------------

    analyze_task(df, CONTENT_TOOL, CONTENT_REASON, "Content Creation", content_categories)

    analyze_task(df, PROOF_TOOL, PROOF_REASON, "Proofreading", proofreading_categories)

    analyze_task(df, IMAGE_TOOL, IMAGE_REASON, "Image Generation", image_categories)

    analyze_task(df, INFO_TOOL, INFO_REASON, "Information Seeking", info_categories)