from build import (browser_frame, check_list, dark_cta, eyebrow, faq_schema,
                   faq_section)

TITLE = "Torpie Digital | Websites that work for a living"
DESCRIPTION = ("Torpie Digital builds fast, custom websites for local businesses, "
               "then takes care of them: hosting, updates, reviews, and your "
               "Google presence, handled.")

FAQ_ITEMS = [
    ("Do I have to buy a monthly plan?",
     "No. The build is yours either way. But a website needs hosting, upkeep, "
     "and attention, and most clients would rather that be our job. That\u2019s "
     "what the plans are for."),
    ("What\u2019s included in the monthly plans?",
     "Care keeps your site online, maintained, and edited, saves every lead to "
     "your contact list, and answers every review. Presence adds active Google "
     "Business Profile management, a monthly page for your site, and a "
     "quarterly report in plain language."),
    ("How long does a build take?",
     "Foundation sites launch in about two weeks. Larger builds take three to "
     "four. We\u2019ll give you a real date before we start."),
    ("Do I own my website?",
     "Yes. Your domain, your website, your content, your contact list. We "
     "manage them for you while you\u2019re on a plan, and if you ever leave, "
     "you take everything with you."),
    ("What does \u201csearch-ready\u201d mean?",
     "Your site launches fast, properly structured, and connected to "
     "Google\u2019s analytics and search tools. Google can find and read it "
     "from day one, and you can see how people are finding you. Rankings build "
     "over time. The foundation is ready immediately."),
]

EXTRA_SCHEMA = faq_schema(FAQ_ITEMS)

BUILD_INCLUDES = [
    "Custom code, no page builders",
    "Mobile-first design",
    "Search-ready launch",
    "Google Analytics and Search Console, set up and verified",
    "Professional copywriting from one 15-minute form",
    "Working forms with instant lead alerts",
    "You own everything",
]

