const botonMostrarModal = document.getElementById('mostrarModal');
const botonCerrarModal = document.getElementById('cerrarModal');
const modal = document.getElementById('dialog');

const form = document.querySelector("form");

const showFormModal = ()=> 
{
    botonMostrarModal.addEventListener('click', () => {
        modal.showModal();
    });

    botonCerrarModal.addEventListener('click', () => {
        modal.close();
    });
}

showFormModal();

ScrollReveal().reveal('.scrollreveal', { delay: 75 });