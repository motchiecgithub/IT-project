document.addEventListener('click', function(event) {
    if (event.target.classList.contains('clickable')) {
        const clickedWord = event.target.innerText;
        alert(`You clicked: ${clickedWord}`);
    }
});
