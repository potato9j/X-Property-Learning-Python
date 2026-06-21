from __future__ import annotations

import textwrap
from pathlib import Path

from bootstrap_course_repository import DAY_SPECS, ROOT, week_slug


def write(path: Path, body: str) -> None:
    path.write_text(textwrap.dedent(body).strip() + "\n", encoding="utf-8")


SNIPPETS = {
    1: '''
    # 값, 표현식, 변수, 타입을 한 줄씩 확인합니다.
    systolic = 118
    diastolic = 76
    label = "stable"
    is_normal_range = systolic < 120 and diastolic < 80

    print("systolic value:", systolic)
    print("systolic type:", type(systolic).__name__)
    print("label type:", type(label).__name__)
    print("comparison result:", is_normal_range, type(is_normal_range).__name__)
    print("reading task:", "오른쪽 값이 먼저 계산되고 왼쪽 이름에 붙습니다.")
    ''',
    2: '''
    # 문자열은 글자의 순서, 리스트는 값의 순서를 다룹니다.
    note = "glucose high"
    tokens = note.split()
    first_word = tokens[0]
    shortened = note[:7]
    tokens.append("review")

    print("original note:", note)
    print("tokens:", tokens)
    print("first word:", first_word)
    print("slice note[:7]:", shortened)
    print("reading task:", "index는 0부터 시작하고 slice의 끝 위치는 포함되지 않습니다.")
    ''',
    3: '''
    # dict는 key로 값을 찾고, tuple과 set은 데이터의 성격을 다르게 표현합니다.
    patient = {"id": "P001", "age": 21, "group": "A"}
    immutable_pair = ("glucose", 107)
    observed_groups = {"A", "B", "A"}

    print("patient keys:", list(patient.keys()))
    print("age by key:", patient["age"])
    print("tuple item:", immutable_pair[0], immutable_pair[1])
    print("unique groups:", sorted(observed_groups))
    print("reading task:", "dict는 순서보다 이름으로 값을 찾는 데 초점을 둡니다.")
    ''',
    4: '''
    # 조건문과 반복문은 여러 행을 같은 기준으로 읽게 합니다.
    glucose_values = [91, 107, 86, 118]
    threshold = 100
    flags = []

    for value in glucose_values:
        if value >= threshold:
            flags.append("review")
        else:
            flags.append("ok")

    compact_flags = ["review" if value >= threshold else "ok" for value in glucose_values]
    print("flags:", flags)
    print("compact flags:", compact_flags)
    print("reading task:", "for는 값을 하나씩 꺼내고 if는 기준에 따라 갈림길을 만듭니다.")
    ''',
    5: '''
    # 함수는 반복되는 절차에 이름을 붙이고 입력과 출력을 분명하게 만듭니다.
    def classify_glucose(value: int, threshold: int = 100) -> str:
        if value >= threshold:
            return "review"
        return "ok"

    values = [91, 107, 86, 118]
    labels = [classify_glucose(value) for value in values]

    print("labels:", labels)
    print("custom threshold:", classify_glucose(107, threshold=110))
    print("reading task:", "parameter는 함수 안에서만 쓰이는 이름이고 return은 밖으로 나가는 값입니다.")
    ''',
    6: '''
    # 오류 메시지와 파일 경로는 코드를 고칠 때 먼저 읽어야 하는 정보입니다.
    from pathlib import Path

    data_path = Path("datasets") / "synthetic_patients.csv"
    print("path text:", str(data_path))
    print("file exists:", data_path.exists())

    raw_value = "107"
    try:
        glucose = int(raw_value)
        print("converted value:", glucose, type(glucose).__name__)
    except ValueError as error:
        print("conversion failed:", error)

    print("reading task:", "traceback이 나오면 마지막 줄의 오류 종류와 위치부터 읽습니다.")
    ''',
    7: '''
    # 1주차 내용을 연결해 작은 입력-처리-출력 흐름을 읽습니다.
    records = [{"id": "P001", "glucose": 91}, {"id": "P002", "glucose": 118}]

    def needs_review(row: dict) -> bool:
        return row["glucose"] >= 100

    report = []
    for row in records:
        report.append({"id": row["id"], "review": needs_review(row)})

    print("records:", records)
    print("report:", report)
    print("reading task:", "list, dict, function, for, if의 역할을 한 줄씩 분리해 설명합니다.")
    ''',
    8: '''
    # 2차원 리스트로 배열의 shape, dtype, indexing 감각을 먼저 익힙니다.
    matrix = [[91, 19], [107, 21], [86, 22]]
    row_count = len(matrix)
    column_count = len(matrix[0])
    first_row = matrix[0]
    glucose_column = [row[0] for row in matrix]

    print("shape:", (row_count, column_count))
    print("first row:", first_row)
    print("glucose column:", glucose_column)
    print("value type:", type(matrix[0][0]).__name__)
    print("reading task:", "shape는 데이터가 몇 행 몇 열인지 말해 주는 약속입니다.")
    ''',
    9: '''
    # 벡터화와 broadcasting을 순수 Python 계산으로 해석합니다.
    values = [91, 107, 86, 118]
    offset = 10
    centered = [value - 100 for value in values]
    broadcast_added = [value + offset for value in values]
    dot = sum(a * b for a, b in zip([1, 2, 3], [4, 5, 6]))

    print("centered:", centered)
    print("broadcast added:", broadcast_added)
    print("dot product:", dot)
    print("reading task:", "반복문으로 읽히는 계산을 배열 라이브러리는 한 번의 연산처럼 표현합니다.")
    ''',
    10: '''
    # DataFrame을 배우기 전, 행과 열 선택을 list와 dict로 해석합니다.
    table = [
        {"id": "P001", "group": "A", "glucose": 91},
        {"id": "P002", "group": "B", "glucose": 118},
        {"id": "P003", "group": "A", "glucose": 86},
    ]
    glucose_column = [row["glucose"] for row in table]
    group_a_rows = [row for row in table if row["group"] == "A"]

    print("glucose column:", glucose_column)
    print("group A rows:", group_a_rows)
    print("reading task:", "pandas의 열 선택과 행 필터링도 결국 이름과 조건으로 값을 고르는 일입니다.")
    ''',
    11: '''
    # 결측치, groupby, merge를 작은 표 두 개로 해석합니다.
    labs = [{"id": "P001", "glucose": 91}, {"id": "P002", "glucose": None}, {"id": "P003", "glucose": 118}]
    groups = {"P001": "A", "P002": "B", "P003": "A"}
    cleaned = [row for row in labs if row["glucose"] is not None]
    merged = [{**row, "group": groups[row["id"]]} for row in cleaned]
    group_a_mean = sum(row["glucose"] for row in merged if row["group"] == "A") / 2

    print("cleaned:", cleaned)
    print("merged:", merged)
    print("group A mean:", group_a_mean)
    print("reading task:", "결측치를 처리한 뒤에야 groupby나 merge 결과를 믿을 수 있습니다.")
    ''',
    12: '''
    # 시각화는 그림을 그리기 전에도 분포와 이상값을 읽는 과정에서 시작합니다.
    values = [82, 91, 94, 107, 118, 165]
    bins = {"under_100": 0, "100_to_139": 0, "140_or_more": 0}
    for value in values:
        if value < 100:
            bins["under_100"] += 1
        elif value < 140:
            bins["100_to_139"] += 1
        else:
            bins["140_or_more"] += 1

    print("histogram bins:", bins)
    print("max value:", max(values))
    print("reading task:", "그래프는 예쁜 그림이 아니라 분포와 이상한 값을 찾는 도구입니다.")
    ''',
    13: '''
    # 표본, 평균, 분산은 일부 관찰값으로 전체를 조심스럽게 설명하는 언어입니다.
    values = [82, 91, 94, 107, 118]
    mean = sum(values) / len(values)
    squared_errors = [(value - mean) ** 2 for value in values]
    variance = sum(squared_errors) / len(values)

    print("sample values:", values)
    print("mean:", round(mean, 2))
    print("variance:", round(variance, 2))
    print("reading task:", "평균은 중심을, 분산은 값들이 중심에서 얼마나 퍼졌는지를 설명합니다.")
    ''',
    14: '''
    # 추론과 회귀는 차이와 관계를 조심스럽게 읽는 절차입니다.
    x_age = [19, 21, 22, 20]
    y_glucose = [91, 107, 86, 118]
    x_mean = sum(x_age) / len(x_age)
    y_mean = sum(y_glucose) / len(y_glucose)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_age, y_glucose))
    denominator = sum((x - x_mean) ** 2 for x in x_age)
    slope = numerator / denominator

    print("age mean:", x_mean)
    print("glucose mean:", y_mean)
    print("simple regression slope:", round(slope, 2))
    print("reading task:", "기울기는 x가 1 증가할 때 y가 평균적으로 어떻게 움직이는지 읽는 값입니다.")
    ''',
    15: '''
    # 머신러닝은 데이터를 나누고 기준 모델과 비교하는 절차부터 시작합니다.
    rows = [{"x": 1, "y": 3}, {"x": 2, "y": 5}, {"x": 3, "y": 7}, {"x": 4, "y": 9}]
    train = rows[:3]
    validation = rows[3:]
    baseline_prediction = sum(row["y"] for row in train) / len(train)
    error = abs(validation[0]["y"] - baseline_prediction)

    print("train rows:", train)
    print("validation rows:", validation)
    print("baseline prediction:", baseline_prediction)
    print("validation absolute error:", error)
    print("reading task:", "검증 데이터는 학습에 쓰지 않은 데이터여야 일반화 질문을 할 수 있습니다.")
    ''',
    16: '''
    # gradient는 손실을 줄이기 위해 어느 방향으로 움직일지 알려 주는 숫자입니다.
    weight = 0.5
    x = 2.0
    target = 5.0
    prediction = weight * x
    loss = (prediction - target) ** 2
    gradient = 2 * (prediction - target) * x

    print("prediction:", prediction)
    print("loss:", loss)
    print("gradient dloss/dweight:", gradient)
    print("reading task:", "autograd는 이런 미분 계산을 tensor 연산 기록에서 자동으로 따라갑니다.")
    ''',
    17: '''
    # layer와 activation은 입력을 다음 표현으로 바꾸는 함수로 읽습니다.
    inputs = [0.5, -1.0, 2.0]
    weights = [0.2, 0.4, -0.3]
    bias = 0.1
    linear_output = sum(x * w for x, w in zip(inputs, weights)) + bias
    relu_output = max(0, linear_output)

    print("linear output:", round(linear_output, 3))
    print("relu output:", round(relu_output, 3))
    print("reading task:", "forward는 입력이 layer를 지나 출력으로 바뀌는 경로입니다.")
    ''',
    18: '''
    # 학습 루프는 예측, 손실, gradient, 업데이트를 반복합니다.
    weight = 0.0
    learning_rate = 0.1
    x = 2.0
    target = 4.0
    for epoch in range(3):
        prediction = weight * x
        loss = (prediction - target) ** 2
        gradient = 2 * (prediction - target) * x
        weight = weight - learning_rate * gradient
        print("epoch", epoch, "loss", round(loss, 3), "weight", round(weight, 3))

    print("reading task:", "optimizer.step은 파라미터를 gradient 반대 방향으로 조금 움직입니다.")
    ''',
    19: '''
    # batch와 metric은 여러 샘플을 묶어 평가하는 방식입니다.
    labels = [1, 0, 1, 1, 0, 0]
    predictions = [1, 0, 0, 1, 0, 1]
    batches = [list(zip(predictions[i:i+2], labels[i:i+2])) for i in range(0, len(labels), 2)]
    correct = sum(pred == label for pred, label in zip(predictions, labels))
    accuracy = correct / len(labels)

    print("batches:", batches)
    print("accuracy:", round(accuracy, 3))
    print("reading task:", "metric은 모델 출력의 품질을 한 가지 관점에서 요약한 값입니다.")
    ''',
    20: '''
    # overfitting은 훈련 점수와 검증 점수가 갈라질 때 의심합니다.
    history = [
        {"epoch": 1, "train_loss": 0.80, "val_loss": 0.90},
        {"epoch": 2, "train_loss": 0.40, "val_loss": 0.55},
        {"epoch": 3, "train_loss": 0.20, "val_loss": 0.70},
    ]
    best = min(history, key=lambda row: row["val_loss"])

    print("history:", history)
    print("best checkpoint:", best)
    print("reading task:", "훈련 손실만 낮아지는 모델보다 검증 손실이 낮은 시점의 모델을 봐야 합니다.")
    ''',
    21: '''
    # 텍스트는 모델 안에서 token id와 embedding 벡터로 바뀝니다.
    vocab = {"patient": 1, "stable": 2, "review": 3}
    sentence = ["patient", "review"]
    token_ids = [vocab[token] for token in sentence]
    embeddings = {1: [0.2, 0.1], 2: [0.0, 0.3], 3: [0.4, -0.2]}
    sentence_vector = [sum(embeddings[i][j] for i in token_ids) / len(token_ids) for j in range(2)]

    print("token ids:", token_ids)
    print("sentence vector:", sentence_vector)
    print("reading task:", "텍스트도 결국 숫자 목록으로 바뀐 뒤 모델에 들어갑니다.")
    ''',
    22: '''
    # tokenization은 문장을 모델이 처리할 수 있는 작은 단위로 바꾸는 첫 단계입니다.
    text = "patient glucose high"
    vocab = {"[PAD]": 0, "patient": 1, "glucose": 2, "high": 3}
    tokens = text.split()
    token_ids = [vocab.get(token, 0) for token in tokens]
    attention_mask = [1 if token_id != 0 else 0 for token_id in token_ids]

    print("tokens:", tokens)
    print("token ids:", token_ids)
    print("attention mask:", attention_mask)
    print("reading task:", "mask는 실제 token과 padding을 구분하게 해 줍니다.")
    ''',
    23: '''
    # embedding similarity는 질문과 문서가 얼마나 가까운지 비교합니다.
    def cosine(a, b):
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = sum(x * x for x in a) ** 0.5
        norm_b = sum(y * y for y in b) ** 0.5
        return dot / (norm_a * norm_b)

    query = [0.2, 0.8]
    docs = {"glucose note": [0.1, 0.9], "surgery note": [0.9, 0.1]}
    scores = {name: round(cosine(query, vector), 3) for name, vector in docs.items()}

    print("similarity scores:", scores)
    print("reading task:", "retrieval은 점수가 높은 문서를 먼저 가져오는 절차입니다.")
    ''',
    24: '''
    # attention은 query가 key를 보고 value를 얼마나 참고할지 정합니다.
    query = [1.0, 0.0]
    keys = [[1.0, 0.0], [0.0, 1.0]]
    values = ["current token", "previous token"]
    scores = [sum(q * k for q, k in zip(query, key)) for key in keys]
    selected_index = scores.index(max(scores))

    print("attention scores:", scores)
    print("selected value:", values[selected_index])
    print("reading task:", "QK 점수는 참고할 위치를 고르고, V는 실제로 가져오는 정보입니다.")
    ''',
    25: '''
    # 언어모델은 다음 token 후보의 점수를 확률처럼 해석합니다.
    context = ["patient", "is"]
    logits = {"stable": 2.0, "critical": 0.5, "unknown": -1.0}
    best_token = max(logits, key=logits.get)
    sorted_candidates = sorted(logits.items(), key=lambda item: item[1], reverse=True)

    print("context:", context)
    print("candidate logits:", sorted_candidates)
    print("next token:", best_token)
    print("reading task:", "logit은 아직 확률이 아니지만 값이 클수록 선택 가능성이 큽니다.")
    ''',
    26: '''
    # 사전학습 모델 사용은 입력 형식, 출력 의미, 한계 확인이 함께 필요합니다.
    model_card = {"task": "text-classification", "license": "teaching-only", "trained_on": "synthetic notes"}
    input_text = "patient glucose high"
    fake_output = {"label": "review", "score": 0.82}

    print("model card:", model_card)
    print("input:", input_text)
    print("output:", fake_output)
    print("reading task:", "모델 출력은 근거와 한계를 함께 읽어야 하며 임상 판단으로 바로 바꾸면 안 됩니다.")
    ''',
    27: '''
    # decoding, prompting, RAG, fine-tuning은 응답이 만들어지는 조건을 바꿉니다.
    prompt = "Summarize the synthetic lab note."
    retrieved_context = "P002 has glucose 118 in the toy dataset."
    decoding = {"temperature": 0.2, "top_k": 3}
    answer_plan = [prompt, retrieved_context, str(decoding)]

    print("answer inputs:", answer_plan)
    print("reading task:", "RAG는 외부 근거를 넣고, decoding은 후보 중 무엇을 고를지 조절합니다.")
    ''',
    28: '''
    # 최종 프로젝트는 입력, 처리, 출력, 위험을 한 장의 보고서로 검증합니다.
    project = {
        "input": "synthetic patient table",
        "processing": ["clean", "summarize", "retrieve evidence", "draft answer"],
        "output": "teaching-only explanation",
        "risks": ["privacy", "hallucination", "over-trust"],
    }
    checks = {risk: "must review" for risk in project["risks"]}

    print("project:", project)
    print("risk checks:", checks)
    print("reading task:", "LLM 프로젝트는 정확도뿐 아니라 개인정보, 근거, 검증 절차까지 함께 평가합니다.")
    ''',
}


