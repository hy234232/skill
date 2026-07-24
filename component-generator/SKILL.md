---
name: component-generator
description: Create Korean UI component spec Markdown documents from a designer's Figma mockup, screenshot, raw notes, or an existing MD file. Use when the user asks to write, restructure, or document a design-system component (modal, toast, button, dropdown, input, etc.) into the standard component spec format that a frontend developer can implement directly.
---

# Component Generator

Use this skill to create or restructure Korean UI component spec `.md` files. A component spec captures what a **designer defined in Figma** and rewrites it so a **frontend developer** can understand and build the component without guessing.

The source is almost always a Figma mockup or screenshot of the design intent. The output must translate visual/design decisions into implementable rules: anatomy, variants, tokens, sizing, states, interaction, and a developer-facing API/CSS hint.

## When To Use

Use this skill when the user asks for:

- 컴포넌트 명세서 / 컴포넌트 MD 작성
- 디자인 시스템 컴포넌트 문서화
- 피그마 시안(스크린샷)을 컴포넌트 문서로 정리
- 모달/토스트/버튼/드롭다운/입력 등 UI 컴포넌트 스펙 정리
- 기존 MD를 표준 컴포넌트 스펙 구조로 재작성

## Required Structure

Every component MD must include these sections in this order. Omit a section only when it genuinely does not apply, and keep the numbering contiguous.

| 순서 | 항목 | 필수 여부 | 작성 내용 |
| --- | --- | --- | --- |
| 0 | 헤더 + 메타 | 필수 | 컴포넌트명 + Figma 링크, Status, Last updated, Owner |
| 1 | Overview | 필수 | 컴포넌트의 목적, 사용 맥락, 적용 범위 |
| 2 | Anatomy | 필수 | 구성 요소 분해(ASCII/표) + Figma 레이어명 |
| 3 | Variants / Rules | 필수 | 변형(variant) 또는 핵심 규칙(예: 사이즈/높이 규칙) |
| 4 | Design Tokens / Spec | 필수 | 색상·간격·타이포·사이즈 토큰 또는 수치 스펙 |
| 5 | States & Interaction | 조건부 | 상태(hover/disabled 등), 애니메이션, 인터랙션 |
| 6 | Content / Do & Don't | 조건부 | 카피 가이드, 올바른/잘못된 예시 |
| 7 | Accessibility | 조건부 | ARIA role, 포커스, 명도 대비 등 |
| 8 | Implementation Notes | 필수 | 프론트 개발자용 CSS/구현 힌트, 레이아웃 전략 |
| 9 | Changelog | 필수 | 일자, 버전, 변경 내용, 작성자 |
| 10 | Related | 선택 | 관련 컴포넌트, 관련 문서 링크 |

> 단일 컴포넌트가 아니라 공통 규칙(예: "모달 높이 공통")을 문서화할 때는 `Variants`를 `Rules`로 대체하고, 최소/최대/조건별 규칙을 표로 정리한다.

## Header & Metadata Block

Start every file with the component name as the H1, then a blockquote meta block:

```md
# {{Component Name}}

> **Figma:** [{{시안명}} → Frame/Component](figma://link/REPLACE_WITH_NODE_ID)  
> **Status:** `Draft` · **Last updated:** {{YYYY-MM-DD}}  
> **Owner:** Design System Team
```

- `Status`: `Draft`, `Review`, `Stable`, `Deprecated` 중 하나.
- `Last updated`: 현재 날짜 또는 사용자 제공 날짜.
- `Figma`: 사용자가 링크/노드 ID를 주면 채우고, 없으면 `REPLACE_WITH_NODE_ID` placeholder를 유지한다. **임의의 링크를 지어내지 않는다.**

## Section Separators

Use a horizontal rule `---` between every top-level section so the document reads cleanly in GitHub and Notion:

```md
---

## 2. Anatomy
```

Do not insert separators inside table cells.

## Designer-to-Developer Translation Rules

This is the core of the skill. The designer expresses intent in Figma; rewrite it as buildable rules.

- 시안에서 **반복되는 수치**(여백, 반경, 최소/최대 크기)는 토큰 또는 px 스펙 표로 명시한다.
- 절대값(px)과 상대값(%, vh/vw)을 **명확히 구분**해서 적는다. (예: 최소 높이 240px 절대값, 최대 높이 90vh 상대값)
- 시안에 "잘못된 예시"가 있으면 `Do & Don't` 표에 그대로 반영한다.
- 스크롤/오버플로우/잘림 동작은 어느 영역에서 일어나는지 영역 단위로 명시한다.
- Anatomy에는 가능하면 Figma 레이어명을 함께 적어 개발자가 시안과 코드를 매칭할 수 있게 한다.
- `Implementation Notes`에는 레이아웃 전략(flex/grid), 핵심 CSS 속성, 스크롤 컨테이너 위치 등 **개발 착수에 필요한 최소 힌트**를 제공한다.

