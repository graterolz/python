import json

def run(data):
    data = json.loads(data)
    data_arr = [
        int(data["ciclo"]),
        int(data["p90_densidad"]),
        int(data["area_rodal"]),
        int(data["p30_prendimiento"]),
        int(data["mes_plantacion"]),
        int(data["sistema_prop"]),
        int(data["control_malezas"]),
        int(data["reposicion"]),
        int(data["perdida_plantacion"]),
        int(data["departamento"]),
        int(data["tipo_suelo"]),
        int(data["clima90_temp_min_media"]),
        int(data["clima90_precipitaciones"])
    ]
    print(data_arr)

data = '{"ciclo":"0","p90_densidad":"0","area_rodal":"0","p30_prendimiento":"0","mes_plantacion":"0","sistema_prop":"0","control_malezas":"0","reposicion":"0","perdida_plantacion":"0","departamento":"0","tipo_suelo":"0","clima90_temp_min_media":"0","clima90_precipitaciones":"0"}'

run (data)