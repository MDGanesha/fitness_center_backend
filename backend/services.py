from sqlalchemy.orm import Session
from models import Branch, Trainer, Package, Promotion, Material, User, Member, Payment, ReminderSetting, Batch
from schemas import *
from datetime import datetime

from sqlalchemy.orm import Session
from datetime import datetime
from models import Branch
import schemas


def create_branch(db: Session, branch: schemas.BranchCreate):
    db_branch = Branch(**branch.model_dump())
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch


def get_branch(db: Session, branch_id: int):
    return db.query(Branch).filter(Branch.id == branch_id, Branch.is_deleted == False).first()


def get_all_branches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Branch).filter(Branch.is_deleted == False).offset(skip).limit(limit).all()


def update_branch(db: Session, branch_id: int, branch_data: schemas.BranchUpdate):
    branch = db.query(Branch).filter(Branch.id == branch_id, Branch.is_deleted == False).first()
    if not branch:
        return None

    update_fields = branch_data.model_dump(exclude_unset=True)
    for key, value in update_fields.items():
        setattr(branch, key, value)

    branch.last_modified_date = datetime.now()
    db.commit()
    db.refresh(branch)
    return branch


def delete_branch(db: Session, branch_id: int, deleted_by: str):
    branch = db.query(Branch).filter(Branch.id == branch_id, Branch.is_deleted == False).first()
    if not branch:
        return None

    branch.is_deleted = True
    branch.deleted_by = deleted_by
    branch.deleted_date = datetime.now()
    db.commit()
    return branch


def create_trainer(db: Session, trainer: TrainerCreate):
    db_trainer = Trainer(**trainer.model_dump())
    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer


def get_trainer(db: Session, trainer_id: int):
    return db.query(Trainer).filter(Trainer.id == trainer_id, Trainer.is_deleted == False).first()


def get_all_trainers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Trainer).filter(Trainer.is_deleted == False).offset(skip).limit(limit).all()


def update_trainer(db: Session, trainer_id: int, trainer: TrainerUpdate):
    db_trainer = db.query(Trainer).filter(Trainer.id == trainer_id, Trainer.is_deleted == False).first()
    if not db_trainer:
        return None

    for key, value in trainer.model_dump(exclude_unset=True).items():
        setattr(db_trainer, key, value)

    db_trainer.last_modified_date = datetime.now()
    db.commit()
    db.refresh(db_trainer)
    return db_trainer


def delete_trainer(db: Session, trainer_id: int, deleted_by: str):
    db_trainer = db.query(Trainer).filter(Trainer.id == trainer_id, Trainer.is_deleted == False).first()
    if not db_trainer:
        return None

    db_trainer.is_deleted = True
    db_trainer.deleted_by = deleted_by
    db_trainer.deleted_date = datetime.now()
    db.commit()
    return db_trainer





def create_package(db: Session, package: schemas.PackageCreate):
    db_package = Package(**package.model_dump())
    db.add(db_package)
    db.commit()
    db.refresh(db_package)
    return db_package

def get_package(db: Session, package_id: int):
    return db.query(Package).filter(Package.id == package_id, Package.is_deleted == False).first()

def get_all_packages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Package).filter(Package.is_deleted == False).offset(skip).limit(limit).all()

def update_package(db: Session, package_id: int, package: schemas.PackageUpdate):
    db_package = db.query(Package).filter(Package.id == package_id, Package.is_deleted == False).first()
    if not db_package:
        return None
    for key, value in package.model_dump(exclude_unset=True).items():
        setattr(db_package, key, value)
    db.commit()
    db.refresh(db_package)
    return db_package

def delete_package(db: Session, package_id: int, deleted_by: str):
    db_package = db.query(Package).filter(Package.id == package_id, Package.is_deleted == False).first()
    if not db_package:
        return None
    db_package.is_deleted = True
    db_package.deleted_by = deleted_by
    db.commit()
    return db_package

def create_promotion(db: Session, promotion: PromotionCreate) -> Promotion:
    db_promotion = Promotion(**promotion.model_dump())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


def get_promotion(db: Session, promotion_id: int) -> Promotion | None:
    return db.query(Promotion).filter(Promotion.id == promotion_id, Promotion.is_deleted == False).first()


def get_all_promotions(db: Session, skip: int = 0, limit: int = 100) -> list[Promotion]:
    return db.query(Promotion).filter(Promotion.is_deleted == False).offset(skip).limit(limit).all()


