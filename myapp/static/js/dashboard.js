document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const pageName = body.dataset.page || 'dashboard';
    const links = document.querySelectorAll('.nav-link');

    links.forEach((link) => {
        const match = link.dataset.page === pageName;
        link.classList.toggle('active', match);
    });

    const dateNode = document.getElementById('todayDate');
    if (dateNode) {
        const today = new Date();
        dateNode.textContent = today.toLocaleDateString('en-US', {
            weekday: 'short',
            month: 'short',
            day: 'numeric',
            year: 'numeric'
        });
    }

    const counters = document.querySelectorAll('[data-target]');
    counters.forEach((counter) => {
        const target = Number(counter.dataset.target || 0);
        const format = target >= 1000 ? new Intl.NumberFormat('en-US').format(target) : target;
        let current = 0;
        const step = Math.max(1, Math.ceil(target / 60));

        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }

            if (target >= 1000) {
                counter.textContent = new Intl.NumberFormat('en-US').format(current);
            } else {
                counter.textContent = current;
            }
        }, 16);
    });

    const bars = document.querySelectorAll('.bar-fill');
    bars.forEach((bar) => {
        const height = bar.dataset.width || '50%';
        requestAnimationFrame(() => {
            bar.style.height = height;
        });
    });
});
