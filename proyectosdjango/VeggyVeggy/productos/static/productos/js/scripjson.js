/**$("#buscar").click(function() {
    $.get('https://raw.githubusercontent.com/Cote17/Trabajo-Programaci-n-Web/master/Admins.json',
        function(data) {
            $.each(data.productos, (function(i, item) {
                $("#producto").append("<tr><td>" + item.idProducto + "</td> <td>" +
                    item.strProducto + "</td> <td> <img src ='" + item.strProductoThumb + "'></td> <td>" +
                    item.strProductoDescription + "</td></tr>");
            }));
        });

});**/

$("Productos.html").ready(function() {
    fetch("https://raw.githubusercontent.com/Cote17/Trabajo-Programaci-n-Web/master/Admins.json")
        .then(Response => Response.json())
        .then(data => {

            $.each(data.productos, (function(i, item) {
                $("#tablaJson").append("<tr>" + "<td>" + item.idProducto + "</td>" + "<td>" + item.strProducto + "</td>" + "<td>" + item.strProductoThumb + "</td>" + "<td>" + item.strProductoDescription + "</td>" + "</tr>");
            }));
        })
});