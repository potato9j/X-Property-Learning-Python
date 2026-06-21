from __future__ import annotations

import csv
import json
import random
import shutil
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

WEEKS = {
    1: ("week01_python_foundations", "Python 핵심 기초 완전 입문"),
    2: ("week02_numpy_pandas_statistics", "NumPy, pandas, 시각화와 통계"),
    3: ("week03_pytorch_and_machine_learning", "PyTorch와 머신러닝 기초"),
    4: ("week04_transformer_and_llm", "Transformer와 LLM"),
}

DAYS = [
    (1, 1, "colab_execution_values_and_types", "Colab 실행, 값, 표현식과 타입"),
    (2, 1, "strings_lists_and_structured_data", "문자열, 리스트와 순서형 자료"),
    (3, 1, "dict_tuple_set_and_object_model", "dictionary, tuple, set과 객체 모델"),
    (4, 1, "conditions_loops_and_comprehension", "조건문, 반복문과 comprehension"),
    (5, 1, "functions_scope_and_type_hints", "함수, scope와 type hint"),
    (6, 1, "modules_errors_files_and_debugging", "module, 오류, 파일과 디버깅"),
    (7, 1, "week1_integrated_review", "1주차 통합 숙달"),
    (8, 2, "numpy_arrays_shape_dtype_indexing", "NumPy 배열, shape, dtype과 indexing"),
    (9, 2, "vectorization_broadcasting_linear_algebra", "vectorization, broadcasting과 선형대수"),
    (10, 2, "pandas_series_dataframe_selection", "pandas Series, DataFrame과 선택"),
    (11, 2, "data_cleaning_groupby_merge_pivot", "결측치, groupby, merge와 reshape"),
    (12, 2, "visualization_exploratory_data_analysis", "시각화와 탐색적 데이터 분석"),
    (13, 2, "probability_distribution_sampling_statistics", "확률, 표본추출과 기술통계"),
    (14, 2, "inference_testing_regression_review", "추론, 검정, 회귀와 2주차 숙달"),
    (15, 3, "machine_learning_workflow_split_baseline", "머신러닝 workflow와 데이터 분할"),
    (16, 3, "tensor_autograd_gradient", "tensor, autograd와 gradient"),
    (17, 3, "nn_module_layer_activation_forward", "nn.Module, layer, activation과 forward"),
    (18, 3, "loss_optimizer_training_loop", "loss, optimizer와 학습 루프"),
    (19, 3, "data_loader_evaluation_metrics", "DataLoader와 학습 루프 평가 지표"),
    (20, 3, "regularization_overfitting_model_management", "검증, overfitting과 모델 관리"),
    (21, 3, "text_tensor_embedding_review", "텍스트 tensor, embedding과 3주차 숙달"),
    (22, 4, "nlp_tokenization_vocabulary_representation", "NLP, tokenization과 어휘 표현"),
    (23, 4, "embedding_similarity_retrieval", "embedding, similarity와 위치 정보"),
    (24, 4, "attention_qkv_mask_multihead", "attention, QKV, mask와 multi-head"),
    (25, 4, "transformer_decoder_language_modeling", "Transformer와 언어모델링"),
    (26, 4, "huggingface_model_usage_generation", "Hugging Face 모델 추론과 생성"),
    (27, 4, "decoding_prompting_rag_finetuning", "decoding, prompting, RAG와 fine-tuning"),
    (28, 4, "integrated_llm_project_ethics_review", "통합 LLM 프로젝트, 윤리와 최종 숙달"),
]

ROOT_DOCS = [
    "README.md",
    "AGENTS.md",
    "AI_LEARNING_GUIDE.md",
    "ASSESSMENT_PLAN.md",
    "COLAB_SETUP.md",
    "COURSE_SYLLABUS.md",
    "CURRICULUM_MAP.md",
    "GENERATION_STATUS.md",
    "GLOSSARY.md",
    "LEARNING_OUTCOMES.md",
    "PRIVACY_AND_ETHICS.md",
    "PROJECT_PLAN.md",
    "TEACHING_GUIDE.md",
    "requirements-colab.txt",
    "requirements-dev.txt",
    "pyproject.toml",
]


