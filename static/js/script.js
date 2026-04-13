<script>
function toggleMenu(element) {
    let menu = element.nextElementSibling;

    // Close all other menus
    document.querySelectorAll('.menu-content').forEach(m => {
        if (m !== menu) m.style.display = 'none';
    });

    // Toggle current
    menu.style.display = (menu.style.display === 'block') ? 'none' : 'block';
}

// Close menu when clicking outside
document.addEventListener('click', function(e) {
    if (!e.target.closest('.menu')) {
        document.querySelectorAll('.menu-content').forEach(m => {
            m.style.display = 'none';
        });
    }
});
</script>