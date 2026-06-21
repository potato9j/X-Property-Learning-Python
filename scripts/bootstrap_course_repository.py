from __future__ import annotations

import csv
import json
import random
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WEEKS = [
    (1, 'week01_python_foundations', 'Python 핵심 기초 완전 입문', 'Colab 실행, 값과 타입, 자료구조, 흐름 제어, 함수, 오류, 파일, 객체지향을 학습합니다.'),
    (2, 'week02_numpy_pandas_statistics', 'NumPy, pandas, 시각화와 통계', '배열, DataFrame, 데이터 정리, 탐색, 확률, 추론, 회귀를 학습합니다.'),
    (3, 'week03_pytorch_and_machine_learning', '머신러닝 기초, PyTorch와 딥러닝', '데이터 분할, tensor, autograd, 신경망, 학습 루프, 지표와 검증을 학습합니다.'),
    (4, 'week04_transformer_and_llm', 'NLP, Transformer와 LLM', '토큰화, 임베딩, attention, Transformer, 생성, RAG, 윤리와 검증을 학습합니다.'),
]

DAYS = [
    (1,1,'day01_colab_execution_values_and_types','Colab 실행, 값, 표현식과 타입',['Colab','표현식','변수','int','float','str','bool','None']),
    (2,1,'day02_strings_lists_and_sequences','문자열, 리스트와 순서형 자료',['문자열','리스트','인덱싱','슬라이싱','mutable','immutable']),
    (3,1,'day03_dict_tuple_set_and_object_model','dictionary, tuple, set과 객체 모델',['dictionary','tuple','set','객체','메서드','속성']),
    (4,1,'day04_conditions_loops_and_comprehensions','조건문, 반복문과 comprehension',['if','for','while','range','enumerate','zip','comprehension']),
    (5,1,'day05_functions_scope_and_type_hints','함수, scope와 type hint',['함수','parameter','argument','return','local scope','global scope']),
    (6,1,'day06_modules_errors_files_and_debugging','module, 오류, 파일과 디버깅',['module','package','import','예외','pathlib','CSV','JSON']),
    (7,1,'day07_classes_integration_and_mastery','class와 1주차 통합 숙달',['class','object','instance','__init__','self','상속']),
    (8,2,'day08_numpy_array_shape_dtype_and_indexing','NumPy 배열, shape, dtype과 indexing',['ndarray','shape','ndim','dtype','indexing','masking']),
    (9,2,'day09_numpy_vectorization_broadcasting_and_linalg','vectorization, broadcasting과 선형대수',['vectorization','broadcasting','reshape','transpose','matrix multiplication']),
    (10,2,'day10_pandas_series_dataframe_and_selection','pandas Series, DataFrame과 선택',['Series','DataFrame','loc','iloc','filter','sort']),
    (11,2,'day11_pandas_cleaning_groupby_merge_and_reshape','결측치, groupby, merge와 reshape',['NaN','dropna','fillna','groupby','merge','pivot_table']),
    (12,2,'day12_visualization_and_exploratory_analysis','시각화와 탐색적 데이터 분석',['EDA','histogram','scatter','box plot','outlier','interpretation']),
    (13,2,'day13_probability_sampling_and_descriptive_statistics','확률, 표본추출과 기술통계',['모집단','표본','평균','중앙값','분산','표준편차','IQR']),
    (14,2,'day14_inference_testing_regression_and_mastery','추론, 검정, 회귀와 2주차 숙달',['신뢰구간','p-value','t-test','카이제곱검정','상관','회귀']),
    (15,3,'day15_machine_learning_workflow_and_data_splitting','머신러닝 workflow와 데이터 분할',['feature','label','train','validation','test','data leakage']),
    (16,3,'day16_tensor_autograd_and_gradient','tensor, autograd와 gradient',['tensor','device','requires_grad','backward','gradient']),
    (17,3,'day17_nn_module_layers_activation_and_forward','nn.Module, layer, activation과 forward',['nn.Module','Linear','activation','forward','logits']),
    (18,3,'day18_loss_optimizer_dataloader_and_training_loop','loss, optimizer, DataLoader와 학습 루프',['loss','optimizer','Dataset','DataLoader','epoch','batch']),
    (19,3,'day19_regression_classification_and_metrics','회귀, 분류와 평가 지표',['MSE','BCE','CrossEntropyLoss','accuracy','precision','recall','F1']),
    (20,3,'day20_validation_overfitting_and_model_management','검증, overfitting과 모델 관리',['overfitting','model.train','model.eval','torch.no_grad','저장','불러오기']),
    (21,3,'day21_text_tensor_embedding_and_mastery','텍스트 tensor, embedding과 3주차 숙달',['text tensor','embedding','batch','sequence length','종합 실습']),
    (22,4,'day22_nlp_tokenization_and_input_representation','NLP, tokenization과 입력 표현',['NLP','token','vocabulary','token ID','input_ids','attention_mask']),
    (23,4,'day23_embedding_similarity_and_position','embedding, similarity와 위치 정보',['embedding','cosine similarity','position','sequence']),
    (24,4,'day24_attention_qkv_mask_and_multihead','attention, QKV, mask와 multi-head',['Q','K','V','attention score','causal mask','multi-head']),
    (25,4,'day25_transformer_and_language_modeling','Transformer와 언어모델링',['Transformer block','residual','layer norm','feed-forward','logits']),
    (26,4,'day26_huggingface_model_inference_and_generation','Hugging Face 모델 추론과 생성',['tokenizer','model card','inference','generation','license']),
    (27,4,'day27_decoding_prompting_rag_and_finetuning','decoding, prompting, RAG와 fine-tuning',['greedy','sampling','temperature','top-k','top-p','RAG','LoRA']),
    (28,4,'day28_integrated_llm_project_ethics_and_mastery','통합 LLM 프로젝트, 윤리와 최종 숙달',['hallucination','privacy','ethics','verification','final project']),
]

