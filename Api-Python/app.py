from flask import Flask,jsonify, request

app = Flask(__name__)


        # Banco de dados
livros = [
    {
        'id':1,
        'title': 'Dias perfeitos',
        'autor': 'Raphael Montes'
    },
     {
        'id':2,
        'title': 'Jantar Secreto',
        'autor': 'Raphael Montes'
    }
]


        # Consultar Todos

@app.route('/livros',methods=['Get'])
def obter_livros():
    return jsonify(livros)



        # Consultar Por Id

@app.route('/livros/<int:id>',methods=['Get'])
def obter_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)



        # Criar

@app.route('/livros',methods=['Post'])
def incluir_novo_livro():
    novo_livro=request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)




        # Editar

@app.route('/livros/<int:id>',methods=['Put'])
def editar_livro_por_id(id):
    livro_alterado= request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])




        # Excluir

@app.route('/livros/<int:id>',methods=['Delete'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)



app.run(port=5000,host='localhost',debug=True)
