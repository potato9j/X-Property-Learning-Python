# Day 07 예제. class와 1주차 통합 숙달

## 예제 목표
class, object, instance, __init__, self, 상속를 코드 실행 결과와 함께 확인합니다.

## 실행 순서
1. notebook을 엽니다.
2. 출력과 shape를 예측합니다.
3. 실행 후 차이를 기록합니다.

## 핵심 예제 코드
```python
day = 7
topic = "class와 1주차 통합 숙달"
scores = [72, 85, 91, 68, 77]
passed = []
for score in scores:
    if score >= 75:
        passed.append(score)
summary = {"day": day, "topic": topic, "student_count": len(scores), "passed_count": len(passed), "average": sum(scores) / len(scores)}
print(summary)
print(type(summary["average"]).__name__)
```

## 확인 질문
- 첫 출력의 자료구조는 무엇인가요?
- shape-like 값은 무엇을 뜻하나요?
- AI 설명에서 검증해야 할 부분은 무엇인가요?
