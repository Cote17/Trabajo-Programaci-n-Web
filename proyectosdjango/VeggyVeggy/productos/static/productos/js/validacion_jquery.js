$("#mensajeErrorPass").hide();
//inicio de sesión
$("#inicioSesion").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 6,
            maxlength: 15
        },
        contrasena: {
            required: true,
            minlength: 5,
            maxlength: 12
        }

    }
})

$("#iniciar").click(function() {
        if ($("#inicioSesion").valid == false) {
            return;
        }
        let nombre = $("#nombre").val()
        let contrasena = $("#contrasena").val()
        console.log(nombre)
    })
    //contacto 
$("#formularioContacto").validate({
    rules: {
        select: {
            required: true

        },
        nombre: {
            required: true,
            minlength: 6,
            maxlength: 15
        },
        telefono: {
            required: true,
            minlength: 9,
            maxlength: 10
        },
        correo: {
            required: true,
            email: true,
            minlength: 9,
            maxlength: 30

        },
        ciudad: {
            required: true,
            minlength: 6,
            maxlength: 60
        },
        mensaje: {
            required: true,
        }

    }



})

$("#btn_contacto").click(function() {
        if ($("#formularioContacto").valid == false) {
            return;
        }
        let select = $("#select").val()
        let nombre = $("#nombre").val()
        let telefono = $("#telefono").val()
        let correo = $("#correo").val()
        let ciudad = $("#ciudad").val()
        let mensaje = $("mensaje").val()


    })
    //trabaja con nosotros
$("#formularioTrabajo").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 6,
            maxlength: 15
        },
        telefono: {
            required: true,
            minlength: 9,
            maxlength: 10
        },
        correo: {
            required: true,
            email: true,
            minlength: 9,
            maxlength: 30

        },
        archivo: {
            required: true
        }


    }
})

$("#enviarTrabajo").click(function() {
    if ($("#formularioTrabajo").valid == false) {
        return;
    }
    let nombre = $("#nombre").val()
    let telefono = $("#telefono").val()
    let correo = $("#correo").val()
    let archivo = $("archivo").val()


})

$("#formularioEnvio").validate({
    rules: {
        nombre: {
            required: true,
            minlength: 6,
            maxlength: 15
        },
        telefono: {
            required: true,
            minlength: 9,
            maxlength: 10
        },
        correo: {
            required: true,
            email: true,
            minlength: 9,
            maxlength: 30

        },
        direccion: {
            required: true,
            minlength: 6,
            maxlength: 60
        },
        ciudad: {
            required: true,
            minlength: 6,
            maxlength: 60
        },

    }



})

$("#btn_envio").click(function() {
    if ($("#formularioEnvio").valid == false) {
        return;
    }
    let nombre = $("#nombre").val()
    let telefono = $("#telefono").val()
    let correo = $("#correo").val()
    let direccion = $("#direccion").val()
    let ciudad = $("#ciudad").val()


})

jQuery.extend(jQuery.validator.messages, {
    required: "Este campo es obligatorio.",
    remote: "Por favor, rellena este campo.",
    email: "Por favor, escribe una dirección de correo válida",
    url: "Por favor, escribe una URL válida.",
    date: "Por favor, escribe una fecha válida.",
    dateISO: "Por favor, escribe una fecha (ISO) válida.",
    number: "Por favor, escribe un número entero válido.",
    digits: "Por favor, escribe sólo dígitos.",
    creditcard: "Por favor, escribe un número de tarjeta válido.",
    equalTo: "Por favor, escribe el mismo valor de nuevo.",
    accept: "Por favor, escribe un valor con una extensión aceptada.",
    maxlength: jQuery.validator.format("Por favor, no escribas más de {0} caracteres."),
    minlength: jQuery.validator.format("Por favor, no escribas menos de {0} caracteres."),
    rangelength: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1} caracteres."),
    range: jQuery.validator.format("Por favor, escribe un valor entre {0} y {1}."),
    max: jQuery.validator.format("Por favor, escribe un valor menor o igual a {0}."),
    min: jQuery.validator.format("Por favor, escribe un valor mayor o igual a {0}.")
});