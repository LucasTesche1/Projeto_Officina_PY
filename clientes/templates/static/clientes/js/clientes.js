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
        aux = document.getElementById('form-att-cliente')
        aux.style.display = 'block'

        nome = document.getElementById('nome').value = data['cliente']['nome']
        sobrenome = document.getElementById('sobrenome').value = data['cliente']['sobrenome']
        email = document.getElementById('email').value = data['cliente']['email']
        cpf = document.getElementById('cpf').value = data['cliente']['cpf']

        div_carros = document.getElementById('carros')
        div_carros.innerHTML = ""

        for(i=0; i<data['carros'].length; i++){
            div_carros.innerHTML += "\<form action='/clientes/update_carro/" + data['carros'][i]['id'] +"' method='POST'>\
                <div class='row'>\
                        <div class='col-md'>\
                            <input class='form-control' name='carro' type='text' value='" + data['carros'][i]['fields']['carro'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' name='placa' type='text' value='" + data['carros'][i]['fields']['placa'] + "'>\
                        </div>\
                        <div class='col-md'>\
                            <input class='form-control' type='text' name='ano' value='" + data['carros'][i]['fields']['ano'] + "' >\
                        </div>\
                        <div class='col-md'>\
                            <input class='btn btn-lg btn-success' type='submit' value='Salvar'>\
                        </div>\
                    </form>\
                    <div class='col-md'>\
                        <a href='/clientes/excluir_carro/"+ data['carros'][i]['id'] +"' class='btn btn-lg btn-danger'>EXCLUIR</a>\
                    </div>\
                </div><br>"

        }
    })


}

