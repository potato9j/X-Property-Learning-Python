from __future__ import annotations

import csv
import shutil
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WEEKS = {
    1: "week01_python_foundations",
    2: "week02_numpy_pandas_statistics",
    3: "week03_pytorch_and_machine_learning",
    4: "week04_transformer_and_llm",
}

TOPICS = [
    (1, 1, "day01_colab_execution_values_and_types", "Colab 실행, 값, 표현식과 타입", ["값", "표현식", "타입", "print", "변수"], ["name = value", "print(value)", "type(value)"]),
    (2, 1, "day02_strings_lists_and_structured_data", "문자열, 리스트와 순서형 자료", ["문자열", "인덱스", "슬라이싱", "리스트", "append"], ["text = \"Python\"", "items = [first, second, third]", "items[index]"]),
    (3, 1, "day03_dict_tuple_set_and_object_model", "dictionary, tuple, set과 객체 모델", ["dictionary", "key", "value", "tuple", "set"], ["data = {\"key\": value}", "data[\"key\"]", "unique_values = {a, b, c}"]),
    (4, 1, "day04_conditions_loops_and_comprehension", "조건문, 반복문과 comprehension", ["if", "for", "while", "condition", "comprehension"], ["if condition:\n    statement", "for item in collection:\n    statement", "[expression for item in collection if condition]"]),
    (5, 1, "day05_functions_scope_and_type_hints", "함수, scope와 type hint", ["function", "parameter", "return", "scope", "type hint"], ["def name(parameter):\n    return result", "result = name(argument)", "def name(value: int) -> int:"]),
    (6, 1, "day06_modules_errors_files_and_debugging", "module, 오류, 파일과 디버깅", ["module", "import", "exception", "file", "debugging"], ["import module_name", "try:\n    statement\nexcept ErrorType:\n    recovery", "with open(path) as file:"]),
    (7, 1, "day07_week1_integrated_review", "1주차 통합 숙달", ["입력", "중간값", "출력", "흐름", "검산"], ["input_value -> rule -> output_value", "name = previous_value", "print(final_value)"]),
    (8, 2, "day08_numpy_arrays_shape_dtype_indexing", "NumPy 배열, shape, dtype과 indexing", ["array", "shape", "dtype", "indexing", "axis"], ["array = np.array(values)", "array.shape", "array[row_index, column_index]"]),
    (9, 2, "day09_vectorization_broadcasting_linear_algebra", "vectorization, broadcasting과 선형대수", ["vectorization", "broadcasting", "matrix", "dot", "axis"], ["result = array + scalar", "result = matrix @ vector", "result = np.mean(array, axis=0)"]),
    (10, 2, "day10_pandas_series_dataframe_selection", "pandas Series, DataFrame과 선택", ["Series", "DataFrame", "column", "row", "selection"], ["df = pd.DataFrame(rows)", "df[\"column\"]", "df.loc[row_condition, column_names]"]),
    (11, 2, "day11_data_cleaning_groupby_merge_pivot", "결측치, groupby, merge와 reshape", ["missing", "groupby", "merge", "pivot", "reshape"], ["df.dropna()", "df.groupby(\"group\")[\"value\"].mean()", "left.merge(right, on=\"key\")"]),
    (12, 2, "day12_visualization_exploratory_data_analysis", "시각화와 탐색적 데이터 분석", ["plot", "distribution", "outlier", "trend", "EDA"], ["df[\"value\"].plot()", "df.plot(kind=\"scatter\", x=\"x\", y=\"y\")", "summary = df.describe()"]),
    (13, 2, "day13_probability_distribution_sampling_statistics", "확률, 표본추출과 기술통계", ["probability", "sample", "mean", "variance", "distribution"], ["sample = population[:n]", "mean = sum(values) / len(values)", "probability = favorable / total"]),
    (14, 2, "day14_inference_testing_regression_review", "추론, 검정, 회귀와 2주차 숙달", ["inference", "hypothesis", "p-value", "regression", "coefficient"], ["prediction = intercept + slope * x", "difference = group_a_mean - group_b_mean", "if p_value < alpha:"]),
    (15, 3, "day15_machine_learning_workflow_split_baseline", "머신러닝 workflow와 데이터 분할", ["feature", "label", "train", "validation", "baseline"], ["X_train, X_valid = split(X)", "model.fit(X_train, y_train)", "score = metric(y_valid, prediction)"]),
    (16, 3, "day16_tensor_autograd_gradient", "tensor, autograd와 gradient", ["tensor", "shape", "gradient", "autograd", "requires_grad"], ["x = torch.tensor(values)", "y = model(x)", "loss.backward()"]),
    (17, 3, "day17_nn_module_layer_activation_forward", "nn.Module, layer, activation과 forward", ["nn.Module", "layer", "activation", "forward", "parameter"], ["class Model(nn.Module):", "self.layer = nn.Linear(in_features, out_features)", "def forward(self, x):\n    return output"]),
    (18, 3, "day18_loss_optimizer_training_loop", "loss, optimizer와 학습 루프", ["loss", "optimizer", "epoch", "batch", "training loop"], ["optimizer.zero_grad()", "loss.backward()", "optimizer.step()"]),
    (19, 3, "day19_data_loader_evaluation_metrics", "DataLoader와 학습 루프 평가 지표", ["Dataset", "DataLoader", "batch", "accuracy", "metric"], ["for batch in dataloader:", "prediction = model(inputs)", "metric = correct / total"]),
    (20, 3, "day20_regularization_overfitting_model_management", "검증, overfitting과 모델 관리", ["validation", "overfitting", "regularization", "checkpoint", "early stopping"], ["if valid_loss < best_loss:", "torch.save(model.state_dict(), path)", "model.eval()"]),
    (21, 3, "day21_text_tensor_embedding_review", "텍스트 tensor, embedding과 3주차 숙달", ["token id", "embedding", "sequence", "padding", "review"], ["ids = tokenizer(text)", "vectors = embedding(ids)", "batch = pad_sequences(sequences)"]),
    (22, 4, "day22_nlp_tokenization_vocabulary_representation", "NLP, tokenization과 어휘 표현", ["token", "vocabulary", "token id", "unknown", "sequence"], ["tokens = tokenizer(text)", "ids = [vocab[token] for token in tokens]", "text = decoder(ids)"]),
    (23, 4, "day23_embedding_similarity_retrieval", "embedding, similarity와 위치 정보", ["embedding", "similarity", "retrieval", "cosine", "position"], ["query_vector = embed(query)", "score = cosine(query_vector, document_vector)", "top_k = sorted(scores)[:k]"]),
    (24, 4, "day24_attention_qkv_mask_multihead", "attention, QKV, mask와 multi-head", ["query", "key", "value", "mask", "head"], ["scores = query @ key.T", "weights = softmax(scores + mask)", "context = weights @ value"]),
    (25, 4, "day25_transformer_decoder_language_modeling", "Transformer와 언어모델링", ["decoder", "logit", "next token", "causal mask", "language model"], ["logits = model(input_ids)", "next_id = argmax(logits[-1])", "input_ids = input_ids + [next_id]"]),
    (26, 4, "day26_huggingface_model_usage_generation", "Hugging Face 모델 추론과 생성", ["pipeline", "model", "tokenizer", "generate", "inference"], ["tokenizer = AutoTokenizer.from_pretrained(name)", "model = AutoModel.from_pretrained(name)", "output = model.generate(input_ids)"]),
    (27, 4, "day27_decoding_prompting_rag_finetuning", "decoding, prompting, RAG와 fine-tuning", ["prompt", "decoding", "RAG", "retriever", "fine-tuning"], ["prompt = instruction + context", "documents = retriever(query)", "answer = model(prompt)"]),
    (28, 4, "day28_integrated_llm_project_ethics_review", "통합 LLM 프로젝트, 윤리와 최종 숙달", ["project", "evaluation", "privacy", "bias", "audit"], ["input -> retrieval -> generation -> evaluation", "risk = check_privacy(output)", "report = summarize(evidence)"]),
]

