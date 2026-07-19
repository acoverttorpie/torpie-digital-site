from build import eyebrow

TITLE = "About Torpie Digital | Small on Purpose"
DESCRIPTION = ("Torpie Digital is a small company run by Aiden Torpie, based "
               "in New York, working with local businesses everywhere. Get a "
               "straight answer within one business day.")

BODY = f"""
<section class="hero" aria-labelledby="hero-heading">
  <div class="container hero__grid">
    <div>
      {eyebrow("About")}
      <h1 id="hero-heading">Torpie Digital is a family name. It\u2019s on everything we build.</h1>
      <p class="hero__lede">Torpie Digital is a small company run by Aiden
      Torpie, based in New York, working with local businesses everywhere.</p>
    </div>
    <div>
      <figure class="photo-card reveal">
          <div class="placeholder-shot">
            <svg viewBox="0 0 24 24" fill="none" stroke="#1E6B4F" stroke-width="1.5"
              stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5"/>
            </svg>
            <span>[PHOTO: Aiden, warm natural light, working. Replace before launch.]</span>
          </div>
      </figure>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="story-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("The story")}
      <h2 id="story-heading">Small on purpose.</h2>
      <p>We started Torpie Digital because of a pattern we kept seeing: a local
      business pays for a website, the web person disappears, and the site
      slowly stops working. Nobody\u2019s watching it. Nobody answers the
      reviews. Nobody notices when the Google listing breaks.</p>
      <p>So we built a company where staying is the business model. We build
      your website, and then we take care of it: hosting, updates, edits,
      reviews, your Google presence. The build is a project. The care is the
      job.</p>
      <p>Being small isn\u2019t a stage we\u2019re getting through. It\u2019s
      the design. Your website is built and maintained by the same hands. When
      you email, the person who answers is the person who can fix it. No
      account managers, no tickets, no \u201clet me check with the
      developer.\u201d</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="believe-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("What we believe")}
      <h2 id="believe-heading" class="visually-hidden">What we believe</h2>
    </div>
    <div class="grid grid-3">
      <div class="reveal">
        <h3>Websites should work for a living.</h3>
        <p class="text-muted">Not sit there looking nice. Get found, get calls,
        get maintained.</p>
      </div>
      <div class="reveal">
        <h3>Plain talk beats jargon.</h3>
        <p class="text-muted">If we can\u2019t explain it in one sentence, we
        haven\u2019t finished thinking about it.</p>
      </div>
      <div class="reveal">
        <h3>Honesty is the sales strategy.</h3>
        <p class="text-muted">Real prices on the site. Real numbers with
        timeframes. A cancellation policy we\u2019re happy to show you.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--sage" id="contact" aria-labelledby="contact-heading">
  <div class="container">
    <div class="grid grid-2 contact-grid">
      <div class="reveal">
        {eyebrow("Contact")}
        <h2 id="contact-heading">Tell us about your business.</h2>
        <p>You\u2019ll get a straight answer within one business day. If
        we\u2019re not the right fit, we\u2019ll say so.</p>
        <p class="mt-3">[EMAIL] &middot; [PHONE]<br>
        <span class="text-muted">Remote-based in New York. Serving local
        businesses everywhere.</span></p>
      </div>
      <form class="card form reveal" data-contact-form novalidate>
        <div class="form__notice" data-form-notice tabindex="-1" aria-live="polite"></div>
        <div class="field">
          <label for="f-name">Your name</label>
          <input id="f-name" name="name" type="text" autocomplete="name" required>
          <p class="field-error">Enter your name so we know who to reply to.</p>
        </div>
        <div class="field">
          <label for="f-business">Business name</label>
          <input id="f-business" name="business" type="text" autocomplete="organization" required>
          <p class="field-error">Enter your business name.</p>
        </div>
        <div class="field">
          <label for="f-phone">Phone</label>
          <input id="f-phone" name="phone" type="tel" autocomplete="tel" required>
          <p class="field-error">Enter a phone number where we can reach you.</p>
        </div>
        <div class="field">
          <label for="f-need">What do you need?</label>
          <select id="f-need" name="need" required>
            <option value="">Choose one</option>
            <option>A new website</option>
            <option>Care for an existing site</option>
            <option>Not sure yet</option>
          </select>
          <p class="field-error">Choose the option closest to what you need.</p>
        </div>
        <div class="field">
          <label for="f-about">Tell us a little about your business</label>
          <textarea id="f-about" name="about" required></textarea>
          <p class="field-error">Tell us a little about your business, even one
          sentence helps.</p>
        </div>
        <div class="hp-field" aria-hidden="true">
          <label for="f-company-website">Leave this field empty</label>
          <input id="f-company-website" name="company_website" type="text" tabindex="-1" autocomplete="off">
        </div>
        <button class="btn btn-primary" type="submit">Send it</button>
      </form>
    </div>
  </div>
</section>
"""
