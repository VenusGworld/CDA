function verificaCpf(cpf){
    var div = document.getElementById("alert");
    var msg = document.querySelector(".msg-alert");
    
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
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = '<h6 class="msg-alert"><i class="fa-solid fa-circle-exclamation icon-size"></i> O CPF informado não é válido!</h6>';
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
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
        div.classList.remove('none');
        msg.innerHTML = "";
        msg.innerHTML = '<h6 class="msg-alert"><i class="fa-solid fa-circle-exclamation icon-size"></i> O CPF informado não é válido!</h6>';
        setTimeout(() =>{
            div.classList.add('none');
        }, 6000);
        return false;
    }

    return true; // CPF válido
}


function formatCPF() {
    var input = document.getElementById('cpf');
    var cpf = input.value;

    // Limpa caracteres não numéricos
    cpf = cpf.replace(/\D/g, '');

    // Aplica a máscara
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2');
    cpf = cpf.replace(/(\d{3})(\d)/, '$1.$2');
    cpf = cpf.replace(/(\d{3})(\d{1,2})$/, '$1-$2');

    input.value = cpf;
}