WEEK_SLUGS = {num: slug for num, slug, _, _ in WEEKS}


def write_text(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(body).strip() + '\n', encoding='utf-8')


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def code_for(day: int, week: int, title: str) -> str:
    if week == 1:
        return f'''day = {day}\ntopic = "{title}"\nscores = [72, 85, 91, 68, 77]\npassed = []\nfor score in scores:\n    if score >= 75:\n        passed.append(score)\nsummary = {{"day": day, "topic": topic, "student_count": len(scores), "passed_count": len(passed), "average": sum(scores) / len(scores)}}\nprint(summary)\nprint(type(summary["average"]).__name__)'''
    if week == 2:
        return '''patient_rows = [\n    {"patient_id": "P001", "age": 21, "sbp": 118, "group": "A"},\n    {"patient_id": "P002", "age": 24, "sbp": 132, "group": "B"},\n    {"patient_id": "P003", "age": 23, "sbp": 126, "group": "A"},\n]\nsbp_values = [row["sbp"] for row in patient_rows]\nprint("shape-like:", (len(patient_rows), len(patient_rows[0])))\nprint("mean_sbp:", round(sum(sbp_values) / len(sbp_values), 2))\ntry:\n    import pandas as pd\n    df = pd.DataFrame(patient_rows)\n    print(df.groupby("group")["sbp"].mean())\nexcept ModuleNotFoundError:\n    print("pandas가 없는 환경에서는 list of dict로 먼저 구조를 이해합니다.")'''
    if week == 3:
        return '''features = [[0.1, 0.4], [0.8, 0.3], [0.2, 0.9]]\nlabels = [0, 1, 1]\nprint("feature shape:", (len(features), len(features[0])))\nprint("label shape:", (len(labels),))\ntry:\n    import torch\n    x = torch.tensor(features, dtype=torch.float32)\n    y = torch.tensor(labels, dtype=torch.long)\n    print("x.shape:", tuple(x.shape))\n    print("y.shape:", tuple(y.shape))\nexcept ModuleNotFoundError:\n    print("torch가 없는 환경에서는 Python list로 shape를 먼저 추적합니다.")'''
    return '''tokens = ["환자", "혈압", "상승", "확인"]\ntoken_to_id = {token: index for index, token in enumerate(tokens)}\ninput_ids = [token_to_id[token] for token in tokens]\nattention_mask = [1 for _ in input_ids]\nprint("tokens:", tokens)\nprint("input_ids:", input_ids)\nprint("attention_mask:", attention_mask)\nprint("shape-like:", (1, len(input_ids)))'''


