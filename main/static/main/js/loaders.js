//loader.js
// Asegura que el loader está oculto inicialmente
document.getElementById("loader-wrapper").style.display = "none";

// Muestra el loader
function showLoader() {
    $("#loader-wrapper").show();
}

// Oculta el loader
function hideLoader() {
    document.getElementById("loader-wrapper").style.display = "none";
}

// Muestra el loader al iniciar cualquier llamada AJAX
$(document).ready(function() {
    // Mostrar el loader al iniciar cualquier llamada AJAX
    $(document).on('ajaxStart', function() {
        showLoader();
    });

    // Ocultar el loader al completar todas las llamadas AJAX
    $(document).on('ajaxStop', function() {
        hideLoader();
    });
});