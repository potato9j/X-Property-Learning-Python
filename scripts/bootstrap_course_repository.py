from __future__ import annotations

import csv
import shutil
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

WEEKS = {
    1: ("week01_python_foundations", "Python 기초: 값을 읽고 코드 흐름을 해석하기"),
    2: ("week02_numpy_pandas_statistics", "데이터 기초: 배열, 표, 통계적 사고"),
    3: ("week03_pytorch_and_machine_learning", "모델 기초: tensor, 학습 루프, 평가"),
    4: ("week04_transformer_and_llm", "LLM 기초: token, attention, 생성, 검증"),
}

DAY_SPECS = [
    (1, 1, "colab_execution_values_and_types", "Colab 실행, 값, 표현식과 타입", "Python 코드는 값을 만들고 이름을 붙이며 위에서 아래로 실행된다.", ["value", "expression", "variable", "type", "execution order"]),
    (2, 1, "strings_lists_and_structured_data", "문자열, 리스트와 순서형 자료", "문자열과 리스트는 여러 값을 순서대로 읽는 첫 번째 자료구조다.", ["str", "index", "slice", "list", "append"]),
    (3, 1, "dict_tuple_set_and_object_model", "dictionary, tuple, set과 객체 모델", "dict는 이름으로 값을 찾고, tuple과 set은 데이터의 성격을 다르게 표현한다.", ["dict", "key", "value", "tuple", "set"]),
    (4, 1, "conditions_loops_and_comprehension", "조건문, 반복문과 comprehension", "조건과 반복은 여러 행을 같은 기준으로 해석하게 해 준다.", ["if", "for", "while", "condition", "comprehension"]),
    (5, 1, "functions_scope_and_type_hints", "함수, scope와 type hint", "함수는 반복되는 해석 절차에 이름을 붙이고 입력과 출력을 분명히 한다.", ["function", "parameter", "return", "scope", "type hint"]),
    (6, 1, "modules_errors_files_and_debugging", "module, 오류, 파일과 디버깅", "파일과 오류 메시지를 읽는 힘은 코드 작성보다 먼저 필요한 실전 기초다.", ["module", "import", "exception", "traceback", "path"]),
    (7, 1, "week1_integrated_review", "1주차 통합 숙달", "값, 타입, 조건, 반복, 함수, 오류를 연결해 작은 Python 프로그램을 읽는다.", ["review", "trace", "input", "process", "output"]),
    (8, 2, "numpy_arrays_shape_dtype_indexing", "NumPy 배열, shape, dtype과 indexing", "배열은 같은 종류의 값을 축과 위치로 다루는 방식이다.", ["array", "shape", "dtype", "axis", "indexing"]),
    (9, 2, "vectorization_broadcasting_linear_algebra", "vectorization, broadcasting과 선형대수", "벡터화는 반복문을 배열 연산으로 바꾸고, broadcasting은 크기가 다른 배열을 맞춘다.", ["vectorization", "broadcasting", "matrix", "dot product", "reshape"]),
    (10, 2, "pandas_series_dataframe_selection", "pandas Series, DataFrame과 선택", "DataFrame은 행과 열로 구성된 표이며, 분석은 필요한 행과 열을 정확히 고르는 일에서 시작한다.", ["Series", "DataFrame", "row", "column", "loc"]),
    (11, 2, "data_cleaning_groupby_merge_pivot", "결측치, groupby, merge와 reshape", "데이터 정리는 잘못되거나 비어 있거나 흩어진 표를 분석 가능한 형태로 바꾸는 과정이다.", ["missing value", "groupby", "merge", "pivot", "reshape"]),
    (12, 2, "visualization_exploratory_data_analysis", "시각화와 탐색적 데이터 분석", "시각화는 정답을 증명하기보다 데이터의 분포와 이상한 지점을 찾는 도구다.", ["EDA", "distribution", "histogram", "scatter", "outlier"]),
    (13, 2, "probability_distribution_sampling_statistics", "확률, 표본추출과 기술통계", "통계는 일부 관찰값에서 전체 경향을 조심스럽게 설명하는 언어다.", ["population", "sample", "mean", "variance", "distribution"]),
    (14, 2, "inference_testing_regression_review", "추론, 검정, 회귀와 2주차 숙달", "추론과 검정은 차이를 보았을 때 그 차이가 우연인지 구조인지 묻는 절차다.", ["confidence interval", "p-value", "test", "correlation", "regression"]),
    (15, 3, "machine_learning_workflow_split_baseline", "머신러닝 workflow와 데이터 분할", "머신러닝은 데이터를 나누고 기준 모델과 비교하며 일반화 성능을 확인하는 절차다.", ["feature", "label", "train", "validation", "baseline"]),
    (16, 3, "tensor_autograd_gradient", "tensor, autograd와 gradient", "tensor는 모델 학습의 숫자 그릇이고 gradient는 손실을 줄이는 방향 정보다.", ["tensor", "gradient", "autograd", "loss", "parameter"]),
    (17, 3, "nn_module_layer_activation_forward", "nn.Module, layer, activation과 forward", "신경망은 layer를 통과하며 입력을 출력으로 바꾸는 함수로 읽을 수 있다.", ["nn.Module", "layer", "activation", "forward", "logits"]),
    (18, 3, "loss_optimizer_training_loop", "loss, optimizer와 학습 루프", "학습 루프는 예측, 손실 계산, gradient 계산, 파라미터 갱신을 반복한다.", ["loss", "optimizer", "backward", "step", "epoch"]),
    (19, 3, "data_loader_evaluation_metrics", "DataLoader와 학습 루프 평가 지표", "평가는 모델이 훈련 데이터가 아닌 새 데이터에서도 설명력을 유지하는지 보는 과정이다.", ["batch", "DataLoader", "metric", "accuracy", "recall"]),
    (20, 3, "regularization_overfitting_model_management", "검증, overfitting과 모델 관리", "overfitting은 훈련 데이터는 잘 맞히지만 새 데이터에는 약한 상태다.", ["overfitting", "regularization", "validation", "checkpoint", "model.eval"]),
    (21, 3, "text_tensor_embedding_review", "텍스트 tensor, embedding과 3주차 숙달", "텍스트도 모델 안에서는 숫자 tensor와 embedding으로 변환되어 처리된다.", ["text", "token id", "embedding", "sequence", "batch"]),
    (22, 4, "nlp_tokenization_vocabulary_representation", "NLP, tokenization과 어휘 표현", "tokenization은 문장을 모델이 처리할 수 있는 작은 단위로 바꾸는 첫 단계다.", ["token", "vocabulary", "token id", "unknown", "mask"]),
    (23, 4, "embedding_similarity_retrieval", "embedding, similarity와 위치 정보", "embedding은 의미나 관계를 숫자 벡터 공간에 놓고 비교하게 해 준다.", ["embedding", "vector", "cosine similarity", "retrieval", "position"]),
    (24, 4, "attention_qkv_mask_multihead", "attention, QKV, mask와 multi-head", "attention은 한 위치가 다른 위치의 정보를 얼마나 참고할지 계산하는 방식이다.", ["query", "key", "value", "mask", "multi-head"]),
    (25, 4, "transformer_decoder_language_modeling", "Transformer와 언어모델링", "언어모델은 앞의 token들을 보고 다음 token의 가능성을 계산한다.", ["Transformer", "decoder", "logits", "probability", "next token"]),
    (26, 4, "huggingface_model_usage_generation", "Hugging Face 모델 추론과 생성", "사전학습 모델을 사용할 때는 입력 형식, 출력 의미, 라이선스, 한계를 함께 읽어야 한다.", ["model card", "tokenizer", "pipeline", "inference", "license"]),
    (27, 4, "decoding_prompting_rag_finetuning", "decoding, prompting, RAG와 fine-tuning", "LLM 응답은 decoding과 prompt, 검색 문맥, 학습 방식의 영향을 받는다.", ["decoding", "temperature", "prompt", "RAG", "fine-tuning"]),
    (28, 4, "integrated_llm_project_ethics_review", "통합 LLM 프로젝트, 윤리와 최종 숙달", "최종 목표는 LLM을 맹신하지 않고 입력, 출력, 근거, 위험을 검증하는 것이다.", ["hallucination", "privacy", "verification", "ethics", "final review"]),
]


