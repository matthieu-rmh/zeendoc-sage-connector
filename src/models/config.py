from redis_om import JsonModel, Migrator, Field
from typing import Optional

class Config(JsonModel):
    id: int = Field(index=True)
    cupboard: int
    suppliers_sync: Optional[int] = None
    account_gateway: Optional[int] = None
    payment_informations: Optional[int] = None
    payment_voucher: Optional[int] = None
    name: Optional[str] = None
    coll_id: Optional[str] = None
    tech_account_login: Optional[str] = None
    tech_account_pwd: Optional[str] = None
    sage_base_url: Optional[str] = None
    sage_login: Optional[str] = None
    sage_pwd: Optional[str] = None
    sage_company: Optional[str] = None
    suppliers_sync_enabled: Optional[bool] = None
    payment_voucher_enabled: Optional[bool] = None