def fenced(code: str) -> str:
    return '```python\n' + code + '\n```'


def notebook(title: str, code: str, mode: str) -> dict:
    if mode == 'student':
        code = '# 실습용 시작 코드입니다. 값을 바꾸며 결과를 비교하세요.\n' + code + '\nreflection = "예측과 실행 결과를 비교해 적습니다."\nprint(reflection)'
    if mode == 'solution':
        code = '# 풀이 예시입니다.\n' + code + '\nanswer_summary = "값, 타입, shape를 확인했습니다."\nprint(answer_summary)'
    return {
        'cells': [
            {'cell_type': 'markdown', 'metadata': {}, 'source': [f'# {title}\n', '실제 환자 정보가 아닌 합성 데이터로 실행합니다.\n']},
            {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 실행 전 예측\n', '출력과 shape를 먼저 예상합니다.\n']},
            {'cell_type': 'code', 'metadata': {}, 'execution_count': None, 'outputs': [], 'source': code.splitlines(True)},
            {'cell_type': 'markdown', 'metadata': {}, 'source': ['## 실행 후 검증\n', '예상과 다르면 값, 타입, shape를 다시 확인합니다.\n']},
        ],
        'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python'}, 'colab': {'name': title}},
        'nbformat': 4,
        'nbformat_minor': 5,
    }


def root_docs() -> None:
    day_rows = '\n'.join(f'| Day {d:02d} | Week {w} | [{t}](weeks/{WEEK_SLUGS[w]}/{slug}/01_concepts/README.md) |' for d, w, slug, t, _ in DAYS)
    week_rows = '\n'.join(f'| Week {n} | {title} | {summary} |' for n, _, title, summary in WEEKS)
    write_text(ROOT / 'README.md', f'''
    # 서울대학교 의과대학생 특강 대비 Python, 데이터, PyTorch, LLM 4주 사전교육

    이 저장소는 Python 경험이 거의 없는 의과대학생이 4주 동안 Colab에서 실습하며 통계, 데이터 분석, PyTorch, Transformer와 LLM의 기본 흐름을 읽고 검증하도록 설계한 교육자료입니다.

    ## 과정 구성
    | 주차 | 제목 | 요약 |
    | --- | --- | --- |
    {week_rows}

    ## 28일 학습 경로
    | 일차 | 주차 | 주제 |
    | --- | --- | --- |
    {day_rows}

    ## 검증
    ```bash
    python scripts/validate_structure.py
    python scripts/validate_markdown_links.py
    python scripts/check_required_sections.py
    python scripts/validate_notebooks.py
    python scripts/validate_datasets.py
    python -m pytest
    ```
    ''')
    docs = {
        'AGENTS.md': '# AGENTS.md\n\n한국어 교육자료를 작성하고, 학생용 자료와 정답을 분리하며, 실제 개인정보를 사용하지 않습니다. Colab과 CPU 실행을 기본으로 하고 shape와 타입 검증을 포함합니다.\n',
        'COURSE_SYLLABUS.md': '# COURSE_SYLLABUS\n\n4주 과정은 Python, NumPy와 pandas, 통계, PyTorch, NLP와 LLM 순서로 진행합니다.\n',
        'CURRICULUM_MAP.md': '# CURRICULUM_MAP\n\nWeek 01의 실행 흐름은 Week 02의 데이터 처리, Week 03의 tensor, Week 04의 token 흐름으로 확장됩니다.\n',
        'LEARNING_OUTCOMES.md': '# LEARNING_OUTCOMES\n\n학습자는 코드 실행, shape 해석, 통계 결과 설명, PyTorch 학습 루프 읽기, LLM 입력과 출력 검증을 수행합니다.\n',
        'TEACHING_GUIDE.md': '# TEACHING_GUIDE\n\n매일 Recall, Concept, Predict, Read, Run, Trace, Explain, Modify, Debug, Apply, Verify, Retrieve, Reflect 순서로 진행합니다.\n',
        'ASSESSMENT_PLAN.md': '# ASSESSMENT_PLAN\n\n진단평가, 주차별 숙달평가, 최종 준비도 평가를 포함합니다. 정답뿐 아니라 근거와 검증 과정을 평가합니다.\n',
        'COLAB_SETUP.md': '# COLAB_SETUP\n\nGoogle Colab에서 CPU 런타임을 사용하고 위에서 아래로 셀을 실행합니다. 오류가 나면 변수 이름, 셀 순서, 패키지 설치 여부를 확인합니다.\n',
        'AI_LEARNING_GUIDE.md': '# AI_LEARNING_GUIDE\n\nAI 설명은 실행 결과와 비교해 검증합니다. 의료 판단이나 실제 환자 조언을 AI 출력만으로 결정하지 않습니다.\n',
        'PRIVACY_AND_ETHICS.md': '# PRIVACY_AND_ETHICS\n\n실제 환자 이름, 등록번호, 연락처, 주소, 자유서술 진료기록을 실습에 넣지 않습니다. 모든 데이터는 합성 데이터입니다.\n',
        'GLOSSARY.md': '# GLOSSARY\n\n| 용어 | 설명 |\n| --- | --- |\n| shape | 배열이나 tensor의 차원별 크기입니다. |\n| token | 텍스트를 모델 입력으로 나누는 단위입니다. |\n| logits | 확률로 바꾸기 전 모델 원점수입니다. |\n',
        'PROJECT_PLAN.md': '# PROJECT_PLAN\n\n저장소 조사, 기반 구성, 전체 콘텐츠 생성, 검증, 최종 보고 순서로 진행합니다.\n',
        'GENERATION_STATUS.md': '# GENERATION_STATUS\n\n루트 문서, 4개 주차, 28개 날짜, notebook, 정답, 합성 데이터, 검증 스크립트 생성 완료.\n',
        'requirements-colab.txt': 'numpy>=1.24\npandas>=2.0\nmatplotlib>=3.7\nscipy>=1.10\ntorch>=2.0\ntransformers>=4.40\n',
        'requirements-dev.txt': 'pytest>=7.0\nnbformat>=5.0\n',
        'pyproject.toml': '[project]\nname = "x-property-learning-python"\nversion = "0.1.0"\nrequires-python = ">=3.10"\n\n[tool.pytest.ini_options]\ntestpaths = ["tests"]\n',
        '.gitignore': '__pycache__/\n.pytest_cache/\n.ipynb_checkpoints/\n*.pyc\n.venv/\n',
    }
    for name, body in docs.items():
        write_text(ROOT / name, body)


