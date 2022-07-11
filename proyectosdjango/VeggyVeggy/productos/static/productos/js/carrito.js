var updateBtns = document.getElementsByClassName('editar-carrito')


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var idProducto = this.dataset.producto //producto es el nombre del dataset data-producto
        var action = this.dataset.action
        console.log("El codigo es: ", idProducto, "action: ", action)

        console.log('USER:', user)
        if (user == 'AnonymousUser') {
            console.log('No se ha iniciado sesion')
        } else {
            updateUserOrder(idProducto, action)
        }
    })
}

function updateUserOrder(idProducto, action) {
    console.log('El usuario está logueado, enviando datos...')

    var url = '/updateItem/'

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ 'idProducto': idProducto, 'action': action })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })
}