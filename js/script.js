// ==========================================================================
// Godoy Auto Detailing — Site Script
// ==========================================================================

document.addEventListener('DOMContentLoaded', function () {

  // ---- Mobile nav toggle ----
  var navToggle = document.getElementById('navToggle');
  var mainNav = document.getElementById('mainNav');

  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function () {
      mainNav.classList.toggle('open');
    });

    // Close menu after clicking a link
    mainNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mainNav.classList.remove('open');
      });
    });
  }

  // ---- Footer year ----
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ---- Scroll reveal animations ----
  var revealSelectors = [
    '.section h2', '.section-eyebrow', '.section-sub',
    '.service-card', '.feature', '.process-step',
    '.gallery-item', '.testimonial-card', '.contact-method', '.contact-form'
  ];
  var revealEls = document.querySelectorAll(revealSelectors.join(','));

  revealEls.forEach(function (el, i) {
    el.setAttribute('data-reveal', '');
    el.style.transitionDelay = (i % 6) * 0.06 + 's';
  });

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in-view'); });
  }

  // ---- Ad conversion tracking hooks ----
  // These fire safely even if gtag/fbq aren't loaded yet (guarded checks).
  // Once you add your Google Ads / Meta Pixel snippets in index.html <head>,
  // these will automatically start reporting conversions.

  function trackConversion(label) {
    if (typeof gtag === 'function') {
      gtag('event', 'generate_lead', { event_label: label });
    }
    if (typeof fbq === 'function') {
      fbq('track', 'Lead', { content_name: label });
    }
  }

  // WhatsApp button clicks (header, hero, contact section, sticky button)
  document.querySelectorAll('a[href*="wa.me"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      trackConversion('WhatsApp Click');
    });
  });

  // Phone call clicks
  document.querySelectorAll('a[href^="tel:"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      trackConversion('Phone Click');
    });
  });

  // ---- FAQ accordion ----
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var question = item.querySelector('.faq-question');
    if (!question) return;
    question.addEventListener('click', function () {
      item.classList.toggle('open');
    });
  });

  // ---- Gallery filters (All / Exterior / Interior) ----
  var galleryFilters = document.querySelectorAll('.gallery-filter');
  var galleryItems = document.querySelectorAll('#galleryGrid .gallery-item');
  galleryFilters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      galleryFilters.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var filter = btn.getAttribute('data-filter');
      galleryItems.forEach(function (item) {
        var show = filter === 'all' || item.getAttribute('data-category') === filter;
        item.classList.toggle('hidden', !show);
      });
    });
  });

  // ---- Gallery lightbox ----
  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxClose = document.getElementById('lightboxClose');
  if (lightbox && lightboxImg) {
    galleryItems.forEach(function (item) {
      item.addEventListener('click', function () {
        var img = item.querySelector('img');
        if (!img) return;
        lightboxImg.src = img.src;
        lightboxImg.alt = img.alt;
        lightbox.classList.add('open');
      });
    });
    function closeLightbox() { lightbox.classList.remove('open'); lightboxImg.src = ''; }
    lightboxClose.addEventListener('click', closeLightbox);
    lightbox.addEventListener('click', function (e) { if (e.target === lightbox) closeLightbox(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeLightbox(); });
  }

  // ---- Pre-select service when a "Request Slot / Get Quote / etc" link is clicked ----
  var serviceSelect = document.getElementById('service');
  document.querySelectorAll('[data-service]').forEach(function (link) {
    link.addEventListener('click', function () {
      if (!serviceSelect) return;
      var value = link.getAttribute('data-service');
      var match = Array.from(serviceSelect.options).find(function (opt) { return opt.value === value; });
      if (match) serviceSelect.value = value;
    });
  });

  // ---- Quote form: builds a WhatsApp message and opens WhatsApp ----
  var quoteForm = document.getElementById('quoteForm');
  if (quoteForm) {
    quoteForm.addEventListener('submit', function (e) {
      e.preventDefault();

      var customerName = document.getElementById('customerName').value.trim();
      var vehicle = document.getElementById('vehicle').value.trim();
      var service = document.getElementById('service').value;
      var location = document.getElementById('location').value.trim();
      var notes = document.getElementById('notes').value.trim();

      var lines = [
        'Hi Godoy Auto Detailing, I\'d like a quote:',
        'Name: ' + customerName,
        'Vehicle: ' + vehicle,
        'Service: ' + service,
        'Location: ' + location
      ];
      if (notes) lines.push('Notes: ' + notes);

      var message = encodeURIComponent(lines.join('\n'));
      trackConversion('Quote Form Submit');
      window.open('https://wa.me/447563718790?text=' + message, '_blank');
    });
  }

});
