document.addEventListener('DOMContentLoaded', function() {
    const params = new URLSearchParams(window.location.search);
    const error = params.get('error');

    if (error === '1') {
        alert('Username atau password Anda salah');
    }
});
