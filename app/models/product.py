from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Product(Base):
  __tablename__ = "products"

  id: Mapped[int] = mapped_column(primary_key=True, index=True)
  name: Mapped[str] = mapped_column(index=True)
  description: Mapped[str | None] = mapped_column(Text)
  price: Mapped[float]
  category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
  image_url: Mapped[str | None]
  created_at: Mapped[datetime] = mapped_column(
      default=lambda: datetime.now(timezone.utc)
  )

  category = relationship("Category", back_populates="products")

  def __repr__(self):
    return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"