def write(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = textwrap.dedent(body).strip() + "\n"
    if path.suffix.lower() == ".md":
        text = "\n".join(line[4:] if line.startswith("    ") else line for line in text.splitlines()) + "\n"
    path.write_text(text, encoding="utf-8")


def clean() -> None:
    for name in ["weeks", "datasets", "assessments", "appendices", "instructor", "tests"]:
        target = ROOT / name
        if target.exists():
            shutil.rmtree(target)
    for name in ROOT_DOCS:
        target = ROOT / name
        if target.exists():
            target.unlink()


def notebook(path: Path, title: str, topic: str, kind: str) -> None:
    code = f"""
records = [
    {{"patient_id": "P001", "age": 19, "glucose": 91, "group": "A"}},
    {{"patient_id": "P002", "age": 21, "glucose": 107, "group": "B"}},
    {{"patient_id": "P003", "age": 22, "glucose": 86, "group": "A"}},
    {{"patient_id": "P004", "age": 20, "glucose": 118, "group": "B"}},
]
glucose = [row["glucose"] for row in records]
mean_glucose = sum(glucose) / len(glucose)
high_count = sum(value >= 100 for value in glucose)
summary = {{"topic": "{topic}", "mean_glucose": round(mean_glucose, 2), "high_count": high_count}}
print(summary)
"""
    if kind == "student":
        code += '\nreflection = "여기에 관찰한 shape, 값의 흐름, 오류 가능성을 한 문장으로 정리합니다."\nprint(reflection)\n'
    if kind == "solution":
        code += '\nanswer = "평균과 기준 이상 개수를 분리해 계산하면 코드의 의도가 검증됩니다."\nprint(answer)\n'
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {title}\n",
                    "\n",
                    "이 노트북은 Colab에서 위에서 아래로 실행하며, 각 셀의 입력과 출력을 직접 확인하도록 구성했습니다.\n",
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"## 학습 맥락\n오늘 주제는 `{topic}`입니다. 의료 데이터 예시는 모두 합성 데이터이며 실제 개인정보를 포함하지 않습니다.\n",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [line + "\n" for line in textwrap.dedent(code).strip().splitlines()],
            },
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    write(path, json.dumps(nb, ensure_ascii=False, indent=2))


