from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime
from uuid import uuid4, UUID
from typing import List

class Base(DeclarativeBase):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.now)
    modified_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class DailyCalorieAggregates(Base):
    __tablename__ = 'daily_calorie_aggregates'
    
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    calorie_intakes: Mapped[List["CalorieIntakes"]] = relationship(back_populates="daily_calorie_aggregate")
    total_calories: Mapped[int] = mapped_column(Integer())

class CalorieIntakes(Base):
    __tablename__ = 'calorie_intakes'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    daily_calorie_aggregate_id: Mapped[UUID] = mapped_column(ForeignKey("daily_calorie_aggregates.id"))
    daily_calorie_aggregate: Mapped["DailyCalorieAggregates"] = relationship(back_populates="calorie_intakes")
    name: Mapped[str] = mapped_column(String(50))
    calories: Mapped[int] = mapped_column(Integer())
    quantity: Mapped[int] = mapped_column(Integer())
