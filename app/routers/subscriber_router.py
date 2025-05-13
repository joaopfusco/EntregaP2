from fastapi import APIRouter, Depends
from rabbitmq.subscriber_db import subscribe as subscribe_db
from rabbitmq.subscriber_email import subscribe as subscribe_email
from rabbitmq.subscriber_sms import subscribe as subscribe_sms

subscriber_router = APIRouter(
    prefix="/subscribers", 
    tags=["Subscribers"]
)

@subscriber_router.get("/db/")
def subscriber_db():
    subscribe_db()

@subscriber_router.get("/email/")
def subscriber_email():
    subscribe_email()

@subscriber_router.get("/sms/")
def subscriber_sms():
    subscribe_sms()