BODY = f"""
<section class="hero" aria-labelledby="hero-heading">
  <div class="container hero__grid">
    <div>
      {eyebrow("Websites + ongoing care for local businesses")}
      <h1 id="hero-heading">Websites that work for a living</h1>
      <p class="hero__lede">We build fast, professional websites for local
      businesses. Then we take care of them. Hosting, updates, reviews, and
      your Google presence, handled.</p>
      <div class="hero__actions">
        <a class="btn btn-primary" data-track-cta="hero" href="/about/#contact">Get a quote</a>
        <a class="btn btn-secondary" href="/pricing/">See pricing</a>
      </div>
      <p class="hero__trust">Custom-built. Search-ready at launch. Every lead
      saved. Every review answered.</p>
    </div>
    <div class="hero__media">
      {browser_frame("yourbusiness.com",
                     "[SCREENSHOT: best live build, warm grade. Replace before launch.]")}
    </div>
  </div>
</section>

<section class="section--white section--quiet" aria-label="Results delivered by our founder">
  <div class="container grid grid-3 reveal">
    <div class="stat">
      <p class="stat__number">233%</p>
      <p class="stat__label">more monthly closes for a pest control company</p>
      <p class="stat__source">(Delivered by our founder)</p>
    </div>
    <div class="stat">
      <p class="stat__number">17.2 &rarr; 7.7</p>
      <p class="stat__label">average Google search position for a local
      caf&eacute;, over 16 months</p>
      <p class="stat__source">(Delivered by our founder)</p>
    </div>
    <div class="stat">
      <p class="stat__number">3 jobs a month</p>
      <p class="stat__label">closed from website leads for a family
      landscaping business</p>
      <p class="stat__source">(Delivered by our founder)</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="problem-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("The problem")}
      <h2 id="problem-heading">Most websites are built, launched, and forgotten.</h2>
      <p>The web guy finishes the job and disappears. Nobody updates the site.
      Reviews pile up with no response. The Google listing goes stale. And the
      owner has no idea if any of it is even working.</p>
      <p><strong>Your website should not be one more thing you have to manage.
      It should be one less.</strong></p>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="solution-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("How we work")}
      <h2 id="solution-heading">We build it right. Then we keep it working.</h2>
    </div>
    <div class="grid grid-2">
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">1</span>
        <h3>The build.</h3>
        <p>A custom website, designed for your business and coded to be fast.
        It launches search-ready and connected to Google\u2019s analytics and
        search tools, so from day one, Google can find it and you can see it
        working. One-time project. You own it.</p>
      </article>
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">2</span>
        <h3>The care.</h3>
        <p>After launch, the website becomes our job, not yours. We host it,
        maintain it, and make your edits. Every lead gets saved to your contact
        list. Every review gets a response. Monthly plan. Cancel anytime.</p>
      </article>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="builds-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("Website builds")}
      <h2 id="builds-heading">Three ways to build. One standard of work.</h2>
    </div>
    <div class="grid grid-3">
      <article class="card reveal">
        <div class="price-line"><h3>Foundation</h3><p class="price">$1,000</p></div>
        <p class="lede">A clean, professional site that gets you found and gets
        you calls. 1 to 3 pages. Ready in about two weeks.</p>
      </article>
      <article class="card card--featured reveal">
        <span class="card__flag">Most chosen</span>
        <div class="price-line"><h3>Storefront</h3><p class="price">$1,500</p></div>
        <p class="lede">A page for every service you offer. 4 to 6 pages. Built
        to win its market.</p>
      </article>
      <article class="card reveal">
        <div class="price-line"><h3>Flagship</h3><p class="price">$2,500</p></div>
        <p class="lede">Your hardest-working salesperson. Conversion strategy,
        integrations, full migration. 7 to 12 pages.</p>
      </article>
    </div>
    <div class="mt-6 reveal">
      <h4>Included with every build:</h4>
      {check_list(BUILD_INCLUDES, inline=True)}
      <p class="mt-3"><a class="arrow-link" href="/websites/">Compare the builds &rarr;</a></p>
    </div>
  </div>
</section>

<section class="section section--sage" aria-labelledby="plans-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("After launch")}
      <h2 id="plans-heading">Then we take care of it.</h2>
    </div>
    <div class="grid grid-2">
      <article class="card reveal">
        <div class="price-line"><h3>Care</h3><p class="price">$79<small>/mo</small></p></div>
        <p class="lede">Your website, handled. Hosting, security, and upkeep.
        Edits when you need them. Every lead saved to your contact list. Every
        review answered.</p>
      </article>
      <article class="card card--featured reveal">
        <span class="card__flag">Most popular</span>
        <div class="price-line"><h3>Presence</h3><p class="price">$149<small>/mo</small></p></div>
        <p class="lede">Everything in Care, plus we keep you active on Google.
        Your Business Profile optimized and posting monthly. A new page about
        your services and area every month. A plain-language check-in report
        every quarter.</p>
      </article>
    </div>
    <div class="mt-4 reveal">
      <p><strong>Pay annually and get two months on us.</strong></p>
      <p class="mt-2"><a class="arrow-link" href="/plans/">Compare the plans &rarr;</a></p>
    </div>
  </div>
</section>

<section class="section section--dark" aria-labelledby="care-matters-heading">
  <div class="container">
    <div class="section-head reveal">
      <h2 id="care-matters-heading">The build is finished once. The website never is.</h2>
      <p>Software needs updating. Content goes stale. Reviews keep arriving.
      Google keeps changing. A website with nobody behind it slowly stops
      working, and most owners never find out until the phone goes quiet.</p>
      <p><strong>Our clients don\u2019t think about any of this. That\u2019s the
      point.</strong></p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="process-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("The process")}
      <h2 id="process-heading">From first call to fully handled.</h2>
    </div>
    <div class="grid grid-4">
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">01</span>
        <h3>Talk.</h3>
        <p>A short call about your business and what you need. You get a clear
        quote, not a pitch.</p>
      </article>
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">02</span>
        <h3>Build.</h3>
        <p>We design and build your site. You review everything before launch.</p>
      </article>
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">03</span>
        <h3>Launch.</h3>
        <p>Live, fast, search-ready, and connected to Google. We confirm
        everything is tracking.</p>
      </article>
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">04</span>
        <h3>Handled.</h3>
        <p>Join a plan and the website becomes our job. You get back to yours.</p>
      </article>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="proof-heading">
  <div class="container">
    <div class="case">
      <div class="reveal">
        {eyebrow("Real work")}
        <h2 id="proof-heading">From \u201cpermanently closed\u201d on Google to 3 jobs a month.</h2>
        <p>A family landscaping business had no website, zero reviews, and a
        Google listing marked \u201cpermanently closed.\u201d We rebuilt their
        online presence from the ground up. Now they average 3 closed jobs a
        month from website leads. <span class="text-muted small">(Delivered by
        our founder)</span></p>
        <p class="mt-3"><a class="arrow-link" href="/work/">See our work &rarr;</a></p>
      </div>
      <div class="case__media">
        {browser_frame("familylandscaping.com",
                       "[SCREENSHOT: landscaping site. Replace before launch.]")}
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="why-heading">
  <div class="container">
    <div class="section-head reveal">
      <h2 id="why-heading">Small on purpose.</h2>
    </div>
    <div class="grid grid-3">
      <div class="reveal">
        <h3>We stay.</h3>
        <p class="text-muted">Most web designers finish and vanish. Staying is
        our business model.</p>
      </div>
      <div class="reveal">
        <h3>Every review answered.</h3>
        <p class="text-muted">Your customers see a business that responds.
        Every review, every time.</p>
      </div>
      <div class="reveal">
        <h3>Built and cared for by the same hands.</h3>
        <p class="text-muted">No handoffs, no tickets, no \u201clet me check
        with the developer.\u201d We are the developer.</p>
      </div>
    </div>
  </div>
</section>

{faq_section("Questions, answered.", FAQ_ITEMS, section_class="section section--white")}

{dark_cta("Ready for a website someone actually takes care of?",
          "Tell us about your business. You\u2019ll get a straight answer and a clear quote.")}
"""