SAMPLE_RECORDS = [
    {"student_id": "S01", "glucose": 92, "pulse": 72, "note_count": 2},
    {"student_id": "S02", "glucose": 107, "pulse": 81, "note_count": 4},
    {"student_id": "S03", "glucose": 86, "pulse": 69, "note_count": 1},
    {"student_id": "S04", "glucose": 118, "pulse": 88, "note_count": 5},
]

DATASET_ROWS = [
    ["P001", 22, 91, 72, "A"],
    ["P002", 24, 107, 81, "B"],
    ["P003", 21, 86, 69, "A"],
    ["P004", 26, 118, 88, "B"],
    ["P005", 23, 99, 75, "A"],
    ["P006", 25, 111, 84, "B"],
    ["P007", 22, 94, 73, "A"],
    ["P008", 27, 121, 90, "B"],
    ["P009", 24, 89, 70, "A"],
    ["P010", 23, 103, 78, "B"],
]


def clean_workspace() -> None:
    weeks = ROOT / "weeks"
    if weeks.exists():
        shutil.rmtree(weeks)
    datasets = ROOT / "datasets"
    datasets.mkdir(exist_ok=True)
    for md in ROOT.glob("*.md"):
        md.unlink()
    for notebook in ROOT.rglob("*.ipynb"):
        if ".git" not in notebook.parts:
            notebook.unlink()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def sentence_terms(terms: list[str]) -> str:
    return ", ".join(f"`{term}`" for term in terms)


