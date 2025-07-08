from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UserInput(BaseModel):
    day: str
    weather: str
    location: str
    schedule: str
    completed: List[str] = []

@app.post("/recommend")
def recommend(input: UserInput):
    all_missions = {
        "맑음": [
            "텀블러 챙기고 카페 가기",
            "제로웨이스트 상점 방문해보기",
            "자전거 타고 근처 이동하기"
        ],
        "비": [
            "우산 오래 쓰기",
            "플라스틱 사용 줄이기 실천",
            "에너지 절약 캠페인 참여하기"
        ],
        "실내": [
            "분리배출 정리하기",
            "에코백 정리하기",
            "냉장고 에너지 효율 확인하기"
        ]
    }

    # 조건에 따라 미션 후보 선택
    if input.weather == "맑음" and "외출" in input.schedule:
        candidates = all_missions["맑음"]
    elif input.weather == "비":
        candidates = all_missions["비"]
    else:
        candidates = all_missions["실내"]

    # 이미 완료한 미션은 제외
    recommendations = [m for m in candidates if m not in input.completed]

    return {
        "recommended_missions": recommendations[:3]
    }
