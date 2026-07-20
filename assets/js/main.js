/* Torpie Digital · site behavior
   No dependencies. Every feature degrades cleanly without JS. */

(function () {
  "use strict";

  /* ------------------------------------------------------------
     Configuration boundary.
     Fill these in before launch. Both are safe no-ops when empty.
     ------------------------------------------------------------ */
  var CONFIG = {
    GA4_ID: "G-BWB3RBKJB8",
    FORM_ENDPOINT: ""  // GoHighLevel inbound webhook URL. In GHL:
                       // Automation > Create Workflow > trigger
                       // "Inbound Webhook", then paste the generated
                       // URL here. Payload keys: name, business, phone,
                       // email, need, about, source_page.
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
          "Paste your GoHighLevel inbound webhook URL into FORM_ENDPOINT in assets/js/main.js. " +
          "Until then, reach us directly by email or phone below.",
          true
        );
        return;
      }

      submitting = true;
      submitBtn.disabled = true;
      submitBtn.classList.add("is-loading");
      var data = new FormData(form);
      data.delete("company_website");
      var payload = {};
      data.forEach(function (value, key) { payload[key] = value; });
      payload.source_page = window.location.pathname;
      payload.submitted_at = new Date().toISOString();

      fetch(CONFIG.FORM_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(payload),
        headers: { "Accept": "application/json", "Content-Type": "application/json" }
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
        submitBtn.classList.remove("is-loading");
      });
    });
  }

  function escapeHtml(str) {
    return str.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
})();

/* ============================================================
   BOLD PASS — motion layer
   Progressive enhancement only: everything checks
   prefers-reduced-motion and fails silently.
   ============================================================ */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Brass scroll progress bar ---------- */
  if (!reduce) {
    var bar = document.createElement("div");
    bar.className = "scroll-progress";
    bar.setAttribute("aria-hidden", "true");
    document.body.appendChild(bar);
    var ticking = false;
    function paint() {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      bar.style.setProperty("--scroll-progress", max > 0 ? (window.scrollY / max).toFixed(4) : 0);
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(paint); ticking = true; }
    }, { passive: true });
    paint();
  }

  /* ---------- Staggered reveals ---------- */
  if (!reduce) {
    var groups = {};
    document.querySelectorAll(".reveal").forEach(function (el) {
      var parent = el.parentElement;
      var key = parent ? Array.prototype.indexOf.call(document.querySelectorAll("*"), parent) : 0;
      groups[key] = (groups[key] || 0);
      el.style.setProperty("--stagger", ((groups[key] % 6) * 0.07).toFixed(2) + "s");
      groups[key]++;
    });
  }

  /* ---------- Hero signature: word-by-word rise + drawn underline ---------- */
  var heroH1 = document.querySelector(".hero h1");
  if (heroH1 && !reduce && heroH1.children.length === 0) {
    var words = heroH1.textContent.trim().split(/\s+/);
    heroH1.textContent = "";
    words.forEach(function (word, i) {
      var span = document.createElement("span");
      span.className = "hero-word";
      span.style.setProperty("--i", i);
      span.textContent = word;
      if (i === words.length - 1) {
        var accent = document.createElement("span");
        accent.className = "hero-accent";
        accent.appendChild(span);
        accent.insertAdjacentHTML("beforeend",
          '<svg viewBox="0 0 100 12" preserveAspectRatio="none" aria-hidden="true">' +
          '<path pathLength="120" d="M2 9 C 25 4, 50 11, 72 6 S 95 7, 98 5"/></svg>');
        heroH1.appendChild(accent);
      } else {
        heroH1.appendChild(span);
        heroH1.appendChild(document.createTextNode(" "));
      }
    });
  }

  /* ---------- Hero mockup: settle into float, tilt toward cursor ---------- */
  var media = document.querySelector(".hero__media");
  if (media && !reduce) {
    var frame = media.querySelector(".browser-frame");
    if (frame) {
      frame.addEventListener("animationend", function onIn(e) {
        if (e.animationName === "frame-in") {
          media.classList.add("is-settled");
          frame.removeEventListener("animationend", onIn);
        }
      });
      if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
        media.addEventListener("mousemove", function (e) {
          var r = media.getBoundingClientRect();
          var x = (e.clientX - r.left) / r.width - 0.5;
          var y = (e.clientY - r.top) / r.height - 0.5;
          media.classList.add("is-tilting");
          media.style.setProperty("--tilt-y", (x * 6).toFixed(2) + "deg");
          media.style.setProperty("--tilt-x", (y * -6).toFixed(2) + "deg");
        });
        media.addEventListener("mouseleave", function () {
          media.classList.remove("is-tilting");
        });
      }
    }
  }

  /* ---------- Marquee band ---------- */
  var bandList = document.querySelector(".divider-band .check-list--inline");
  if (bandList && !reduce) {
    var marquee = document.createElement("div");
    marquee.className = "marquee";
    var track = document.createElement("div");
    track.className = "marquee__track";
    bandList.parentNode.insertBefore(marquee, bandList);
    track.appendChild(bandList);
    var clone = bandList.cloneNode(true);
    clone.setAttribute("aria-hidden", "true");
    track.appendChild(clone);
    marquee.appendChild(track);
  }

  /* ---------- Stat count-up ---------- */
  var stats = document.querySelectorAll(".stat__number");
  if (stats.length && !reduce && "IntersectionObserver" in window) {
    var NUM = /\d+(?:\.\d+)?/g;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        var el = entry.target;
        var template = el.textContent;
        var targets = (template.match(NUM) || []).map(Number);
        if (!targets.length) return;
        var decimals = (template.match(NUM) || []).map(function (t) {
          return (t.split(".")[1] || "").length;
        });
        var start = null, DURATION = 1100;
        function tick(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / DURATION, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          var i = 0;
          el.textContent = template.replace(NUM, function () {
            var v = targets[i] * eased;
            return v.toFixed(decimals[i++]);
          });
          if (p < 1) window.requestAnimationFrame(tick);
          else el.textContent = template;
        }
        window.requestAnimationFrame(tick);
      });
    }, { threshold: 0.5 });
    stats.forEach(function (el) { io.observe(el); });
  }
})();

