
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class NivelCriticidad(str, Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"


class ExtraccionTecnica(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tecnologias: list[str] = Field(
        min_length=1,
        description="Tecnologías identificadas en el texto técnico.",
    )

    nivel_de_criticidad: NivelCriticidad = Field(
        description="Criticidad técnica: baja, media o alta.",
    )

    resumen_tecnico: str = Field(
        min_length=10,
        description="Resumen técnico claro y conciso.",
    )

    @field_validator("tecnologias")
    @classmethod
    def validar_tecnologias(cls, tecnologias: list[str]) -> list[str]:
        tecnologias_limpias = [
            tecnologia.strip()
            for tecnologia in tecnologias
            if tecnologia.strip()
        ]

        if not tecnologias_limpias:
            raise ValueError(
                "Debe identificarse al menos una tecnología."
            )

        return tecnologias_limpias

    @field_validator("resumen_tecnico")
    @classmethod
    def validar_resumen(cls, resumen: str) -> str:
        resumen = resumen.strip()

        if len(resumen) < 10:
            raise ValueError(
                "El resumen debe tener al menos 10 caracteres."
            )

        return resumen
