from build import check_list, dark_cta, eyebrow, faq_schema, faq_section

TITLE = "Monthly Website Care Plans | Torpie Digital"
DESCRIPTION = ("A website is never finished. Torpie Digital plans keep your "
               "site hosted, maintained, edited, and answered-for from "
               "$79 a month. No contracts, cancel anytime.")

FAQ_ITEMS = [
    ("Can I get the website without a plan?",
     "Yes. The site is yours regardless. You\u2019d handle hosting, upkeep, "
     "forms, and reviews yourself. Most clients hand it to us."),
    ("Is there a contract?",
     "No. Monthly plans cancel anytime. If you go, you take your site, your "
     "domain, and your full contact list with you."),
    ("How do the review responses work?",
     "Every review gets a response, usually within the day. AI drafts them "
     "fast; we hold them to a human standard. Thank-yous for the good ones, "
     "calm and professional replies to the rough ones."),
    ("Can I switch plans?",
     "Anytime, prorated. Most clients start on Care and move up when they "
     "want more visibility."),
]

EXTRA_SCHEMA = faq_schema(FAQ_ITEMS)

BODY = f"""
<section class="hero hero--simple" aria-labelledby="hero-heading">
  <div class="container">
    <div class="section-head">
      {eyebrow("Monthly plans")}
      <h1 id="hero-heading">A website is never finished.</h1>
      <p class="hero__lede">Software needs updating. Content goes stale.
      Reviews keep arriving. Google keeps changing. Our plans exist so none of
      that is ever your problem.</p>
      <div class="hero__actions">
        <a class="btn btn-primary" href="/pricing/#plans">See plan pricing</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="fade-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("What happens to websites nobody watches")}
      <h2 id="fade-heading">Abandoned websites don\u2019t crash. They fade.</h2>
      <p>We\u2019ve seen a family business whose Google listing was marked
      \u201cpermanently closed\u201d while their trucks were out working every
      day. Nobody was watching, so nobody caught it. They weren\u2019t losing
      their website. They were losing every customer who searched for them.</p>
      <p>That\u2019s the quiet version of what happens without care. Forms
      silently stop sending. Reviews sit unanswered and customers notice. The
      site slips down the rankings. And the owner finds out months later, when
      the phone slows down.</p>
      <p><strong>You could watch all of this yourself. Or it could just be
      handled.</strong></p>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="care-heading">
  <div class="container">
    <article class="card reveal">
      <div class="price-line">
        <h2 id="care-heading" class="mt-0 h-md">Care</h2>
        <p class="price">$79<small>/mo</small> <small>(or $790/yr)</small></p>
      </div>
      <p class="lede"><strong>Your website, handled.</strong> The website we
      built stays our responsibility. Here\u2019s what that covers:</p>
      <div class="grid grid-2 mt-3">
        <div>
          <h3>It stays online.</h3>
          <p class="text-muted">Hosting on our infrastructure, security, and
          technical upkeep. If something breaks, we fix it before you know it
          broke.</p>
        </div>
        <div>
          <h3>Your edits get done.</h3>
          <p class="text-muted">New hours, new photos, price changes, small
          tweaks. Up to 30 minutes a month, usually turned around in a couple
          of days. Bigger jobs get a fair quote first.</p>
        </div>
        <div>
          <h3>Every lead gets saved.</h3>
          <p class="text-muted">Each inquiry lands in your contact list
          automatically. Log in anytime and see everyone who\u2019s ever
          reached out. If you leave, the list exports and goes with you.</p>
        </div>
        <div>
          <h3>Every review gets answered.</h3>
          <p class="text-muted">Positive or negative, every review your
          business receives gets a professional response, drafted with AI, held
          to a human standard, posted within the day. Your customers see a
          business that answers.</p>
        </div>
      </div>
      <p class="mt-3">Care is hands-off on purpose. You\u2019ll barely hear
      from us, and that\u2019s the product: everything keeps working, and you
      don\u2019t have to think about it.</p>
    </article>

    <article class="card card--featured reveal plan-gap">
      <span class="card__flag">Most popular</span>
      <div class="price-line">
        <h2 class="mt-0 h-md">Presence</h2>
        <p class="price">$149<small>/mo</small> <small>(or $1,490/yr)</small></p>
      </div>
      <p class="lede"><strong>Handled, and actively visible.</strong>
      Everything in Care, plus real work every month that keeps your business
      showing up:</p>
      <div class="grid grid-2 mt-3">
        <div>
          <h3>Your Google Business Profile, managed.</h3>
          <p class="text-muted">Optimized, accurate, and posting once a month.
          For local businesses, this listing matters as much as the website.
          Most owners never touch theirs.</p>
        </div>
        <div>
          <h3>A new page every month.</h3>
          <p class="text-muted">One article about your services and your area,
          added to your site. Month by month, your site covers more of what
          your customers actually search for. It compounds quietly.</p>
        </div>
        <div>
          <h3>Reviews, monitored everywhere.</h3>
          <p class="text-muted">We watch your review platforms so nothing slips
          past, and everything gets answered.</p>
        </div>
        <div>
          <h3>A quarterly check-in, in plain language.</h3>
          <p class="text-muted">Every three months: how many people visited,
          how many found you on Google, how often you showed up in search, and
          a short note from us on what it means. No dashboards. No jargon. One
          page.</p>
        </div>
      </div>
    </article>
  </div>
</section>

<section class="section section--sage" aria-labelledby="month-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("A month on Presence")}
      <h2 id="month-heading">That\u2019s every month, without a single task on your list.</h2>
    </div>
    <div class="timeline reveal">
      <div class="timeline__item">
        <span class="timeline__week">Week 1</span>
        <p>Google post published.</p>
      </div>
      <div class="timeline__item">
        <span class="timeline__week">Week 2</span>
        <p>New review answered same day.</p>
      </div>
      <div class="timeline__item">
        <span class="timeline__week">Week 3</span>
        <p>This month\u2019s article goes live on your site.</p>
      </div>
      <div class="timeline__item">
        <span class="timeline__week">Week 4</span>
        <p>Profile checked and updated.</p>
      </div>
      <div class="timeline__item">
        <span class="timeline__week">End of quarter</span>
        <p>Your check-in report arrives.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="annual-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("Annual")}
      <h2 id="annual-heading">Pay for the year, get two months on us.</h2>
      <p>Care: $790. Presence: $1,490. One payment, twelve months covered,
      nothing to think about. Same service, same everything.</p>
    </div>
    <div class="reveal">
      <h3>Founding client rates</h3>
      <p>These prices are for our first group of clients. When the group is
      full, rates go up for new clients only. Whatever you join at, you keep.
      <a class="arrow-link" href="/pricing/">Full pricing &rarr;</a></p>
    </div>
  </div>
</section>

<section class="section--quiet section" aria-labelledby="more-heading">
  <div class="container">
    <div class="section-head reveal mb-0">
      <h3 id="more-heading">Need more than care?</h3>
      <p class="text-muted">For clients ready to grow faster, we also build and
      run: Google and Meta ads, automation systems like missed-call text back
      and review requests, and conversion landing pages. Quoted per project,
      available to existing clients. If you\u2019re ready, ask.</p>
    </div>
  </div>
</section>

{faq_section("Plans FAQ", FAQ_ITEMS, section_class="section section--white")}

{dark_cta("Get back to running your business.",
          "The website, the reviews, the Google listing: handled. Start with "
          "a build, or ask us about caring for a site you already have.")}
"""