def update_promotion(db: Session, promotion_id: int, promotion: PromotionUpdate) -> Promotion | None:
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id, Promotion.is_deleted == False).first()
    if not db_promotion:
        return None

    for key, value in promotion.model_dump(exclude_unset=True).items():
        setattr(db_promotion, key, value)

    db_promotion.last_modified_date = datetime.now()
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


def delete_promotion(db: Session, promotion_id: int, deleted_by: str) -> Promotion | None:
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id, Promotion.is_deleted == False).first()
    if not db_promotion:
        return None

    db_promotion.is_deleted = True
    db_promotion.deleted_by = deleted_by
    db_promotion.deleted_date = datetime.now()
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


def create_material(db: Session, material: MaterialCreate) -> Material:
    db_material = Material(**material.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def get_material(db: Session, material_id: int) -> Material | None:
    return db.query(Material).filter(Material.id == material_id, Material.is_deleted == False).first()


def get_all_materials(db: Session, skip: int = 0, limit: int = 100) -> list[Material]:
    return db.query(Material).filter(Material.is_deleted == False).offset(skip).limit(limit).all()


def update_material(db: Session, material_id: int, material: MaterialUpdate) -> Material | None:
    db_material = db.query(Material).filter(Material.id == material_id, Material.is_deleted == False).first()
    if not db_material:
        return None

    for key, value in material.model_dump(exclude_unset=True).items():
        setattr(db_material, key, value)

    db_material.last_modified_date = datetime.now()
    db.commit()
    db.refresh(db_material)
    return db_material


def delete_material(db: Session, material_id: int, deleted_by: str) -> Material | None:
    db_material = db.query(Material).filter(Material.id == material_id, Material.is_deleted == False).first()
    if not db_material:
        return None

    db_material.is_deleted = True
    db_material.deleted_by = deleted_by
    db_material.deleted_date = datetime.now()
    db.commit()
    db.refresh(db_material)
    return db_material

from sqlalchemy.orm import Session
from datetime import datetime
from models import User
from schemas import UserCreate, UserUpdate
import bcrypt


def create_user(db: Session, user: UserCreate) -> User:
    # Hash the password before saving
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    db_user = User(
        email=user.email,
        password_hash=hashed_password,
        role=user.role,
        created_by=user.created_by
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id, User.is_deleted == False).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).filter(User.is_deleted == False).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserUpdate) -> User | None:
    db_user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
    if db_user is None:
        return None

    update_data = user.model_dump(exclude_unset=True)
    if "password" in update_data:
        update_data["password_hash"] = bcrypt.hashpw(update_data.pop("password").encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db_user.last_modified_date = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int, deleted_by: str) -> User | None:
    db_user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
    if db_user is None:
        return None

    db_user.is_deleted = True
    db_user.deleted_by = deleted_by
    db_user.deleted_date = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user

@staticmethod
def generate_member_id(session: Session, branch_code: str) -> str:
    last_member = (
        session.query(Member)
        .filter(Member.id.like(f"{branch_code}%"))
        .order_by(Member.id.desc())
        .first()
    )

    if last_member:
        try:
            last_seq = int(last_member.id.replace(branch_code, ""))
        except ValueError:
            last_seq = 0
    else:
        last_seq = 0

    new_seq = last_seq + 1
    return f"{branch_code}{new_seq:03d}"
def create_member(db: Session, member: schemas.MemberCreate):
    member_id = generate_member_id(db, member.branch_code)
    member_data = member.model_dump()
    member_data["id"] = member_id
    del member_data["branch_code"]
    db_member = Member(**member_data)
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member

def get_member(db: Session, member_id: str):
    return db.query(Member).filter(Member.id == member_id, Member.is_deleted == False).first()

def get_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).filter(Member.is_deleted == False).offset(skip).limit(limit).all()

def update_member(db: Session, member_id: str, member: schemas.MemberUpdate):
    db_member = db.query(Member).filter(Member.id == member_id, Member.is_deleted == False).first()
    if not db_member:
        return None

    update_data = member.model_dump(exclude_unset=True)

    # Optional: Handle branch_code and regenerate member_id
    branch_code = update_data.pop("branch_code", None)
    if branch_code:
        new_member_id = Member.generate_member_id(db, branch_code)
        db_member.id = new_member_id

    for key, value in update_data.items():
        setattr(db_member, key, value)

    db.commit()
    db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_id: str, deleted_by: str):
    db_member = db.query(Member).filter(Member.id == member_id, Member.is_deleted == False).first()
    if not db_member:
        return None
    db_member.is_deleted = True
    db_member.deleted_by = deleted_by
    db.commit()
    return db_member