def make_structure_blocks(title: str, structures: list[str]) -> str:
    blocks = []
    for index, code in enumerate(structures, start=1):
        blocks.append(textwrap.dedent(f"""
        ### 구조 {index}

        ```python
        {code}
        ```

        이 일반식은 `{title}`에서 자주 보게 되는 코드의 뼈대이다. 여기서 영어 단어처럼 보이는 이름은 실제 코드에서 다른 변수명, 함수명, 열 이름, 모델 이름으로 바뀌는 자리이다. 괄호는 입력을 받는 자리이고, 대괄호는 여러 값에서 일부를 고르는 자리이며, 콜론은 아래쪽 들여쓰기 블록이 같은 규칙 안에 묶인다는 뜻이다. 코드를 읽을 때는 먼저 왼쪽에 새 이름이 생기는지 보고, 그다음 오른쪽에서 어떤 값이 만들어지는지 읽는다. 마지막으로 그 결과가 다음 줄에서 입력으로 다시 쓰이는지 확인한다.
        """))
    return "\n".join(blocks)


def make_concept(day: int, week: int, title: str, terms: list[str], structures: list[str]) -> str:
    term_list = sentence_terms(terms)
    term_rows = "\n".join(
        f"| `{term}` | 이 장에서 `{title}`을 읽기 위해 필요한 핵심 단어이다. 코드에서 값, 이름, 규칙, 출력 중 어느 역할을 하는지 확인한다. |"
        for term in terms
    )
    structure_blocks = make_structure_blocks(title, structures)
    small_example_terms = repr(terms[:3])
    return textwrap.dedent(f"""
    # Day {day:02d}. {title}

    ## 1. 이 장에서 배우는 내용이 무엇인지

    이 장은 `{title}`을 처음 배우는 학생을 위한 교과서 장이다. 목표는 코드를 많이 외우는 것이 아니라, 이미 작성된 Python 코드를 보고 값이 어디에서 만들어지고 어디로 이동하는지 읽는 능력을 기르는 것이다. 수업 도구는 Colab일 수 있지만, 핵심은 Colab 버튼의 위치가 아니라 코드의 구조를 해석하는 일이다.

    이번 장은 Week {week} 과정 안에 놓인다. 앞 장에서 배운 값, 이름, 자료구조, 출력의 흐름을 바탕으로 새 개념을 쌓는다. 학생은 이 장을 읽은 뒤 `{title}`이라는 말을 들었을 때 단어 뜻만 말하는 것이 아니라, 어떤 일반식으로 코드에 나타나는지, 어떤 줄이 입력이고 어떤 줄이 중간 계산이며 어떤 줄이 출력인지 설명할 수 있어야 한다.

    이 장에서 계속 붙잡을 질문은 세 가지이다. 첫째, 코드가 처음 받아들이는 값은 무엇인가. 둘째, 그 값이 어떤 문법 일반식을 지나며 바뀌는가. 셋째, 마지막 출력은 무엇을 말하고 무엇까지는 말하지 않는가. 의학 데이터나 LLM 출력도 이 세 질문을 벗어나지 않는다. 숫자, 표, tensor, token, 문장 출력은 모두 값의 한 형태이고, 코드는 그 값을 일정한 규칙으로 바꾸는 글이다.

    ## 2. 전체개념

    `{title}`의 전체개념은 다음 문장으로 요약된다.

    > 코드는 값을 만들고, 이름을 붙이고, 정해진 일반식에 따라 값을 변환한 뒤, 출력으로 확인하는 글이다.

    초보자는 코드를 볼 때 낯선 영어 단어와 괄호 때문에 먼저 겁을 낸다. 그러나 Python 코드는 아무 줄이나 마음대로 읽는 글이 아니다. 대부분 위에서 아래로 읽고, 들여쓰기가 같은 줄끼리 같은 단계로 묶인다. 그래서 처음 할 일은 모든 단어를 외우는 것이 아니라 줄의 역할을 나누는 일이다. 어떤 줄은 데이터를 만든다. 어떤 줄은 데이터를 고른다. 어떤 줄은 조건을 검사한다. 어떤 줄은 반복한다. 어떤 줄은 함수나 모델에 값을 넣고 결과를 받는다.

    이 장의 중심 용어는 {term_list}이다. 이 용어들은 서로 떨어진 단어가 아니다. 예를 들어 어떤 용어는 값을 담는 그릇을 가리키고, 어떤 용어는 값을 고르는 방법을 가리키며, 어떤 용어는 값을 바꾸는 규칙을 가리킨다. 교과서식 읽기는 이 차이를 분리하는 데서 시작한다. 학생이 용어를 볼 때마다 `이 단어는 값인가, 이름인가, 규칙인가, 결과인가`라고 묻는 습관을 만들면 긴 코드도 한 번에 덩어리로 보이지 않는다.

    전체개념을 데이터 흐름으로 쓰면 `입력 -> 구조 -> 변환 -> 출력`이다. 입력은 숫자 하나일 수도 있고, 문자열 하나일 수도 있으며, 여러 행을 가진 표일 수도 있다. 구조는 list, dict, DataFrame, tensor, token sequence처럼 값을 담는 모양이다. 변환은 조건문, 반복문, 함수, 벡터 연산, 모델 호출처럼 입력을 다른 값으로 바꾸는 규칙이다. 출력은 사람이 확인하는 결과이다. 출력은 계산 결과이지 자동으로 참인 결론이 아니다. 이 구분은 의료 데이터와 LLM을 다룰 때 특히 중요하다.

    ## 3. 전체 구조

    전체 구조는 수학의 일반식처럼 읽는다. 수학에서 `y = ax + b`를 보면 `x` 자리에 값이 들어가고, `a`와 `b`가 규칙을 정하며, `y`가 결과라는 사실을 먼저 읽는다. Python도 같다. 코드의 일반식은 `어떤 자리에 어떤 값이 들어가고, 어떤 이름으로 결과가 남는가`를 보여 준다.

    {structure_blocks}

    일반식을 읽는 순서는 항상 같다. 첫째, 새로 생기는 이름을 찾는다. 둘째, 오른쪽이나 괄호 안에 들어가는 입력을 찾는다. 셋째, 콜론과 들여쓰기가 있으면 그 아래 줄이 같은 규칙에 속한다고 읽는다. 넷째, 출력 줄이 실제로 무엇을 출력하는지 확인한다. 이 순서를 지키면 `for A in B:` 같은 코드는 `B라는 여러 값 묶음에서 A라는 이름으로 하나씩 꺼낸다`로 해석된다. `if 조건:`은 `조건이 참일 때만 아래 블록을 실행한다`로 해석된다. 함수 호출은 `괄호 안 값을 함수에 넣고 결과를 받는다`로 해석된다.

    ## 4. 전체용어

    | 용어 | 이 장에서의 뜻 |
    | --- | --- |
    {term_rows}

    용어는 암기 카드가 아니라 코드 읽기의 표지판이다. 학생은 용어를 볼 때 한글 뜻을 하나 붙이고 끝내면 안 된다. 그 용어가 코드의 어느 자리에 놓이는지, 어떤 값과 연결되는지, 잘못 읽으면 어떤 출력 해석이 틀어지는지까지 확인한다. 예를 들어 `for`를 `반복`이라고만 외우면 부족하다. `for item in items:`라는 일반식에서 `items`는 여러 값의 묶음이고 `item`은 그중 하나를 임시로 가리키는 이름이라는 사실까지 읽어야 한다.

    ## 5. 설명

    프로그래밍 초보자에게 가장 어려운 부분은 컴퓨터가 사람처럼 문맥을 알아서 채워 넣지 않는다는 점이다. 사람은 문장을 읽다가 빠진 내용을 추측하지만, Python은 현재 줄까지 만들어진 값만 사용한다. 아직 만들어지지 않은 이름을 쓰면 오류가 난다. 숫자에 문자열 전용 연산을 적용하면 오류가 난다. 표에 없는 열 이름을 꺼내면 오류가 난다. 그래서 코드 읽기의 첫 번째 원칙은 `현재 이 줄에서 사용할 수 있는 값이 무엇인가`를 묻는 것이다.

    `{title}`을 배울 때도 같은 원칙을 적용한다. 처음에는 용어가 낯설 수 있다. 하지만 모든 코드는 결국 값을 다룬다. 값은 숫자, 문자열, 리스트, 표, tensor, token 같은 형태를 가진다. 형태가 다르면 사용할 수 있는 연산도 달라진다. 숫자는 더하고 비교할 수 있다. 문자열은 붙이고 자를 수 있다. 리스트는 순서를 가진 여러 값의 묶음이다. dict는 key로 값을 찾는다. DataFrame은 행과 열로 값을 고른다. tensor는 shape를 가진 숫자 묶음이다. token sequence는 문장을 모델이 다룰 수 있는 번호 묶음으로 바꾼 결과이다.

    두 번째 원칙은 이름과 값을 구분하는 것이다. 변수 이름은 값 자체가 아니라 값을 가리키는 표지이다. `score = 90`이라는 줄을 읽을 때 `score라는 상자 안에 90을 넣는다`라고만 말하면 초보 단계에서는 도움이 될 수 있지만, 더 정확하게는 `90이라는 값에 score라는 이름을 붙인다`라고 읽는다. 나중에 `score = score + 5` 같은 줄을 만나면 이 차이가 중요하다. 오른쪽 `score`는 이전 값이고, 왼쪽 `score`는 새 결과에 붙는 이름이다.

    세 번째 원칙은 일반식을 먼저 읽는 것이다. `{title}`에서 자주 쓰는 구조는 위의 코드 블록처럼 일정한 모양을 가진다. 일반식은 세부 내용을 모두 담지 않는다. 대신 어느 자리에 입력이 들어가고 어느 자리에 결과가 남는지 보여 준다. 학생은 일반식을 보고 나서 실제 예제의 변수명과 값으로 바꾸어 읽는다. 이 방식은 수학의 공식 대입과 비슷하다. 공식 자체를 외우는 것이 끝이 아니라, 문제의 값이 공식의 어느 자리에 들어가는지 읽는 것이 핵심이다.

    네 번째 원칙은 출력의 의미를 제한하는 것이다. 코드가 어떤 숫자를 출력했다고 해서 그 숫자가 곧 의학적 판단이나 모델의 진실이 되지는 않는다. 출력은 입력과 규칙이 만든 계산 결과이다. 의료 데이터라면 결측치, 측정 단위, 표본 크기, 편향이 영향을 줄 수 있다. LLM이라면 prompt, 검색 문서, decoding 방식, 모델 한계가 영향을 줄 수 있다. 코드를 읽는 학생은 `이 출력은 무엇을 계산한 결과인가`까지만 정확하게 말하고, 그 너머의 결론은 별도로 검토한다.

    이 장의 학습은 직접 코드를 새로 짜는 훈련보다 해석 훈련에 가깝다. 이미 작성된 `lesson.py`를 열고 주석을 따라가며 읽는다. 먼저 합성 데이터가 어떤 모양인지 본다. 다음으로 하나의 열 또는 값이 어떻게 선택되는지 본다. 그다음 조건, 반복, 함수, 모델 같은 규칙이 값을 어떻게 바꾸는지 본다. 마지막으로 출력 문장을 보고 어떤 입력과 규칙이 그 결과를 만들었는지 말로 설명한다.

    ## 6. py파일과 별개로 예제

    아래 예제는 `lesson.py`와 별개로 읽는 작은 코드이다. 목적은 `{title}`의 모든 기능을 쓰는 것이 아니라, 값과 이름과 일반식의 관계를 가장 작은 형태로 다시 보는 것이다.

    ```python
    chapter_title = "{title}"
    chapter_terms = {small_example_terms}
    first_term = chapter_terms[0]

    print("장 제목:", chapter_title)
    print("첫 용어:", first_term)

    for index, term in enumerate(chapter_terms, start=1):
        print(index, term)
    ```

    이 예제의 첫 줄은 문자열 값에 `chapter_title`이라는 이름을 붙인다. 둘째 줄은 여러 문자열을 list로 묶고 `chapter_terms`라는 이름을 붙인다. 셋째 줄은 list의 첫 번째 값을 골라 `first_term`이라는 이름을 붙인다. 마지막 `for` 일반식은 list 안의 값을 하나씩 꺼내 `term`이라는 이름으로 읽는다. `enumerate`는 순서 번호와 값을 함께 꺼내는 도구이다.

    이 작은 예제를 읽을 때 학생은 다음 질문에 답한다. `chapter_terms`는 값 하나인가 여러 값의 묶음인가. `first_term`은 어디에서 만들어지는가. `for index, term in ...`에서 `index`와 `term`은 반복이 한 번 돌 때마다 어떻게 바뀌는가. 출력된 번호와 용어는 어떤 입력에서 왔는가. 이 질문에 답할 수 있으면 더 긴 `lesson.py`에서도 같은 방식으로 줄의 역할을 분리할 수 있다.
    """)


