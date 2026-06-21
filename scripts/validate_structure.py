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
