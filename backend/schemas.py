from pydantic import BaseModel,field_validator
from typing import Optional
from datetime import time, datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class BranchBase(BaseModel):
    name: str
    code: str
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    pincode: Optional[str]
    phone: Optional[str]
    email: Optional[str]


class BranchCreate(BranchBase):
    created_by: str


class BranchUpdate(BaseModel):
    name: Optional[str]
    code: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    pincode: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    last_modified_by: Optional[str]


class BranchOut(BranchBase):
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



class TrainerBase(BaseModel):
    full_name: str = Field(..., max_length=100)
    phone: str = Field(..., max_length=15)
    email: Optional[EmailStr]
    expertise: Optional[str] = Field(None, max_length=100)
    branch_id: Optional[int]
    status: Optional[str] = Field("Active", max_length=20)


class TrainerCreate(TrainerBase):
    created_by: str = Field(..., max_length=100)


class TrainerUpdate(BaseModel):
    full_name: Optional[str] = Field(None, max_length=100)
    phone: Optional[str] = Field(None, max_length=15)
    email: Optional[EmailStr]
    expertise: Optional[str] = Field(None, max_length=100)
    branch_id: Optional[int]
    status: Optional[str] = Field(None, max_length=20)
    last_modified_by: Optional[str] = Field(None, max_length=100)


class TrainerOut(TrainerBase):
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



class BatchBase(BaseModel):
    name: str = Field(..., max_length=50)
    trainer_id: Optional[int]
    branch_id: Optional[int]
    start_time: Optional[time]
    end_time: Optional[time]
    days: Optional[str] = Field(None, max_length=100)
    capacity: Optional[int]


class BatchCreate(BatchBase):
    created_by: str = Field(..., max_length=100)


class BatchUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    trainer_id: Optional[int]
    branch_id: Optional[int]
    start_time: Optional[time]
    end_time: Optional[time]
    days: Optional[str] = Field(None, max_length=100)
    capacity: Optional[int]
    last_modified_by: Optional[str] = Field(None, max_length=100)


class BatchOut(BatchBase):
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


from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PackageBase(BaseModel):
    name: str = Field(..., max_length=100)
    duration_months: int
    fee_amount: Decimal
    max_classes_per_week: int

class PackageCreate(PackageBase):
    created_by: str = Field(..., max_length=100)

class PackageUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    duration_months: Optional[int]
    fee_amount: Optional[Decimal]
    max_classes_per_week: Optional[int]
    last_modified_by: Optional[str] = Field(None, max_length=100)

class PackageOut(PackageBase):
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



class PromotionBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    message_template: Optional[str]


class PromotionCreate(PromotionBase):
    created_by: str = Field(..., max_length=100)


class PromotionUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    message_template: Optional[str]
    last_modified_by: Optional[str] = Field(None, max_length=100)


class PromotionOut(PromotionBase):
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


class MaterialBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str]
    link: Optional[str]
    batch_id: Optional[int]


class MaterialCreate(MaterialBase):
    created_by: str = Field(..., max_length=100)


class MaterialUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str]
    link: Optional[str]
    batch_id: Optional[int]
    last_modified_by: Optional[str] = Field(None, max_length=100)


class MaterialOut(MaterialBase):
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

from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    role: Optional[str] = "admin"


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)
    created_by: str = Field(..., max_length=100)


class UserUpdate(BaseModel):
    email: Optional[EmailStr]
    password: Optional[str] = Field(None, min_length=6)
    role: Optional[str]
    last_modified_by: Optional[str] = Field(None, max_length=100)


class UserOut(UserBase):
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





from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from decimal import Decimal
from datetime import date, datetime

class MemberBase(BaseModel):
    full_name: str = Field(..., max_length=100)
    mobile_number: str = Field(..., max_length=15)
    email: Optional[EmailStr] = None
    date_of_joining: date
    package_id: Optional[int]
    fee_amount: Decimal
    payment_due_date: date
    status: Optional[str] = "Active"
    notes: Optional[str] = None
    batch_id: Optional[int]

class MemberCreate(MemberBase):
    created_by: str = Field(..., max_length=100)
    branch_code: str = Field(..., max_length=10)  # Used to generate member ID

class MemberUpdate(BaseModel):
    full_name: Optional[str] = Field(None, max_length=100)
    mobile_number: Optional[str] = Field(None, max_length=15)
    email: Optional[EmailStr]
    date_of_joining: Optional[date]
    package_id: Optional[int]
    fee_amount: Optional[Decimal]
    payment_due_date: Optional[date]
    status: Optional[str]
    notes: Optional[str]
    batch_id: Optional[int]
    last_modified_by: Optional[str] = Field(None, max_length=100)

class MemberOut(MemberBase):
    id: str
    created_by: str
    created_date: datetime
    last_modified_by: Optional[str]
    last_modified_date: Optional[datetime]
    is_deleted: bool
    deleted_by: Optional[str]
    deleted_date: Optional[date]

    class Config:
        from_attributes = True


class PaymentBase(BaseModel):
    member_id: str = Field(..., max_length=10)
    amount_paid: Decimal
    date_paid: date
    payment_method: Optional[str] = Field(None, max_length=20)
    receipt_file: Optional[str]
    notes: Optional[str]


class PaymentCreate(PaymentBase):
    created_by: str = Field(..., max_length=100)


class PaymentUpdate(BaseModel):
    member_id: Optional[str] = Field(None, max_length=10)
    amount_paid: Optional[Decimal]
    date_paid: Optional[date]
    payment_method: Optional[str] = Field(None, max_length=20)
    receipt_file: Optional[str]
    notes: Optional[str]
    last_modified_by: Optional[str] = Field(None, max_length=100)


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
    created_by: str = Field(..., max_length=100)


class ReminderSettingUpdate(BaseModel):
    days_before_due: Optional[int]
    message_template: Optional[str]
    reminder_time: Optional[time]
    last_modified_by: Optional[str] = Field(None, max_length=100)


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