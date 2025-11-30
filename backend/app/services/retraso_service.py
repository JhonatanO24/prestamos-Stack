from datetime import datetime

def calcular_retraso_en_dias(fecha_esperada: datetime, fecha_real: datetime) -> int:
    """
    Retorna:
    - 0 si no hay retraso
    - Número positivo de días si hay retraso
    """
    diferencia = fecha_real.date() - fecha_esperada.date()
    dias = diferencia.days

    if dias < 0:
        return 0

    return dias
