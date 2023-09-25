# Infrastructure

### 개요
다양한 Infrastructure template code를 작성합니다.

### 구성요소

- `python` : 3.12.0
- `fastapi` : 0.103.1

### 브랜치 운영 규칙
- `main` 브랜치는 `staging` 용도입니다.
- `dev` 브랜치에 `feature/*` 형식으로 `Pull Request` 하여 동료들의 리뷰 후 `Merge` 를 진행합니다.
- `dev` 에 `Merge` 가 완료되면 다시 `Main` 브랜치로 `Merge` 를 진행합니다.

### 비고
- template 브랜치이기 때문에 배포용 브랜치와 다른 운영규칙 적용을 시도하였습니다.
- 운영규칙은 추후에 상의 후 변경 될 수 있습니다. 