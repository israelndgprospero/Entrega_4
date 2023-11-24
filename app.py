from flask import Flask, request

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):    
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

app = Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    #return 'Hello, World!'
    return {'Teste': 1, 'A': '123asd'}

# @app.route('/myapi', methods=['POST', 'GET'])
@app.route('/myapi', methods=['POST'])
def myapi():
    input_data = request.get_json(force=True)

    fact_number = input_data.get("fact")
    fib_number = input_data.get("fib")

    # Não calcular fatorial para números maiores que 20
    if (fact_number <= 20 and fact_number >= 0):
        fact_result = factorial(fact_number)
    else:
        raise ValueError('O fatorial é calculado somente para números entre 0 e 20')

    # Não calcular o número de fibonnaci para números maiores que 50
    if (fib_number <= 50 and fib_number >= 1):
        fib_result = fibonacci(fib_number)
    else:
        raise ValueError('O número de fibonnaci é calculado somente para números entre 1 e 50')
    
    return {'fact': fact_result, 'fib': fib_result}