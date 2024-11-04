from redis_om import JsonModel, Field
from typing import Optional

class Config(JsonModel):
    id: int = Field(index=True)
    cupboard: int = Field(index=True)
    name: Optional[str] = Field(index=True, default=None)
    coll_id: Optional[str] = Field(index=True, default=None)
    tech_account_login: Optional[str] = Field(index=True, default=None)
    tech_account_pwd: Optional[str] = Field(index=True, default=None)
    sage_base_url: Optional[str] = Field(index=True, default=None)
    sage_login: Optional[str] = Field(index=True, default=None)
    sage_pwd: Optional[str] = Field(index=True, default=None)
    sage_company: Optional[str] = Field(index=True, default=None)
    suppliers_sync: Optional[int] = Field(index=True, default=None)
    suppliers_sync_enabled: Optional[bool] = Field(index=True, default=None)
    account_gateway: Optional[int] = Field(index=True, default=None)
    account_gateway_enabled: Optional[bool] = Field(index=True, default=None)
    payment_informations: Optional[int] = Field(index=True, default=None)
    payment_voucher: Optional[int] = Field(index=True, default=None)
    payment_voucher_enabled: Optional[bool] = Field(index=True, default=None)