def root_docs() -> None:
    rows = "\n".join(
        f"| Week {week} | Day {day:02d} | [{title}](weeks/{WEEKS[week][0]}/day{day:02d}_{slug}/{'concept.md' if day == 1 else '01_concepts/README.md'}) |"
        for day, week, slug, title in DAYS
    )
    write(
        ROOT / "README.md",
        f"""
# 서울대학교 의과대학생 특강 대비 Python, 데이터, PyTorch, LLM 4주 사전교육

이 저장소는 Python 경험이 거의 없는 의과대학생이 4주 동안 Colab에서 실습하며 통계, 데이터 분석, PyTorch, Transformer와 LLM의 핵심 흐름을 익히도록 설계한 수업 자료입니다. 모든 예제 데이터는 합성 데이터이며 실제 환자 정보, 연락처, 주소, 진료기록을 포함하지 않습니다.

## 과정 운영 원칙

- Colab은 실행 도구로만 사용하고, 학습의 중심은 Python 코드 읽기와 해석에 둡니다.
- Day 1은 `concept.md`와 `lesson.py` 두 파일만 사용해 학생이 읽을 파일과 실행할 파일을 명확히 구분합니다.
- 이후 일차도 개념 설명, 실행 예제, 실습 문제, 퀴즈, 해설을 학생이 따라갈 수 있는 순서로 제공합니다.
- 로컬 검증 스크립트는 문서 구조, 링크, 노트북 또는 Python 파일의 실행 가능성을 확인합니다.
- 생성형 AI는 학습 보조 도구로만 다루며, 개인정보 입력과 검증 없는 임상 판단을 금지합니다.

## 28일 학습 경로

| 주차 | 일차 | 주제 |
| --- | --- | --- |
{rows}

## 검증

```bash
python scripts/validate_structure.py
python scripts/validate_markdown_links.py
python scripts/check_required_sections.py
python scripts/validate_notebooks.py
python scripts/validate_datasets.py
python scripts/execute_notebooks.py
python -m pytest
```
""",
    )
    docs = {
        "COURSE_SYLLABUS.md": "# Course Syllabus\n\n## 대상\n\n서울대학교 의과대학생 중 Python, 데이터 분석, 딥러닝 경험이 적은 학습자를 대상으로 합니다.\n\n## 수업 방식\n\n각 일차는 90분 기준입니다. 전반 30분은 개념과 코드 읽기, 중반 40분은 Colab 실습, 후반 20분은 퀴즈와 오류 점검으로 운영합니다.\n\n## 주차별 산출물\n\n1주차에는 Python 코드의 실행 흐름을 읽고 작은 함수를 작성합니다. 2주차에는 합성 임상 표 형태 데이터를 정리하고 요약 통계를 설명합니다. 3주차에는 학습 루프의 입력, 손실, gradient, 평가 지표를 말로 설명합니다. 4주차에는 token, embedding, attention, RAG의 한계와 윤리 기준을 설명합니다.\n",
        "TEACHING_GUIDE.md": "# Teaching Guide\n\n## 수업 전 준비\n\n강사는 해당 일차의 concepts, examples, practice, quiz, answers 폴더를 미리 확인합니다. 학생에게는 practice_student 노트북을 먼저 열게 하고, solution 노트북은 토론 후 공개합니다.\n\n## 설명 방식\n\n처음부터 긴 코드를 작성하게 하지 않습니다. 먼저 출력값을 예측하게 하고, 그 다음 한 줄씩 값의 흐름을 추적하게 합니다. 데이터 분석 파트에서는 shape, 행, 열, 결측치, 기준값을 항상 말로 설명하게 합니다.\n",
        "ASSESSMENT_PLAN.md": "# Assessment Plan\n\n평가는 암기보다 설명 가능성을 봅니다. 학생은 코드의 출력, 데이터 shape, 모델 입력과 출력, 윤리적 제한을 자신의 말로 설명해야 합니다.\n\n## 구성\n\n- 매일 5문항 실습과 4문항 퀴즈\n- 주차별 통합 복습\n- 4주차 최종 LLM 미니 프로젝트\n",
        "PRIVACY_AND_ETHICS.md": "# Privacy And Ethics\n\n이 과정의 모든 데이터는 합성 데이터입니다. 학생은 실습 중 실제 환자 이름, 학번, 연락처, 주소, 진료기록, 검사결과 원문을 입력하지 않습니다.\n\n## LLM 사용 원칙\n\nLLM 출력은 근거가 아니라 초안입니다. 의료적 판단, 진단, 처방, 위험도 안내는 검증된 자료와 지도교수의 확인 없이 사용하지 않습니다.\n",
        "AI_LEARNING_GUIDE.md": "# AI Learning Guide\n\nAI에게 답을 바로 묻기보다 먼저 자신의 가설을 작성합니다. 그 다음 AI에게 오류 가능성, 반례, 더 작은 예제를 요청합니다.\n",
        "COLAB_SETUP.md": "# Colab Setup\n\n1. GitHub에서 원하는 일차의 노트북을 엽니다.\n2. Colab으로 열어 Python 3 런타임을 사용합니다.\n3. 셀은 위에서 아래로 실행합니다.\n4. 오류가 나면 실행 순서, 변수 이름, 데이터 길이, 패키지 설치 여부를 확인합니다.\n",
        "CURRICULUM_MAP.md": "# Curriculum Map\n\nPython 기초는 데이터 분석의 문법 기반입니다. NumPy와 pandas는 표와 배열을 다루는 기술입니다. PyTorch는 tensor와 gradient를 통해 모델 학습 과정을 설명합니다. LLM 파트는 token, embedding, attention을 앞선 tensor 사고와 연결합니다.\n",
        "LEARNING_OUTCOMES.md": "# Learning Outcomes\n\n수료자는 Python 코드의 실행 순서를 읽고, 합성 표 데이터를 정리하며, 간단한 학습 루프를 설명하고, LLM 출력의 한계와 개인정보 위험을 구분할 수 있어야 합니다.\n",
        "GLOSSARY.md": "# Glossary\n\n- value: Python 코드가 계산해 만드는 실제 값입니다.\n- type: 값이 어떤 종류인지 나타내는 분류입니다.\n- shape: 배열이나 tensor의 축별 크기입니다.\n- gradient: 손실을 줄이기 위해 파라미터를 어느 방향으로 바꿀지 알려주는 값입니다.\n- token: 모델이 텍스트를 처리하기 위해 나눈 단위입니다.\n- embedding: token이나 항목을 숫자 벡터로 표현한 것입니다.\n- attention: 현재 위치가 다른 위치의 정보를 얼마나 참고할지 계산하는 방식입니다.\n",
        "PROJECT_PLAN.md": "# Project Plan\n\n이 저장소의 목표는 4주 사전교육 자료를 수업 가능한 품질로 유지하는 것입니다. 새 자료를 추가할 때는 학생용 파일과 해설 파일을 분리하고, 합성 데이터만 사용하며, 검증 스크립트가 통과해야 합니다.\n",
        "GENERATION_STATUS.md": "# Generation Status\n\n28일 수업 구조, 학생용 노트북, 해설 노트북, 퀴즈, 데이터셋, 강사용 자료, 검증 스크립트를 생성했습니다. README의 표와 링크는 GitHub에서 일반 Markdown으로 렌더링되도록 들여쓰기를 제거했습니다.\n",
        "AGENTS.md": "# AGENTS\n\n이 저장소를 수정할 때는 수업 품질을 우선합니다. 파일 수를 늘리는 변경보다 개념 설명, 실습 지시, 해설 분리, 검증 가능성을 개선하는 변경을 우선합니다.\n",
    }
    for name, body in docs.items():
        write(ROOT / name, body)
    write(ROOT / "requirements-colab.txt", "numpy\npandas\nmatplotlib\nscikit-learn\ntorch\ntransformers\n")
    write(ROOT / "requirements-dev.txt", "pytest>=8\n")
    write(ROOT / "pyproject.toml", '[tool.pytest.ini_options]\ntestpaths = ["tests"]\npython_files = ["test_*.py"]\n')


