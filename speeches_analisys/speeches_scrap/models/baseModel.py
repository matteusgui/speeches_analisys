from pydantic import BaseModel, ConfigDict


class BaseClass(BaseModel):
    model_config = ConfigDict(populate_by_name=True,
                              frozen=True)
