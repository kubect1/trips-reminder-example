from typing import Optional, Any
from sqlalchemy import Integer, String, DateTime, JSON, Boolean, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base
from pydantic import Enum

class TransportEnum(Enum):
    subway = 1
    bus = 2
    car = 3
    train = 3
    plane = 4

class Trip(Base):
    __tablename__ = "trip"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    chat_id: Mapped[int] = mapped_column(Integer(), ForeignKey("user.chat_id"), nullable=False)
    to_place: Mapped[dict[Any, Any]] = mapped_column(JSON(), nullable=False)
    from_place: Mapped[dict[Any, Any]] = mapped_column(JSON(), nullable=False)
    to_place_title: Mapped[str] = mapped_column(String(150), nullable=False)
    from_place_title: Mapped[str] = mapped_column(String(150), nullable=False)
    transport_type: Mapped[TransportEnum] = mapped_column(String(150), nullable=False)
    create_date: Mapped[DateTime] = mapped_column(DateTime(), nullable=False)
    travel_date: Mapped[DateTime] = mapped_column(DateTime(), nullable=False)
    notification_before_travel: Mapped[DateTime] = mapped_column(DateTime(), nullable=False)
    isEnded: Mapped[bool] = mapped_column(Boolean(), nullable=False)