from flask import Flask, request
from funcoes import sigla, ordenar_cidades , lista_Cidades

app = Flask(__name__)

@app.route("/lista_ibge") 
def Todas_cidades():
    cidades = lista_Cidades() 
    ordenadas = ordenar_cidades(cidades) 
    return ordenadas 

    

@app.route("/consulta_ibge", methods=['GET'])  
def estado(): 
    UF = request.args.get('UF') 
    resposta = sigla(UF) 
    return resposta 

@app.route("/ordenar_cidades", methods=['GET']) 
def ordenar(): 
    UF = request.args.get('UF') 
    cidades = sigla(UF) 
    cidades_ordenadas = ordenar_cidades(cidades)  
    return {f"cidades_ordenadas de {UF}": cidades_ordenadas} 

if __name__ == "__main__":
    app.run(debug=True)
