from sqlalchemy import Column, Integer, String, Text, Boolean, TIMESTAMP, ForeignKey, Time, Numeric, Date
from sqlalchemy.sql import func
from db import Base

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(Text)
    city = Column(String(50))
    state = Column(String(50))
    pincode = Column(String(10))
    phone = Column(String(15))
    email = Column(String(100))

    # Audit columns
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

    # Audit columns
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

    # Audit columns
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
    max_classes_per_week = Column(Integer)

    # Audit columns
    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    message_template = Column(Text)

    # Audit columns
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

    # Audit columns
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

    # Audit columns
    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
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

    # Audit columns
    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("members.id"))
    amount_paid = Column(Numeric(10, 2), nullable=False)
    date_paid = Column(Date, nullable=False)
    payment_method = Column(String(20))
    receipt_file = Column(Text)
    notes = Column(Text)

    # Audit columns
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

    # Audit columns
    created_by = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    last_modified_by = Column(String(100))
    last_modified_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_by = Column(String(100))
    deleted_date = Column(TIMESTAMP)