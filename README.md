# 서울대학교 의과대학생 특강 대비 Python, 데이터, PyTorch, LLM 4주 사전교육

이 저장소는 Python 경험이 거의 없는 의과대학생을 위한 4주 사전교육 교재이다. Colab은 실행 도구로만 사용하고, 핵심은 Python 코드와 데이터 흐름을 읽고 해석하는 능력을 기르는 것이다.

## 자료 구조

각 일차 폴더에는 두 파일만 둡니다.

```text
concept.md  # 개념 설명
lesson.py   # 주석을 따라 읽고 실행하는 Python 코드
```

불필요한 다중 md 파일, 학생용/해설용 노트북 분리, 반복되는 퀴즈 폴더는 제거했습니다. 학생이 무엇을 읽고 무엇을 실행해야 하는지 헷갈리지 않게 하는 것이 우선이다.

## 학습 경로

| 주차 | 일차 | 개념 파일 |
| --- | --- | --- |
| Week 1 | Day 01 | [Colab 실행, 값, 표현식과 타입](weeks/week01_python_foundations/day01_colab_execution_values_and_types/concept.md) |
| Week 1 | Day 02 | [문자열, 리스트와 순서형 자료](weeks/week01_python_foundations/day02_strings_lists_and_structured_data/concept.md) |
| Week 1 | Day 03 | [dictionary, tuple, set과 객체 모델](weeks/week01_python_foundations/day03_dict_tuple_set_and_object_model/concept.md) |
| Week 1 | Day 04 | [조건문, 반복문과 comprehension](weeks/week01_python_foundations/day04_conditions_loops_and_comprehension/concept.md) |
| Week 1 | Day 05 | [함수, scope와 type hint](weeks/week01_python_foundations/day05_functions_scope_and_type_hints/concept.md) |
| Week 1 | Day 06 | [module, 오류, 파일과 디버깅](weeks/week01_python_foundations/day06_modules_errors_files_and_debugging/concept.md) |
| Week 1 | Day 07 | [1주차 통합 숙달](weeks/week01_python_foundations/day07_week1_integrated_review/concept.md) |
| Week 2 | Day 08 | [NumPy 배열, shape, dtype과 indexing](weeks/week02_numpy_pandas_statistics/day08_numpy_arrays_shape_dtype_indexing/concept.md) |
| Week 2 | Day 09 | [vectorization, broadcasting과 선형대수](weeks/week02_numpy_pandas_statistics/day09_vectorization_broadcasting_linear_algebra/concept.md) |
| Week 2 | Day 10 | [pandas Series, DataFrame과 선택](weeks/week02_numpy_pandas_statistics/day10_pandas_series_dataframe_selection/concept.md) |
| Week 2 | Day 11 | [결측치, groupby, merge와 reshape](weeks/week02_numpy_pandas_statistics/day11_data_cleaning_groupby_merge_pivot/concept.md) |
| Week 2 | Day 12 | [시각화와 탐색적 데이터 분석](weeks/week02_numpy_pandas_statistics/day12_visualization_exploratory_data_analysis/concept.md) |
| Week 2 | Day 13 | [확률, 표본추출과 기술통계](weeks/week02_numpy_pandas_statistics/day13_probability_distribution_sampling_statistics/concept.md) |
| Week 2 | Day 14 | [추론, 검정, 회귀와 2주차 숙달](weeks/week02_numpy_pandas_statistics/day14_inference_testing_regression_review/concept.md) |
| Week 3 | Day 15 | [머신러닝 workflow와 데이터 분할](weeks/week03_pytorch_and_machine_learning/day15_machine_learning_workflow_split_baseline/concept.md) |
| Week 3 | Day 16 | [tensor, autograd와 gradient](weeks/week03_pytorch_and_machine_learning/day16_tensor_autograd_gradient/concept.md) |
| Week 3 | Day 17 | [nn.Module, layer, activation과 forward](weeks/week03_pytorch_and_machine_learning/day17_nn_module_layer_activation_forward/concept.md) |
| Week 3 | Day 18 | [loss, optimizer와 학습 루프](weeks/week03_pytorch_and_machine_learning/day18_loss_optimizer_training_loop/concept.md) |
| Week 3 | Day 19 | [DataLoader와 학습 루프 평가 지표](weeks/week03_pytorch_and_machine_learning/day19_data_loader_evaluation_metrics/concept.md) |
| Week 3 | Day 20 | [검증, overfitting과 모델 관리](weeks/week03_pytorch_and_machine_learning/day20_regularization_overfitting_model_management/concept.md) |
| Week 3 | Day 21 | [텍스트 tensor, embedding과 3주차 숙달](weeks/week03_pytorch_and_machine_learning/day21_text_tensor_embedding_review/concept.md) |
| Week 4 | Day 22 | [NLP, tokenization과 어휘 표현](weeks/week04_transformer_and_llm/day22_nlp_tokenization_vocabulary_representation/concept.md) |
| Week 4 | Day 23 | [embedding, similarity와 위치 정보](weeks/week04_transformer_and_llm/day23_embedding_similarity_retrieval/concept.md) |
| Week 4 | Day 24 | [attention, QKV, mask와 multi-head](weeks/week04_transformer_and_llm/day24_attention_qkv_mask_multihead/concept.md) |
| Week 4 | Day 25 | [Transformer와 언어모델링](weeks/week04_transformer_and_llm/day25_transformer_decoder_language_modeling/concept.md) |
| Week 4 | Day 26 | [Hugging Face 모델 추론과 생성](weeks/week04_transformer_and_llm/day26_huggingface_model_usage_generation/concept.md) |
| Week 4 | Day 27 | [decoding, prompting, RAG와 fine-tuning](weeks/week04_transformer_and_llm/day27_decoding_prompting_rag_finetuning/concept.md) |
| Week 4 | Day 28 | [통합 LLM 프로젝트, 윤리와 최종 숙달](weeks/week04_transformer_and_llm/day28_integrated_llm_project_ethics_review/concept.md) |

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
