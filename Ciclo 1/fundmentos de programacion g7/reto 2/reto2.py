def cliente(informacion:dict):
    if informacion["edad"]>18:
        boleta=20000
        atraccion="X-Treme"
        apto=True
        if informacion["primer_ingreso"]== True:
            boleta=-boleta*0.05+boleta 
    
    elif informacion["edad"]>=15 and informacion["edad"]<=18:
        boleta=5000
        atraccion="Carros chocones"
        apto=True
        if informacion["primer_ingreso"]== True:
            boleta=-boleta*0.07+boleta
        
            
    elif informacion["edad"]>=7 and informacion["edad"]<=15:
        boleta=10000
        atraccion="Sillas voladoras"
        apto=True
        if informacion["primer_ingreso"]== True:
            boleta=-boleta*0.05+boleta 
            
    else:
        
        boleta="N/A "
        atraccion="N/A" 
        apto= False  
    return{"nombre":informacion["nombre"],"edad":informacion["edad"],"atraccion":atraccion,"apto":apto,"primer_ingreso":informacion["primer_ingreso"],"total_boleta":boleta}  
    
cliente({"id_cliente":1,"nombre":"juan","edad":6,"primer_ingreso":True})   