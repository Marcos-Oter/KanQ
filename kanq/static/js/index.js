const botonMostrarModal = document.getElementById('mostrarModal');
const modal = document.getElementById('dialog');
const botonCerrarModal = document.getElementById('cerrarModal');
const botonCerrarModal2 = document.getElementById('cerrarModal2');

const showFormModal = ()=> 
{
    botonMostrarModal.addEventListener('click', () => {
        modal.showModal();
    });

    botonCerrarModal.addEventListener('click', () => {
        modal.close();
    });

    botonCerrarModal2.addEventListener('click', () => {
        modal.close();
    });
}
console.log("xddd");
showFormModal();

ScrollReveal().reveal('.scrollreveal', { delay: 75 });
ScrollReveal().reveal('.scrollreveal2', { delay: 175 });