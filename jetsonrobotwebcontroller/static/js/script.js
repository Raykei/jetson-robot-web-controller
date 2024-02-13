$(document).ready(function () {
    // Verificar el estado inicial de transmission_active
    var currentTransmissionActive = window.location.href.includes('transmission_active=true');
    console.log("Estado inicial de stream:", currentTransmissionActive);

    $('#startButton').click(function (event) {
        $("#stream-activated-container").toggle(); //muestra transmision
        $("#stream-deactivated-container").toggle(); // esconde gato
        //event.preventDefault();
        // Obtener el estado actual de transmission_active
        var currentTransmissionActive = window.location.href.includes('transmission_active=true');
        console.log("Estado de stream antes de la solicitud AJAX:", currentTransmissionActive)
        document.getElementById("stream-activated-container").src = "/webcam";
        // Realizar una solicitud AJAX para cambiar el estado en el servidor
        $.get('/webcam', { transmission_active: !currentTransmissionActive }, function(data) {
            //console.log("Respuesta de la solicitud AJAX:", data);

            //var newTransmissionActive = window.location.href.includes('transmission_active=true');
            //console.log("Nuevo estado de stream:", newTransmissionActive);
            
            Console.log("Estado de stream cambiado a:", currentTransmissionActive);
        }).fail(function(error) {
            Console.error("Error en la solicitud AJAX:", error);
        });

    });

    $('#stopButton').click(function (event) {
        $("#stream-deactivated-container").toggle(); // muestra gato
        $("#stream-activated-container").toggle(); // esconde transmision
        //event.preventDefault();
        var currentTransmissionActive = window.location.href.includes('transmission_active=false');
        console.log("Estado de stream post spotButtom:", currentTransmissionActive)
        $.get('webcam', { transmission_active: false }, function(data) {
            console.log("Estado de stream cambiado a: FALSE");
        });
    });

    // $('#refreshButton').click(function (event) {
    //     $("#stream-activated-container").toggle(); // muestra transmision que guarda frames
    //     $("#stream-activated-container-inicial").toggle(); // esconde transmision inicial
    //     //event.preventDefault();
    // });

});