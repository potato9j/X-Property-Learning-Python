# Day 25. Transformer와 언어모델링

## 1. 오늘의 위치
Week 4의 학습 주제입니다. 이전 개념을 다시 사용하고 이후 데이터, tensor, LLM 흐름으로 연결합니다.

## 2. 학습 목표
- Transformer block을 한 문장으로 설명한다.
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
| Transformer block | 오늘 코드에서 확인할 핵심 개념입니다. |
| residual | 오늘 코드에서 확인할 핵심 개념입니다. |
| layer norm | 오늘 코드에서 확인할 핵심 개념입니다. |
| feed-forward | 오늘 코드에서 확인할 핵심 개념입니다. |
| logits | 오늘 코드에서 확인할 핵심 개념입니다. |

## 5. 예측하고 실행하기
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

## 6. 흔한 오해
- 출력만 보고 타입과 shape를 확인하지 않는 실수를 피합니다.
- 합성 데이터는 실제 환자 정보가 아닙니다.

## 7. 참고자료
- Python 공식 문서: https://docs.python.org/3/
- NumPy 공식 문서: https://numpy.org/doc/
- pandas 공식 문서: https://pandas.pydata.org/docs/
- PyTorch 공식 문서: https://pytorch.org/docs/stable/index.html
- Hugging Face 문서: https://huggingface.co/docs/transformers/index