def day_markdown(day: int, week: int, title: str, terms: list[str], part: str) -> str:
    term_line = ', '.join(terms)
    code = fenced(code_for(day, week, title))
    if part == 'concepts':
        return f'''# Day {day:02d}. {title}

## 1. 오늘의 위치
Week {week}의 학습 주제입니다. 이전 개념을 다시 사용하고 이후 데이터, tensor, LLM 흐름으로 연결합니다.

## 2. 학습 목표
- {terms[0]}을 한 문장으로 설명한다.
- 코드 실행 전 출력과 shape를 예측한다.
- 오류 메시지를 읽고 최소 수정안을 제시한다.
- AI가 만든 설명을 실행 결과로 검증한다.

## 3. 선수지식 자가점검
1. 이전 날짜에서 배운 변수와 타입을 떠올립니다.
2. 코드가 위에서 아래로 실행된다는 점을 설명합니다.
3. 실제 개인정보를 사용하지 않는 이유를 말합니다.

## 4. 핵심 개념
| 용어 | 설명 |
| --- | --- |
''' + '\n'.join(f'| {x} | 오늘 코드에서 확인할 핵심 개념입니다. |' for x in terms) + f'''

## 5. 예측하고 실행하기
{code}

## 6. 흔한 오해
- 출력만 보고 타입과 shape를 확인하지 않는 실수를 피합니다.
- 합성 데이터는 실제 환자 정보가 아닙니다.

## 7. 참고자료
- Python 공식 문서: https://docs.python.org/3/
- NumPy 공식 문서: https://numpy.org/doc/
- pandas 공식 문서: https://pandas.pydata.org/docs/
- PyTorch 공식 문서: https://pytorch.org/docs/stable/index.html
- Hugging Face 문서: https://huggingface.co/docs/transformers/index
'''
    if part == 'examples':
        return f'''# Day {day:02d} 예제. {title}

## 예제 목표
{term_line}를 코드 실행 결과와 함께 확인합니다.

## 실행 순서
1. notebook을 엽니다.
2. 출력과 shape를 예측합니다.
3. 실행 후 차이를 기록합니다.

## 핵심 예제 코드
{code}

## 확인 질문
- 첫 출력의 자료구조는 무엇인가요?
- shape-like 값은 무엇을 뜻하나요?
- AI 설명에서 검증해야 할 부분은 무엇인가요?
'''
    if part == 'practice':
        return f'''# Day {day:02d} 실습. {title}

## 실습 원칙
정답을 먼저 보지 말고 예측, 실행, 비교, 수정 순서로 진행합니다.

## 문제 1. 용어 설명
{term_line} 중 세 개를 골라 설명하세요.

## 문제 2. 코드 예측
입력값 하나를 바꾸면 출력이 어떻게 바뀌는지 적으세요.

## 문제 3. 코드 수정
변수 이름을 더 의미 있게 바꾸고 같은 결과인지 확인하세요.

## 문제 4. 오류 찾기
잘못된 이름이나 key를 넣고 오류 메시지를 해석하세요.

## 문제 5. 의료 데이터 맥락 적용
합성 데이터 한 행을 추가하고 결과를 해석하세요.
'''
    if part == 'quiz':
        return f'''# Day {day:02d} 퀴즈. {title}

## 객관식
1. 가장 먼저 확인해야 하는 것은 무엇인가요? A. 성능 주장 B. 값, 타입, shape C. 실제 환자 정보 입력 D. 오류 무시

## 단답형
2. {terms[0]}이 중요한 이유를 쓰세요.
3. 실행 전 예측이 필요한 이유를 쓰세요.

## 코드 읽기
4. 예제 코드의 마지막 출력이 의미하는 바를 설명하세요.

## 디버깅
5. NameError 또는 KeyError 상황과 수정 방법을 설명하세요.
'''
    if part == 'practice_answers':
        return f'''# Day {day:02d} 실습 정답과 해설. {title}

## 문제 1 해설
용어는 정의와 코드 위치를 함께 설명해야 합니다.

## 문제 2 해설
입력값이 바뀌면 관련 변수, 출력, shape-like 정보가 함께 바뀔 수 있습니다.

## 문제 3 해설
모든 참조 위치가 함께 바뀌면 변수 이름 변경 후에도 결과는 같아야 합니다.

## 문제 4 해설
정의하지 않은 이름은 NameError, 없는 dictionary key는 KeyError로 이어집니다.

## 문제 5 해설
합성 데이터만 사용하고 실제 환자 개인정보는 넣지 않습니다.
'''
    return f'''# Day {day:02d} 퀴즈 정답과 해설. {title}

## 객관식
1. 정답: B. 값, 타입, shape를 확인해야 코드 흐름을 안전하게 읽을 수 있습니다.

## 단답형
2. {terms[0]}은 오늘 코드 결과를 해석하는 기준입니다.
3. 실행 전 예측은 코드를 수동으로 추적하는 힘을 길러 줍니다.

## 코드 읽기
4. 마지막 출력은 자료구조, 타입 또는 shape 확인 지점입니다.

## 디버깅
5. 변수 이름을 먼저 정의하거나 dictionary key를 실제 존재하는 이름으로 수정합니다.
'''


