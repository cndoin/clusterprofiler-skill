# clusterprofiler-skill · YuLab-SMU R 생물정보학 생태계 스킬

<p align="center"><img src="docs/clusterprofiler-skill.svg" alt="스킬 워크플로" width="900"></p>

**38개 패키지 · API 허용 목록 6,137개 키 · 오프라인 Python 도구 · 자체 점검 19/19 통과**

AI 에이전트가 YuLab-SMU 생물정보학 R 생태계에서 분석을 작성하고, 검사하고, 계획하고, 실행하도록 돕는 교차 에이전트 스킬입니다. API 색인은 업스트림 `NAMESPACE`와 R 소스의 시그니처에서 생성되며, `cp_lint.py`가 R 스크립트를 전달하기 전에 검사합니다.

## 기능

- `cp_lint.py`: 오프라인 R 스크립트 검사. 알 수 없는 생태계 함수, 시그니처를 아는 경우의 잘못된 인자, 흔한 오타, 문법 오류, 전각 문장부호를 찾습니다.
- `cp_api.py`: 로컬 API 색인에서 실제 시그니처를 조회합니다.
- `cp_plan.py`: 자연어 요청을 분석 단계와 함수 제안으로 바꿉니다.
- YuLab-SMU 생태계 38개 패키지와 6,137개 키를 포함하며, 3,087개는 형식 인자를 분석했습니다.
- `scripts/run_cp.R`은 실제 R 패키지를 실행합니다. Python이 결과를 만들어 내지 않습니다.

## 빠른 시작

```bash
python3 install.py --host codex       # claude, workbuddy, deepseek도 지원
python3 tools/selftest.py             # 19개 자체 점검
python3 tools/cp_lint.py analysis.R --json
```

Windows에서 `python3`를 찾을 수 없으면 `python`을 사용하세요. Python 도구는 표준 라이브러리만 사용합니다. 실제 분석 실행에는 R과 관련 Bioconductor/CRAN 패키지가 필요합니다. [설치 안내](INSTALL.md)를 참고하세요.

자체 점검은 R 회귀 fixture 9개, 문서 코드 블록 44개, 도구 스모크 점검, API 색인 무결성을 확인하며 **19/19 통과**입니다. 검증 환경에 R이 설치되지 않아 실제 R 분석은 실행하지 않았습니다.

## 문서

[영문 홈](README.md) · [설치 안내](INSTALL.md) · [스킬 지침](SKILL.md) · [변경 기록](CHANGELOG.md)

이 프로젝트는 독립 커뮤니티 스킬이며 YuLab-SMU 또는 clusterProfiler의 공식 제품이 아닙니다. 라이선스와 출처는 [NOTICE](NOTICE)를 확인하세요.
