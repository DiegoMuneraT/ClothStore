$(document).ready(function(){
    // Controlador de eventos para obtener datos internos
    $("#btn-get-internal-data").click(function(){
        // Peticion get a la api
        $.get("/api/products/", function(data) {
            // Formatear la respuesta
            var formattedData = JSON.stringify(data, null, 4);

            // Mostrar el json en el contenedor
            $("#data-container-internal").html("<pre>" + formattedData + "</pre>");
        });
    });

    // Controlador de eventos para obtener datos externos
    $("#btn-get-external-data").click(function(){
        // Peticion get a la api (CAMBIAR CON LA IP DEL GRUPO)
        $.get("https://jsonplaceholder.typicode.com/posts?_limit=4", function(data) {
            // Formatear la respuesta
            var formattedData = JSON.stringify(data, null, 4);
            // Mostrar el json en el contenedor
            $("#data-container-external").html("<pre>" + formattedData + "</pre>");
        });
    });

    // Controlador de eventos para limpiar datos internos
    $("#btn-clear-internal").click(function(){
        // Limpiar el contenido del contenedor de datos internos
        $("#data-container-internal").empty();
    });

    // Controlador de eventos para limpiar datos externos
    $("#btn-clear-external").click(function(){
        // Limpiar el contenido del contenedor de datos internos
        $("#data-container-external").empty();
    });
});