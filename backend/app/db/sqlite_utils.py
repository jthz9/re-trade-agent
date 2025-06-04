import sqlite3
from pathlib import Path
from typing import List, Tuple, Any, Optional

# Database file will be in the /database_data directory inside the container,
# which is mounted from ./data on the host.
DB_FILE = Path("/database_data") / "re_opt_agent.db"
DB_FILE.parent.mkdir(parents=True, exist_ok=True) # data 디렉터리 생성 보장

def get_db_connection() -> sqlite3.Connection:
    """데이터베이스 연결을 생성하고 반환합니다."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row # 결과를 딕셔너리처럼 접근 가능하게 함
    return conn

def initialize_db():
    """데이터베이스를 초기화하고 필요한 테이블을 생성합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        hashed_password TEXT NOT NULL,
        is_active BOOLEAN DEFAULT TRUE
    )
    """)
    # 다른 테이블들도 필요에 따라 여기에 추가

    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_FILE}")

# --- User CRUD 함수 예시 ---

def create_user(email: str, hashed_password: str, is_active: bool = True) -> Optional[int]:
    """새로운 사용자를 생성하고 ID를 반환합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (email, hashed_password, is_active) VALUES (?, ?, ?)",
            (email, hashed_password, is_active)
        )
        conn.commit()
        return cursor.lastrowid # 생성된 사용자의 ID
    except sqlite3.IntegrityError: # UNIQUE 제약 조건 위반 (이메일 중복 등)
        print(f"Error: Could not create user {email}. It might already exist.")
        return None
    finally:
        conn.close()

def get_user_by_email(email: str) -> Optional[sqlite3.Row]:
    """이메일로 사용자를 조회합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id: int) -> Optional[sqlite3.Row]:
    """ID로 사용자를 조회합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users() -> List[sqlite3.Row]:
    """모든 사용자를 조회합니다."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

if __name__ == "__main__":
    initialize_db()
    # 예시: 테스트 사용자 생성
    # test_email = "test@example.com"
    # existing_user = get_user_by_email(test_email)
    # if not existing_user:
    #     new_id = create_user(test_email, "password123")
    #     if new_id:
    #         print(f"Test user created with id: {new_id}")
    #         retrieved = get_user_by_id(new_id)
    #         if retrieved:
    #             print(f"Retrieved test user: {dict(retrieved)}")
    # else:
    #     print(f"Test user {test_email} already exists: {dict(existing_user)}")
    
    # print("All users:")
    # for user_row in get_all_users():
    #     print(dict(user_row))
