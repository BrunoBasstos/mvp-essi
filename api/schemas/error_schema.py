# schemas/error_schema.py
from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    message: str = "Mensagem de erro"
    code: int = 400
    detail: str = "Detalhes do erro"