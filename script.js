// Elementos DOM
const faqItems = document.querySelectorAll('.faq-item');
const consultoriaForm = document.getElementById('consultoriaForm');
const whatsappInput = document.getElementById('whatsapp');

// Inicialização
document.addEventListener('DOMContentLoaded', function() {
    initFAQ();
    initForm();
    initScrollAnimations();
    initSmoothScroll();
});

// FAQ Functionality
function initFAQ() {
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Fechar todos os outros itens
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                }
            });
            
            // Toggle do item atual
            item.classList.toggle('active', !isActive);
        });
    });
}

// Form Functionality
function initForm() {
    // Máscara para WhatsApp
    if (whatsappInput) {
        whatsappInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            value = value.replace(/^(\d{2})(\d{5})(\d{4}).*/, '($1) $2-$3');
            e.target.value = value;
        });
    }

    // Submit do formulário
    if (consultoriaForm) {
        consultoriaForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const nome = formData.get('nome');
            const whatsapp = formData.get('whatsapp');
            const interesse = formData.get('interesse');
            
            // Validação básica
            if (!nome || !whatsapp || !interesse) {
                alert('Por favor, preencha todos os campos.');
                return;
            }
            
            // Mensagem para WhatsApp
            const mensagem = `Olá! Acabei de preencher o formulário no site e gostaria de agendar minha consultoria especializada para ${interesse}. Meu nome é ${nome}.`;
            
            // Número do WhatsApp da Nessler (substitua pelo número real)
            const numeroWhatsApp = '5547986455858';
            
            // URL do WhatsApp
            const whatsappURL = `https://wa.me/${numeroWhatsApp}?text=${encodeURIComponent(mensagem)}`;
            
            // Abrir WhatsApp
            window.open(whatsappURL, '_blank');
            
            // Feedback visual
            showSuccessMessage();
        });
    }
}

// Mensagem de sucesso
function showSuccessMessage() {
    const button = document.querySelector('.btn-primary-premium');
    const originalText = button.textContent;
    
    button.textContent = 'Redirecionando para WhatsApp...';
    button.style.background = '#4CAF50';
    
    setTimeout(() => {
        button.textContent = originalText;
        button.style.background = '';
    }, 3000);
}

// Animações de scroll suaves
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observar elementos para animação
    const animatedElements = document.querySelectorAll('.diferencial-card, .produto-card, .stat-item');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Scroll suave para âncoras
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerHeight = document.querySelector('.header-premium').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Header scroll effect
window.addEventListener('scroll', function() {
    const header = document.querySelector('.header-premium');
    if (window.scrollY > 100) {
        header.style.background = 'rgba(0, 0, 0, 0.98)';
    } else {
        header.style.background = 'rgba(0, 0, 0, 0.95)';
    }
});

// Prevenção de spam no formulário
let formSubmitted = false;
if (consultoriaForm) {
    consultoriaForm.addEventListener('submit', function() {
        if (formSubmitted) {
            return false;
        }
        formSubmitted = true;
        
        setTimeout(() => {
            formSubmitted = false;
        }, 5000);
    });
}

// Analytics tracking (opcional)
function trackEvent(eventName, eventData = {}) {
    if (typeof gtag !== 'undefined') {
        gtag('event', eventName, eventData);
    }
}

// Track form submission
if (consultoriaForm) {
    consultoriaForm.addEventListener('submit', function() {
        trackEvent('form_submit', {
            form_name: 'consultoria_especializada'
        });
    });
}

// Track CTA clicks
document.querySelectorAll('.btn-primary-premium, .btn-secondary').forEach(button => {
    button.addEventListener('click', function() {
        trackEvent('cta_click', {
            button_text: this.textContent.trim(),
            button_location: this.closest('section')?.className || 'unknown'
        });
    });
});

// Performance optimization
if ('requestIdleCallback' in window) {
    requestIdleCallback(() => {
        // Lazy load de imagens não críticas
        const lazyImages = document.querySelectorAll('img[data-src]');
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    });
}