def make_lesson(day: int, title: str, terms: list[str]) -> str:
    records_literal = repr(SAMPLE_RECORDS)
    terms_literal = repr(terms)
    return textwrap.dedent(f'''\
    """
    Day {day:02d}. {title}

    이 파일은 처음부터 코드를 작성하기 위한 파일이 아니다.
    이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 수업 파일이다.
    """

    print("DAY:", {day})
    print("TOPIC:", "{title}")

    # 1. 수업용 합성 데이터
    # 실제 환자 정보가 아니라 코드 읽기를 위한 작은 표본 데이터이다.
    # 각 dict는 한 행이다. key는 열 이름처럼 읽고 value는 그 열의 값으로 읽는다.
    records = {records_literal}

    # 2. 입력 구조 확인
    # records는 여러 행을 담은 list이다. len(records)는 행의 개수를 계산한다.
    row_count = len(records)
    print("row_count:", row_count)

    # 3. 기준값 만들기
    # threshold는 뒤의 조건문에서 비교 기준으로 쓰이는 값이다.
    threshold = 100

    # 4. 여러 행에서 같은 열의 값만 모은다
    # for row in records는 records 안의 행을 하나씩 row라는 이름으로 꺼낸다는 뜻이다.
    glucose_values = []
    for row in records:
        glucose_values.append(row["glucose"])

    # 5. 조건문으로 값을 해석한다
    # value >= threshold가 참이면 review, 거짓이면 ok라는 문자열을 붙인다.
    flags = []
    for value in glucose_values:
        if value >= threshold:
            flags.append("review")
        else:
            flags.append("ok")

    # 6. 같은 흐름을 comprehension으로 압축한 형태이다.
    # 긴 반복문과 같은 결과를 만들지만, 처음 배울 때는 위의 긴 형태를 먼저 읽는다.
    compact_flags = ["review" if value >= threshold else "ok" for value in glucose_values]

    # 7. 오늘의 용어를 코드 안의 값으로 둔다
    # terms는 설명용 list이다. 코드 실행 결과보다 용어의 위치를 읽는 데 목적이 있다.
    terms = {terms_literal}

    # 8. 출력은 계산 결과이다
    # 출력이 곧 의학적 결론이라는 뜻은 아니다. 어떤 입력과 규칙이 결과를 만들었는지 읽는다.
    print("glucose_values:", glucose_values)
    print("flags:", flags)
    print("compact_flags:", compact_flags)
    print("terms:", terms)

    # 9. 읽기 과제
    # 1. records의 타입과 records 안의 첫 번째 행 타입을 말한다.
    # 2. threshold가 어느 줄에서 만들어지고 어느 줄에서 다시 쓰이는지 찾는다.
    # 3. flags와 compact_flags가 같은 결과를 만드는 이유를 설명한다.
    # 4. {title}에서 오늘의 핵심 일반식이 어느 줄에 나타나는지 표시한다.
    ''' )