def create_payment(db: Session, payment: PaymentCreate) -> Payment:
    db_payment = Payment(**payment.model_dump())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def get_payments(db: Session, skip: int = 0, limit: int = 100) -> list[Payment]:
    return db.query(Payment).filter(Payment.is_deleted == False).offset(skip).limit(limit).all()


def get_payment(db: Session, payment_id: int) -> Payment | None:
    return db.query(Payment).filter(Payment.id == payment_id, Payment.is_deleted == False).first()


def update_payment(db: Session, payment_id: int, payment: PaymentUpdate) -> Payment | None:
    db_payment = db.query(Payment).filter(Payment.id == payment_id, Payment.is_deleted == False).first()
    if not db_payment:
        return None

    for key, value in payment.model_dump(exclude_unset=True).items():
        setattr(db_payment, key, value)

    db_payment.last_modified_date = datetime.now()
    db.commit()
    db.refresh(db_payment)
    return db_payment


def delete_payment(db: Session, payment_id: int, deleted_by: str) -> Payment | None:
    db_payment = db.query(Payment).filter(Payment.id == payment_id, Payment.is_deleted == False).first()
    if not db_payment:
        return None

    db_payment.is_deleted = True
    db_payment.deleted_by = deleted_by
    db_payment.deleted_date = datetime.now()
    db.commit()
    db.refresh(db_payment)
    return db_payment

def create_reminder_setting(db: Session, setting: ReminderSettingCreate) -> ReminderSetting:
    db_setting = ReminderSetting(**setting.model_dump())
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting


def get_reminder_settings(db: Session, skip: int = 0, limit: int = 100) -> list[ReminderSetting]:
    return db.query(ReminderSetting)\
             .filter(ReminderSetting.is_deleted == False)\
             .offset(skip).limit(limit).all()


def get_reminder_setting(db: Session, setting_id: int) -> ReminderSetting | None:
    return db.query(ReminderSetting)\
             .filter(ReminderSetting.id == setting_id, ReminderSetting.is_deleted == False)\
             .first()


def update_reminder_setting(db: Session, setting_id: int, setting: ReminderSettingUpdate) -> ReminderSetting | None:
    db_setting = db.query(ReminderSetting)\
                   .filter(ReminderSetting.id == setting_id, ReminderSetting.is_deleted == False)\
                   .first()
    if not db_setting:
        return None

    for key, value in setting.model_dump(exclude_unset=True).items():
        setattr(db_setting, key, value)
    db_setting.last_modified_date = datetime.now()
    db.commit()
    db.refresh(db_setting)
    return db_setting


def delete_reminder_setting(db: Session, setting_id: int, deleted_by: str) -> ReminderSetting | None:
    db_setting = db.query(ReminderSetting)\
                   .filter(ReminderSetting.id == setting_id, ReminderSetting.is_deleted == False)\
                   .first()
    if not db_setting:
        return None

    db_setting.is_deleted = True
    db_setting.deleted_by = deleted_by
    db_setting.deleted_date = datetime.now()
    db.commit()
    db.refresh(db_setting)
    return db_setting
def create_batch(db: Session, batch: BatchCreate) -> Batch:
    db_batch = Batch(**batch.model_dump())
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch


def get_batch(db: Session, batch_id: int) -> Batch | None:
    return db.query(Batch).filter(Batch.id == batch_id, Batch.is_deleted == False).first()


def get_all_batches(db: Session, skip: int = 0, limit: int = 100) -> list[Batch]:
    return db.query(Batch).filter(Batch.is_deleted == False).offset(skip).limit(limit).all()


def update_batch(db: Session, batch_id: int, batch_update: BatchUpdate) -> Batch | None:
    db_batch = db.query(Batch).filter(Batch.id == batch_id, Batch.is_deleted == False).first()
    if not db_batch:
        return None

    for field, value in batch_update.model_dump(exclude_unset=True).items():
        setattr(db_batch, field, value)

    db_batch.last_modified_date = datetime.now()
    db.commit()
    db.refresh(db_batch)
    return db_batch


def delete_batch(db: Session, batch_id: int, deleted_by: str) -> Batch | None:
    db_batch = db.query(Batch).filter(Batch.id == batch_id, Batch.is_deleted == False).first()
    if not db_batch:
        return None

    db_batch.is_deleted = True
    db_batch.deleted_by = deleted_by
    db_batch.deleted_date = datetime.now()
    db.commit()
    return db_batch
