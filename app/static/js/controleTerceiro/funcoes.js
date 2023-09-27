let contadorInputs = 2;
let contadorAcomp = 1;
let qtdeAcomps = parseInt(document.getElementById("qtdeAcomps").value);

function adicionarInput() {
    if ( contadorInputs <= qtdeAcomps+1){
        const inputsContainer = document.getElementById('inputs-container');

        const novoInput = document.createElement('div');
        novoInput.classList.add("row");
        novoInput.classList.add("mb-3");
        novoInput.setAttribute('id', `acomp_${contadorInputs}`);
        novoInput.innerHTML = `
            <div class="header-acomp">
                <label for="">Acompanhante ${contadorAcomp}</label>
                <a class="btn btn-sm btn-outline-danger" onclick="excluirInput(${contadorInputs})"><i class="fa-solid fa-trash-can"></i></a>
            </div>
            <div class="div-cpf col-4">
                <label for="" class="cpf">CPF:</label>
                <span class="alerta-cpf none">*CPF inválido</span>
                <input type="text" class="form-control upper" oninput="formatCPF()" maxlength="14" tabindex="11" name="cpf_${contadorInputs}" id="cpf_${contadorInputs}" required>
            </div>
            <div class="col-8">
                <label for="">Nome:</label>
                <input type="text" class="form-control upper" name="nome_${contadorInputs}" maxlength="45" tabindex="12" id="nome_${contadorInputs}" required>
            </div>
        `;

        inputsContainer.appendChild(novoInput);

        contadorInputs++;
        contadorAcomp++;

        const inputsCPF = document.querySelectorAll('input[id^="cpf"]');

        inputsCPF.forEach((input) => {
            input.addEventListener('input', function() {
                formatarCPF(input);
            });
            input.addEventListener('input', function() {
                verificaCpfDiv(input);
            });
            input.addEventListener('keyup', function() {
                pesquisaCpf(input);
            });
            input.addEventListener('keypress', function() {
                verificaCpfDiv(input);
            });
            input.addEventListener('blur', function() {
                buscaCPF(input);
                verificaCpfDiv(input);
            });
        });
    }else {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        let div = document.getElementById("alert");
        let msg = document.querySelector(".msg-alert");
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = "<h6 class='msg-alert'>O número máximo de acompanhantes foi atingido.</h6>";
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
    }
}


function excluirInput(id) {
    const divASerExcluida = document.getElementById(`acomp_${id}`);
    divASerExcluida.remove();
    contadorInputs--;
    contadorAcomp--;
}


function formatarCPF(input) {
    let cpf = input.value.replace(/\D/g, '');

    if (cpf.length > 11) {
        cpf = cpf.slice(0, 11);
    }

    if (cpf.length > 9) {
        cpf = cpf.replace(/^(\d{3})(\d{3})(\d{3})(\d{2})$/, '$1.$2.$3-$4');
    } else if (cpf.length > 6) {
        cpf = cpf.replace(/^(\d{3})(\d{3})(\d{3})$/, '$1.$2.$3');
    } else if (cpf.length > 3) {
        cpf = cpf.replace(/^(\d{3})(\d{3})$/, '$1.$2');
    }

    input.value = cpf;
}


function buscaCPF(InputCpf){
    var cpf = InputCpf.value.replace(/\D/g, '');
    var inputNome = document.getElementById(`nome_${InputCpf.name.charAt(InputCpf.name.length - 1)}`);
    var respCpf = "";

    $.ajax({
        url: `/terceiro-pesquisa-mov/${cpf}`,
        type: 'GET',
        async: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            respCpf = data.nome;
        }
    });

    if (respCpf != ""){
        inputNome.value = respCpf;
    }
    
}


function formatarPlaca(input) {
    // Remove caracteres não alfanuméricos
    let placa = input.value.replace(/[^a-zA-Z0-9]/g, '');

    // Insere o hífen após a terceira letra
    if (placa.length > 3) {
      placa = placa.slice(0, 3) + '-' + placa.slice(3);
    }

    // Limita a placa em 8 caracteres (3 letras + hífen + 4 dígitos)
    if (placa.length > 8) {
      placa = placa.slice(0, 8);
    }

    input.value = placa.toUpperCase();
}


