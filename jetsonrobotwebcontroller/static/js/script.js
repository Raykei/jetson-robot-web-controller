
$(document).ready(function () {
    $('#startButton').click(function (event) {
        $("#stream-activated-container").toggle();
        $("#stream-deactivated-container").toggle();
        event.preventDefault();
        // Obtener el estado actual de transmission_active
        var currentTransmissionActive = window.location.href.includes('transmission_active=true');
        console.log("Estado de stream:", currentTransmissionActive)
        // Realizar una solicitud AJAX para cambiar el estado en el servidor
        $.get('webcam', { transmission_active: !currentTransmissionActive }, function(data) {
            console.log("Estado de stream cambiado a:", !currentTransmissionActive);
        });
        
        
    });
});

$(document).ready(function() {
    $('#stopButton').click(function (event) {
        $("#stream-deactivated-container").toggle();
        $("#stream-activated-container").toggle();
        event.preventDefault();
        $.get('webcam', { transmission_active: false }, function(data) {
            console.log("Estado de stream cambiado a: false");
        });
    });
});