def day1_concept() -> str:
    return """
# Day 01. Colab 실행, 값, 표현식과 타입

## 1. 오늘 수업의 목적

첫날의 목표는 Python 문법을 많이 외우는 것이 아닙니다. 학생이 코드 한 줄을 보았을 때 "이 줄은 어떤 값을 만들고, 그 값은 어디로 이동하며, 마지막 출력은 무엇을 뜻하는가"를 설명할 수 있게 만드는 것입니다. 의학 데이터 분석, PyTorch, LLM 코드도 결국 값이 만들어지고 전달되고 변환되는 과정입니다. 그래서 Day 1에서는 가장 작은 단위인 값, 표현식, 변수, 타입, 실행 순서를 정확히 잡습니다.

Colab은 여기서 특별한 프로그래밍 언어가 아닙니다. 브라우저에서 Python을 실행하게 해 주는 도구입니다. 학생은 노트북 파일 형식 자체를 깊게 배울 필요가 없습니다. 대신 Colab에서 `lesson.py`를 실행하고, 출력이 왜 그렇게 나오는지 읽는 연습을 합니다.

## 2. 학생이 반드시 알아야 할 Colab 사용법

Colab에서 알아야 할 것은 많지 않습니다. 첫째, 코드 셀은 Python 코드를 실행합니다. 둘째, 위에서 아래로 실행해야 앞에서 만든 변수를 뒤에서 사용할 수 있습니다. 셋째, 런타임을 다시 시작하면 이전에 만들었던 변수는 사라집니다. 넷째, `.py` 파일도 Colab에서 실행할 수 있습니다.

예를 들어 Day 1 폴더에 있는 `lesson.py`는 Colab 코드 셀에서 다음처럼 실행할 수 있습니다.

```python
%run lesson.py
```

또는 셸 명령 방식으로 다음처럼 실행할 수 있습니다.

```python
!python lesson.py
```

두 방식 모두 Python 파일을 실행한다는 점은 같습니다. 이 수업에서는 Colab을 "코드를 돌려 보는 공간"으로만 사용하고, 실제 학습은 `.py` 코드의 흐름을 읽는 데 집중합니다.

## 3. 값이란 무엇인가

값은 Python이 계산해서 실제로 들고 있는 데이터입니다. 예를 들어 `3`, `3.14`, `"glucose"`, `True`는 모두 값입니다. 학생이 처음 헷갈리는 지점은 코드에 보이는 글자와 실행 후 Python이 들고 있는 값을 구분하지 못하는 데서 생깁니다.

```python
3 + 4
```

이 코드는 글자로는 `3 + 4`이지만, 실행 결과로는 `7`이라는 값을 만듭니다. Python은 코드를 읽고 계산한 뒤 값을 만듭니다. 앞으로 모든 데이터 분석 코드는 이 원리를 반복합니다. 입력값을 받고, 계산하고, 새로운 값을 만들고, 그 값을 변수나 자료구조에 저장합니다.

## 4. 표현식이란 무엇인가

표현식은 실행하면 하나의 값이 되는 코드 조각입니다. 아래 예시는 모두 표현식입니다.

```python
10
10 + 5
"patient" + "_001"
80 >= 70
```

각 표현식은 값으로 바뀝니다. `10 + 5`는 `15`가 되고, `"patient" + "_001"`은 `"patient_001"`이 되며, `80 >= 70`은 `True`가 됩니다. 코드 읽기 수업에서 중요한 질문은 "이 표현식은 어떤 값으로 바뀌는가"입니다.

## 5. 변수는 값을 담는 이름이다

변수는 상자가 아니라 이름표에 가깝습니다. `glucose = 96`이라고 쓰면 Python은 `96`이라는 값을 만들고, 그 값에 `glucose`라는 이름을 붙입니다. 이후 코드에서 `glucose`라고 쓰면 Python은 그 이름이 가리키는 값을 가져옵니다.

```python
glucose = 96
threshold = 100
is_high = glucose >= threshold
```

이 세 줄을 해석하면 다음과 같습니다. 첫째 줄은 `96`에 `glucose`라는 이름을 붙입니다. 둘째 줄은 `100`에 `threshold`라는 이름을 붙입니다. 셋째 줄은 `glucose >= threshold`를 계산해 `False`라는 값을 만들고, 그 값에 `is_high`라는 이름을 붙입니다.

학생은 코드를 직접 많이 쓰기 전에 이 해석을 말로 할 수 있어야 합니다.

## 6. 타입은 값의 종류다

타입은 값이 어떤 종류인지 알려줍니다. Python은 값의 타입에 따라 할 수 있는 연산을 다르게 판단합니다.

| 타입 | 예시 | 의미 |
| --- | --- | --- |
| `int` | `21` | 정수 |
| `float` | `36.5` | 소수점이 있는 수 |
| `str` | `"P001"` | 문자열 |
| `bool` | `True` | 참 또는 거짓 |
| `list` | `[91, 107, 86]` | 여러 값을 순서대로 담는 묶음 |
| `dict` | `{"patient_id": "P001"}` | 이름과 값을 짝지은 묶음 |

예를 들어 `91 + 10`은 숫자 덧셈이지만, `"91" + "10"`은 문자열 연결입니다. 둘 다 `+` 기호를 쓰지만 타입이 달라 결과가 다릅니다. 그래서 코드 해석에서 타입 확인은 선택 사항이 아닙니다.

## 7. 실행 순서가 중요한 이유

Python은 기본적으로 위에서 아래로 실행됩니다. 아래 코드는 정상입니다.

```python
score = 85
passed = score >= 70
```

하지만 아래 코드는 실패합니다.

```python
passed = score >= 70
score = 85
```

첫 줄을 실행하는 시점에는 아직 `score`라는 이름이 만들어지지 않았기 때문입니다. Colab에서 셀을 뒤섞어 실행할 때도 같은 문제가 생깁니다. 그래서 학생은 오류가 나면 먼저 "이 변수를 만드는 줄이 먼저 실행되었는가"를 확인해야 합니다.

## 8. 의료 데이터 예제를 읽는 방법

Day 1의 `lesson.py`는 실제 환자 데이터가 아니라 합성 데이터 네 건을 사용합니다. 목표는 분석 결과를 내는 것이 아니라 코드 읽는 순서를 익히는 것입니다. 다음 질문을 순서대로 던지면 됩니다.

1. `records`에는 몇 개의 행이 있는가?
2. 각 행은 어떤 타입인가?
3. `glucose_values`는 어디에서 만들어지는가?
4. `mean_glucose`는 어떤 값들을 사용해 계산되는가?
5. `is_high`는 숫자인가, 문자열인가, 참/거짓인가?
6. 마지막 출력은 어떤 의도로 만들어졌는가?

이 질문에 답할 수 있으면 학생은 이미 코드의 큰 흐름을 읽고 있는 것입니다.

## 9. 오늘의 핵심 문장

Python 코드는 위에서 아래로 실행되며, 각 줄은 값을 만들거나 이름을 붙이거나 기존 값을 이용해 새 값을 만듭니다. 코드 해석은 "값", "타입", "이름", "실행 순서"를 차례로 확인하는 작업입니다.

## 10. 수업 진행 방식

강사는 학생에게 처음부터 코드를 새로 짜게 하지 않습니다. 먼저 `lesson.py`를 열고 주석을 읽게 합니다. 그 다음 각 줄이 만드는 값을 예측하게 합니다. 마지막으로 Colab에서 파일을 실행해 예측과 출력이 맞는지 확인합니다. 학생이 수정해야 하는 부분은 마지막 10분에 기준값 하나를 바꿔 보는 정도로 제한합니다.
"""