def make_readme() -> str:
    rows = []
    for day, week, slug, title, _terms, _structures in TOPICS:
        rows.append(f"| Week {week} | Day {day:02d} | [{title}](weeks/{WEEKS[week]}/{slug}/concept.md) |")
    return textwrap.dedent(f"""
    # 서울대학교 의과대학생 특강 대비 Python, 데이터, PyTorch, LLM 4주 사전교육

    이 저장소는 Python 경험이 거의 없는 의과대학생을 위한 4주 사전교육 교재이다. Colab은 실행 도구로만 사용하고, 핵심은 Python 코드와 데이터 흐름을 읽고 해석하는 능력이다.

    ## 자료 구조

    각 일차 폴더에는 두 파일만 둔다.

    ```text
    concept.md  # 개념 교재
    lesson.py   # 주석을 따라 읽고 실행하는 Python 코드
    ```

    불필요한 다중 md 파일, 학생용/해설용 노트북 분리, 반복되는 퀴즈 폴더는 두지 않는다. 학생이 무엇을 읽고 무엇을 실행할지 바로 알 수 있게 하는 것이 우선이다.

    ## 학습 경로

    | 주차 | 일차 | 개념 파일 |
    | --- | --- | --- |
    {chr(10).join(rows)}

    ## Colab 실행

    각 일차 폴더의 `lesson.py`를 Colab에 올린 뒤 다음 중 하나로 실행한다.

    ```python
    %run lesson.py
    ```

    또는

    ```python
    !python lesson.py
    ```

    ## 검증

    ```bash
    python scripts/validate_structure.py
    python scripts/validate_markdown_links.py
    python scripts/check_required_sections.py
    python scripts/execute_lessons.py
    python scripts/validate_datasets.py
    python -m pytest
    ```
    """)


