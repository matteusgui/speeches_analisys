from pydantic import Field
from . import base_model


class Deputado(base_model.BaseClass):
    '''Represents a deputy'''
    Id: int = Field(alias='id')
    uri: str = Field(alias="uri")
    nome: str = Field(alias="nome")
    sigla_partido: str = Field(alias="siglaPartido")
    uri_partido: str = Field(alias="uriPartido")
    sigla_uf: str = Field(alias="siglaUf")
    id_legislatura: int = Field(alias="idLegislatura")
    url_foto: str | None = Field(alias="urlFoto")
    email: str | None = Field(alias="email")

    def to_list(self) -> list[str | int | None]:
        return [self.Id,
                self.uri,
                self.nome,
                self.sigla_partido,
                self.uri_partido,
                self.sigla_uf,
                self.id_legislatura,
                self.url_foto,
                self.email]

    @classmethod
    def get_variables(cls):
        return ["IdDeputado",
                "uri",
                "nome",
                "siglaPartido",
                "uriPartido",
                "siglaUf",
                "idLegislatura",
                "urlFoto",
                "email"]