def day1_code() -> str:
    return '''
"""
Day 01 lesson.py

이 파일은 "코드를 직접 많이 작성하는" 자료가 아니라
"이미 작성된 Python 코드를 읽고 해석하는" 자료입니다.

Colab에서는 같은 폴더에 이 파일을 둔 뒤 다음 중 하나로 실행합니다.

%run lesson.py
!python lesson.py
"""


# 1. records는 네 명의 가상 환자 행을 담은 list입니다.
#    실제 환자 정보가 아니라 수업용 합성 데이터입니다.
#    바깥쪽 []는 "여러 행을 순서대로 담는다"는 뜻입니다.
records = [
    {"patient_id": "P001", "age": 19, "glucose": 91, "group": "A"},
    {"patient_id": "P002", "age": 21, "glucose": 107, "group": "B"},
    {"patient_id": "P003", "age": 22, "glucose": 86, "group": "A"},
    {"patient_id": "P004", "age": 20, "glucose": 118, "group": "B"},
]


# 2. type은 값의 종류를 확인하는 함수입니다.
#    records 자체는 list이고, records 안의 첫 번째 행은 dict입니다.
print("records의 타입:", type(records).__name__)
print("첫 번째 행의 타입:", type(records[0]).__name__)
print("전체 행 개수:", len(records))


# 3. 아래 코드는 각 행에서 glucose 값만 꺼내 새 list를 만듭니다.
#    for row in records는 records 안의 dict를 하나씩 row라는 이름으로 꺼냅니다.
#    row["glucose"]는 한 행에서 glucose 열에 해당하는 값을 꺼냅니다.
glucose_values = [row["glucose"] for row in records]

print("glucose 값 목록:", glucose_values)
print("glucose_values의 타입:", type(glucose_values).__name__)


# 4. 평균은 "합계 / 개수"입니다.
#    sum(glucose_values)는 glucose 값들의 합계를 계산합니다.
#    len(glucose_values)는 glucose 값이 몇 개인지 계산합니다.
mean_glucose = sum(glucose_values) / len(glucose_values)

print("glucose 평균:", mean_glucose)
print("mean_glucose의 타입:", type(mean_glucose).__name__)


# 5. threshold는 기준값입니다.
#    기준값을 변수로 빼 두면, 나중에 100을 95나 110으로 바꿔 비교하기 쉽습니다.
threshold = 100


# 6. 각 환자의 glucose가 기준 이상인지 해석합니다.
#    row["glucose"] >= threshold는 True 또는 False를 만듭니다.
#    즉 is_high의 타입은 bool입니다.
for row in records:
    patient_id = row["patient_id"]
    glucose = row["glucose"]
    is_high = glucose >= threshold

    print(patient_id, "glucose:", glucose, "기준 이상인가?", is_high)


# 7. 마지막 summary는 수업에서 말로 설명할 최종 요약입니다.
#    dictionary는 이름과 값을 짝으로 묶어서 결과를 정리할 때 유용합니다.
summary = {
    "patient_count": len(records),
    "threshold": threshold,
    "mean_glucose": round(mean_glucose, 2),
    "high_count": sum(row["glucose"] >= threshold for row in records),
}

print("요약:", summary)


# 8. 읽기 과제:
#    아래 네 질문에 답할 수 있으면 Day 1 목표를 달성한 것입니다.
#    - records는 어떤 타입인가?
#    - records[0]은 어떤 타입인가?
#    - glucose_values는 어떤 과정을 거쳐 만들어졌는가?
#    - high_count는 어떤 기준으로 계산되었는가?
'''


