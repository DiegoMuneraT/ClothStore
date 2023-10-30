$(document).ready(function(){
    // Controlador de eventos
    $("#btn-get-data").click(function(){
        // Peticion get a la api
        $.get("/api/products/", function(data) {
            // Formatear la respuesta
            var formattedData = JSON.stringify(data, null, 4);

            // Mostrar el json en el contenedor
            $("#data-container").html("<pre>" + formattedData + "</pre>");
        });
    });
});