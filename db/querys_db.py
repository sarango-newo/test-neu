def obtener_datos(cursor, mes):
    cursor.execute("""
        SELECT
            r.id_service,
            r.record_timestamp,
            c.value AS consumo_energia,
            i.value AS inyeccion_energia,
            xm.value AS valor_xm,
            t.cu,
            t.c
        FROM
            records r
            INNER JOIN consumption c ON r.id_record = c.id_record
            INNER JOIN injection i ON r.id_record = i.id_record
            INNER JOIN services s ON r.id_service = s.id_service
            INNER JOIN xm_data_hourly_per_agent xm ON xm.record_timestamp = r.record_timestamp
            INNER JOIN tariffs t ON 
                s.id_market = t.id_market AND 
                (
                    (s.voltage_level IN (2, 3) AND s.voltage_level = t.voltage_level) OR
                    (s.voltage_level NOT IN (2, 3) AND (s.cdi = t.cdi AND s.voltage_level = t.voltage_level))
                )
                
        WHERE
            EXTRACT(MONTH FROM r.record_timestamp) = 9
            ORDER BY
                r.id_service
    """, (mes,))

    datos = []
    for fila in cursor.fetchall():
        datos.append(fila)

    return datos