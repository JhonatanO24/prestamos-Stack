from datetime import datetime, timedelta
from app.services.retraso_service import calcular_retraso_en_dias

def test_sin_retraso():
    fecha_esperada = datetime.now()
    fecha_real = datetime.now()

    retraso = calcular_retraso_en_dias(fecha_esperada, fecha_real)
    assert retraso == 0


def test_con_retraso_de_5_dias():
    fecha_esperada = datetime.now()
    fecha_real = fecha_esperada + timedelta(days=5)

    retraso = calcular_retraso_en_dias(fecha_esperada, fecha_real)
    assert retraso == 5


def test_entrega_antes_de_tiempo():
    fecha_esperada = datetime.now()
    fecha_real = fecha_esperada - timedelta(days=3)

    retraso = calcular_retraso_en_dias(fecha_esperada, fecha_real)
    assert retraso == 0
