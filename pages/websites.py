from build import (browser_frame, check_list, dark_cta, eyebrow, faq_schema,
                   faq_section)

TITLE = "Website Builds for Local Businesses | Torpie Digital"
DESCRIPTION = ("Custom-coded websites for local businesses. Fast to load, easy "
               "to trust, and connected to Google from day one. Three builds "
               "from $1,000, yours forever.")

FAQ_ITEMS = [
    ("What do you need from me?",
     "About 15 minutes. One intake form covers your business, your services, "
     "and how you talk to customers. We write everything from there. Add your "
     "logo and photos of your work, and we\u2019re building."),
    ("What if I already have a website?",
     "We build you a new one and move over anything worth keeping. Old sites "
     "on page builders usually aren\u2019t worth saving, but the content "
     "sometimes is."),
    ("Can I edit the site myself?",
     "The site is custom code, so edits go through us. On a plan, they\u2019re "
     "included up to a fair monthly allowance and usually done within a couple "
     "of days. Most owners find this beats fighting a page builder at 11pm."),
    ("What if I need more pages later?",
     "Easy. Quoted fairly, built by the same hands, matched to your existing "
     "design."),
]

EXTRA_SCHEMA = faq_schema(FAQ_ITEMS)

EVERY_BUILD = [
    "Custom code, fast and secure",
    "Mobile-first design",
    "Search-ready launch",
    "Google Analytics and Search Console, set up and verified",
    "Professional copywriting from one 15-minute form",
    "Working forms with instant confirmation and lead alerts",
    "SSL security",
    "Full ownership: your domain, your site, your content",
]