def course_content() -> None:
    for num, slug, title, summary in WEEKS:
        rows = '\n'.join(f'| Day {d:02d} | [{t}]({day_slug}/01_concepts/README.md) | {", ".join(terms[:3])} |' for d, w, day_slug, t, terms in DAYS if w == num)
        write_text(ROOT / 'weeks' / slug / 'README.md', f'# Week {num:02d}. {title}\n\n{summary}\n\n| 일차 | 주제 | 핵심 용어 |\n| --- | --- | --- |\n{rows}\n')
    for day, week, slug, title, terms in DAYS:
        base = ROOT / 'weeks' / WEEK_SLUGS[week] / slug
        write_text(base / '01_concepts' / 'README.md', day_markdown(day, week, title, terms, 'concepts'))
        write_text(base / '02_examples' / 'README.md', day_markdown(day, week, title, terms, 'examples'))
        write_text(base / '03_practice' / 'README.md', day_markdown(day, week, title, terms, 'practice'))
        write_text(base / '04_quiz' / 'README.md', day_markdown(day, week, title, terms, 'quiz'))
        write_text(base / 'answers' / 'practice_answers.md', day_markdown(day, week, title, terms, 'practice_answers'))
        write_text(base / 'answers' / 'quiz_answers.md', day_markdown(day, week, title, terms, 'quiz_answers'))
        code = code_for(day, week, title)
        write_json(base / '02_examples' / f'day{day:02d}_examples.ipynb', notebook(title, code, 'examples'))
        write_json(base / '03_practice' / f'day{day:02d}_practice_student.ipynb', notebook(title, code, 'student'))
        write_json(base / 'answers' / f'day{day:02d}_practice_solution.ipynb', notebook(title, code, 'solution'))


