from sqlalchemy.orm import Session
from passlib.context import CryptContext

from backend.app.models.user import User
from backend.app.schemas.user import UserCreate

# 비밀번호 해싱을 위한 설정
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate) -> User:
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# PoC 단계에서는 단일 admin 사용자만 관리하므로,
# admin 사용자가 이미 존재하는지 확인하고, 없으면 생성하는 유틸리티 함수를 추가할 수 있습니다.
def get_or_create_admin_user(db: Session, admin_user_in: UserCreate) -> User:
    admin_user = get_user_by_email(db, email=admin_user_in.email)
    if not admin_user:
        admin_user = create_user(db, user=admin_user_in)
    # 여기서 admin_user.is_active 등을 True로 설정하거나, 역할을 부여하는 로직을 추가할 수 있습니다.
    # PoC에서는 단순하게 생성 또는 조회만 합니다.
    return admin_user