def write(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(body).strip() + "\n", encoding="utf-8")


def clean_generated() -> None:
    for name in ["weeks", "datasets", "assessments", "appendices", "instructor", "tests"]:
        target = ROOT / name
        if target.exists():
            shutil.rmtree(target)
    for name in [
        "README.md",
        "TEACHING_GUIDE.md",
        "COURSE_SYLLABUS.md",
        "ASSESSMENT_PLAN.md",
        "PRIVACY_AND_ETHICS.md",
        "AI_LEARNING_GUIDE.md",
        "COLAB_SETUP.md",
        "CURRICULUM_MAP.md",
        "LEARNING_OUTCOMES.md",
        "GLOSSARY.md",
        "PROJECT_PLAN.md",
        "GENERATION_STATUS.md",
        "AGENTS.md",
    ]:
        path = ROOT / name
        if path.exists():
            path.unlink()


def week_slug(week: int) -> str:
    return WEEKS[week][0]


def concept_text(day: int, week: int, slug: str, title: str, idea: str, terms: list[str]) -> str:
    previous = "이전 지식이 거의 없다고 가정하고 시작합니다." if day == 1 else f"이전 일차에서 배운 내용을 바탕으로 오늘은 `{title}`를 더 구체적으로 읽습니다."
    next_day = "다음 날에는 오늘 배운 관찰 방법을 더 복잡한 자료구조나 데이터 흐름에 적용합니다." if day < 28 else "오늘은 전체 과정을 정리하고 이후 독학 방향을 세웁니다."
    term_rows = "\n".join(f"| `{term}` | 오늘 코드에서 반드시 말로 설명해야 할 핵심 용어입니다. |" for term in terms)
    return f"""
# Day {day:02d}. {title}

## 1. 오늘의 위치

{previous} 이 과정은 학생이 코드를 많이 외우게 만드는 수업이 아닙니다. 목표는 이미 작성된 Python 코드를 열었을 때, 한 줄씩 읽으면서 입력이 무엇이고, 중간 값이 어떻게 바뀌며, 최종 출력이 무엇을 뜻하는지 설명하게 만드는 것입니다.

오늘의 중심 문장은 다음과 같습니다.

> {idea}

이 문장을 수업이 끝날 때 학생이 자기 말로 설명할 수 있으면 충분합니다. 처음 배우는 학생에게는 빠른 진도보다 개념의 층위를 차례대로 쌓는 것이 중요합니다.

## 2. 왜 이 개념을 먼저 배우는가

Python, 데이터 분석, PyTorch, LLM은 서로 달라 보이지만 모두 같은 기본 질문으로 읽을 수 있습니다. 첫째, 어떤 값이 들어오는가. 둘째, 그 값의 타입과 모양은 무엇인가. 셋째, 어떤 규칙으로 값이 변하는가. 넷째, 출력은 어떤 의미인가. 오늘 주제는 이 네 질문 중 하나 이상을 더 정확히 답하게 해 줍니다.

의과대학생에게 이 관점은 특히 중요합니다. 의료 데이터나 모델 출력은 그럴듯해 보여도, 입력이 잘못되었거나 기준이 모호하거나 타입을 잘못 해석하면 잘못된 결론으로 이어질 수 있습니다. 따라서 처음부터 코드를 "작성 대상"이 아니라 "검증하며 읽는 대상"으로 다룹니다.

## 3. 핵심 용어

| 용어 | 수업에서의 뜻 |
| --- | --- |
{term_rows}

용어는 외우기보다 코드에서 위치를 찾는 방식으로 익힙니다. 학생에게 "이 단어의 사전적 정의가 무엇인가"보다 "이 코드에서 이 개념이 어느 줄에 나타나는가"를 먼저 묻습니다.

## 4. 개념을 읽는 순서

오늘 개념은 다음 순서로 읽습니다.

1. 코드가 다루는 입력을 찾습니다.
2. 입력의 타입, 길이, 행과 열, 또는 shape를 확인합니다.
3. 중간 변수가 어떻게 만들어지는지 봅니다.
4. 조건, 반복, 함수, 모델 호출이 어떤 변환을 하는지 말로 풉니다.
5. 출력이 계산 결과인지, 요약인지, 판단인지 구분합니다.

초보자는 한 번에 전체 코드를 이해하려고 하면 막힙니다. 그래서 매 줄마다 "이 줄이 새로 만든 값은 무엇인가"만 답하게 합니다. 이 작은 질문을 반복하면 긴 코드도 읽을 수 있습니다.

## 5. 교과서식 설명

{title}를 배울 때 가장 먼저 피해야 할 오해는, 코드를 눈으로 훑는 것과 코드를 이해하는 것이 같다고 생각하는 것입니다. 이해한다는 것은 변수의 이름을 읽는 것이 아니라 그 이름이 가리키는 실제 값과 그 값이 만들어진 과정을 설명하는 것입니다.

예를 들어 데이터가 네 행으로 주어졌다면 학생은 "네 행이 있다"에서 멈추지 말고, 각 행이 어떤 묶음인지, 행 안에서 어떤 이름으로 값을 꺼내는지, 그 값이 숫자인지 문자열인지, 여러 값을 모으면 어떤 자료구조가 되는지까지 말해야 합니다. 이 습관은 나중에 pandas의 DataFrame, PyTorch의 tensor, Transformer의 token sequence를 읽을 때 그대로 이어집니다.

오늘의 개념은 실제 임상 판단을 하기 위한 것이 아닙니다. 합성 데이터를 이용해 코드 읽기 훈련을 하는 것입니다. 따라서 출력값이 의학적으로 어떤 결론을 뜻한다고 말하지 않습니다. 수업에서는 "이 코드는 어떤 기준으로 어떤 값을 세었다" 또는 "이 코드는 어떤 목록의 평균을 계산했다"처럼 코드가 실제로 한 일만 설명합니다.

## 6. 코드 해석 질문

`lesson.py`를 읽을 때 학생은 다음 질문에 답해야 합니다.

- 이 파일에서 가장 먼저 만들어지는 데이터는 무엇인가?
- 그 데이터는 숫자 하나인가, 문자열 하나인가, 여러 값을 담은 묶음인가?
- 중간 변수는 어떤 줄에서 만들어지는가?
- 같은 계산을 여러 행에 적용하는 부분은 어디인가?
- 출력문은 학습을 위해 무엇을 보여 주는가?
- 기준값을 바꾸면 어떤 출력이 달라지는가?

이 질문은 시험 문제가 아니라 수업 중 읽기 순서입니다. 강사는 학생이 답을 못 하더라도 바로 정답을 주기보다, 어느 줄을 다시 봐야 하는지 안내합니다.

## 7. Colab에서 실행하는 방법

Colab은 Python을 실행하는 도구일 뿐입니다. 이 수업의 핵심은 노트북 형식이 아니라 Python 파일을 읽고 실행하는 것입니다. Day {day:02d} 폴더를 Colab에 올렸다면 다음 중 하나로 실행합니다.

```python
%run lesson.py
```

또는

```python
!python lesson.py
```

실행 후에는 출력이 맞는지보다, 출력이 어느 줄에서 만들어졌는지 찾는 것을 우선합니다.

## 8. 수업 중 활동

1. 학생에게 `lesson.py`를 먼저 눈으로 읽게 합니다.
2. 주석만 보고 코드가 무엇을 할지 예측하게 합니다.
3. 실행하기 전에 출력될 값의 타입을 말하게 합니다.
4. 실행 후 예측과 다른 부분을 표시하게 합니다.
5. 마지막으로 기준값이나 입력값 하나만 바꿔 출력 변화를 관찰합니다.

## 9. 흔한 오해와 교정

- "실행되면 이해한 것이다"라는 오해가 있습니다. 실행은 확인일 뿐이고, 이해는 설명할 수 있을 때 시작됩니다.
- "코드를 많이 쓰면 빨리 는다"는 오해가 있습니다. 초반에는 많이 쓰기보다 정확히 읽는 것이 더 중요합니다.
- "출력 숫자가 맞으면 끝"이라는 오해가 있습니다. 어떤 입력에서 어떤 과정으로 나온 숫자인지 설명해야 합니다.
- "Colab을 배우는 수업"이라는 오해가 있습니다. Colab은 도구이고, 본질은 Python과 데이터 흐름입니다.

## 10. 아주 작은 예시를 해석하는 법

초보자는 긴 코드를 한 번에 이해하려고 하면 거의 반드시 막힙니다. 그래서 오늘 주제를 배울 때는 다음처럼 아주 작은 예시로 해석을 시작합니다.

```python
values = [91, 107, 86, 118]
threshold = 100
flags = [value >= threshold for value in values]
```

이 코드를 "평균을 구한다"처럼 대충 말하면 안 됩니다. 아직 평균을 구하지 않았기 때문입니다. 정확한 설명은 다음과 같습니다. 첫 줄은 네 개의 숫자를 순서가 있는 목록으로 묶고 `values`라는 이름을 붙입니다. 둘째 줄은 기준값 `100`에 `threshold`라는 이름을 붙입니다. 셋째 줄은 `values` 안의 숫자를 하나씩 꺼내 `threshold`와 비교하고, 그 결과인 `True` 또는 `False`를 새 목록으로 만듭니다.

이런 식의 설명은 느려 보이지만, 처음 배우는 학생에게 가장 안전합니다. 나중에 코드가 길어져도 결국 같은 방식으로 읽습니다. 데이터를 확인하고, 기준을 확인하고, 반복되는 변환을 확인하고, 출력이 무엇인지 확인합니다.

## 11. 말로 설명하는 예시 답안

수업 중 학생에게 요구하는 답은 긴 문장이 아니어도 됩니다. 대신 정확해야 합니다. 예를 들어 `summary`라는 dictionary가 나오면 다음처럼 말할 수 있어야 합니다.

- `summary`는 여러 계산 결과를 이름과 함께 묶은 dictionary입니다.
- `patient_count`는 `records`의 행 개수를 센 값입니다.
- `mean_glucose`는 glucose 값 목록의 평균을 반올림한 값입니다.
- `high_glucose_count`는 glucose가 기준값 이상인 행의 개수입니다.

이 정도 설명을 할 수 있으면 코드를 단순히 실행한 것이 아니라, 코드가 만든 결과의 의미를 읽은 것입니다. 반대로 "그냥 결과입니다" 또는 "AI가 계산한 값입니다"라고 말하면 아직 해석이 부족한 상태입니다.

## 12. 교사가 칠판에 남길 핵심 구조

강의 중에는 다음 네 줄을 계속 반복해서 보여 주는 것이 좋습니다.

```text
입력 데이터 확인
-> 타입과 크기 확인
-> 변환 규칙 확인
-> 출력 의미 설명
```

이 구조는 Python 기초, pandas, PyTorch, LLM까지 계속 유지됩니다. DataFrame을 배울 때도 먼저 행과 열을 확인합니다. tensor를 배울 때도 shape와 dtype을 확인합니다. LLM을 배울 때도 token의 개수와 attention mask를 확인합니다. 도구가 바뀌어도 읽는 질문은 크게 바뀌지 않습니다.

## 13. 자기 점검 문제

학생은 오늘 수업을 마치기 전에 다음 질문에 말로 답합니다.

1. 오늘 코드에서 가장 먼저 만들어지는 값은 무엇인가요?
2. 그 값은 숫자, 문자열, list, dict 중 무엇인가요?
3. 반복문 또는 list comprehension이 있다면 어떤 값을 하나씩 꺼내나요?
4. 출력값 중 하나를 고르고, 그 값이 어떤 줄들에 의해 만들어졌는지 설명하세요.
5. 기준값 하나를 바꾸면 어떤 출력이 달라질지 예측하세요.

정답을 외우는 것이 목적이 아닙니다. 코드 안에서 근거 줄을 찾아 설명하는 것이 목적입니다.

## 14. 오늘의 정리

오늘의 목표는 `{title}`를 완벽히 암기하는 것이 아닙니다. 학생이 `lesson.py`를 열고, 주석을 따라가며, 각 줄이 만드는 값을 설명하는 것이 목표입니다. {next_day}
"""


