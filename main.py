from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
import services, schemas
from db import get_db

app = FastAPI()

@app.post("/branches/", response_model=schemas.Branch)
def create(branch: schemas.BranchCreate, db: Session = Depends(get_db)):
    return services.create_branch(db, branch)

@app.get("/branches/{branch_id}", response_model=schemas.Branch)
def read(branch_id: int, db: Session = Depends(get_db)):
    branch = services.get_branch(db, branch_id)
    if not branch:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch

@app.get("/branches/", response_model=list[schemas.Branch])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_branches(db, skip=skip, limit=limit)

@app.put("/branches/{branch_id}", response_model=schemas.Branch)
def update(branch_id: int, branch: schemas.BranchUpdate, db: Session = Depends(get_db)):
    updated = services.update_branch(db, branch_id, branch)
    if not updated:
        raise HTTPException(status_code=404, detail="Branch not found")
    return updated

@app.delete("/branches/{branch_id}", response_model=schemas.Branch)
def soft_delete(branch_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_branch(db, branch_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Branch not found or already deleted")
    return deleted



@app.post("/trainers/", response_model=schemas.Trainer)
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    return services.create_trainer(db, trainer)

@app.get("/trainers/{trainer_id}", response_model=schemas.Trainer)
def get_trainer(trainer_id: int, db: Session = Depends(get_db)):
    trainer = services.get_trainer(db, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return trainer

@app.get("/trainers/", response_model=list[schemas.Trainer])
def get_all_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_trainers(db, skip=skip, limit=limit)

@app.put("/trainers/{trainer_id}", response_model=schemas.Trainer)
def update_trainer(trainer_id: int, trainer: schemas.TrainerUpdate, db: Session = Depends(get_db)):
    updated = services.update_trainer(db, trainer_id, trainer)
    if not updated:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return updated

@app.delete("/trainers/{trainer_id}", response_model=schemas.Trainer)
def delete_trainer(trainer_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_trainer(db, trainer_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Trainer not found or already deleted")
    return deleted

@app.post("/batches/", response_model=schemas.Batch)
def create_batch(batch: schemas.BatchCreate, db: Session = Depends(get_db)):
    return services.create_batch(db, batch)

@app.get("/batches/{batch_id}", response_model=schemas.Batch)
def read_batch(batch_id: int, db: Session = Depends(get_db)):
    db_batch = services.get_batch(db, batch_id)
    if not db_batch:
        raise HTTPException(status_code=404, detail="Batch not found")
    return db_batch

@app.get("/batches/", response_model=list[schemas.Batch])
def read_batches(db: Session = Depends(get_db)):
    return services.get_all_batches(db)

@app.put("/batches/{batch_id}", response_model=schemas.Batch)
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


@app.post("/packages/", response_model=schemas.Package)
def create_package(package: schemas.PackageCreate, db: Session = Depends(get_db)):
    return services.create_package(db, package)

@app.get("/packages/{package_id}", response_model=schemas.Package)
def get_package(package_id: int, db: Session = Depends(get_db)):
    package = services.get_package(db, package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package

@app.get("/packages/", response_model=list[schemas.Package])
def get_all_packages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_packages(db, skip=skip, limit=limit)

@app.put("/packages/{package_id}", response_model=schemas.Package)
def update_package(package_id: int, package: schemas.PackageUpdate, db: Session = Depends(get_db)):
    updated = services.update_package(db, package_id, package)
    if not updated:
        raise HTTPException(status_code=404, detail="Package not found")
    return updated

@app.delete("/packages/{package_id}", response_model=schemas.Package)
def delete_package(package_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_package(db, package_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Package not found or already deleted")
    return deleted

@app.post("/promotions/", response_model=schemas.Promotion)
def create_promotion(promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    return services.create_promotion(db, promotion)


@app.get("/promotions/{promotion_id}", response_model=schemas.Promotion)
def get_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = services.get_promotion(db, promotion_id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion


@app.get("/promotions/", response_model=list[schemas.Promotion])
def get_all_promotions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_promotions(db, skip=skip, limit=limit)


@app.put("/promotions/{promotion_id}", response_model=schemas.Promotion)
def update_promotion(promotion_id: int, promotion: schemas.PromotionUpdate, db: Session = Depends(get_db)):
    updated = services.update_promotion(db, promotion_id, promotion)
    if not updated:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return updated


@app.delete("/promotions/{promotion_id}", response_model=schemas.Promotion)
def delete_promotion(promotion_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_promotion(db, promotion_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="Promotion not found or already deleted")
    return deleted


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = services.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/", response_model=list[schemas.User])
def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_all_users(db, skip=skip, limit=limit)


@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = services.update_user(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, deleted_by: str, db: Session = Depends(get_db)):
    deleted = services.delete_user(db, user_id, deleted_by)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found or already deleted")
    return deleted



@app.post("/members/", response_model=schemas.MemberOut)
def create_member(member: schemas.MemberCreate, db: Session = Depends(get_db)):
    return services.create_member(db, member)


@app.get("/members/", response_model=list[schemas.MemberOut])
def read_members(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_members(db, skip, limit)


@app.get("/members/{member_id}", response_model=schemas.MemberOut)
def read_member(member_id: int, db: Session = Depends(get_db)):
    db_member = services.get_member(db, member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@app.put("/members/{member_id}", response_model=schemas.MemberOut)
def update_member(member_id: int, member: schemas.MemberUpdate, db: Session = Depends(get_db)):
    db_member = services.update_member(db, member_id, member)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member


@app.delete("/members/{member_id}")
def delete_member(member_id: int, deleted_by: str, db: Session = Depends(get_db)):
    db_member = services.delete_member(db, member_id, deleted_by)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"detail": "Member soft-deleted successfully"}



@app.post("/payments/", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    return services.create_payment(db, payment)


@app.get("/payments/", response_model=list[schemas.PaymentOut])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_payments(db, skip, limit)


@app.get("/payments/{payment_id}", response_model=schemas.PaymentOut)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = services.get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment


@app.put("/payments/{payment_id}", response_model=schemas.PaymentOut)
def update_payment(payment_id: int, payment: schemas.PaymentUpdate, db: Session = Depends(get_db)):
    db_payment = services.update_payment(db, payment_id, payment)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment


@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int, deleted_by: str, db: Session = Depends(get_db)):
    db_payment = services.delete_payment(db, payment_id, deleted_by)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"detail": "Payment soft-deleted successfully"}


@app.post("/reminder-settings/", response_model=schemas.ReminderSettingOut)
def create_reminder_setting(setting: schemas.ReminderSettingCreate, db: Session = Depends(get_db)):
    return services.create_reminder_setting(db, setting)


@app.get("/reminder-settings/", response_model=list[schemas.ReminderSettingOut])
def read_reminder_settings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.get_reminder_settings(db, skip, limit)


@app.get("/reminder-settings/{setting_id}", response_model=schemas.ReminderSettingOut)
def read_reminder_setting(setting_id: int, db: Session = Depends(get_db)):
    db_setting = services.get_reminder_setting(db, setting_id)
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Reminder setting not found")
    return db_setting


@app.put("/reminder-settings/{setting_id}", response_model=schemas.ReminderSettingOut)
def update_reminder_setting(setting_id: int, setting: schemas.ReminderSettingUpdate, db: Session = Depends(get_db)):
    db_setting = services.update_reminder_setting(db, setting_id, setting)
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Reminder setting not found")
    return db_setting


@app.delete("/reminder-settings/{setting_id}")
def delete_reminder_setting(setting_id: int, deleted_by: str, db: Session = Depends(get_db)):
    db_setting = services.delete_reminder_setting(db, setting_id, deleted_by)
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Reminder setting not found")
    return {"detail": "Reminder setting soft-deleted successfully"}