def day_docs() -> None:
    for day, week, slug, title in DAYS:
        base = ROOT / "weeks" / WEEKS[week][0] / f"day{day:02d}_{slug}"
        if day == 1:
            write(base / "concept.md", day1_concept())
            write(base / "lesson.py", day1_code())
            continue
        write(base / "01_concepts" / "README.md", f"""# Day {day:02d}. {title}

## 1. 오늘의 위치

오늘은 `{title}`를 다룹니다. 이 주제는 {WEEKS[week][1]} 흐름 안에서 다음 단계의 코드를 읽기 위한 기반입니다.

## 2. 학습 목표

- 오늘 주제의 핵심 용어를 자신의 말로 설명합니다.
- 합성 의료 데이터 예제에서 입력, 처리, 출력을 구분합니다.
- 코드가 실패할 때 타입, 길이, 이름, 실행 순서를 기준으로 원인을 좁힙니다.

## 3. 선수지식 점검

수업 전에 변수, 리스트, 표 형태 데이터, 평균 계산 중 하나라도 낯설면 예제 노트북의 첫 셀부터 천천히 실행합니다.

## 4. 핵심 개념

핵심은 코드를 외우는 것이 아니라 값의 흐름을 추적하는 것입니다. 입력 데이터가 어떤 형태로 들어오고, 어떤 기준으로 걸러지며, 어떤 숫자나 문장으로 요약되는지 확인합니다.

## 5. 의료 데이터 맥락

실습 데이터는 모두 합성입니다. `patient_id`는 실제 환자가 아니라 행을 연결하기 위한 가짜 식별자입니다. 수업에서는 민감정보를 코드나 프롬프트에 넣지 않습니다.

## 6. 코드 읽기 순서

1. 데이터가 어디에서 만들어지는지 봅니다.
2. 각 변수의 타입과 길이를 확인합니다.
3. 조건문과 반복문이 어떤 행을 선택하는지 봅니다.
4. 출력값이 학습 목표와 맞는지 설명합니다.

## 7. 흔한 오류

셀 실행 순서를 건너뛰면 이름이 정의되지 않습니다. 숫자와 문자열을 섞으면 비교나 계산이 실패합니다. 리스트 길이가 다르면 표로 묶을 때 행이 어긋납니다.

## 8. 다음 학습과 연결

오늘의 작은 데이터 흐름 읽기는 pandas 표 처리, PyTorch tensor, Transformer attention까지 같은 방식으로 확장됩니다.
""")
        write(base / "02_examples" / "README.md", f"""# Day {day:02d} Examples

## 예제 목표

`{title}`를 작은 합성 데이터로 확인합니다. 예제는 정답을 외우기 위한 코드가 아니라, 각 줄이 어떤 값을 만드는지 관찰하기 위한 자료입니다.

## 실행 순서

1. `day{day:02d}_examples.ipynb`를 엽니다.
2. 첫 셀의 데이터 구조를 읽습니다.
3. 출력 dictionary에서 평균과 개수를 확인합니다.
4. 값을 하나 바꾸고 출력이 어떻게 달라지는지 비교합니다.
""")
        write(base / "03_practice" / "README.md", f"""# Day {day:02d} Practice

## 실습 원칙

학생용 노트북을 먼저 풀고, 해설은 토론 뒤 확인합니다. 모든 답은 코드 결과와 한 문장 설명을 함께 제출합니다.

## 문제 1

예제 데이터에서 각 행이 무엇을 의미하는지 표기합니다.

## 문제 2

평균 계산에 들어가는 값 목록을 직접 출력합니다.

## 문제 3

기준값을 하나 바꾸고 결과가 어떻게 달라지는지 설명합니다.

## 문제 4

오류가 날 수 있는 지점을 두 곳 찾고, 확인 방법을 적습니다.

## 문제 5

오늘 주제를 다음 주차의 데이터 분석 또는 모델 학습과 연결해 한 문단으로 정리합니다.
""")
        write(base / "04_quiz" / "README.md", f"""# Day {day:02d} Quiz

## 객관식

1. 코드 실행 순서를 확인해야 하는 가장 직접적인 이유는 무엇인가요?
   - A. 변수 정의와 출력이 셀 순서에 의존하기 때문
   - B. 글꼴 크기가 달라지기 때문
   - C. 파일명이 길어지기 때문
   - D. 링크 색이 바뀌기 때문

## 단답형

`{title}`에서 입력과 출력이 무엇인지 한 문장으로 적으세요.

## 코드 읽기

`high_count = sum(value >= 100 for value in glucose)`가 계산하는 값을 설명하세요.

## 디버깅

`NameError`가 발생했을 때 가장 먼저 확인할 두 가지를 적으세요.
""")
        answer = f"""# Day {day:02d} Answers

## 실습 해설

문제 1은 행 단위 관찰을 요구합니다. 문제 2는 계산 대상이 된 값 목록을 확인해야 합니다. 문제 3은 기준값 변화가 결과에 미치는 영향을 설명해야 합니다. 문제 4는 실행 순서와 타입 오류를 우선 점검합니다. 문제 5는 오늘 개념을 다음 데이터 처리 또는 모델 학습 단계와 연결하면 충분합니다.

## 퀴즈 정답

객관식 정답은 A입니다. 단답형은 입력 데이터, 처리 기준, 출력 요약을 모두 포함해야 합니다. 코드 읽기 문항은 기준 이상인 값을 True로 세어 개수를 구한다는 뜻입니다. 디버깅 문항은 셀 실행 여부와 변수 이름을 먼저 확인합니다.
"""
        write(base / "answers" / "practice_answers.md", answer)
        write(base / "answers" / "quiz_answers.md", answer)
        notebook(base / "02_examples" / f"day{day:02d}_examples.ipynb", f"Day {day:02d} Examples", title, "example")
        notebook(base / "03_practice" / f"day{day:02d}_practice_student.ipynb", f"Day {day:02d} Student Practice", title, "student")
        notebook(base / "answers" / f"day{day:02d}_practice_solution.ipynb", f"Day {day:02d} Solution", title, "solution")


