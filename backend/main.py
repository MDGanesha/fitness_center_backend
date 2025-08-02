from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import services
import schemas
from db import get_db

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BRANCH ROUTES
@app.post("/branches/", response_model=schemas.BranchOut)
def create_branch(branch: schemas.BranchCreate, db: Session = Depends(get_db)):
    return services.create_branch(db, branch)

@app.get("/branches/{branch_id}", response_model=schemas.BranchOut)
def get_branch(branch_id: int, db: Session = Depends(get_db)):
    branch = services.get_branch(db, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch

@app.get("/branches/", response_model=List[schemas.BranchOut])
def get_all_branches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_branches(db, skip, limit)

@app.put("/branches/{branch_id}", response_model=schemas.BranchOut)
def update_branch(branch_id: int, branch: schemas.BranchUpdate, db: Session = Depends(get_db)):
    updated = services.update_branch(db, branch_id, branch)
    if not updated:
        raise HTTPException(status_code=404, detail="Branch not found")
    return updated

@app.delete("/branches/{branch_id}", response_model=schemas.BranchOut)
def delete_branch(branch_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_branch(db, branch_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Branch not found or already deleted")
    return deleted

# TRAINER ROUTES
@app.post("/trainers/", response_model=schemas.TrainerOut)
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    return services.create_trainer(db, trainer)

@app.get("/trainers/{trainer_id}", response_model=schemas.TrainerOut)
def get_trainer(trainer_id: int, db: Session = Depends(get_db)):
    trainer = services.get_trainer(db, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return trainer

@app.get("/trainers/", response_model=List[schemas.TrainerOut])
def get_all_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_trainers(db, skip, limit)

@app.put("/trainers/{trainer_id}", response_model=schemas.TrainerOut)
def update_trainer(trainer_id: int, trainer: schemas.TrainerUpdate, db: Session = Depends(get_db)):
    updated = services.update_trainer(db, trainer_id, trainer)
    if not updated:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return updated

@app.delete("/trainers/{trainer_id}", response_model=schemas.TrainerOut)
def delete_trainer(trainer_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_trainer(db, trainer_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Trainer not found or already deleted")
    return deleted

# BATCH ROUTES
@app.post("/batches/", response_model=schemas.BatchOut)
def create_batch(batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    return services.create_batch(db, batch)

@app.get("/batches/{batch_id}", response_model=schemas.BatchOut)
def get_batch(batch_id: int, db: Session = Depends(get_db)):
    batch = services.get_batch(db, batch_id)
    if not batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return batch

@app.get("/batches/", response_model=List[schemas.BatchOut])
def get_all_batches(db: Session = Depends(get_db)):
    return services.get_all_batches(db)

@app.put("/batches/{batch_id}", response_model=schemas.BatchOut)
def update_batch(batch_id: int, batch: schemas.BatchUpdate, db: Session = Depends(get_db)):
    updated = services.update_batch(db, batch_id, batch)
    if not updated:
        raise HTTPException(status_code=404, detail="Batch not found")
    return updated

@app.delete("/batches/{batch_id}")
def delete_batch(batch_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_batch(db, batch_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Batch not found")
    return {"message": "Batch deleted successfully"}

# PACKAGE ROUTES

@app.post("/packages/", response_model=schemas.PackageOut)
def create_package(package: schemas.PackageCreate, db: Session = Depends(get_db)):
    return services.create_package(db, package)

@app.get("/packages/{package_id}", response_model=schemas.PackageOut)
def get_package(package_id: int, db: Session = Depends(get_db)):
    package = services.get_package(db, package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package

@app.get("/packages/", response_model=List[schemas.PackageOut])
def get_all_packages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_packages(db, skip, limit)

@app.put("/packages/{package_id}", response_model=schemas.PackageOut)
def update_package(package_id: int, package: schemas.PackageUpdate, db: Session = Depends(get_db)):
    updated = services.update_package(db, package_id, package)
    if not updated:
        raise HTTPException(status_code=404, detail="Package not found")
    return updated

@app.delete("/packages/{package_id}", response_model=schemas.PackageOut)
def delete_package(package_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_package(db, package_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Package not found or already deleted")
    return deleted

# PROMOTION ROUTES
@app.post("/promotions/", response_model=schemas.PromotionOut)
def create_promotion(promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    return services.create_promotion(db, promotion)

@app.get("/promotions/{promotion_id}", response_model=schemas.PromotionOut)
def get_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = services.get_promotion(db, promotion_id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion

@app.get("/promotions/", response_model=List[schemas.PromotionOut])
def get_all_promotions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_promotions(db, skip, limit)

@app.put("/promotions/{promotion_id}", response_model=schemas.PromotionOut)
def update_promotion(promotion_id: int, promotion: schemas.PromotionUpdate, db: Session = Depends(get_db)):
    updated = services.update_promotion(db, promotion_id, promotion)
    if not updated:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return updated

@app.delete("/promotions/{promotion_id}", response_model=schemas.PromotionOut)
def delete_promotion(promotion_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_promotion(db, promotion_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Promotion not found or already deleted")
    return deleted

# USER ROUTES
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = services.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=List[schemas.UserOut])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_users(db, skip, limit)

@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = services.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@app.delete("/users/{user_id}", response_model=schemas.UserOut)
def delete_user(user_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_user(db, user_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found or already deleted")
    return deleted

# MEMBER ROUTES

@app.post("/members/", response_model=schemas.MemberOut)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return services.create_member(db, member)

@app.get("/members/", response_model=List[schemas.MemberOut])
def get_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_members(db, skip, limit)

@app.get("/members/{member_id}", response_model=schemas.MemberOut)
def get_member(member_id: str, db: Session = Depends(get_db)):
    member = services.get_member(db, member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@app.put("/members/{member_id}", response_model=schemas.MemberOut)
def update_member(member_id: str, member: schemas.MemberUpdate, db: Session = Depends(get_db)):
    updated = services.update_member(db, member_id, member)
    if not updated:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated

@app.delete("/members/{member_id}")
def delete_member(member_id: str, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_member(db, member_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"detail": "Member soft-deleted successfully"}

# PAYMENT ROUTES
@app.post("/payments/", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return services.create_payment(db, payment)

@app.get("/payments/", response_model=List[schemas.PaymentOut])
def get_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_payments(db, skip, limit)

@app.get("/payments/{payment_id}", response_model=schemas.PaymentOut)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = services.get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.put("/payments/{payment_id}", response_model=schemas.PaymentOut)
def update_payment(payment_id: int, payment: schemas.PaymentUpdate, db: Session = Depends(get_db)):
    updated = services.update_payment(db, payment_id, payment)
    if not updated:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated

@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_payment(db, payment_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"detail": "Payment soft-deleted successfully"}

# REMINDER SETTINGS ROUTES
@app.post("/reminder-settings/", response_model=schemas.ReminderSettingOut)
def create_reminder_setting(setting: schemas.ReminderSettingCreate, db: Session = Depends(get_db)):
    return services.create_reminder_setting(db, setting)

@app.get("/reminder-settings/", response_model=List[schemas.ReminderSettingOut])
def get_reminder_settings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_reminder_settings(db, skip, limit)

@app.get("/reminder-settings/{setting_id}", response_model=schemas.ReminderSettingOut)
def get_reminder_setting(setting_id: int, db: Session = Depends(get_db)):
    setting = services.get_reminder_setting(db, setting_id)
    if not setting:
        raise HTTPException(status_code=404, detail="Reminder setting not found")
    return setting

@app.put("/reminder-settings/{setting_id}", response_model=schemas.ReminderSettingOut)
def update_reminder_setting(setting_id: int, setting: schemas.ReminderSettingUpdate, db: Session = Depends(get_db)):
    updated = services.update_reminder_setting(db, setting_id, setting)
    if not updated:
        raise HTTPException(status_code=404, detail="Reminder setting not found")
    return updated

@app.delete("/reminder-settings/{setting_id}")
def delete_reminder_setting(setting_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_reminder_setting(db, setting_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Reminder setting not found")
    return {"detail": "Reminder setting soft-deleted successfully"}
