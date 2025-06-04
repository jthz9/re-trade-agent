# RE-OptAgent 백엔드 개발 계획

이 문서는 RE-OptAgent 백엔드 시스템 개발의 단계별 진행 순서를 정의합니다.

## 개발 순서

1.  **데이터베이스 설정**:
    *   SQLite 사용 (README 기반).
    *   SQLAlchemy를 사용하여 데이터 모델 정의 (`app/models`).
    *   Alembic을 설정하여 데이터베이스 스키마 마이그레이션 관리.

2.  **기본 CRUD API 및 서비스 계층 구축**:
    *   핵심 데이터 모델(기상, 시장, REC, 대기질, 예측, 거래 등)에 대한 Pydantic 스키마 정의 (`app/schemas`).
    *   데이터베이스와 상호작용하는 서비스 로직 구현 (`app/services`).
    *   FastAPI 라우터를 사용하여 CRUD API 엔드포인트 생성 (`app/api/v1/...`).

3.  **외부 데이터 수집기 개발**:
    *   KMA, KPX, KNREC, 환경부 API 클라이언트 구현.
    *   스케줄링(APScheduler 또는 BackgroundTasks)을 통해 주기적으로 데이터 수집 및 DB 저장.
    *   데이터 정제 및 기본 전처리 로직 포함 (`app/services/data_collectors`).

4.  **머신러닝 파이프라인 구축**:
    *   Prophet, XGBoost, TensorFlow, scikit-learn을 활용한 예측 모델 개발.
    *   학습 데이터 준비, 피처 엔지니어링, 모델 학습, 모델 저장/버전 관리.
    *   새로운 데이터에 대한 예측 수행 및 결과 저장 로직 구현 (`app/services/ml_pipeline` 또는 `app/models/predictors`).
    *   예측 결과 제공 API 엔드포인트 생성.

5.  **LangChain AI 에이전트 개발**:
    *   LangChain과 OpenAI API를 사용하여 거래 전략 결정 AI 에이전트 구축 (`app/agent`).
    *   프롬프트 엔지니어링, 외부 도구(ML 모델, 데이터 API) 연동.
    *   에이전트 추천/분석 결과 제공 API 엔드포인트 생성.

6.  **사용자 인증 및 권한 부여**:
    *   FastAPI Security 유틸리티 (OAuth2)를 사용한 인증/권한 기능 구현.
    *   로그인, 토큰 발급, 사용자 관리 (`app/core/security.py`, 관련 모델/API).

7.  **WebSocket 실시간 연동**:
    *   FastAPI WebSocket을 사용하여 프론트엔드에 실시간 데이터 업데이트 푸시.
    *   실시간 시장 현황, 에이전트 추천 등 (`app/api/websockets.py`).

8.  **테스트 작성**:
    *   `pytest`와 `TestClient`를 사용한 단위 테스트 및 통합 테스트.
    *   API 엔드포인트, 서비스 로직, ML 모델 등 검증 (`tests/`).

9.  **로깅 및 모니터링 시스템 구축**:
    *   Python `logging` 모듈 설정.
    *   필요시 외부 모니터링 도구 연동 고려 (`app/core/logging_config.py`).

10. **배포 준비 및 문서화**:
    *   프로덕션용 Dockerfile 최적화.
    *   Railway 호스팅 환경 변수 및 DB 연결 설정.
    *   Railway 배포 파이프라인 설정.
    *   API 자동 문서화 (FastAPI) 최종 검토 및 추가 설명.
    *   보안 설정 (HTTPS, CORS) 강화.
