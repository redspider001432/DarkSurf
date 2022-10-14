const model = document.getElementById('main2');
const open = document.getElementById('upload-text');
const field = document.getElementById('input-post')
const btn = document.getElementById('submit-post-id');
let windowsContainer = document.getElementById('windows-container');
const userContentH = document.getElementById('user-content');


window.onload = function(){
   windowsContainer.style.height = userContentH.offsetHeight  + 650 + 'px'
}

open.addEventListener('click', () => {
    model.classList.replace('main2','show12345');

});

function myFunction() {
    model.classList.replace('show12345','main2')
}

