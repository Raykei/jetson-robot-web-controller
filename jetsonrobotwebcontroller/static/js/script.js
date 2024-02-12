// $(document).ready(function() {
//     $('#startButton').click(function() {
//         // Cuando se hace clic en el botón, establecer la variable a True
//         var start_transmission = true;
//         console.log('Start transmission:', start_transmission);
//         // Enviar la variable al servidor Django mediante una solicitud HTTP con jQuery
//         $.post('C:/Users/Usuario/Desktop/django_projects/jetson-robot-web-controller/jetson-robot-web-controller/jetsonrobotwebcontroller/views.py', { start_transmission: start_transmission })
//             .done(function(response) {
//                 console.log('La solicitud fue exitosa');
//             })
//             .fail(function(error) {
//                 console.error('Hubo un error en la solicitud');
//             });
//     });
// });

$(document).ready(function() {
    $('#startButton').click(function() {
        // Cuando se hace clic en el botón, redirigir a la vista de Django con el parámetro en la URL
        window.location.href = '/?start_transmission=true';
    });
});