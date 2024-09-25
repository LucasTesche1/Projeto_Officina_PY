function add_carro(){

    const container = document.getElementById('form-carro');

    let html = "<br> <div class = 'row'> <div class = 'col-md'> <input type = 'text' placeholder = 'carro' class = 'form-control' name = 'carro'>  </div> <div class= 'col-md'>  <input type = 'text' placeholder = 'placa' class = 'form-control' name = 'placa'> </div> <div class= 'col-md'> <input type = 'number' placeholder = 'ano' class = 'form-control' name = 'ano'> </div>  </div>";

    container.innerHTML += html;

}

function exibir_form(tipo){

    const add_cliente = document.getElementById('adicionar-cliente')
    const att_cliente = document.getElementById('att_cliente')

    if(tipo == "1"){
        add_cliente.style.display = "block"
        att_cliente.style.display = "none"


    }else if(tipo == "2"){
        att_cliente.style.display = "block";
        add_cliente.style.display = "none"
    }

}

function dados_cliente(){
    const csrf_token = document.querySelector('[name = csrfmiddlewaretoken]').value
    const cliente = document.getElementById('cliente-select')
    let id_cliente = cliente.value

    data = new FormData()
    data.append('id_cliente', id_cliente)

    fetch("/clientes/atualiza_cliente/" , {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data
    }).then(function (result){
        return result.json();
    }).then(function (data){
        document.getElementById('form-att-cliente').style.display = 'block'

        nome = document.getElementById('nome')
        nome.value = data['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['sobrenome']

        email = document.getElementById('email')
        email.value = data['email']

        cpf = document.getElementById('cpf')
        cpf.value = data['cpf']

    })


}