def lesson_code(day: int, week: int, title: str, idea: str, terms: list[str]) -> str:
    term_list = ", ".join(terms)
    return f'''
"""
Day {day:02d}. {title}

이 파일은 학생이 코드를 처음부터 직접 작성하기 위한 파일이 아닙니다.
이미 작성된 코드를 읽고, 주석을 따라가며, 값의 흐름을 해석하기 위한 파일입니다.

오늘의 중심 생각:
{idea}

핵심 용어:
{term_list}
"""


# 1. 수업용 합성 데이터입니다.
#    실제 환자 정보가 아니며, 코드 읽기 연습을 위한 작은 표라고 보면 됩니다.
#    records는 list이고, list 안의 각 원소는 dict입니다.
records = [
    {{"patient_id": "P001", "age": 19, "glucose": 91, "group": "A", "tokens": ["patient", "stable"]}},
    {{"patient_id": "P002", "age": 21, "glucose": 107, "group": "B", "tokens": ["glucose", "high"]}},
    {{"patient_id": "P003", "age": 22, "glucose": 86, "group": "A", "tokens": ["follow", "up"]}},
    {{"patient_id": "P004", "age": 20, "glucose": 118, "group": "B", "tokens": ["review", "needed"]}},
]


# 2. 먼저 전체 데이터의 크기와 타입을 확인합니다.
#    초보자는 계산보다 먼저 "무엇을 들고 있는지" 확인해야 합니다.
print("DAY:", {day})
print("TOPIC:", "{title}")
print("records type:", type(records).__name__)
print("row count:", len(records))
print("first row type:", type(records[0]).__name__)


# 3. 한 행에서 값을 꺼내 봅니다.
#    dict는 key를 이용해 값을 꺼냅니다.
first_row = records[0]
print("first patient id:", first_row["patient_id"])
print("first glucose:", first_row["glucose"])


# 4. 여러 행에서 같은 열의 값만 모읍니다.
#    이 줄은 나중에 pandas 열 선택, tensor feature 추출, token id 목록 만들기의 기초가 됩니다.
glucose_values = [row["glucose"] for row in records]
ages = [row["age"] for row in records]
groups = [row["group"] for row in records]

print("glucose values:", glucose_values)
print("ages:", ages)
print("groups:", groups)


# 5. 요약값을 계산합니다.
#    평균은 합계를 개수로 나눈 값입니다.
mean_glucose = sum(glucose_values) / len(glucose_values)
mean_age = sum(ages) / len(ages)

print("mean glucose:", round(mean_glucose, 2))
print("mean age:", round(mean_age, 2))


# 6. 기준값을 변수로 둡니다.
#    숫자를 코드 곳곳에 직접 쓰지 않고 이름을 붙이면 해석하기 쉬워집니다.
threshold = 100


# 7. 각 행이 기준을 만족하는지 읽습니다.
#    비교식은 True 또는 False를 만듭니다.
for row in records:
    is_high = row["glucose"] >= threshold
    print(row["patient_id"], "glucose >=", threshold, "?", is_high)


# 8. 수업용 최종 요약입니다.
#    이 dict를 보고 어떤 계산이 있었는지 거꾸로 설명하는 것이 오늘의 과제입니다.
summary = {{
    "topic": "{title}",
    "core_idea": "{idea}",
    "patient_count": len(records),
    "mean_glucose": round(mean_glucose, 2),
    "high_glucose_count": sum(row["glucose"] >= threshold for row in records),
    "unique_groups": sorted(set(groups)),
}}

print("summary:", summary)


# 9. 읽기 과제입니다.
#    아래 질문에 답해 보세요. 답을 새 코드로 쓰기보다 말로 설명하는 것이 먼저입니다.
#    1. records와 first_row의 타입은 각각 무엇인가?
#    2. glucose_values는 어느 줄에서 어떤 방식으로 만들어졌는가?
#    3. threshold를 110으로 바꾸면 어떤 출력이 달라지는가?
#    4. summary의 각 key는 어떤 계산 결과를 담고 있는가?
'''