def datasets() -> None:
    random.seed(7)
    rows = [{"patient_id": f"P{idx:03d}", "age": str(18 + idx % 6), "cohort": "A" if idx % 2 else "B", "baseline_score": str(70 + idx)} for idx in range(1, 13)]
    lab_rows = [{"patient_id": row["patient_id"], "glucose": str(82 + i * 3), "crp": f"{0.2 + i * 0.1:.1f}"} for i, row in enumerate(rows)]
    visit_rows = [{"patient_id": row["patient_id"], "visit_week": str((i % 4) + 1), "attendance": "present"} for i, row in enumerate(rows)]
    note_rows = [{"patient_id": row["patient_id"], "synthetic_note": "합성 증례 요약 문장입니다"} for row in rows]
    for name, data in {"synthetic_patients.csv": rows, "synthetic_labs.csv": lab_rows, "synthetic_visits.csv": visit_rows, "synthetic_notes.csv": note_rows}.items():
        path = ROOT / "datasets" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0]))
            writer.writeheader()
            writer.writerows(data)
    write(ROOT / "datasets" / "README.md", "# Datasets\n\n이 폴더의 CSV 파일은 모두 합성 데이터입니다. 파일 간 연결은 `patient_id`로 하며, 실제 개인을 식별할 수 있는 값은 포함하지 않습니다.\n")


def supporting_materials() -> None:
    write(ROOT / "assessments" / "final_project.md", "# Final Project\n\n합성 데이터로 질문을 만들고, 분석 또는 LLM 보조 요약을 수행한 뒤 한계와 윤리 기준을 설명합니다.\n")
    write(ROOT / "appendices" / "debugging_checklist.md", "# Debugging Checklist\n\n셀 실행 순서, 변수 이름, 타입, 길이, 파일 경로를 차례로 확인합니다.\n")
    write(ROOT / "instructor" / "rubric.md", "# Instructor Rubric\n\n설명 가능성, 재현 가능성, 개인정보 보호, 오류 점검 습관을 평가합니다.\n")


