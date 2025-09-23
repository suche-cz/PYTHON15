const images = document.querySelectorAll('#grid-image>img');
const mainImage = document.getElementById('main-image');

images.forEach(image => {
    image.style.opacity = '.5'; // jen ukázka nastavení stylu

    image.addEventListener('click', event => {
        const src = image.src.replace('/200/120', '/1000/600');
        mainImage.src = src;
    });

    image.addEventListener('error', event => {
        image.remove();
    });
});