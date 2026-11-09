(() => {
    'use strict';

    window.addEventListener('DOMContentLoaded', () => {
        const activeEl = document.querySelector(`aside nav li a[href='${location.pathname.substring(1)}']`);
        if (activeEl) {
            activeEl.classList.add('active');
        }
    })
})()
