from pydantic import BaseModel,field_validator
from typing import Optional
from datetime import time, datetime, date
from decimal import Decimal

class BranchBase(BaseModel):
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class BranchCreate(BranchBase):
    created_by: str

class BranchUpdate(BranchBase):
    last_modified_by: Optional[str] = None

class Branch(BranchBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    class Config:
        from_attributes = True  # formerly from_orm=True

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TrainerBase(BaseModel):
    full_name: str
    phone: str
    email: Optional[str] = None
    expertise: Optional[str] = None
    branch_id: Optional[int] = None
    status: Optional[str] = "Active"

class TrainerCreate(TrainerBase):
    created_by: str

class TrainerUpdate(TrainerBase):
    last_modified_by: str

class Trainer(TrainerBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    class Config:
        from_attributes = True



class BatchBase(BaseModel):
    name: str
    trainer_id: int
    branch_id: int
    start_time: datetime
    end_time: datetime
    days: str
    capacity: int
    created_by: str

class BatchCreate(BatchBase):
    pass

class BatchUpdate(BaseModel):
    name: Optional[str] = None
    trainer_id: Optional[int] = None
    branch_id: Optional[int] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    days: Optional[str] = None
    capacity: Optional[int] = None
    last_modified_by: Optional[str] = None

class Batch(BaseModel):
    id: int
    name: str
    trainer_id: int
    branch_id: int
    start_time: time       # Change from datetime to time
    end_time: time         # Change from datetime to time
    days: str
    capacity: int
    created_by: str

    class Config:
        from_attribute = True

# Shared properties
class PackageBase(BaseModel):
    name: str
    duration_months: int
    fee_amount: Decimal
    max_classes_per_week: Optional[int] = None

# Create
class PackageCreate(PackageBase):
    created_by: str

# Update
class PackageUpdate(PackageBase):
    last_modified_by: Optional[str] = None

# Response model
class Package(PackageBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str] = None
    last_modified_date: Optional[datetime] = None
    is_deleted: bool
    deleted_by: Optional[str] = None
    deleted_date: Optional[datetime] = None

    class Config:
        from_attribute = True


class PromotionBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    message_template: Optional[str] = None


class PromotionCreate(PromotionBase):
    created_by: str


class PromotionUpdate(PromotionBase):
    last_modified_by: str


class Promotion(PromotionBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str] = None
    last_modified_date: Optional[datetime] = None
    is_deleted: bool
    deleted_by: Optional[str] = None
    deleted_date: Optional[datetime] = None

    class Config:
        from_attribute = True

class MaterialBase(BaseModel):
    title: str
    description: Optional[str] = None
    link: Optional[str] = None
    batch_id: Optional[int] = None


class MaterialCreate(MaterialBase):
    created_by: str


class MaterialUpdate(MaterialBase):
    last_modified_by: Optional[str] = None


class Material(MaterialBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    class Config:
        from_attribute = True

class UserBase(BaseModel):
    email: str
    role: Optional[str] = "admin"


class UserCreate(UserBase):
    password_hash: str
    created_by: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password_hash: Optional[str] = None
    role: Optional[str] = None
    last_modified_by: Optional[str] = None


class User(BaseModel):
    id: int
    email: str
    password_hash: str
    role: str
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    class Config:
        from_attributes = True  # This allows ORM-to-schema conversion



class MemberBase(BaseModel):
    full_name: str
    mobile_number: str
    email: Optional[str]
    date_of_joining: date
    package_id: int
    fee_amount: float
    payment_due_date: date
    status: Optional[str] = "Active"
    notes: Optional[str]
    batch_id: int


class MemberCreate(MemberBase):
    created_by: str


class MemberUpdate(MemberBase):
    last_modified_by: Optional[str]



class MemberOut(MemberBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    class Config:
        from_attributes = True

class PaymentBase(BaseModel):
    member_id: int
    amount_paid: float
    date_paid: date
    payment_method: Optional[str] = None
    receipt_file: Optional[str] = None
    notes: Optional[str] = None


class PaymentCreate(PaymentBase):
    created_by: str


class PaymentUpdate(PaymentBase):
    last_modified_by: Optional[str] = None


class PaymentOut(PaymentBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    class Config:
        from_attribute = True



class ReminderSettingBase(BaseModel):
    days_before_due: int
    message_template: str
    reminder_time: Optional[time] = None


class ReminderSettingCreate(ReminderSettingBase):
    created_by: str


class ReminderSettingUpdate(ReminderSettingBase):
    last_modified_by: Optional[str] = None


class ReminderSettingOut(ReminderSettingBase):
    id: int
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[datetime]

    class Config:
        from_attribute = True