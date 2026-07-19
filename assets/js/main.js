/* Torpie Digital · site behavior
   No dependencies. Every feature degrades cleanly without JS. */

(function () {
  "use strict";

  /* ------------------------------------------------------------
     Configuration boundary.
     Fill these in before launch. Both are safe no-ops when empty.
     ------------------------------------------------------------ */
  var CONFIG = {
    GA4_ID: "",        // e.g. "G-XXXXXXXXXX". Leave empty until supplied.
    FORM_ENDPOINT: ""  // POST destination for the contact form (Formspree,
                       // Basin, a serverless function, etc.). Leave empty
                       // until a working destination is configured.
  };

  /* ---------- Google Analytics 4 (guarded) ---------- */
  var analyticsReady = false;
  if (CONFIG.GA4_ID) {
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + CONFIG.GA4_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", CONFIG.GA4_ID);
    analyticsReady = true;
  }
  function track(eventName, params) {
    if (analyticsReady && typeof window.gtag === "function") {
      window.gtag("event", eventName, params || {});
    }
  }

  /* ---------- Announcement bar ---------- */
  var bar = document.querySelector("[data-announcement]");
  if (bar) {
    var DISMISS_KEY = "torpie-announcement-dismissed";
    var dismissed = false;
    try { dismissed = localStorage.getItem(DISMISS_KEY) === "1"; } catch (e) {}
    if (dismissed) {
      bar.hidden = true;
    } else {
      bar.hidden = false;
      var close = bar.querySelector("[data-announcement-close]");
      if (close) {
        close.addEventListener("click", function () {
          bar.hidden = true;
          try { localStorage.setItem(DISMISS_KEY, "1"); } catch (e) {}
        });
      }
    }
  }

  /* ---------- Mobile navigation ---------- */
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---------- Scroll reveal (respects prefers-reduced-motion) ---------- */
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (revealEls.length && !reduceMotion && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ---------- Sticky mobile CTA after ~50% scroll ---------- */
  var sticky = document.querySelector("[data-sticky-cta]");
  if (sticky) {
    document.body.classList.add("has-sticky-cta");
    var ticking = false;
    function updateSticky() {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      var progress = max > 0 ? window.scrollY / max : 0;
      sticky.classList.toggle("is-visible", progress >= 0.5);
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(updateSticky); ticking = true; }
    }, { passive: true });
    updateSticky();
  }

  /* ---------- Pricing toggle (monthly / annual) ---------- */
  var billingWrap = document.querySelector("[data-billing]");
  if (billingWrap) {
    var buttons = document.querySelectorAll("[data-billing-choice]");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var choice = btn.getAttribute("data-billing-choice");
        billingWrap.setAttribute("data-billing", choice);
        buttons.forEach(function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
      });
    });
  }

  /* ---------- Primary CTA tracking ---------- */
  document.querySelectorAll("[data-track-cta]").forEach(function (el) {
    el.addEventListener("click", function () {
      track("cta_click", { cta: el.getAttribute("data-track-cta") });
    });
  });

  /* ---------- Contact form ---------- */
  var form = document.querySelector("[data-contact-form]");
  if (form) {
    var notice = form.querySelector("[data-form-notice]");
    var submitBtn = form.querySelector("[type=submit]");
    var submitting = false;

    function showNotice(html, isError) {
      notice.innerHTML = html;
      notice.classList.add("is-visible");
      notice.classList.toggle("form__notice--error", !!isError);
      notice.focus();
    }

    function validateField(field) {
      var input = field.querySelector("input, select, textarea");
      if (!input) return true;
      var valid = input.checkValidity();
      field.classList.toggle("is-invalid", !valid);
      input.setAttribute("aria-invalid", valid ? "false" : "true");
      return valid;
    }

    form.querySelectorAll(".field").forEach(function (field) {
      var input = field.querySelector("input, select, textarea");
      if (input) {
        input.addEventListener("blur", function () { validateField(field); });
        input.addEventListener("input", function () {
          if (field.classList.contains("is-invalid")) validateField(field);
        });
      }
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (submitting) return;

      var allValid = true;
      form.querySelectorAll(".field").forEach(function (field) {
        if (!validateField(field)) allValid = false;
      });
      if (!allValid) {
        var firstInvalid = form.querySelector(".is-invalid input, .is-invalid select, .is-invalid textarea");
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      /* Honeypot: silently drop bot submissions */
      var hp = form.querySelector("[name=company_website]");
      if (hp && hp.value) return;

      if (!CONFIG.FORM_ENDPOINT) {
        showNotice(
          "This form is not connected to a destination yet. " +
          "Set FORM_ENDPOINT in assets/js/main.js before launch. " +
          "Until then, reach us directly by email or phone below.",
          true
        );
        return;
      }

      submitting = true;
      submitBtn.disabled = true;
      var data = new FormData(form);
      data.delete("company_website");

      fetch(CONFIG.FORM_ENDPOINT, {
        method: "POST",
        body: data,
        headers: { "Accept": "application/json" }
      }).then(function (res) {
        if (!res.ok) throw new Error("Request failed");
        var name = (data.get("name") || "").toString().trim().split(" ")[0] || "there";
        form.querySelectorAll(".field, [type=submit]").forEach(function (el) { el.hidden = true; });
        showNotice(
          "Got it. Thanks, " + escapeHtml(name) + ". You\u2019ll hear from us within one " +
          "business day, usually much sooner. In the meantime, feel free to look at " +
          "<a href=\"/work/\">our work</a>.<br><br>" +
          "<span class=\"small\">(And yes: this form does exactly what your customers\u2019 " +
          "forms will do. You just got a confirmation in under a minute.)</span>"
        );
        track("form_submit_success", { form: "contact" });
      }).catch(function () {
        showNotice(
          "Something went wrong sending your message. Please try again, or reach us " +
          "directly by email or phone below.",
          true
        );
      }).finally(function () {
        submitting = false;
        submitBtn.disabled = false;
      });
    });
  }

  function escapeHtml(str) {
    return str.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
})();