def make_teaching_guide() -> str:
    return textwrap.dedent("""
    # Teaching Guide

    이 교재의 수업 방식은 코드 작성보다 코드 해석에 둔다. 학생은 매일 `concept.md`를 먼저 읽고, 그다음 `lesson.py`를 실행하며 출력이 어떤 입력과 규칙에서 나왔는지 말로 설명한다.

    ## 진행 원칙

    - 처음부터 빈 파일에 코드를 쓰게 하지 않는다.
    - 교사는 일반식, 입력, 중간값, 출력을 칠판에 분리해서 남긴다.
    - 학생 답안은 실행 결과 암기가 아니라 값의 흐름 설명으로 평가한다.
    - Colab 사용법은 최소화하고 Python 문법 해석에 시간을 둔다.
    - 의료 데이터와 LLM 출력은 계산 결과와 현실 판단을 구분해서 다룬다.

    ## 매일 반복할 질문

    1. 첫 입력은 무엇인가.
    2. 입력은 어떤 자료구조에 담겼는가.
    3. 어떤 일반식이 값을 바꾸는가.
    4. 중간 결과는 어떤 이름으로 남는가.
    5. 출력은 무엇을 계산한 결과인가.
    """)


def write_course_config() -> None:
    days_repr = repr([(day, week, slug, title) for day, week, slug, title, _terms, _structures in TOPICS])
    content = f"WEEKS = {repr(WEEKS)}\nDAYS = {days_repr}\n"
    write_text(ROOT / "scripts" / "course_config.py", content)


def write_dataset() -> None:
    path = ROOT / "datasets" / "synthetic_patients.csv"
    path.parent.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["patient_id", "age", "glucose", "pulse", "group"])
        writer.writerows(DATASET_ROWS)


def write_requirements() -> None:
    write_text(ROOT / "requirements-colab.txt", "numpy\npandas\nmatplotlib\n")
    write_text(ROOT / "requirements-dev.txt", "pytest\n")
    write_text(ROOT / "pyproject.toml", textwrap.dedent("""
    [tool.pytest.ini_options]
    testpaths = ["tests"]
    python_files = ["test_*.py"]
    """))


def main() -> None:
    clean_workspace()
    write_course_config()
    write_dataset()
    write_requirements()
    write_text(ROOT / "README.md", make_readme())
    write_text(ROOT / "TEACHING_GUIDE.md", make_teaching_guide())

    for day, week, slug, title, terms, structures in TOPICS:
        base = ROOT / "weeks" / WEEKS[week] / slug
        write_text(base / "concept.md", make_concept(day, week, title, terms, structures))
        write_text(base / "lesson.py", make_lesson(day, title, terms))

    print("bootstrap_course_repository: OK")


if __name__ == "__main__":
    main()
