from flask import Flask, render_template

app = Flask(__name__)

# Dados das matemáticas para o acervo vivo
matematicas = [
    {
        "id": "hypatia",
        "nome": "Hipátia de Alexandria",
        "periodo": "Antiguidade Clássica",
        "descricao": "Especialista em álgebra, astronomia e engenharia de instrumentos científicos. Conhecida por seus aprimoramentos no astrolábio e hidrômetro.",
        "detalhes": "Hipátia foi uma líder da escola neoplatônica em Alexandria. Sua contribuição para a matemática incluiu comentários sobre a Aritmética de Diofanto e as Cônicas de Apolônio."
    },
    {
        "id": "agnesi",
        "nome": "Maria Gaetana Agnesi",
        "periodo": "Século XVIII (Itália)",
        "descricao": "Matemática, filósofa e teóloga italiana. Autora do primeiro livro didático de cálculo. Famosa pela Curva de Agnesi.",
        "detalhes": "Maria Gaetana Agnesi (1718-1799) foi uma das primeiras mulheres a ser reconhecida como matemática. Seu tratado 'Instituzioni Analitiche' foi um marco na educação matemática. A curva que leva seu nome, conhecida como 'Bruxa de Agnesi', é um clássico da geometria analítica."
    },
    {
        "id": "ada",
        "nome": "Ada Lovelace",
        "periodo": "Século XIX",
        "descricao": "Criadora do primeiro algoritmo da história para a Máquina Analítica de Babbage. Pioneira da computação.",
        "detalhes": "Ada percebeu que a máquina de Babbage poderia ir além de simples cálculos numéricos, podendo processar qualquer símbolo, lançando as bases para a computação moderna."
    },
    {
        "id": "sophie",
        "nome": "Sophie Germain",
        "periodo": "Século XVIII/XIX",
        "descricao": "Usou o pseudônimo 'Antoine-Auguste Le Blanc' para estudar. Contribuiu significativamente para a teoria dos números e elasticidade.",
        "detalhes": "Seu trabalho no Último Teorema de Fermat foi um marco. Ela superou barreiras institucionais severas para se comunicar com Gauss e Lagrange."
    },
    {
        "id": "emmy",
        "nome": "Emmy Noether",
        "periodo": "Século XX",
        "descricao": "Fundamental para a álgebra abstrata e física teórica. Criadora do Teorema de Noether sobre leis de conservação.",
        "detalhes": "Descrita por Einstein como a mulher mais importante na história da matemática, seu teorema conecta simetrias físicas com leis de conservação."
    },
    {
        "id": "marilia",
        "nome": "Marília Chaves Peixoto",
        "periodo": "Século XX (Brasil)",
        "descricao": "Primeira mulher a ingressar na Academia Brasileira de Ciências. Especialista em funções convexas e pontos estruturalmente estáveis.",
        "detalhes": "Uma das pioneiras da matemática brasileira, seu trabalho em sistemas dinâmicos e análise é reconhecido internacionalmente."
    },
    {
        "id": "carolina",
        "nome": "Carolina Araújo",
        "periodo": "Contemporânea (Brasil)",
        "descricao": "Pesquisadora em geometria algébrica e variedades de Fano. Liderança feminina na matemática atual.",
        "detalhes": "Vencedora do prêmio Ramanujan, Carolina é uma voz ativa na promoção de mulheres na matemática e pesquisa avançada no IMPA."
    }
]

@app.route('/')
def index():
    return render_template('index.html', matematicas=matematicas)

@app.route('/biografia/<id>')
def biografia(id):
    matematica = next((m for m in matematicas if m['id'] == id), None)
    if matematica:
        return render_template('biografia.html', m=matematica)
    return "Página não encontrada", 404

@app.route('/laboratorio')
def laboratorio():
    return render_template('laboratorio.html', matematicas=matematicas)

@app.route('/multimidia')
def multimidia():
    return render_template('multimidia.html')

@app.route('/multimidia/storytelling')
def storytelling():
    return render_template('storytelling.html')

if __name__ == '__main__':
    app.run()
