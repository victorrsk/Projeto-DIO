def recomendar_plano(consumo_usuario):
    
    if consumo_usuario <= 10:
        return 'Plano Essencial Fibra - 50Mpbs'
    elif 10 <= consumo_usuario <= 20:
        return 'Plano Prata Fibra - 100Mbps'
    elif consumo_usuario > 20:
        return 'Plano Premium Fibra - 300Mbps'
    