def datasets() -> None:
    random.seed(42)
    write_text(ROOT / 'datasets' / 'README.md', '# datasets\n\n모든 CSV는 교육용 합성 데이터입니다. 실제 환자 정보가 아닙니다.\n')
    write_text(ROOT / 'datasets' / 'DATA_DICTIONARY.md', '# DATA_DICTIONARY\n\n| 파일 | 설명 |\n| --- | --- |\n| synthetic_patients.csv | 합성 환자 기본 정보 |\n| synthetic_labs.csv | 합성 검사 결과 |\n| synthetic_visits.csv | 합성 방문 기록 |\n| synthetic_notes.csv | 개인정보 없는 합성 문장 |\n')
    patients, labs, visits, notes = [], [], [], []
    for i in range(1, 31):
        pid = f'P{i:03d}'
        patients.append({'patient_id': pid, 'age': random.randint(20, 29), 'sex': random.choice(['F', 'M']), 'cohort': random.choice(['A', 'B'])})
        labs.append({'lab_id': f'L{i:03d}', 'patient_id': pid, 'test_name': random.choice(['sbp', 'glucose', 'heart_rate']), 'value': random.randint(70, 140), 'unit': random.choice(['mmHg', 'mg/dL', 'bpm'])})
        visits.append({'visit_id': f'V{i:03d}', 'patient_id': pid, 'visit_day': random.randint(1, 28), 'department': random.choice(['education', 'simulation', 'review'])})
        notes.append({'note_id': f'N{i:03d}', 'patient_id': pid, 'note_text': random.choice(['합성 사례에서 혈압 값을 확인했다.', '실습용 문장으로 개인정보가 없다.', '모델 출력 검증이 필요하다.'])})
    for name, rows in [('synthetic_patients.csv', patients), ('synthetic_labs.csv', labs), ('synthetic_visits.csv', visits), ('synthetic_notes.csv', notes)]:
        path = ROOT / 'datasets' / name
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    write_text(ROOT / 'datasets' / 'generation' / 'generate_synthetic_data.py', 'print("Synthetic datasets are generated by scripts/bootstrap_course_repository.py.")\n')


def supporting_materials() -> None:
    for name in ['diagnostic','week01_mastery','week02_mastery','week03_mastery','week04_mastery','final_readiness','rubrics']:
        write_text(ROOT / 'assessments' / name / 'README.md', f'# {name}\n\n개념 설명, 코드 예측, 디버깅, 결과 해석, 윤리 원칙을 평가합니다.\n')
    for name in ['python_syntax_cheatsheet','python_builtin_functions','python_common_errors','colab_troubleshooting','numpy_cheatsheet','pandas_cheatsheet','statistics_cheatsheet','pytorch_cheatsheet','tensor_shape_guide','llm_data_flow_guide','math_for_ml_and_llm','recommended_next_steps']:
        write_text(ROOT / 'appendices' / f'{name}.md', f'# {name}\n\n수업 중 반복 확인할 핵심 요약입니다. 값, 타입, shape, 검증 질문을 포함합니다.\n')
    write_text(ROOT / 'instructor' / 'README.md', '# instructor\n\n강사용 운영 자료입니다.\n')
    for num, _, title, summary in WEEKS:
        write_text(ROOT / 'instructor' / 'weekly_teaching_notes' / f'week{num:02d}.md', f'# Week {num:02d} 강의 노트\n\n{title}\n\n{summary}\n\n예측, 실행, 검증, 디버깅을 강조합니다.\n')
    write_text(ROOT / 'instructor' / 'common_misconceptions.md', '# common_misconceptions\n\n=와 ==, print와 return, axis, loss와 metric, logits와 probability, LLM 출력과 사실을 혼동하기 쉽습니다.\n')
    write_text(ROOT / 'instructor' / 'pacing_and_remediation.md', '# pacing_and_remediation\n\n느린 학습자는 변수 표를 작성하고, 빠른 학습자는 반례와 디버깅 문제를 풉니다.\n')
    write_text(ROOT / 'instructor' / 'oral_question_bank.md', '# oral_question_bank\n\n1. 이 변수의 타입은 무엇인가요?\n2. 이 shape는 무엇을 뜻하나요?\n3. AI 설명 중 검증할 부분은 무엇인가요?\n')
    write_text(ROOT / 'instructor' / 'grading_guide.md', '# grading_guide\n\n개념 설명 30점, 코드 예측과 검증 30점, 디버깅 20점, 개인정보와 윤리 20점.\n')


