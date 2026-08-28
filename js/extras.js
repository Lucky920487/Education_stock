document.addEventListener("DOMContentLoaded", function() {
    // 1. Page Transition Loader
    const loader = document.createElement('div');
    loader.id = 'page-transition-loader';
    loader.innerHTML = '<div class="loader-spinner"></div><div style="font-size:18px; font-weight:700;">Processing...</div>';
    document.body.appendChild(loader);

    setTimeout(() => { loader.classList.add('hidden'); }, 800); // Hide after short delay

    // Intercept link clicks for transition
    document.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if(href && !href.startsWith('#') && !href.startsWith('http') && !href.startsWith('mailto') && this.target !== '_blank') {
                e.preventDefault();
                loader.classList.remove('hidden');
                setTimeout(() => { window.location.href = href; }, 500);
            }
        });
    });

    // 2. Countdown Timer Banner (Only insert if header exists)
    const header = document.querySelector('header');
    if(header) {
        const banner = document.createElement('div');
        banner.id = 'countdown-banner';
        banner.innerHTML = '<marquee scrollamount="6" behavior="scroll" direction="left" style="display: flex; align-items: center; justify-content: center; width: 100%;"><span><i class="fa-solid fa-bolt" style="color:#fbbf24;"></i> LIMITED TIME OFFER ENDS IN: <span class="timer-box" id="timer-display">14:59:59</span> <a href="courses.html" style="background:#fff; color:#b91c1c; padding:2px 8px; border-radius:4px; font-size:12px; text-decoration:none; margin-left: 10px;">Claim Now</a></span></marquee>';
        header.appendChild(banner);
        
        let timeLeft = 14 * 3600 + 59 * 60 + 59; // 14:59:59
        setInterval(() => {
            timeLeft--;
            if(timeLeft < 0) timeLeft = 0;
            const h = Math.floor(timeLeft / 3600).toString().padStart(2, '0');
            const m = Math.floor((timeLeft % 3600) / 60).toString().padStart(2, '0');
            const s = (timeLeft % 60).toString().padStart(2, '0');
            document.getElementById('timer-display').innerText = `::`;
        }, 1000);
    }

    // 3. Social Proof Toast
    const toast = document.createElement('div');
    toast.id = 'social-proof-toast';
    toast.innerHTML = '<div class="toast-icon"><i class="fa-solid fa-graduation-cap"></i></div><div><div class="toast-text" id="toast-name">Raj joined</div><div class="toast-time" id="toast-time-ago">just 15 mins ago</div></div>';
    document.body.appendChild(toast);

    const names = ["Raj", "Rahul", "Priya", "Amit", "Sneha", "Vikram", "Anjali"];
    const actions = ["joined Super Trader VIP", "purchased Mentorship", "enrolled in Advanced Strategies"];
    
    function showToast() {
        const randomName = names[Math.floor(Math.random() * names.length)];
        const randomAction = actions[Math.floor(Math.random() * actions.length)];
        const randomMins = Math.floor(Math.random() * 59) + 1;

        document.getElementById('toast-name').innerText = randomName + " " + randomAction;
        document.getElementById('toast-time-ago').innerText = "just " + randomMins + " mins ago";
        
        toast.classList.add('show');
        setTimeout(() => { toast.classList.remove('show'); }, 4000);
    }

    setTimeout(showToast, 3000); // Show first toast after 3s
    setInterval(showToast, 15000); // Show a toast every 15s
});