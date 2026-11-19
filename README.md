# FanStay

콘서트 팬이 "공연 전 휴식 → 공연 → 안전한 귀가"를 한 서비스에서 해결하는 공연 연계 숙소·이동 플랫폼. (기업과 경영 기말 팀프로젝트)

## 폴더 구조

```
fanstay/
├── docs/
│   ├── PRD.md                          기획 문서 (1105 1차 회의록 기반)
│   ├── IA.md                           정보구조(IA), 원본은 FigJam
│   └── design/
│       ├── DESIGN-SYSTEM.md            디자인 시스템 (토스 페이스페이 기반, PPT 제작 가이드 포함)
│       └── offline-slides-reference.html   디자인 시스템 적용 예시 (1920×1080 HTML 슬라이드)
└── wireframes/
    └── index.html                      로파이 와이어프레임 (브라우저로 열기)
```

## 문서 바로가기

| 문서 | 내용 |
|---|---|
| [PRD](docs/PRD.md) | 문제 정의, MVP 범위, 요구사항 |
| [IA](docs/IA.md) | 화면 구조와 진입 흐름 |
| [디자인 시스템](docs/design/DESIGN-SYSTEM.md) | 컬러·타이포·레이아웃·컴포넌트·모션. **최종 발표 자료는 이 기준으로 PPT를 만들어요** |
| [슬라이드 레퍼런스](docs/design/offline-slides-reference.html) | 디자인 시스템을 슬라이드로 옮긴 예시 (키보드 ←/→) |
| [와이어프레임](wireframes/index.html) | 앱 화면 초안 |

## 이어서 작업하기

```bash
git clone https://github.com/dear-my-sunday/fanstay.git
cd fanstay
open wireframes/index.html   # macOS
```

## 현재 상태

- MVP 범위: 숙소 선택, 티켓 인증, 보호자 알림·위치 공유, 승합차 귀가, 공연장 지도, 동행 매칭
- 와이어프레임의 문구와 데이터는 모두 예시임
- 발표 자료는 디자인 시스템 기준으로 PPT(.pptx) 제작 예정
