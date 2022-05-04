'use strict';


// Get the navbar
let navbar = document.querySelector(".nav");


// Get the offset position of the navbar
let sticky = navbar.offsetTop;


// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }

  if (document.documentElement.scrollTop > 500) {
    btnTop.style.display = 'block';
  } else {
    btnTop.style.display = 'none';
  }
}


// When the user scrolls the page, execute myFunction
window.onscroll = function () { myFunction() };


//  SCROll TO TOP
const btnTop = document.querySelector('.btn-top');

btnTop.addEventListener('click', function () {
  window.scroll({ top: 0, behavior: "smooth" })
})


// MODAL CART
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnOpenModal = document.querySelector('.cart-header');

const openModal = function () {
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');
};

btnOpenModal.addEventListener('click', openModal);
btnCloseModal.addEventListener('click', closeModal);
overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    closeModal();
  }
});