def validation_scripts() -> None:
    write(ROOT / "scripts" / "course_config.py", "WEEKS = " + repr({k: v[0] for k, v in WEEKS.items()}) + "\nDAYS = " + repr([(day, week, f"day{day:02d}_{slug}") for day, week, slug, _ in DAYS]) + "\n")
    write(ROOT / "scripts" / "validate_structure.py", '''
from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
standard_required = [
    "01_concepts/README.md",
    "02_examples/README.md",
    "03_practice/README.md",
    "04_quiz/README.md",
    "answers/practice_answers.md",
    "answers/quiz_answers.md",
]

for day, week, slug in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    required = ["concept.md", "lesson.py"] if day == 1 else standard_required
    for rel in required:
        if not (base / rel).exists():
            raise AssertionError(f"missing {base / rel}")

day1 = ROOT / "weeks" / WEEKS[1] / DAYS[0][2]
old_day1_dirs = ["01_concepts", "02_examples", "03_practice", "04_quiz", "answers"]
for name in old_day1_dirs:
    if (day1 / name).exists():
        raise AssertionError(f"Day 1 should not keep split subfolder: {day1 / name}")

notebooks = list((ROOT / "weeks").rglob("*.ipynb"))
if len(notebooks) != 81:
    raise AssertionError(f"expected 81 notebooks after Day 1 py conversion, found {len(notebooks)}")
print("validate_structure: OK")
''')
    write(ROOT / "scripts" / "validate_markdown_links.py", 'import re\nfrom pathlib import Path\nROOT = Path(__file__).resolve().parents[1]\nlink_re = re.compile(r"\\[[^\\]]+\\]\\(([^)]+)\\)")\nerrors = []\nfor md in ROOT.rglob("*.md"):\n    text = md.read_text(encoding="utf-8")\n    for target in link_re.findall(text):\n        if target.startswith(("http://", "https://", "mailto:", "#")):\n            continue\n        clean = target.split("#", 1)[0]\n        if clean and not (md.parent / clean).exists():\n            errors.append(f"{md.relative_to(ROOT)} -> {target}")\nif errors:\n    raise AssertionError("\\n".join(errors[:50]))\nprint("validate_markdown_links: OK")\n')
    write(ROOT / "scripts" / "check_required_sections.py", '''
from pathlib import Path
from course_config import DAYS, WEEKS

ROOT = Path(__file__).resolve().parents[1]
for day, week, slug in DAYS:
    base = ROOT / "weeks" / WEEKS[week] / slug
    if day == 1:
        checks = {
            "concept.md": ["## 1. 오늘 수업의 목적", "## 3. 값이란 무엇인가", "## 6. 타입은 값의 종류다", "## 10. 수업 진행 방식"],
            "lesson.py": ["# 1. records는", "# 3. 아래 코드는", "# 8. 읽기 과제"],
        }
    else:
        checks = {
            "01_concepts/README.md": ["## 1. 오늘의 위치", "## 2. 학습 목표", "## 4. 핵심 개념"],
            "02_examples/README.md": ["## 예제 목표", "## 실행 순서"],
            "03_practice/README.md": ["## 실습 원칙", "## 문제 1", "## 문제 5"],
            "04_quiz/README.md": ["## 객관식", "## 단답형", "## 코드 읽기", "## 디버깅"],
        }
    for rel, headings in checks.items():
        text = (base / rel).read_text(encoding="utf-8")
        for heading in headings:
            if heading not in text:
                raise AssertionError(f"missing {heading} in {base / rel}")
print("check_required_sections: OK")
''')
    write(ROOT / "scripts" / "validate_notebooks.py", 'import json\nfrom pathlib import Path\nROOT = Path(__file__).resolve().parents[1]\ncount = 0\nfor path in ROOT.rglob("*.ipynb"):\n    data = json.loads(path.read_text(encoding="utf-8"))\n    if data.get("nbformat") != 4 or not data.get("cells"):\n        raise AssertionError(f"invalid notebook: {path}")\n    joined = json.dumps(data, ensure_ascii=False)\n    for token in ["TODO", "placeholder", "추후 작성", "생략"]:\n        if token in joined:\n            raise AssertionError(f"banned token {token}: {path}")\n    if "practice_student" in path.name and "정답" in joined:\n        raise AssertionError(f"solution leak: {path}")\n    count += 1\nif count != 81:\n    raise AssertionError(f"expected 81 notebooks, found {count}")\nprint("validate_notebooks: OK")\n')
    write(ROOT / "scripts" / "execute_notebooks.py", 'import json\nfrom pathlib import Path\nROOT = Path(__file__).resolve().parents[1]\nexecuted = 0\nfor path in ROOT.rglob("*.ipynb"):\n    data = json.loads(path.read_text(encoding="utf-8"))\n    env = {"__name__": "__notebook__"}\n    for cell in data["cells"]:\n        if cell["cell_type"] == "code":\n            source = "".join(cell["source"])\n            exec(compile(source, str(path), "exec"), env)\n    executed += 1\nprint(f"execute_notebooks: OK ({executed} notebooks)")\n')
    write(ROOT / "scripts" / "validate_datasets.py", 'import csv\nfrom pathlib import Path\nROOT = Path(__file__).resolve().parents[1]\npatient_rows = list(csv.DictReader((ROOT / "datasets" / "synthetic_patients.csv").open(encoding="utf-8")))\npatient_ids = {row["patient_id"] for row in patient_rows}\nif len(patient_ids) != len(patient_rows):\n    raise AssertionError("duplicate patient_id")\nfor name in ["synthetic_labs.csv", "synthetic_visits.csv", "synthetic_notes.csv"]:\n    rows = list(csv.DictReader((ROOT / "datasets" / name).open(encoding="utf-8")))\n    if not rows:\n        raise AssertionError(f"empty dataset: {name}")\n    for row in rows:\n        if row["patient_id"] not in patient_ids:\n            raise AssertionError(f"orphan patient_id in {name}")\nprint("validate_datasets: OK")\n')


def tests() -> None:
    write(ROOT / "tests" / "test_course_contract.py", '''
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_readme_renders_as_markdown():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert text.startswith("# 서울대학교")
    assert "day01_colab_execution_values_and_types/concept.md" in text


def test_day1_is_two_file_lesson():
    day1 = ROOT / "weeks" / "week01_python_foundations" / "day01_colab_execution_values_and_types"
    assert (day1 / "concept.md").exists()
    assert (day1 / "lesson.py").exists()
    assert not (day1 / "01_concepts").exists()
    assert not (day1 / "answers").exists()


def test_remaining_days_keep_answer_materials():
    days = list((ROOT / "weeks").glob("week*/day*"))
    assert len(days) == 28
    for day in days:
        if day.name.startswith("day01_"):
            continue
        assert (day / "answers" / "practice_answers.md").exists()


def test_datasets_are_synthetic():
    text = (ROOT / "datasets" / "README.md").read_text(encoding="utf-8")
    assert "합성 데이터" in text
''')


def main() -> None:
    clean()
    root_docs()
    day_docs()
    datasets()
    supporting_materials()
    validation_scripts()
    tests()
    print("Course repository regenerated with teaching-ready materials.")


if __name__ == "__main__":
    main()
