from collections import defaultdict

def calcular_factura_septiembre(datos):
    resultados = defaultdict(lambda: {'ea': 0, 'ee1': 0, 'ee2': 0, 'ec': 0})

    # Agrupar los datos por id_service
    datos_por_servicio = defaultdict(list)

    for id_service, date, consumo, inyeccion, valor_xm, cu, c in datos:
        datos_por_servicio[id_service].append((consumo, inyeccion, cu, c, valor_xm))

    # Calcular los valores para cada id_service
    for id_service, datos_servicio in datos_por_servicio.items():
        consumo_total = sum(consumo for consumo, _, _, _, _ in datos_servicio)
        inyeccion_total = sum(inyeccion for _, inyeccion, _, _, _ in datos_servicio)

        ea, ec = calcular_ea_ec(datos_servicio)
        ee1 = calcular_ee1(consumo_total, inyeccion_total, datos_servicio)
        ee2 = calcular_ee2(consumo_total, inyeccion_total, datos_servicio)

        resultados[id_service] = {'ea': ea, 'ee1': ee1, 'ee2': ee2, 'ec': ec}

    return resultados

def calcular_ea_ec(datos):
    ea = sum(cu * consumo for consumo, _, cu, _, _ in datos)
    ec = sum(c * inyeccion for _, inyeccion, _, c, _ in datos)
    return ea, ec

def calcular_ee1(consumo_total, inyeccion_total, datos):
    if inyeccion_total <= consumo_total:
        ee1 = -sum(cu * inyeccion for _, inyeccion, cu, _, _ in datos)
    else:
        ee1 = -sum(cu * consumo for consumo, _, cu, _, _ in datos)
    return ee1

def calcular_ee2(consumo_total, inyeccion_total, datos):
    if inyeccion_total <= consumo_total:
        return 0
    else:
        ee2 = sum(((inyeccion - consumo) * - valor_xm for consumo, inyeccion, _, _, valor_xm in datos))
        return ee2