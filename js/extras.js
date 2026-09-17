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
        banner.innerHTML = '<marquee scrollamount="5" behavior="scroll" direction="left" style="display: flex; align-items: center; justify-content: center; width: 100%;"><span><i class="fa-solid fa-bolt" style="color:#fbbf24;"></i> LIMITED TIME OFFER ENDS IN: <span class="timer-box" class="timer-box timer-display">14:59:59</span> <a href="https://razorpay.com/" target="_blank" style="background:#fff; color:#b91c1c; padding:2px 8px; border-radius:4px; font-size:12px; text-decoration:none; margin-left: 10px;">Claim Now</a></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span><i class="fa-solid fa-bolt" style="color:#fbbf24;"></i> LIMITED TIME OFFER ENDS IN: <span class="timer-box" class="timer-box timer-display">14:59:59</span> <a href="https://razorpay.com/" target="_blank" style="background:#fff; color:#b91c1c; padding:2px 8px; border-radius:4px; font-size:12px; text-decoration:none; margin-left: 10px;">Claim Now</a></span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span><i class="fa-solid fa-bolt" style="color:#fbbf24;"></i> LIMITED TIME OFFER ENDS IN: <span class="timer-box" class="timer-box timer-display">14:59:59</span> <a href="https://razorpay.com/" target="_blank" style="background:#fff; color:#b91c1c; padding:2px 8px; border-radius:4px; font-size:12px; text-decoration:none; margin-left: 10px;">Claim Now</a></span></marquee>';
        header.appendChild(banner);
        
        let timeLeft = 14 * 3600 + 59 * 60 + 59; // 14:59:59
        setInterval(() => {
            timeLeft--;
            if(timeLeft < 0) timeLeft = 0;
            const h = Math.floor(timeLeft / 3600).toString().padStart(2, '0');
            const m = Math.floor((timeLeft % 3600) / 60).toString().padStart(2, '0');
            const s = (timeLeft % 60).toString().padStart(2, '0');
            document.querySelectorAll('.timer-display').forEach(el => el.innerText = h + ':' + m + ':' + s);
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

    // 4. Zoom Session Booking Modal Logic
    window.openZoomBookingModal = function() {
        let modal = document.getElementById('zoom-booking-modal');
        if (!modal) {
            modal = createZoomModalElement();
        }
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    window.closeZoomBookingModal = function() {
        const modal = document.getElementById('zoom-booking-modal');
        if (modal) modal.classList.remove('active');
        document.body.style.overflow = '';
    };

    function createZoomModalElement() {
        const modalDiv = document.createElement('div');
        modalDiv.id = 'zoom-booking-modal';
        modalDiv.className = 'zoom-modal-overlay';
        modalDiv.innerHTML = `
            <div class="zoom-modal-card">
                <button class="zoom-modal-close" onclick="closeZoomBookingModal()">&times;</button>
                <div id="zoom-modal-body">
                    <div class="zoom-badge"><i class="fa-solid fa-video"></i> 1-ON-1 LIVE ZOOM SESSION</div>
                    <div class="zoom-modal-title">Book a Session with Me</div>
                    <div class="zoom-modal-sub">Schedule a private 1-on-1 Zoom call to review trading setups, price action logic, & risk management strategy.</div>
                    
                    <form id="zoom-booking-form" onsubmit="handleZoomSubmit(event)">
                        <div class="zoom-form-group">
                            <label><i class="fa-solid fa-user" style="color:var(--blue); margin-right:5px;"></i> Full Name</label>
                            <input type="text" class="zoom-form-input" placeholder="Enter your full name" required />
                        </div>
                        <div class="zoom-form-group">
                            <label><i class="fa-brands fa-whatsapp" style="color:#22c55e; margin-right:5px;"></i> WhatsApp / Mobile Number</label>
                            <input type="tel" class="zoom-form-input" placeholder="+91 98765 43210" required />
                        </div>
                        <div class="zoom-form-group">
                            <label><i class="fa-solid fa-envelope" style="color:var(--blue); margin-right:5px;"></i> Email Address</label>
                            <input type="email" class="zoom-form-input" placeholder="you@example.com" required />
                        </div>
                        <div class="zoom-form-group">
                            <label><i class="fa-solid fa-calendar-days" style="color:var(--gold); margin-right:5px;"></i> Preferred Date & Time Slot</label>
                            <select class="zoom-form-select" required>
                                <option value="">Select a Slot</option>
                                <option value="Tomorrow 4:00 PM">Tomorrow at 4:00 PM IST</option>
                                <option value="Tomorrow 7:30 PM">Tomorrow at 7:30 PM IST</option>
                                <option value="Saturday 11:00 AM">Saturday Special (11:00 AM IST)</option>
                                <option value="Sunday 5:00 PM">Sunday Wrap-up (5:00 PM IST)</option>
                            </select>
                        </div>
                        <div class="zoom-form-group">
                            <label><i class="fa-solid fa-graduation-cap" style="color:#a78bfa; margin-right:5px;"></i> Session Focus Topic</label>
                            <select class="zoom-form-select">
                                <option value="Price Action & SMC">Price Action & Smart Money Concepts</option>
                                <option value="Options Buying Strategy">Options Buying & Risk Management</option>
                                <option value="1-on-1 Portfolio & Mentorship">1-on-1 Portfolio & Mentorship Review</option>
                                <option value="Live Market Execution">Live Market Setup & Q&A</option>
                            </select>
                        </div>
                        <button type="submit" class="btn-zoom-submit">
                            <i class="fa-solid fa-video"></i> Confirm Booking & Get Zoom Link
                        </button>
                    </form>
                </div>
            </div>
        `;
        document.body.appendChild(modalDiv);
        
        modalDiv.addEventListener('click', function(e) {
            if (e.target === modalDiv) closeZoomBookingModal();
        });

        return modalDiv;
    }

    window.handleZoomSubmit = function(e) {
        e.preventDefault();
        const body = document.getElementById('zoom-modal-body');
        if (body) {
            body.innerHTML = `
                <div style="text-align: center; padding: 20px 10px;">
                    <div style="width: 70px; height: 70px; background: rgba(34, 197, 94, 0.15); border: 2px solid #22c55e; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: #22c55e; font-size: 34px; animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);">
                        <i class="fa-solid fa-check"></i>
                    </div>
                    <h3 style="font-size: 22px; font-weight: 800; margin-bottom: 10px; color: #fff;">Zoom Session Confirmed! 🎉</h3>
                    <p style="font-size: 14px; color: var(--w70); margin-bottom: 20px; line-height: 1.6;">
                        Your 1-on-1 session has been reserved. Check your email & WhatsApp for the calendar invite and meeting pass.
                    </p>
                    
                    <div style="background: rgba(45, 140, 255, 0.1); border: 1px dashed rgba(45, 140, 255, 0.4); border-radius: 14px; padding: 18px; margin-bottom: 24px; text-align: left;">
                        <div style="font-size: 12px; font-weight: 700; color: #2D8CFF; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px;">
                            <i class="fa-solid fa-video"></i> Zoom Meeting Details
                        </div>
                        <div style="font-size: 14px; color: #fff; font-weight: 600; margin-bottom: 4px;">Meeting ID: 892 0487 1920</div>
                        <div style="font-size: 13px; color: var(--w70); margin-bottom: 12px;">Passcode: TIS2026</div>
                        <a href="https://zoom.us/j/8920487192" target="_blank" class="btn-zoom-submit" style="margin-top: 0; padding: 10px 16px; font-size: 14px;">
                            <i class="fa-solid fa-arrow-up-right-from-square"></i> Join Zoom Room Direct
                        </a>
                    </div>
                    
                    <button onclick="closeZoomBookingModal()" class="btn-ghost" style="padding: 10px 24px; border-radius: 10px; width: 100%; cursor: pointer;">
                        Close Window
                    </button>
                </div>
            `;
        }
    };

    // 5. Auto-Attach Scroll Reveal Observer for All Boxes
    const boxSelector = '.card, .fcard, .stat, .hck, .hero-stats > div, .blog-card, .plan-card, .auth-box, .premium-box-cta, .tradingview-widget-container';
    const boxes = document.querySelectorAll(boxSelector);

    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

        boxes.forEach((box) => {
            if (!box.classList.contains('reveal') && !box.classList.contains('box-reveal')) {
                box.classList.add('box-reveal');
            }
            const parent = box.parentElement;
            if (parent && (parent.classList.contains('cards-grid') || parent.classList.contains('hero-stats') || parent.classList.contains('plans-grid') || getComputedStyle(parent).display === 'grid')) {
                const siblingIndex = Array.from(parent.children).indexOf(box);
                const delayClass = 'd' + ((siblingIndex % 4) + 1);
                box.classList.add(delayClass);
            }
            observer.observe(box);
        });
    } else {
        boxes.forEach(box => box.classList.add('visible'));
    }
});