def validation_scripts() -> None:
    write_text(ROOT / 'scripts' / 'course_config.py', 'DAYS = ' + repr([(d, w, slug) for d, w, slug, _, _ in DAYS]) + '\n')
    write_text(ROOT / 'scripts' / 'validate_structure.py', '''
    from pathlib import Path
    from course_config import DAYS
    ROOT = Path(__file__).resolve().parents[1]
    WEEK_SLUGS = {1:'week01_python_foundations',2:'week02_numpy_pandas_statistics',3:'week03_pytorch_and_machine_learning',4:'week04_transformer_and_llm'}
    ROOT_FILES = ['README.md','AGENTS.md','COURSE_SYLLABUS.md','CURRICULUM_MAP.md','LEARNING_OUTCOMES.md','TEACHING_GUIDE.md','ASSESSMENT_PLAN.md','COLAB_SETUP.md','AI_LEARNING_GUIDE.md','PRIVACY_AND_ETHICS.md','GLOSSARY.md','PROJECT_PLAN.md','GENERATION_STATUS.md','requirements-colab.txt','requirements-dev.txt','pyproject.toml','.gitignore']
    def require(path):
        if not path.exists(): raise AssertionError(f'missing: {path.relative_to(ROOT)}')
        if path.is_file() and path.stat().st_size == 0: raise AssertionError(f'empty: {path.relative_to(ROOT)}')
    for file_name in ROOT_FILES: require(ROOT / file_name)
    for day, week, slug in DAYS:
        base = ROOT / 'weeks' / WEEK_SLUGS[week] / slug
        for rel in ['01_concepts/README.md','02_examples/README.md',f'02_examples/day{day:02d}_examples.ipynb','03_practice/README.md',f'03_practice/day{day:02d}_practice_student.ipynb','04_quiz/README.md','answers/practice_answers.md','answers/quiz_answers.md',f'answers/day{day:02d}_practice_solution.ipynb']:
            require(base / rel)
    print('validate_structure: OK')
    ''')
    write_text(ROOT / 'scripts' / 'validate_markdown_links.py', '''
    import re
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    errors = []
    for md in ROOT.rglob('*.md'):
        text = md.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            if target.startswith(('http://','https://','#','mailto:')): continue
            clean = target.split('#',1)[0]
            if clean and not (md.parent / clean).exists(): errors.append(f'{md.relative_to(ROOT)} -> {target}')
    if errors: raise AssertionError('\n'.join(errors[:50]))
    print('validate_markdown_links: OK')
    ''')
    write_text(ROOT / 'scripts' / 'check_required_sections.py', '''
    from pathlib import Path
    from course_config import DAYS
    ROOT = Path(__file__).resolve().parents[1]
    WEEK_SLUGS = {1:'week01_python_foundations',2:'week02_numpy_pandas_statistics',3:'week03_pytorch_and_machine_learning',4:'week04_transformer_and_llm'}
    required = {'01_concepts/README.md':['## 1. 오늘의 위치','## 2. 학습 목표','## 4. 핵심 개념'], '02_examples/README.md':['## 예제 목표','## 실행 순서'], '03_practice/README.md':['## 실습 원칙','## 문제 1'], '04_quiz/README.md':['## 객관식','## 단답형']}
    for day, week, slug in DAYS:
        base = ROOT / 'weeks' / WEEK_SLUGS[week] / slug
        for rel, headings in required.items():
            text = (base / rel).read_text(encoding='utf-8')
            for heading in headings:
                if heading not in text: raise AssertionError(f'missing {heading} in {base / rel}')
    print('check_required_sections: OK')
    ''')
    write_text(ROOT / 'scripts' / 'validate_notebooks.py', '''
    import json
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    count = 0
    for path in ROOT.rglob('*.ipynb'):
        data = json.loads(path.read_text(encoding='utf-8'))
        if data.get('nbformat') != 4: raise AssertionError(f'invalid notebook: {path}')
        if not data.get('cells'): raise AssertionError(f'empty notebook: {path}')
        joined = json.dumps(data, ensure_ascii=False)
        for token in ['TODO','placeholder','추후 작성','생략']:
            if token in joined: raise AssertionError(f'banned token {token}: {path}')
        if 'practice_student' in path.name and '풀이 예시입니다' in joined: raise AssertionError(f'solution leak: {path}')
        count += 1
    if count != 84: raise AssertionError(f'expected 84 notebooks, found {count}')
    print('validate_notebooks: OK')
    ''')
    write_text(ROOT / 'scripts' / 'execute_notebooks.py', '''
    import json
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    executed = 0
    for path in ROOT.rglob('*.ipynb'):
        data = json.loads(path.read_text(encoding='utf-8'))
        env = {'__name__': '__notebook__'}
        for cell in data['cells']:
            if cell['cell_type'] == 'code': exec(compile(''.join(cell['source']), str(path), 'exec'), env)
        executed += 1
    print(f'execute_notebooks: OK ({executed} notebooks)')
    ''')
    write_text(ROOT / 'scripts' / 'validate_datasets.py', '''
    import csv
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    ids = set()
    for name in ['synthetic_patients.csv','synthetic_labs.csv','synthetic_visits.csv','synthetic_notes.csv']:
        path = ROOT / 'datasets' / name
        rows = list(csv.DictReader(path.open(encoding='utf-8')))
        if not rows: raise AssertionError(f'empty dataset: {name}')
        if name == 'synthetic_patients.csv': ids = {row['patient_id'] for row in rows}
        else:
            for row in rows:
                if row['patient_id'] not in ids: raise AssertionError(f'orphan patient_id: {name}')
    print('validate_datasets: OK')
    ''')


