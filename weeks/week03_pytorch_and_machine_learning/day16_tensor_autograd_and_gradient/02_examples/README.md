# Day 16 예제. tensor, autograd와 gradient

## 예제 목표
tensor, device, requires_grad, backward, gradient를 코드 실행 결과와 함께 확인합니다.

## 실행 순서
1. notebook을 엽니다.
2. 출력과 shape를 예측합니다.
3. 실행 후 차이를 기록합니다.

## 핵심 예제 코드
```python
features = [[0.1, 0.4], [0.8, 0.3], [0.2, 0.9]]
labels = [0, 1, 1]
print("feature shape:", (len(features), len(features[0])))
print("label shape:", (len(labels),))
try:
    import torch
    x = torch.tensor(features, dtype=torch.float32)
    y = torch.tensor(labels, dtype=torch.long)
    print("x.shape:", tuple(x.shape))
    print("y.shape:", tuple(y.shape))
except ModuleNotFoundError:
    print("torch가 없는 환경에서는 Python list로 shape를 먼저 추적합니다.")
```

## 확인 질문
- 첫 출력의 자료구조는 무엇인가요?
- shape-like 값은 무엇을 뜻하나요?
- AI 설명에서 검증해야 할 부분은 무엇인가요?
