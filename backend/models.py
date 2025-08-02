from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey, Time, Numeric, Date
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from db import Base

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(10), nullable=False, unique=True)  
    address = Column(Text)
    city = Column(String(50))
    state = Column(String(50))
    pincode = Column(String(10))
    phone = Column(String(15))
    email = Column(String(100))

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100))
    expertise = Column(String(100))
    branch_id = Column(Integer, ForeignKey("branches.id"))
    status = Column(String(20), default="Active")

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class Batch(Base):
    __tablename__ = "batches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    trainer_id = Column(Integer, ForeignKey("trainers.id"))
    branch_id = Column(Integer, ForeignKey("branches.id"))
    start_time = Column(Time)
    end_time = Column(Time)
    days = Column(String(100))
    capacity = Column(Integer)

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    duration_months = Column(Integer, nullable=False)
    fee_amount = Column(Numeric(10, 2), nullable=False)
    max_classes_per_week = Column(Integer, nullable=False)
    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100), default="")
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)
    deleted_by = Column(String(100), default="")
    deleted_date = Column(TIMESTAMP)

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    message_template = Column(Text)

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class Material(Base):
    __tablename__ = "materials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    link = Column(Text)
    batch_id = Column(Integer, ForeignKey("batches.id"))

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(Text, nullable=False)
    role = Column(String(20), default="admin")

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

from sqlalchemy import Column, String, Integer, Numeric, Date, ForeignKey, Boolean, Text, TIMESTAMP, func
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

from sqlalchemy import Column, String, Integer, ForeignKey, Date, Numeric, Boolean, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship, Session
from db import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(String(10), primary_key=True, index=True)  # e.g., ML001
    full_name = Column(String(100), nullable=False)
    mobile_number = Column(String(15), nullable=False)
    email = Column(String(100))
    date_of_joining = Column(Date, nullable=False)
    package_id = Column(Integer, ForeignKey("packages.id"))
    fee_amount = Column(Numeric(10, 2), nullable=False)
    payment_due_date = Column(Date, nullable=False)
    status = Column(String(20), default="Active")
    notes = Column(Text)
    batch_id = Column(Integer, ForeignKey("batches.id"))
    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100), default="")
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)
    deleted_by = Column(String(100), default="")
    deleted_date = Column(Date, nullable=True)

    # ForeignKey relationships (optional)
    package = relationship("Package", backref="members")
    batch = relationship("Batch", backref="members")

    @staticmethod
    def generate_member_id(session: Session, branch_code: str) -> str:
        last_member = (
            session.query(Member)
            .filter(Member.id.like(f"{branch_code}%"))
            .order_by(Member.id.desc())
            .first()
        )
        if last_member:
            last_seq = int(last_member.id[len(branch_code):])
        else:
            last_seq = 0
        new_seq = last_seq + 1
        return f"{branch_code}{new_seq:03d}"



class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(String(10), ForeignKey("members.id"))
    amount_paid = Column(Numeric(10, 2), nullable=False)
    date_paid = Column(Date, nullable=False)
    payment_method = Column(String(20))
    receipt_file = Column(Text)
    notes = Column(Text)

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class ReminderSetting(Base):
    __tablename__ = "reminder_settings"

    id = Column(Integer, primary_key=True, index=True)
    days_before_due = Column(Integer, nullable=False)
    message_template = Column(Text, nullable=False)
    reminder_time = Column(Time)

    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)
