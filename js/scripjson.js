$("#buscar").click(function () {
    $.get("http://127.0.0.1:5500/js/Productos.json",
        function (data) {
            $.each(data.productos, (function (i, item) {
                $("#producto").append("<tr><td>" + item.idProducto + "</td> <td>" +
                    item.strProducto + "</td> <td> <img src ='" + item.strProductoThumb + "'></td> <td>" +
                    item.strProductoDescription + "</td></tr>");
            }));
        });

});

