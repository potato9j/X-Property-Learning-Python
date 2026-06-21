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
    for name in [
        "scripts/generate_repository.py",
        "scripts/generate_quality_repository.py",
        "scripts/validate_notebooks.py",
        "scripts/execute_notebooks.py",
    ]:
        path = ROOT / name
        if path.exists():
            path.unlink()


def slug_for(day: int) -> str:
    for spec in DAY_SPECS:
        if spec[0] == day:
            return f"day{spec[0]:02d}_{spec[2]}"
    raise KeyError(day)


def week_slug(week: int) -> str:
    return WEEKS[week][0]


def concept_text(day: int, week: int, slug: str, title: str, idea: str, terms: list[str]) -> str:
    week_name = WEEKS[week][1]
    previous = "이 장은 Python을 처음 접하는 학생도 따라올 수 있도록, 프로그램이 값을 다루는 가장 기본 방식부터 시작합니다." if day == 1 else f"이 장은 앞에서 배운 코드 읽기 습관을 이어 받아 `{title}`라는 새 개념을 하나의 장으로 정리합니다."
    next_text = "다음 장에서는 오늘 배운 구조를 더 큰 데이터 흐름이나 모델 흐름에 연결합니다." if day < 28 else "이 장을 마치면 전체 과정에서 배운 Python, 데이터, 모델, LLM 개념을 하나의 검증 가능한 프로젝트 관점으로 정리합니다."
    term_rows = "\n".join(
        f"| `{term}` | 이 장을 읽을 때 계속 등장하는 기본 단어입니다. 코드에서 이 이름이 어떤 값, 규칙, 구조를 가리키는지 확인해야 합니다. |"
        for term in terms
    )
    structure_rows = "\n".join(
        f"{idx}. `{term}`를 코드 안에서 찾고, 이 용어가 입력인지 중간 계산인지 출력인지 구분합니다."
        for idx, term in enumerate(terms, 1)
    )
    example_values = ", ".join(f'"{term}"' for term in terms[:3])
    return f"""
# Day {day:02d}. {title}

## 1. 이 장에서 배우는 내용이 무엇인지

{previous}

이번 주차의 큰 주제는 **{week_name}**입니다. 그 안에서 이 장은 **{title}**를 다룹니다. 이 장의 핵심 문장은 다음과 같습니다.

> {idea}

학생은 이 문장을 외우는 것이 아니라, 이 문장이 코드에서 어떻게 보이는지 읽을 수 있어야 합니다. 코딩 초보자는 보통 코드를 "명령어의 모음"으로만 봅니다. 하지만 교과서적으로는 코드를 "값을 만들고, 이름을 붙이고, 규칙에 따라 바꾸고, 결과를 확인하는 글"로 읽어야 합니다. 이 장은 바로 그 읽기 방식을 한 단계 더 구체화합니다.

이 장을 다 읽은 학생은 다음 질문에 답할 수 있어야 합니다.

- 이 장의 개념은 어떤 문제를 해결하기 위해 필요한가?
- 코드에서 이 개념은 어떤 값, 자료구조, 계산 흐름으로 나타나는가?
- 초보자가 이 개념을 잘못 이해하면 어떤 종류의 오류가 생기는가?
- `lesson.py`와 별개로 아주 작은 예제를 보면 같은 원리를 설명할 수 있는가?

## 2. 전체개념

Python 학습은 문법 목록을 외우는 방식으로 시작하면 금방 막힙니다. 문법은 중요하지만, 문법보다 먼저 잡아야 할 것은 "컴퓨터가 값을 다루는 방식"입니다. 컴퓨터는 사람처럼 문맥을 넓게 추측하지 않습니다. 어떤 값이 들어왔는지, 그 값이 숫자인지 문자열인지 목록인지 표인지, 그리고 어떤 규칙으로 변하는지를 매우 엄격하게 따릅니다.

**{title}**는 이 큰 흐름 안에서 특정한 역할을 맡습니다. 어떤 장은 값을 담는 그릇을 설명하고, 어떤 장은 여러 값을 반복해서 처리하는 법을 설명하며, 어떤 장은 모델이 숫자를 이용해 예측을 만드는 과정을 설명합니다. 겉으로는 서로 다른 내용처럼 보여도, 모든 장은 같은 질문으로 연결됩니다.

1. 입력은 무엇인가?
2. 입력은 어떤 형태인가?
3. 어떤 변환 규칙이 적용되는가?
4. 중간 결과는 어떤 이름으로 저장되는가?
5. 최종 출력은 무엇을 의미하는가?

이 장의 중심 개념을 한 문장으로 다시 쓰면 다음과 같습니다.

> {idea}

이 문장을 코드 읽기 관점으로 바꾸면, 학생은 먼저 값의 출발점을 찾아야 합니다. 그다음 값이 어떤 이름에 저장되는지 보고, 계산이 일어나는 줄과 출력이 일어나는 줄을 구분해야 합니다. 코드가 길어져도 이 원칙은 바뀌지 않습니다. pandas를 쓰든, PyTorch를 쓰든, LLM API를 쓰든 결국 입력, 구조, 변환, 출력의 흐름을 읽는 일입니다.

의과대학생이 이 관점을 가져야 하는 이유도 분명합니다. 의료 데이터와 모델 출력은 겉으로는 정돈되어 보여도, 실제로는 결측치, 잘못된 타입, 기준의 불명확함, 데이터 누수, 모델 환각 같은 문제가 숨어 있을 수 있습니다. 코드를 읽는 능력은 단순한 프로그래밍 기술이 아니라, 데이터와 모델이 낸 결론을 검증하는 기초 체력입니다.

## 3. 전체 구조

이 장은 다음 구조로 읽습니다.

1. **문제 상황을 잡는다.**  
   왜 이 개념이 필요한지 먼저 봅니다. 초보자는 문법부터 보려 하지만, 실제 이해는 "왜 이런 도구가 필요한가"에서 시작됩니다.

2. **값의 모양을 확인한다.**  
   값 하나인지, 여러 값의 묶음인지, 행과 열을 가진 표인지, 숫자로 된 tensor인지 확인합니다. 값의 모양을 모르면 뒤의 계산을 제대로 읽을 수 없습니다.

3. **이름과 역할을 구분한다.**  
   변수 이름은 사람이 이해하기 쉽게 붙인 표지입니다. 이름 자체가 중요한 것이 아니라, 그 이름이 가리키는 값과 역할이 중요합니다.

4. **변환 규칙을 읽는다.**  
   조건문, 반복문, 함수, 배열 연산, 모델 호출은 모두 입력을 출력으로 바꾸는 규칙입니다. 이 장에서는 그 규칙이 어떤 방식으로 나타나는지 봅니다.

5. **출력의 의미를 제한해서 말한다.**  
   코드 출력은 코드가 계산한 결과입니다. 그것을 의학적 결론, 모델의 진실, 자동 판단으로 확대 해석하면 안 됩니다. 초보 단계에서는 "이 코드는 무엇을 계산했는가"까지만 정확히 말합니다.

이 구조는 1일차부터 28일차까지 계속 유지됩니다. 처음에는 숫자와 문자열을 대상으로 연습하고, 뒤로 갈수록 DataFrame, tensor, token, attention, LLM 출력으로 대상이 커집니다. 하지만 읽는 순서는 같습니다.

{structure_rows}

## 4. 전체용어

| 용어 | 수업에서의 뜻 |
| --- | --- |
{term_rows}

용어는 사전처럼 외우지 않습니다. 교과서에서 용어를 배우는 목적은 이후 문장을 정확하게 읽기 위해서입니다. 예를 들어 `type`이라는 단어를 배운다면, 단순히 "자료형"이라고 외우는 데서 끝나지 않습니다. 어떤 값이 숫자인지 문자열인지 목록인지에 따라 사용할 수 있는 연산이 달라진다는 사실까지 연결해야 합니다.

이 장의 용어도 마찬가지입니다. 각 용어는 독립된 단어가 아니라 코드 흐름 안에서 역할을 가집니다. 학생은 용어를 볼 때마다 다음 세 가지를 함께 확인합니다.

- 이 용어는 값 자체를 말하는가, 값의 형태를 말하는가, 변환 규칙을 말하는가?
- 코드에서 이 용어는 어느 줄에 나타나는가?
- 이 용어를 잘못 이해하면 어떤 출력이 잘못 해석되는가?

## 5. 설명

이 장의 개념을 이해하려면 먼저 "코드는 위에서 아래로 읽히는 글"이라는 사실을 받아들여야 합니다. 사람은 문장을 읽을 때 앞뒤 맥락을 추측하지만, Python은 한 줄씩 실행하면서 현재까지 만들어진 값만 사용합니다. 아직 만들어지지 않은 이름은 사용할 수 없고, 숫자에 문자열 연산을 적용할 수 없으며, 없는 열이나 key를 꺼내려고 하면 오류가 납니다.

**{title}**를 배울 때도 이 원칙은 그대로 적용됩니다. 먼저 가장 작은 예를 봅니다. 값 하나가 만들어지고, 그 값에 이름이 붙고, 그 이름이 다시 계산에 사용됩니다. 그다음 여러 값이 묶이고, 반복이나 조건을 통해 같은 규칙이 여러 값에 적용됩니다. 나중에는 이 흐름이 표와 tensor와 모델 출력으로 확장됩니다.

초보자가 자주 하는 실수는 코드를 한 덩어리로 보려는 것입니다. 긴 코드를 보면 "전체가 무슨 뜻인지"부터 알고 싶어 합니다. 하지만 프로그래밍 교과서의 기본 읽기법은 반대입니다. 한 줄이 만든 값을 정확히 알고, 그 다음 줄이 그 값을 어떻게 사용하는지 보는 방식으로 천천히 올라갑니다. 전체 이해는 작은 줄 이해가 쌓인 결과입니다.

이 장에서는 특히 다음 관점을 반복해서 사용합니다.

- 값은 반드시 어떤 형태를 가진다.
- 변수는 값을 담는 상자가 아니라, 값에 붙인 이름이다.
- 함수나 연산은 입력을 받아 출력으로 바꾸는 규칙이다.
- 출력은 계산 결과이지, 자동으로 현실의 결론이 되지는 않는다.
- 모델과 LLM도 결국 입력을 받고 내부 규칙을 거쳐 출력을 만든다.

의료 데이터나 LLM을 다룰 때는 이 태도가 더 중요합니다. 예를 들어 모델이 높은 점수를 출력했다고 해서 곧바로 의학적 판단이 되는 것은 아닙니다. 코드가 어떤 입력을 받았는지, 어떤 기준으로 값을 처리했는지, 출력이 어떤 제한을 갖는지 확인해야 합니다. 이 장은 그런 검증 능력을 기르는 기초 장입니다.

아래 문장은 이 장의 설명을 한 번 더 압축한 것입니다.

> {idea}

이 문장을 이해했다는 것은, 비슷한 코드를 보았을 때 입력, 중간 값, 출력의 위치를 직접 찾을 수 있다는 뜻입니다. 단어를 외웠다는 뜻이 아닙니다.

## 6. py파일과 별개로 예제

아래 예제는 `lesson.py`와 별개의 작은 예제입니다. 수업 코드와 완전히 같을 필요는 없습니다. 목적은 이 장의 개념을 더 작은 형태로 다시 보는 것입니다.

```python
chapter_terms = [{example_values}]
chapter_title = "{title}"
core_idea = "{idea}"

print("장 제목:", chapter_title)
print("중심 문장:", core_idea)
print("용어 개수:", len(chapter_terms))

for index, term in enumerate(chapter_terms):
    print(index, term)
```

이 예제는 일부러 단순합니다. 첫 줄은 이 장에서 자주 볼 용어 몇 개를 list로 묶습니다. 둘째 줄과 셋째 줄은 문자열에 이름을 붙입니다. `len(chapter_terms)`는 목록 안에 들어 있는 값의 개수를 계산합니다. `for` 반복문은 목록의 값을 하나씩 꺼내면서 순서 번호와 함께 출력합니다.

이 작은 코드에서도 교과서적 읽기 순서는 유지됩니다.

1. `chapter_terms`는 여러 문자열을 담은 list입니다.
2. `chapter_title`은 이 장의 제목을 담은 문자열입니다.
3. `core_idea`는 이 장의 중심 문장을 담은 문자열입니다.
4. `len()`은 list 안의 값 개수를 계산합니다.
5. `for`는 list 안의 값을 순서대로 꺼냅니다.

이 예제는 실제 분석이나 모델링을 하지 않습니다. 대신 "값을 만들고, 이름을 붙이고, 구조를 확인하고, 반복해서 출력한다"는 기본 구조를 보여 줍니다. 복잡한 코드도 결국 이 구조의 확장입니다.

### 스스로 확인하기

다음 질문에 답해 보세요.

- `chapter_terms`의 타입은 무엇인가요?
- `chapter_terms` 안의 첫 번째 값은 무엇인가요?
- `len(chapter_terms)`의 출력은 왜 그 숫자가 되나요?
- `for` 반복문은 몇 번 실행되나요?
- 이 예제를 `{title}`의 중심 문장과 연결하면 무엇을 설명할 수 있나요?

이 질문에 답할 수 있으면, 학생은 최소한 이 장의 용어와 코드 구조를 분리해서 읽을 준비가 된 것입니다. {next_text}
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
link_re = re.compile(r"\\[[^\\]]+\\]\\(([^)]+)\\)")
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
    "## 1. 이 장에서 배우는 내용이 무엇인지",
    "## 2. 전체개념",
    "## 3. 전체 구조",
    "## 4. 전체용어",
    "## 5. 설명",
    "## 6. py파일과 별개로 예제",
]

for day, week, slug, _title in DAYS:
    concept = (ROOT / "weeks" / WEEKS[week] / slug / "concept.md").read_text(encoding="utf-8")
    lesson = (ROOT / "weeks" / WEEKS[week] / slug / "lesson.py").read_text(encoding="utf-8")
    if len(concept) < 4500:
        raise AssertionError(f"concept too short: day {day}")
    for section in required_sections:
        if section not in concept:
            raise AssertionError(f"missing {section}: day {day}")
    forbidden_sections = [
        "오늘의 " + "위치",
        "왜 이 개념을 " + "먼저 배우는가",
        "교과서식 " + "설명",
        "코드 해석 " + "질문",
        "수업 중 " + "활동",
    ]
    for phrase in forbidden_sections:
        if phrase in concept:
            raise AssertionError(f"forbidden old concept heading remains: {phrase}: day {day}")
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
