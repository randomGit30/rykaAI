const inputSide = document.getElementById('signup');
const emailSide = document.getElementById('signin');
const container = document.querySelector('.container');

inputSide.addEventListener('click', () => {
    container.classList.add('active');
});

emailSide.addEventListener('click', () => {
    container.classList.remove('active');
});
document.querySelectorAll('.overlay-left, .overlay-right').forEach(item => {
    item.addEventListener('mousemove', function(e) {
        const glow = this.querySelector('.glow');
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left; // X position within the element.
        const y = e.clientY - rect.top;  // Y position within the element.
        glow.style.left = `${x}px`;
        glow.style.top = `${y}px`;
    });
});