function verificaCpf(cpf){
    cpf = cpf.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos

    if (cpf.length !== 11) {
        return false;
    }

    // Verifica se todos os dígitos são iguais (CPF inválido)
    if (/^(\d)\1+$/.test(cpf)) {
        return false;
    }

    // Calcula o primeiro dígito verificador
    let soma = 0;
    for (let i = 0; i < 9; i++) {
        soma += parseInt(cpf.charAt(i)) * (10 - i);
    }
    let resto = 11 - (soma % 11);
    let digito1 = resto >= 10 ? 0 : resto;

    // Verifica o primeiro dígito verificador
    if (digito1 !== parseInt(cpf.charAt(9))) {
        return false;
    }

    // Calcula o segundo dígito verificador
    soma = 0;
    for (let i = 0; i < 10; i++) {
        soma += parseInt(cpf.charAt(i)) * (11 - i);
    }
    resto = 11 - (soma % 11);
    let digito2 = resto >= 10 ? 0 : resto;

    // Verifica o segundo dígito verificador
    if (digito2 !== parseInt(cpf.charAt(10))) {
        return false;
    }

    return true; // CPF válido
}


function verificaPessoaVisit(){
    var pessoa = document.getElementById("pessoaVisit").value.split(" ");
    var respPessoa = false;

    $.ajax({
        url: `/funcionario-pesquisa-mov/${pessoa[0]}`,
        type: 'GET',
        async: false,
        dataType: 'json',
        contentType: 'application/json',
        success: function(data){
            respPessoa = data;
        }
    });

    if (!respPessoa){
        return false;
    }else{
        return true;
    }
}

function verificaCPFs(){
    var div = document.getElementById("alert");
    var msg = document.querySelector(".msg-alert");
    const divsCPF = document.querySelectorAll('div[class^="div-cpf"]');
    var resp = true

    divsCPF.forEach((divCpf) => {
        var cpf = divCpf.querySelector('input[id^="cpf"]');
        if (!verificaCpf(cpf)){
            div.classList.remove('none');
            msg.innerHTML = "";
            msg.innerHTML = "<h6 class='msg-alert'>O CPF informado não é válido!</h6>";
            setTimeout(() =>{
                div.classList.add('none');
            }, 6000);
            cpf.focus();
            resp = false;
        }else if (!verificaPessoaVisit()) {
            div.classList.remove('none');
            msg.innerHTML = "";
            msg.innerHTML = "<h6 class='msg-alert'>A pessoa informada não existe</h6>";
            setTimeout(() =>{
                div.classList.add('none');
            }, 6000);
            resp = false;
        }else {
            resp = true;
        }
    });

    if (!resp){
        return resp
    }else{
        return resp
    }
}


function verificaCpfDiv(input){
    const divMae = input.parentNode;
    var cpf = divMae.querySelector('input[id^="cpf"]');
    var labelCpf = divMae.querySelector(".cpf");
    var spanAlerta = divMae.querySelector(".alerta-cpf");

    cpf = cpf.value.replace(/\D/g, ''); // Remove todos os caracteres não numéricos

    if (cpf.trim().length === 0){
        labelCpf.classList.remove("cpf-invalido-label");
        spanAlerta.classList.add("none");
        input.classList.remove("cpf-invalido");
        return 0
    }else if (cpf.length !== 11) {
        labelCpf.classList.add("cpf-invalido-label");
        spanAlerta.classList.remove("none");
        input.classList.add("cpf-invalido");
    }

    // Verifica se todos os dígitos são iguais (CPF inválido)
    if (/^(\d)\1+$/.test(cpf)) {
        labelCpf.classList.add("cpf-invalido-label");
        spanAlerta.classList.remove("none");
        input.classList.add("cpf-invalido");
    }

    // Calcula o primeiro dígito verificador
    let soma = 0;
    for (let i = 0; i < 9; i++) {
        soma += parseInt(cpf.charAt(i)) * (10 - i);
    }
    let resto = 11 - (soma % 11);
    let digito1 = resto >= 10 ? 0 : resto;

    // Verifica o primeiro dígito verificador
    if (digito1 !== parseInt(cpf.charAt(9))) {
        labelCpf.classList.add("cpf-invalido-label");
        spanAlerta.classList.remove("none");
        input.classList.add("cpf-invalido");
    }else{
        labelCpf.classList.remove("cpf-invalido-label");
        spanAlerta.classList.add("none");
        input.classList.remove("cpf-invalido");
    }

    // Calcula o segundo dígito verificador
    soma = 0;
    for (let i = 0; i < 10; i++) {
        soma += parseInt(cpf.charAt(i)) * (11 - i);
    }
    resto = 11 - (soma % 11);
    let digito2 = resto >= 10 ? 0 : resto;

    // Verifica o segundo dígito verificador
    if (digito2 !== parseInt(cpf.charAt(10))) {
        labelCpf.classList.add("cpf-invalido-label");
        spanAlerta.classList.remove("none");
        input.classList.add("cpf-invalido");
    }else{
        labelCpf.classList.remove("cpf-invalido-label");
        spanAlerta.classList.add("none");
        input.classList.remove("cpf-invalido");
    }

}