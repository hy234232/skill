# hy0909 Codex Skills

개인/팀에서 반복 사용하는 Codex 스킬 모음입니다. 각 폴더는 독립 실행 가능한 스킬 패키지이며, `SKILL.md`와 필요한 `references/`, `assets/`, `scripts/`, `agents/` 파일을 함께 포함합니다.

## 포함된 스킬

| 스킬 | 용도 | 주요 포함 파일 |
| --- | --- | --- |
| `feature-generator` | 한국어 기능명세서 MD/XLSX 생성, XLSX→MD 변환, MD/Table→표준 XLSX 변환 | `references/`, `scripts/`, `assets/feature_xlsx_template.xlsx`, `agents/openai.yaml` |
| `policy-generator` | 한국어 정책 문서 MD 작성/재구성, 표준 7단 정책 구조 적용 | `SKILL.md`, `agents/openai.yaml` |
| `component-generator` | Figma/스크린샷/메모 기반 UI 컴포넌트 명세 MD 작성 | `SKILL.md` |
| `write-feature-spec` | 기존 기능명세서 형식과 톤을 기준으로 새 기능명세서 작성 | `references/feature_spec_style.md`, `scripts/`, `agents/openai.yaml` |
| `figma` | Figma MCP 기반 디자인 컨텍스트 수집, 디자인-코드 구현 지원 | `references/`, `assets/`, `agents/openai.yaml` |

## 설치

전체 스킬을 Codex가 자동 인식하는 위치에 복사합니다.

```bash
git clone git@github.com:hy0909/skills.git
mkdir -p ~/.codex/skills
rsync -a skills/ ~/.codex/skills/
```

특정 스킬만 설치하려면 해당 폴더만 복사합니다.

```bash
rsync -a skills/feature-generator/ ~/.codex/skills/feature-generator/
```

## 사용 예시

```text
$feature-generator로 이 회의록을 기능명세서.md로 만들어줘.
$policy-generator로 알림 정책 문서를 표준 구조로 정리해줘.
$component-generator로 이 Figma 컴포넌트를 개발자가 구현 가능한 MD로 정리해줘.
```

## 관리 원칙

- 스킬 폴더 안에는 실행에 필요한 파일만 둡니다.
- 상세 작성 규칙은 `references/`에 분리하고, 반복 변환 로직은 `scripts/`에 둡니다.
- 템플릿이나 샘플 산출물처럼 결과 생성에 필요한 파일은 `assets/`에 둡니다.
- `.DS_Store`, `__pycache__`, `*.pyc` 같은 로컬 캐시 파일은 커밋하지 않습니다.
