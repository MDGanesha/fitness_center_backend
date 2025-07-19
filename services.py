from sqlalchemy.orm import Session
from models import Branch, Trainer, Package, Promotion, Material, User, Member, Payment, ReminderSetting, Batch
import schemas
from datetime import datetime

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
    for key, value in branch_data.model_dump(exclude_unset=True).items():
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

from schemas import TrainerCreate, TrainerUpdate

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
    for key, value in trainer.data.model_dump().items():
        setattr(db_trainer, key, value)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer

def delete_trainer(db: Session, trainer_id: int, deleted_by: str):
    db_trainer = db.query(Trainer).filter(Trainer.id == trainer_id, Trainer.is_deleted == False).first()
    if not db_trainer:
        return None
    db_trainer.is_deleted = True
    db_trainer.deleted_by = deleted_by
    db_trainer.deleted_date = datetime.utcnow()
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
    db_package.deleted_date = datetime.utcnow()
    db.commit()
    db.refresh(db_package)
    return db_package

def create_promotion(db: Session, promotion: schemas.PromotionCreate):
    db_promotion = Promotion(**promotion.model_dump())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion


def get_promotion(db: Session, promotion_id: int):
    return db.query(Promotion).filter(Promotion.id == promotion_id, Promotion.is_deleted == False).first()


def get_all_promotions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Promotion).filter(Promotion.is_deleted == False).offset(skip).limit(limit).all()


def update_promotion(db: Session, promotion_id: int, promotion: schemas.PromotionUpdate):
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id, Promotion.is_deleted == False).first()
    if db_promotion:
        for key, value in promotion.model_dump(exclude_unset=True).items():
            setattr(db_promotion, key, value)
        db.commit()
        db.refresh(db_promotion)
    return db_promotion


def delete_promotion(db: Session, promotion_id: int, deleted_by: str):
    db_promotion = db.query(Promotion).filter(Promotion.id == promotion_id, Promotion.is_deleted == False).first()
    if db_promotion:
        db_promotion.is_deleted = True
        db_promotion.deleted_by = deleted_by
        db_promotion.deleted_date = datetime.utcnow()
        db.commit()
        db.refresh(db_promotion)
    return db_promotion


def create_material(db: Session, material: schemas.MaterialCreate):
    db_material = Material(**material.data.model_dump())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def get_material(db: Session, material_id: int):
    return db.query(Material).filter(Material.id == material_id, Material.is_deleted == False).first()


def get_all_materials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Material).filter(Material.is_deleted == False).offset(skip).limit(limit).all()


def update_material(db: Session, material_id: int, material: schemas.MaterialUpdate):
    db_material = db.query(Material).filter(Material.id == material_id, Material.is_deleted == False).first()
    if not db_material:
        return None
    for key, value in material.model_dump(exclude_unset=True).items():
        setattr(db_material, key, value)
    db.commit()
    db.refresh(db_material)
    return db_material


def delete_material(db: Session, material_id: int, deleted_by: str):
    db_material = db.query(Material).filter(Material.id == material_id, Material.is_deleted == False).first()
    if not db_material:
        return None
    db_material.is_deleted = True
    db_material.deleted_by = deleted_by
    db_material.deleted_date = datetime.now()
    db.commit()
    return db_material

def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id, User.is_deleted == False).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).filter(User.is_deleted == False).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
    if db_user is None:
        return None

    for key, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int, deleted_by: str):
    db_user = db.query(User).filter(User.id == user_id, User.is_deleted == False).first()
    if db_user is None:
        return None

    db_user.is_deleted = True
    db_user.deleted_by = deleted_by
    from datetime import datetime
    db_user.deleted_date = datetime.now()

    db.commit()
    db.refresh(db_user)
    return db_user


def create_member(db: Session, member: schemas.MemberCreate):
    db_member = Member(**member.model_dump())
    db.add(db_member)
    db.commit()
    db.refresh(db_member)
    return db_member


def get_members(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Member).filter(Member.is_deleted == False).offset(skip).limit(limit).all()


