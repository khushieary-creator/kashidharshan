/**
 * Ayodhya Dharshan - Conversion & Funnel Tracker
 * (A lightweight tracking utility for SEO / AEO conversion signals)
 */
(function() {
  // Helper to safely dispatch custom events for future GA4/GTM integrations
  function dispatchTrackingEvent(eventName, eventData) {
    console.log(`[Yatra Tracker] Event Triggered: ${eventName}`, eventData);
    
    // Dispatch standard CustomEvent
    const event = new CustomEvent(eventName, { detail: eventData });
    document.dispatchEvent(event);

    // If Google Analytics (gtag) is present on the window, push to dataLayer
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, eventData);
    }
    // If Facebook Pixel (fbq) is present, trigger custom event
    if (typeof window.fbq === 'function') {
      window.fbq('trackCustom', eventName, eventData);
    }
  }

  // 1. Track WhatsApp Clicks
  document.addEventListener('click', function(e) {
    // Find the closest anchor tag
    const anchor = e.target.closest('a');
    if (!anchor) return;

    const href = anchor.href || '';
    
    // Check if it's a WhatsApp link
    if (href.includes('wa.me') || anchor.classList.contains('whatsapp-float')) {
      const pagePath = window.location.pathname.split('/').pop() || 'index.html';
      const textParam = new URLSearchParams(href.split('?')[1] || '').get('text') || '';
      
      dispatchTrackingEvent('whatsapp_click', {
        page: pagePath,
        text_sent: textParam,
        timestamp: new Date().toISOString()
      });
    }
  });

  // 2. Track Form Enquiry Submissions (Redirect to Thank You Page)
  // Since the forms redirect to thankyou.html, we can detect if the current page is thankyou.html
  const currentPath = window.location.pathname.split('/').pop() || '';
  if (currentPath.includes('thankyou.html')) {
    const params = new URLSearchParams(window.location.search);
    const name = params.get('name');
    const phone = params.get('phone');
    const city = params.get('city') || 'Ramayana Circuit';
    const people = params.get('people');
    const dates = params.get('dates');

    // Only fire event if we have a name and phone (meaning it was a real redirect, not direct hit)
    if (name || phone) {
      dispatchTrackingEvent('lead_conversion_success', {
        destination: city,
        travellers: people || 'Not Specified',
        dates: dates || 'Not Specified',
        timestamp: new Date().toISOString(),
        method: 'Web3Forms'
      });
    }
  }
})();