## Spec & Token Rules

- 색상/간격/타이포/사이즈는 표로 정리하고, 토큰명이 있으면 토큰명을, 없으면 수치를 적는다.
- 토큰명을 모를 때 그럴듯한 토큰명을 지어내지 말고 수치 + `(토큰 미정)`으로 표기한다.
- 수치 단위(px, %, vh, ms)를 항상 명시한다.
- 사용자/시안에 없는 variant, state, breakpoint를 추측해서 추가하지 않는다. 누락 정보는 `TBD` 또는 `시안 기준 추가 정의 필요`로 적는다.

## Image / Asset Rules

- 시안 캡처를 문서에 포함할 때는 해당 섹션 근처에 배치하고, MD 파일 위치 기준 상대 경로를 쓴다.
- 문서별 이미지는 `assets/<topic>/` 폴더에 저장한다.
- 사용자가 제공한 원본 이미지 내용을 그대로 보존한다. 리사이즈/크롭/재작성/재생성 금지.
- 모든 이미지 에셋에 4면 1px 연한 회색 `#D9DEE7` 외곽 테두리를 적용한다(원본 픽셀 바깥으로 추가, 캔버스가 가로·세로 각 2px 증가). 사용자가 테두리 불필요를 명시하면 생략한다.
- 테두리 추가 후 치수와 결과를 확인한 뒤 링크한다.

## File Naming Rules

- 컴포넌트 MD 파일은 `<topic>.md` 형식으로, 간결한 영문 kebab-case 토픽을 쓴다.
- `component`, `컴포넌트`, `spec` 등 문서 유형 단어와 날짜/버전/순번/상태 접미사를 파일명에 넣지 않는다.
- 디렉터리 맥락을 반복하는 접두사를 넣지 않는다.
- 문서별 에셋은 동일 토픽으로 `assets/<topic>/`을 사용한다.
- 기존 파일명이 규칙에 맞으면 보존하고, 아니면 rename 후 내부 링크/에셋 경로를 갱신한다.
- 예시:
  - 모달 높이 공통 스펙: `modal-height.md`
  - 토스트 알림 컴포넌트: `toast-notification.md`
  - 액션 완료 드롭다운: `action-complete-dropdown.md`

## Changelog Author Rules

- 사용자(김혜연) 요청으로 생성·수정한 컴포넌트 문서의 모든 changelog `Author`(작성자) 칸에는 `Claude, 김혜연`을 적는다.
- 초안 생성 행과 이후 수정 행 모두에 적용한다.
- `Design System Team`, `개발팀`, `Claude` 단독을 changelog 작성자로 쓰지 않는다.

## Writing Rules

- 별도 요청이 없으면 한국어로 작성한다. (구조 키워드/토큰명/CSS는 영문 유지)
- 용어를 문서 전체에서 일관되게 쓴다.
- 한국어 사용자 액션 문구에서는 모바일 제스처를 설명할 때도 `탭`보다 `선택`을 우선 사용한다. 예: `버튼 탭` → `버튼 선택`, `영상 영역 탭` → `영상 영역 선택`. 단, 기술 구현 설명·이벤트명·제스처 자체가 중요한 경우에는 `tap`, `double tap`, `pinch-to-zoom`, `drag/pan`처럼 영문 이벤트/제스처명을 유지할 수 있다.
- 시안에 없는 동작·API·breakpoint·접근성 규격을 지어내지 않는다. 직접 구현 가능한 사실만 적는다.
- 정보가 없으면 `TBD` 또는 `시안 기준 추가 정의 필요`로 표기한다.
- `Implementation Notes`의 코드는 구현 힌트 수준으로 간결하게 유지하고, 실제 컴포넌트 코드 전체를 작성하지 않는다.

## Output Rules

- 최종 산출물은 별도 요청이 없으면 `.md` 파일이다.
- `<topic>.md` 네이밍 규칙을 모든 산출물에 적용한다.
- 필수 섹션을 비워두지 않는다.
- 원본 시안의 의미를 보존하고 규칙을 삭제하지 않는다.
- 디스크에 저장할 때는 소스 파일 옆 또는 사용자가 지정한 출력 디렉터리(예: `design-system/`)에 저장한다.
- 사용자가 명시적으로 요청하지 않으면 소스를 덮어쓰지 않는다.