BODY = f"""
<section class="hero hero--simple" aria-labelledby="hero-heading">
  <div class="container">
    <div class="section-head">
      {eyebrow("Website builds")}
      <h1 id="hero-heading">Your website has one job: turn lookers into callers.</h1>
      <p class="hero__lede">We design and build custom websites for local
      businesses. Fast to load, easy to trust, and connected to Google from
      day one. Built once, built right, and yours forever.</p>
      <div class="hero__actions">
        <a class="btn btn-primary" data-track-cta="hero" href="/about/#contact">Get a quote</a>
        <a class="btn btn-secondary" href="/pricing/">See pricing</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="built-right-heading">
  <div class="container">
    <div class="section-head reveal">
      <h2 id="built-right-heading">No templates. No page builders. No plugins to break.</h2>
      <p>Every Torpie Digital website is custom-coded. That\u2019s why they
      load in under a second, why they don\u2019t break when some plugin
      updates, and why edits get done fast: we wrote the code, so we don\u2019t
      have to fight it.</p>
      <p>Fast sites keep visitors around. Clean code keeps Google happy. And a
      site built by hand is a site one person can actually take care of.
      That\u2019s the whole model.</p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="builds-heading">
  <div class="container">
    <div class="section-head reveal">
      <h2 id="builds-heading">Pick the size. The standard of work never changes.</h2>
    </div>

    <div class="stack-40">
    <article class="card reveal">
      <div class="card-cols">
        <div class="card-cols__aside">
          <div class="price-line"><h3>Foundation</h3><p class="price">$1,000</p></div>
          <p class="lede"><strong>The professional essentials, done properly.</strong></p>
          <p>For solo operators and businesses with one core offer. You need to
          look legitimate, show up on Google, and make it dead simple to call you.</p>
        </div>
        <div>
          <h4>What you get</h4>
          <p>1 to 3 pages, home, services, and contact. Custom design on our proven
          structure. Professional copywriting included: you fill out one 15-minute
          form, we write the whole site in your voice. Click-to-call, contact form,
          map. One revision round. Live in about two weeks.</p>
          <p class="text-muted small"><strong>Best for:</strong> a detailer, a
          towing company, a one-crew operation that needs to exist online,
          properly, this month.</p>
        </div>
      </div>
    </article>

    <article class="card card--featured reveal">
      <span class="card__flag">Most chosen</span>
      <div class="card-cols">
        <div class="card-cols__aside">
          <div class="price-line"><h3>Storefront</h3><p class="price">$1,500</p></div>
          <p class="lede"><strong>A page for everything you do.</strong></p>
          <p>For established businesses with multiple services. When someone
          searches for one specific thing you offer, they should land on a page
          about exactly that.</p>
        </div>
        <div>
          <h4>What you get</h4>
          <p>4 to 6 pages, including a dedicated page for each core service.
          Deeper custom design. Professional copywriting from your intake form. A
          review display section so your reputation does some selling. An articles
          section built in, ready if you ever want your site growing month over
          month. Two revision rounds. Live in about three weeks.</p>
          <p class="text-muted small"><strong>Best for:</strong> a landscaper with
          five services, a barbershop with a real brand, a restaurant that\u2019s
          more than a menu PDF.</p>
        </div>
      </div>
    </article>

    <article class="card reveal">
      <div class="card-cols">
        <div class="card-cols__aside">
          <div class="price-line"><h3>Flagship</h3><p class="price">$2,500</p></div>
          <p class="lede"><strong>Your hardest-working salesperson.</strong></p>
          <p>For competitive markets, multi-service businesses, and owners who want
          the website carrying real weight.</p>
        </div>
        <div>
          <h4>What you get</h4>
          <p>7 to 12 pages and full custom design, written from your intake form
          with conversion strategy on every page, so each one has a job and a next
          step. Integrations: booking, menus, galleries, whatever your operation
          runs on. Content moved over from your old site, with redirects so Google
          follows you. Extended tracking where your setup calls for it. Two weeks
          of post-launch support. Priority timeline.</p>
          <p class="text-muted small"><strong>Best for:</strong> a med spa, a
          multi-location operation, a contractor going after bigger jobs in a
          crowded market.</p>
        </div>
      </div>
    </article>
    </div>
  </div>
</section>

<div class="divider-band" aria-labelledby="every-build-heading">
  <div class="container reveal">
    <h4 id="every-build-heading">Every Torpie Digital website, at every price:</h4>
    {check_list(EVERY_BUILD, inline=True)}
  </div>
</div>

<section class="section" aria-labelledby="search-ready-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("Search-ready, explained")}
      <h2 id="search-ready-heading">Ready for Google on day one.</h2>
      <p>A lot of websites launch invisible. Wrong structure, missing
      information, nothing telling Google what the business is or where it
      operates. Then the owner wonders why nobody finds them.</p>
      <p>Every Torpie Digital site launches with the structure, metadata, and
      sitemap Google looks for, and it\u2019s connected to Google\u2019s
      analytics and search tools before we call it done. We verify both are
      collecting correctly at launch.</p>
      <p><strong>What that means for you:</strong> Google can find and read
      your site immediately, and you can see how people are finding you.
      Rankings build over time, months, not days, and we\u2019ll never pretend
      otherwise. But the foundation is ready the moment you launch, and the
      data will be there to prove what\u2019s working.</p>
    </div>
  </div>
</section>

<section class="section section--sage" aria-labelledby="leads-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("Your leads, handled from second one")}
      <h2 id="leads-heading">When someone reaches out, they hear back in under a minute.</h2>
      <p>Every form on your site does three things instantly: your customer
      gets a branded confirmation so they know you got their message, you get
      the lead by email so you can follow up while they\u2019re still
      interested, and the contact gets saved to your list so you never lose
      them.</p>
      <p>Most businesses take hours to respond to a lead, if they respond at
      all. Yours acknowledges every inquiry in under a minute, around the
      clock. Then you close them. That part\u2019s still yours.</p>
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
        <p>A short call about your business. You get a clear quote and a real
        timeline.</p>
      </article>
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">02</span>
        <h3>Build.</h3>
        <p>We design and build. You see everything before it goes live.</p>
      </article>
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">03</span>
        <h3>Launch.</h3>
        <p>Fast, search-ready, tracking verified. We confirm it all works.</p>
      </article>
      <article class="card step-card reveal">
        <span class="step-card__num" aria-hidden="true">04</span>
        <h3>Handled.</h3>
        <p>Join a plan and it becomes our job to keep it working.
        <a class="arrow-link" href="/plans/">See plans &rarr;</a></p>
      </article>
    </div>
  </div>
</section>

{faq_section("Websites FAQ", FAQ_ITEMS, section_class="section section--white")}

{dark_cta("Let\u2019s build the one that fits.",
          "Not sure which build you need? Tell us about your business and "
          "we\u2019ll tell you straight, even if the answer is the cheapest one.")}
"""