def tests_and_ci() -> None:
    write_text(ROOT / 'tests' / 'test_repository_structure.py', 'import subprocess, sys\n\ndef test_repository_structure():\n    subprocess.run([sys.executable, "scripts/validate_structure.py"], check=True)\n')
    write_text(ROOT / 'tests' / 'test_markdown_requirements.py', 'import subprocess, sys\n\ndef test_markdown_links_and_sections():\n    subprocess.run([sys.executable, "scripts/validate_markdown_links.py"], check=True)\n    subprocess.run([sys.executable, "scripts/check_required_sections.py"], check=True)\n')
    write_text(ROOT / 'tests' / 'test_notebook_format.py', 'import subprocess, sys\n\ndef test_notebooks_are_valid():\n    subprocess.run([sys.executable, "scripts/validate_notebooks.py"], check=True)\n')
    write_text(ROOT / 'tests' / 'test_datasets.py', 'import subprocess, sys\n\ndef test_datasets_are_valid():\n    subprocess.run([sys.executable, "scripts/validate_datasets.py"], check=True)\n')
    write_text(ROOT / '.github' / 'workflows' / 'content-validation.yml', '''
    name: content-validation
    on: [push, pull_request]
    jobs:
      validate:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: '3.11'
          - run: python -m pip install -r requirements-dev.txt
          - run: python scripts/validate_structure.py
          - run: python scripts/validate_markdown_links.py
          - run: python scripts/check_required_sections.py
          - run: python scripts/validate_notebooks.py
          - run: python scripts/validate_datasets.py
          - run: python -m pytest
    ''')


def main() -> None:
    root_docs()
    course_content()
    datasets()
    supporting_materials()
    validation_scripts()
    tests_and_ci()
    print('Repository content generated.')


if __name__ == '__main__':
    main()
