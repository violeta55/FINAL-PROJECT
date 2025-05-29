function verMas(boton) {
const descripcion = boton.previousElementSibling;
descripcion.textContent += " ¡Reserva ya tu cupo para esta experiencia inolvidable!";
boton.disabled = true;
}