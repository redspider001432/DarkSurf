const toggleButton = document.getElementsByClassName('toggle-button')[0];

const navbar = document.getElementsByClassName('nav-links')[0];
const bg = document.getElementById('bg');

toggleButton.addEventListener('click',()=>{
    navbar.classList.toggle('active');
    if (bg.classList.contains('bg')){
        bg.classList.remove('bg');
    }else{
        bg.classList.add('bg');
    }

})