def lesson_text(day: int, title: str, idea: str, terms: list[str]) -> str:
    terms_text = ", ".join(terms)
    return f'''
    """
    Day {day:02d}. {title}

    이 파일은 학생이 처음부터 코드를 작성하기 위한 파일이 아닙니다.
    이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일입니다.

    오늘의 중심 생각:
    {idea}

    핵심 용어:
    {terms_text}
    """

    print("DAY:", {day})
    print("TOPIC:", "{title}")
    print("CORE IDEA:", "{idea}")

    # 1. 수업용 합성 데이터입니다.
    #    실제 환자 정보가 아니라, 오늘 개념을 읽기 위한 작은 예제입니다.
    # 4. 여러 행에서 같은 열의 값만 모읍니다.
    #    일차별 주제가 달라도 "입력 -> 중간 값 -> 출력" 흐름을 찾는 연습은 같습니다.

    {textwrap.indent(textwrap.dedent(SNIPPETS[day]).strip(), "    ")}

    # 9. 읽기 과제입니다.
    # 마지막 확인 질문입니다.
    # 1. 이 파일에서 가장 먼저 만들어진 값은 무엇인가?
    # 2. 중간 변수 중 하나를 골라 어느 줄에서 만들어졌는지 설명하세요.
    # 3. 출력값 하나를 골라 어떤 입력과 규칙으로 만들어졌는지 설명하세요.
    # 4. 기준값이나 입력값 하나를 바꾸면 어떤 출력이 바뀔지 예측하세요.
    '''


def main() -> None:
    for day, week, slug, title, idea, terms in DAY_SPECS:
        base = ROOT / "weeks" / week_slug(week) / f"day{day:02d}_{slug}"
        write(base / "lesson.py", lesson_text(day, title, idea, terms))
    print("enrich_lessons: OK")


if __name__ == "__main__":
    main()