def create_lessons() -> None:
    for day, week, slug, title, idea, terms in DAY_SPECS:
        base = ROOT / "weeks" / week_slug(week) / f"day{day:02d}_{slug}"
        write(base / "concept.md", concept_text(day, week, slug, title, idea, terms))
        write(base / "lesson.py", lesson_code(day, week, title, idea, terms))


def create_root_docs() -> None:
    rows = "\n".join(
        f"| Week {week} | Day {day:02d} | [{title}](weeks/{week_slug(week)}/day{day:02d}_{slug}/concept.md) |"
        for day, week, slug, title, _idea, _terms in DAY_SPECS
    )
    write(
        ROOT / "README.md",
        f"""
# 서울대학교 의과대학생 특강 대비 Python, 데이터, PyTorch, LLM 4주 사전교육

이 저장소는 Python 경험이 거의 없는 의과대학생을 위한 4주 사전교육 교재입니다. Colab은 실행 도구로만 사용하고, 핵심은 Python 코드와 데이터 흐름을 읽고 해석하는 능력을 기르는 것입니다.

## 자료 구조

각 일차 폴더에는 두 파일만 둡니다.

```text
concept.md  # 교과서식 개념 설명
lesson.py   # 주석을 따라 읽고 실행하는 Python 코드
```

불필요한 다중 md 파일, 학생용/해설용 노트북 분리, 반복되는 퀴즈 폴더는 제거했습니다. 학생이 무엇을 읽고 무엇을 실행해야 하는지 헷갈리지 않게 하는 것이 우선입니다.

## 학습 경로

| 주차 | 일차 | 개념 파일 |
| --- | --- | --- |
{rows}

## Colab 실행

각 일차 폴더의 `lesson.py`를 Colab에 올린 뒤 다음 중 하나로 실행합니다.

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
""",
    )
    write(
        ROOT / "TEACHING_GUIDE.md",
        """
# Teaching Guide

## 운영 원칙

학생에게 처음부터 코드를 많이 쓰게 하지 않습니다. 먼저 `concept.md`를 읽고, `lesson.py`의 주석을 따라가며, 각 줄이 만드는 값을 말로 설명하게 합니다.

## 90분 수업 흐름

1. 15분: 오늘 개념의 위치와 핵심 용어 설명
2. 25분: `lesson.py`를 실행하지 않고 주석과 코드만 읽기
3. 20분: Colab에서 실행하고 예측과 출력 비교
4. 20분: 기준값이나 입력값 하나만 바꾸어 출력 변화 관찰
5. 10분: 오늘의 핵심 문장을 학생 말로 다시 설명

## 질문 방식

- 이 줄은 어떤 값을 만드나요?
- 이 값의 타입은 무엇인가요?
- 이 변수는 어디에서 처음 만들어졌나요?
- 이 출력은 어떤 계산에서 나왔나요?
- 실제 환자 데이터라면 어떤 개인정보 문제가 생길 수 있나요?
""",
    )
    write(ROOT / "requirements-colab.txt", "numpy\npandas\nmatplotlib\nscikit-learn\ntorch\ntransformers\n")
    write(ROOT / "requirements-dev.txt", "pytest>=8\n")
    write(ROOT / "pyproject.toml", '[tool.pytest.ini_options]\ntestpaths = ["tests"]\npython_files = ["test_*.py"]\n')
    write(ROOT / ".gitignore", "__pycache__/\n.pytest_cache/\n.ipynb_checkpoints/\n*.pyc\n.venv/\ngithub_tree_payload.json\n")


