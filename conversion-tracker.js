/**
 * Kashi Dharshan - Universal Conversion & Lead Engine
 * Ensures 100% reliable WhatsApp lead capture across all devices & forms
 */

// Global WhatsApp Submission Function
window.submitYatraFormToWhatsApp = function(event, defaultPackage) {
  if (event && event.preventDefault) {
    event.preventDefault();
  }
  
  var form = (event && event.target && event.target.tagName === 'FORM') 
             ? event.target 
             : (document.getElementById('yatraForm') || document.getElementById('kashiPkgForm') || document.forms[0]);

  if (!form) {
    console.error('[Lead Engine] No form found to submit.');
    return false;
  }

  // Field extractors with robust fallbacks
  var nameEl = form.querySelector('[name="fullname"], [name="name"], #name, input[type="text"]');
  var phoneEl = form.querySelector('[name="mobile"], [name="phone"], #phone, input[type="tel"]');
  var dateEl = form.querySelector('[name="travel_date"], [name="date"], #date, input[type="date"]');
  var paxEl = form.querySelector('[name="guests"], [name="people"], [name="pax"], #people, select[name="people"]');
  var budgetEl = form.querySelector('[name="budget"], select[name="budget"], #budget');
  var pkgEl = form.querySelector('[name="package"], [name="city"], #city');
  var notesEl = form.querySelector('[name="msg"], [name="message"], textarea, #msg');

  var name = (nameEl && nameEl.value && nameEl.value.trim()) ? nameEl.value.trim() : 'Pilgrim Guest';
  var phone = (phoneEl && phoneEl.value) ? phoneEl.value.trim() : '';
  var date = (dateEl && dateEl.value && dateEl.value.trim()) ? dateEl.value.trim() : 'Upcoming / Flexible';
  var pax = (paxEl && paxEl.value) ? paxEl.value.trim() : '2–4 Persons';
  var budget = (budgetEl && budgetEl.value) ? budgetEl.value.trim() : 'Standard (Recommended)';
  var notes = (notesEl && notesEl.value && notesEl.value.trim()) ? notesEl.value.trim() : '';
  
  var pkgName = (pkgEl && pkgEl.value && pkgEl.value.trim()) 
                ? pkgEl.value.trim() 
                : (defaultPackage || (document.title ? document.title.split('|')[0].trim() : 'Kashi Ayodhya Tour Package'));

  // Mobile Validation (At least 10 digits)
  var digits = phone.replace(/\D/g, '');
  if (!digits || digits.length < 10) {
    alert('कृपया सही 10-अंकों का मोबाइल नंबर दर्ज करें ताकि हम आपको तुरंत पैकेज का रेट और यात्रा प्लान WhatsApp पर भेज सकें!');
    if (phoneEl) phoneEl.focus();
    return false;
  }

  // Compose formatted WhatsApp message
  var message = "🚩 *NEW YATRA ENQUIRY - KASHI DHARSHAN*\n\n" +
                "👤 *Devotee Name:* " + name + "\n" +
                "📞 *Mobile No:* " + phone + "\n" +
                "🛕 *Tour Package:* " + pkgName + "\n" +
                "📅 *Travel Date:* " + date + "\n" +
                "👥 *Travellers:* " + pax + "\n" +
                "🏨 *Comfort Tier:* " + budget + "\n";

  if (notes) {
    message += "📝 *Special Requests:* " + notes + "\n";
  }

  message += "\n🙏 Please share detailed day-wise itinerary & lowest price quote!";

  var waUrl = "https://wa.me/917011960307?text=" + encodeURIComponent(message);

  // Store in local storage as backup
  try {
    var stored = JSON.parse(localStorage.getItem('kd_leads') || '[]');
    stored.push({ name: name, phone: phone, pkg: pkgName, date: date, pax: pax, time: new Date().toISOString() });
    localStorage.setItem('kd_leads', JSON.stringify(stored));
  } catch(e) {}

  // Dispatch analytics tracking event
  if (typeof window.dispatchTrackingEvent === 'function') {
    window.dispatchTrackingEvent('lead_conversion_success', {
      name: name,
      package: pkgName,
      phone: phone,
      destination: pkgName
    });
  }

  // Direct redirection to WhatsApp
  window.location.href = waUrl;
  return false;
};

// Auto-bind to all forms on page
document.addEventListener('DOMContentLoaded', function() {
  var forms = document.querySelectorAll('form');
  forms.forEach(function(form) {
    // If form doesn't already have a valid submission handler, attach one
    if (!form.getAttribute('data-kd-bound')) {
      form.setAttribute('data-kd-bound', 'true');
      form.addEventListener('submit', function(e) {
        var pkg = form.getAttribute('data-package') || '';
        return window.submitYatraFormToWhatsApp(e, pkg);
      });
    }
  });

  // Track WhatsApp link clicks
  document.addEventListener('click', function(e) {
    var anchor = e.target.closest('a');
    if (!anchor) return;
    var href = anchor.href || '';
    if (href.indexOf('wa.me') !== -1 || anchor.classList.contains('whatsapp-float')) {
      var path = window.location.pathname.split('/').pop() || 'index';
      if (typeof window.dispatchTrackingEvent === 'function') {
        window.dispatchTrackingEvent('whatsapp_click', {
          page: path,
          timestamp: new Date().toISOString()
        });
      }
    }
  });
});

// Analytics Helper
function dispatchTrackingEvent(eventName, eventData) {
  try {
    console.log('[Lead Engine] Event:', eventName, eventData);
    var event = new CustomEvent(eventName, { detail: eventData });
    document.dispatchEvent(event);
    if (typeof window.gtag === 'function') {
      window.gtag('event', eventName, eventData);
    }
  } catch(e) {}
}
window.dispatchTrackingEvent = dispatchTrackingEvent;
