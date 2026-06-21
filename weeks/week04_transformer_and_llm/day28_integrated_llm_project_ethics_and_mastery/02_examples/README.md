# Day 28 예제. 통합 LLM 프로젝트, 윤리와 최종 숙달

## 예제 목표
hallucination, privacy, ethics, verification, final project를 코드 실행 결과와 함께 확인합니다.

## 실행 순서
1. notebook을 엽니다.
2. 출력과 shape를 예측합니다.
3. 실행 후 차이를 기록합니다.

## 핵심 예제 코드
```python
tokens = ["환자", "혈압", "상승", "확인"]
token_to_id = {token: index for index, token in enumerate(tokens)}
input_ids = [token_to_id[token] for token in tokens]
attention_mask = [1 for _ in input_ids]
print("tokens:", tokens)
print("input_ids:", input_ids)
print("attention_mask:", attention_mask)
print("shape-like:", (1, len(input_ids)))
```

## 확인 질문
- 첫 출력의 자료구조는 무엇인가요?
- shape-like 값은 무엇을 뜻하나요?
- AI 설명에서 검증해야 할 부분은 무엇인가요?