/* ============================================================
   FANCY PASS 2 — chrome choreography
   ============================================================ */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Header shrinks + deepens after scroll ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var ticking = false;
    function paintHeader() {
      header.classList.toggle("is-scrolled", window.scrollY > 12);
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(paintHeader); ticking = true; }
    }, { passive: true });
    paintHeader();
  }

  /* ---------- Timeline connector draws in ---------- */
  var timelines = document.querySelectorAll(".timeline");
  if (timelines.length && !reduce && "IntersectionObserver" in window) {
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-inview");
          tio.unobserve(entry.target);
        }
      });
    }, { threshold: 0.3 });
    timelines.forEach(function (el) { tio.observe(el); });
  } else {
    timelines.forEach(function (el) { el.classList.add("is-inview"); });
  }

  /* ---------- FAQ: animated open/close ---------- */
  if (!reduce) {
    document.querySelectorAll(".faq details").forEach(function (details) {
      var summary = details.querySelector("summary");
      var body = details.querySelector(".faq__answer");
      if (!summary || !body) return;
      summary.addEventListener("click", function (e) {
        e.preventDefault();
        if (details.classList.contains("is-animating")) return;
        details.classList.add("is-animating");
        if (details.open) {
          body.style.height = body.scrollHeight + "px";
          requestAnimationFrame(function () {
            requestAnimationFrame(function () { body.style.height = "0px"; });
          });
          body.addEventListener("transitionend", function done() {
            details.open = false;
            body.style.height = "";
            details.classList.remove("is-animating");
            body.removeEventListener("transitionend", done);
          });
        } else {
          details.open = true;
          var h = body.scrollHeight;
          body.style.height = "0px";
          requestAnimationFrame(function () {
            requestAnimationFrame(function () { body.style.height = h + "px"; });
          });
          body.addEventListener("transitionend", function done() {
            body.style.height = "";
            details.classList.remove("is-animating");
            body.removeEventListener("transitionend", done);
          });
        }
      });
    });
  }
})();
