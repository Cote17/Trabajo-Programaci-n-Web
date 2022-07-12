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
    var regex = /^[0-9]+$/;
    if (!regex.test(telefono)) {
        return false;
    } else {
        return true;
    }
}

if (document.body.classList.contains('formularioRegistro')) {
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
        if (((telefono.length < 8) || (telefono.length > 10)) || (!IsFono(telefono))) {
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
        console.log(submit)
    }
}


function IsCorreo2(correo2) {
    var regex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
    if (!regex.test(correo2)) {
        return false;
    } else {
        return true;
    }
}

function IsFono2(telefono2) {
    var regex = /^[0-9]+$/;
    if (!regex.test(telefono2)) {
        return false;
    } else {
        return true;
    }
}

if (document.body.classList.contains('formularioPago')) {
    document.addEventListener("DOMContentLoaded", function() {
        document.getElementById("formularioPago").addEventListener("submit", validarFormulario2);
    });

    function validarFormulario(evento) {
        evento.preventDefault();
        var errorNom2 = document.getElementById('errorNom2');
        var usuario2 = document.getElementById('usuario2').value;
        var telefono2 = document.getElementById('telefono2').value;
        var errorFono2 = document.getElementById('errorFono2');
        var correo2 = document.getElementById('correo2').value;
        var errorCorreo2 = document.getElementById('errorCorreo2');
        var errordirec = document.getElementById('errordirec');
        var direccion = document.getElementById('direccion').value;
        var errorciud = document.getElementById('errorciud');
        var ciudad = document.getElementById('ciudad').value;


        errorNom2.classList.add('hide');
        errorNom2.classList.remove('show');
        errorFono2.classList.add('hide');
        errorFono2.classList.remove('show');
        errorCorreo2.classList.add('hide');
        errorCorreo2.classList.remove('show');
        errordirec.classList.add('hide');
        errordirec.classList.remove('show');
        errorciud.classList.add('hide');
        errorciud.classList.remove('show');

        if (usuario2.length == 0) {
            errorNom2.classList.remove('hide');
            errorNom2.classList.add('show');
            return;
        }
        if (((telefono2.length < 8) || (telefono2.length > 10)) || (!IsFono2(telefono2))) {
            errorFono2.classList.remove('hide');
            errorFono2.classList.add('show');
            return;
        }
        if ((correo2.length == 0) || (!IsCorreo2(correo2))) {
            errorCorreo2.classList.remove('hide');
            errorCorreo2.classList.add('show');
            return;
        }
        if (direccion.length == 0) {
            errordirec.classList.remove('hide');
            errordirec.classList.add('show');
            return;
        }
        if (ciudad.length == 0) {
            errorciud.classList.remove('hide');
            errorciud.classList.add('show');
            return;
        }

        this.submit();
        console.log(submit)
    }
}