def create_datasets() -> None:
    rows = [
        {"patient_id": f"P{i:03d}", "age": str(18 + i % 7), "group": "A" if i % 2 else "B", "glucose": str(82 + i * 3)}
        for i in range(1, 13)
    ]
    path = ROOT / "datasets" / "synthetic_patients.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    write(
        ROOT / "datasets" / "README.md",
        """
# Datasets

이 폴더의 CSV는 수업용 합성 데이터입니다. 실제 환자 정보, 연락처, 주소, 자유서술 진료기록을 포함하지 않습니다.
""",
    )


def create_validation_scripts() -> None:
    write(
        ROOT / "scripts" / "course_config.py",
        "WEEKS = " + repr({k: v[0] for k, v in WEEKS.items()}) + "\n"
        "DAYS = " + repr([(day, week, f"day{day:02d}_{slug}", title) for day, week, slug, title, _idea, _terms in DAY_SPECS]) + "\n",
    )
    write(
        ROOT / "scripts" / "validate_structure.py",
        """
from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]

for day, week, slug, _title in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    expected = {"concept.md", "lesson.py"}
    actual_files = {p.name for p in base.iterdir() if p.is_file()}
    actual_dirs = [p.name for p in base.iterdir() if p.is_dir()]
    if actual_files != expected:
        raise AssertionError(f"{base.relative_to(ROOT)} should contain only {expected}, found {actual_files}")
    if actual_dirs:
        raise AssertionError(f"{base.relative_to(ROOT)} should not contain subdirectories: {actual_dirs}")

if list((ROOT / "weeks").rglob("*.ipynb")):
    raise AssertionError("ipynb files should not remain in the simplified curriculum")

allowed_root_md = {"README.md", "TEACHING_GUIDE.md"}
root_md = {p.name for p in ROOT.glob("*.md")}
if root_md != allowed_root_md:
    raise AssertionError(f"unexpected root markdown files: {sorted(root_md - allowed_root_md)}")

print("validate_structure: OK")
""",
    )
    write(
        ROOT / "scripts" / "validate_markdown_links.py",
        """
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
errors = []

for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for target in link_re.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (md.parent / clean).exists():
            errors.append(f"{md.relative_to(ROOT)} -> {target}")

if errors:
    raise AssertionError(chr(10).join(errors[:50]))
print("validate_markdown_links: OK")
""",
    )
    write(
        ROOT / "scripts" / "check_required_sections.py",
        """
from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
required_sections = [
    "## 1. 오늘의 위치",
    "## 2. 왜 이 개념을 먼저 배우는가",
    "## 3. 핵심 용어",
    "## 5. 교과서식 설명",
    "## 7. Colab에서 실행하는 방법",
    "## 14. 오늘의 정리",
]

for day, week, slug, _title in DAYS:
    concept = (ROOT / "weeks" / WEEKS[week] / slug / "concept.md").read_text(encoding="utf-8")
    lesson = (ROOT / "weeks" / WEEKS[week] / slug / "lesson.py").read_text(encoding="utf-8")
    if len(concept) < 4500:
        raise AssertionError(f"concept too short: day {day}")
    for section in required_sections:
        if section not in concept:
            raise AssertionError(f"missing {section}: day {day}")
    for marker in ["# 1. 수업용 합성 데이터", "# 4. 여러 행에서 같은 열의 값만 모읍니다", "# 9. 읽기 과제"]:
        if marker not in lesson:
            raise AssertionError(f"missing lesson marker {marker}: day {day}")

print("check_required_sections: OK")
""",
    )
    write(
        ROOT / "scripts" / "execute_lessons.py",
        """
from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
count = 0
for day, week, slug, _title in DAYS:
    path = ROOT / "weeks" / WEEKS[week] / slug / "lesson.py"
    env = {"__name__": "__lesson__"}
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), env)
    count += 1
print(f"execute_lessons: OK ({count} lessons)")
""",
    )
    write(
        ROOT / "scripts" / "validate_datasets.py",
        """
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "datasets" / "synthetic_patients.csv"
rows = list(csv.DictReader(path.open(encoding="utf-8")))
if len(rows) < 10:
    raise AssertionError("synthetic dataset should contain at least 10 rows")
if len({row["patient_id"] for row in rows}) != len(rows):
    raise AssertionError("duplicate patient_id")
print("validate_datasets: OK")
""",
    )


def create_tests() -> None:
    write(
        ROOT / "tests" / "test_course_contract.py",
        """
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_every_day_has_only_concept_and_lesson():
    days = list((ROOT / "weeks").glob("week*/day*"))
    assert len(days) == 28
    for day in days:
        assert (day / "concept.md").exists()
        assert (day / "lesson.py").exists()
        assert not [p for p in day.iterdir() if p.is_dir()]


def test_no_notebooks_remain():
    assert not list(ROOT.rglob("*.ipynb"))


def test_root_markdown_is_minimal():
    assert {p.name for p in ROOT.glob("*.md")} == {"README.md", "TEACHING_GUIDE.md"}


def test_concepts_are_textbook_length():
    for path in (ROOT / "weeks").rglob("concept.md"):
        assert len(path.read_text(encoding="utf-8")) >= 4500
""",
    )


def main() -> None:
    clean_generated()
    create_root_docs()
    create_lessons()
    create_datasets()
    create_validation_scripts()
    create_tests()
    print("Simplified textbook-style curriculum generated.")


if __name__ == "__main__":
    main()
