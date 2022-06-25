/**const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
    usuario: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    password: /^.{4,12}$/, // 4 a 12 digitos.
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = {
    usuario: false,
    nombre: false,
    password: false,
    password2: false,
    correo: false,
    telefono: false
}

const validarFormulario = (e) => {
    switch (e.target.name) {
        case "usuario":
            validarCampo(expresiones.usuario, e.target, 'usuario');
            break;
        case "nombre":
            validarCampo(expresiones.nombre, e.target, 'nombre');
            break;
        case "password":
            validarCampo(expresiones.password, e.target, 'password');
            validarPassword2();
            break;
        case "password2":
            validarPassword2();
            break;
        case "correo":
            validarCampo(expresiones.correo, e.target, 'correo');
            break;
        case "telefono":
            validarCampo(expresiones.telefono, e.target, 'telefono');
            break;
    }
}

const validarCampo = (expresion, input, campo) => {
    if (expresion.test(input.value)) {
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
    } else {
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false;
    }
}

const validarPassword2 = () => {
    const inputPassword1 = document.getElementById('password');
    const inputPassword2 = document.getElementById('password2');

    if (inputPassword1.value !== inputPassword2.value) {
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos['password'] = false;
    } else {
        document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos['password'] = true;
    }
}



inputs.forEach((input) => {
    input.addEventListener('keyup', validarFormulario);
    input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    const terminos = document.getElementById('terminos');
    if (campos.usuario && campos.nombre && campos.password && campos.correo && campos.telefono && terminos.checked) {
        formulario.reset();

        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);

        document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
            icono.classList.remove('formulario__grupo-correcto');
        });
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
        setTimeout(() => {
            document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo');
        }, 3000);
    }
});**/

function IsCorreo(correo) {
    var regex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    if (!regex.test(correo)) {
        return false;
    } else {
        return true;
    }
}

function IsFono(telefono) {
    var regex = /^\d{7,14}$/;
    if (!regex.test(telefono)) {
        return false;
    } else {
        return true;
    }
}


document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formularioRegistro").addEventListener("submit", validarFormulario);
});

function validarFormulario(evento) {
    evento.preventDefault();
    var errorNom = document.getElementById('errorNom');
    var usuario = document.getElementById('nombre').value;
    var telefono = document.getElementById('telefono').value;
    var errorFono = document.getElementById('errorFono');
    var correo = document.getElementById('correo').value;
    var errorCorreo = document.getElementById('errorCorreo');
    var errorClave = document.getElementById('errorClave');
    var errorMismaClave = document.getElementById('errorMismaClave');
    var terminos = document.getElementById('terminos').checked;
    var errorTyc = document.getElementById('errorTyc');
    console.log(terminos.checked);
    errorNom.classList.add('hide');
    errorNom.classList.remove('show');
    errorFono.classList.add('hide');
    errorFono.classList.remove('show');
    errorCorreo.classList.add('hide');
    errorCorreo.classList.remove('show');
    errorClave.classList.add('hide');
    errorClave.classList.remove('show');
    errorMismaClave.classList.add('hide');
    errorMismaClave.classList.remove('show');
    errorTyc.classList.add('hide');
    errorTyc.classList.remove('show');
    if (usuario.length == 0) {
        errorNom.classList.remove('hide');
        errorNom.classList.add('show');
        return;
    }
    if (((telefono.length == 0) || (telefono.length > 10)) && (!IsFono(telefono))) {
        errorFono.classList.remove('hide');
        errorFono.classList.add('show');
        return;
    }
    if ((correo.length == 0) || (!IsCorreo(correo))) {
        errorCorreo.classList.remove('hide');
        errorCorreo.classList.add('show');
        return;
    }
    var clave = document.getElementById('password').value;
    if ((clave.length < 4) || (clave.length > 10)) {
        errorClave.classList.remove('hide');
        errorClave.classList.add('show');
        return;
    }
    var clave2 = document.getElementById('password2').value;
    if (clave != clave2) {
        errorMismaClave.classList.remove('hide');
        errorMismaClave.classList.add('show');
        return;
    }
    if (!terminos) {
        errorTyc.classList.remove('hide');
        errorTyc.classList.add('show');
        return;
    }
    this.submit();
}