def get_member(db: Session, member_id: int):
    return db.query(Member).filter(Member.id == member_id, Member.is_deleted == False).first()


def update_member(db: Session, member_id: int, member: schemas.MemberUpdate):
    db_member = db.query(Member).filter(Member.id == member_id, Member.is_deleted == False).first()
    if db_member:
        for key, value in member.model_dump(exclude_unset=True).items():
            setattr(db_member, key, value)
        db.commit()
        db.refresh(db_member)
    return db_member


def delete_member(db: Session, member_id: int, deleted_by: str):
    db_member = db.query(Member).filter(Member.id == member_id, Member.is_deleted == False).first()
    if db_member:
        db_member.is_deleted = True
        db_member.deleted_by = deleted_by
        db.commit()
    return db_member

def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = Payment(**payment.model_dump())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Payment).filter(Payment.is_deleted == False).offset(skip).limit(limit).all()


def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id, Payment.is_deleted == False).first()


def update_payment(db: Session, payment_id: int, payment: schemas.PaymentUpdate):
    db_payment = db.query(Payment).filter(Payment.id == payment_id, Payment.is_deleted == False).first()
    if db_payment:
        for key, value in payment.model_dump(exclude_unset=True).items():
            setattr(db_payment, key, value)
        db.commit()
        db.refresh(db_payment)
    return db_payment


def delete_payment(db: Session, payment_id: int, deleted_by: str):
    db_payment = db.query(Payment).filter(Payment.id == payment_id, Payment.is_deleted == False).first()
    if db_payment:
        db_payment.is_deleted = True
        db_payment.deleted_by = deleted_by
        db.commit()
    return db_payment


def create_reminder_setting(db: Session, setting: schemas.ReminderSettingCreate):
    db_setting = ReminderSetting(**setting.model_dump())
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting


def get_reminder_settings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ReminderSetting).filter(ReminderSetting.is_deleted == False).offset(skip).limit(limit).all()


def get_reminder_setting(db: Session, setting_id: int):
    return db.query(ReminderSetting).filter(ReminderSetting.id == setting_id, ReminderSetting.is_deleted == False).first()


def update_reminder_setting(db: Session, setting_id: int, setting: schemas.ReminderSettingUpdate):
    db_setting = db.query(ReminderSetting).filter(ReminderSetting.id == setting_id, ReminderSetting.is_deleted == False).first()
    if db_setting:
        for key, value in setting.model_dump(exclude_unset=True).items():
            setattr(db_setting, key, value)
        db.commit()
        db.refresh(db_setting)
    return db_setting


def delete_reminder_setting(db: Session, setting_id: int, deleted_by: str):
    db_setting = db.query(ReminderSetting).filter(ReminderSetting.id == setting_id, ReminderSetting.is_deleted == False).first()
    if db_setting:
        db_setting.is_deleted = True
        db_setting.deleted_by = deleted_by
        db.commit()
    return db_setting


def create_batch(db: Session, batch: schemas.BatchCreate):
    db_batch = Batch(**batch.model_dump())
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch

def get_batch(db: Session, batch_id: int):
    return db.query(Batch).filter(Batch.id == batch_id, Batch.is_deleted == False).first()

def get_all_batches(db: Session):
    return db.query(Batch).filter(Batch.is_deleted == False).all()

def update_batch(db: Session, batch_id: int, batch_update: schemas.BatchUpdate):
    db_batch = db.query(Batch).filter(Batch.id == batch_id, Batch.is_deleted == False).first()
    if not db_batch:
        return None
    for field, value in batch_update.model_dump(exclude_unset=True).items():
        setattr(db_batch, field, value)
    db_batch.last_modified_date = datetime.utcnow()
    db.commit()
    db.refresh(db_batch)
    return db_batch

def delete_batch(db: Session, batch_id: int, deleted_by: str):
    db_batch = db.query(Batch).filter(Batch.id == batch_id, Batch.is_deleted == False).first()
    if not db_batch:
        return None
    db_batch.is_deleted = True
    db_batch.deleted_by = deleted_by
    db_batch.deleted_date = datetime.utcnow()
    db.commit()
    return db_batch