from build import check_list, dark_cta, eyebrow, faq_schema, faq_section

TITLE = "Pricing | Torpie Digital"
DESCRIPTION = ("Straight prices, no surprises. Website builds from $1,000, "
               "monthly care plans from $79. Everything listed, including "
               "what happens if you ever leave.")

FAQ_ITEMS = [
    ("Why is the monthly plan separate from the build?",
     "The build is a project: it starts and finishes. Keeping a website "
     "online, maintained, edited, and answered-for is ongoing work. Separating "
     "them means you only pay for ongoing work if you want it."),
    ("What does the analytics setup include, exactly?",
     "We install Google Analytics and Search Console, connect them, and verify "
     "at launch that both are collecting correctly. You\u2019ll always be able "
     "to see how people find and use your site. Ongoing reporting and strategy "
     "are separate work; Presence includes a quarterly plain-language "
     "check-in, and deeper reporting is available by quote."),
    ("What counts as a \u201creasonable edit\u201d on Care?",
     "Text changes, photo swaps, hours updates, small tweaks: up to about 30 "
     "minutes a month. New pages or redesign-level changes get a fair quote "
     "first. We\u2019ll always tell you before anything costs extra."),
    ("Can I skip the plan and host it myself?",
     "Yes. The site is yours. You\u2019d handle hosting, maintenance, forms, "
     "and reviews on your own or with another provider. Most clients do the "
     "math and hand it to us."),
    ("Will my rate ever go up?",
     "Not while you stay. Rate increases only apply to new clients."),
]

EXTRA_SCHEMA = faq_schema(FAQ_ITEMS)

EVERY_BUILD = [
    "Custom code. Fast, secure, no page builders, no plugins to break",
    "Mobile-first design",
    "Search-ready launch: proper structure, metadata, and sitemap so Google "
    "can find and read your site from day one",
    "Google Analytics and Google Search Console, set up, connected, and "
    "verified working at launch",
    "Professional copywriting from one 15-minute intake form",
    "Working forms: your customer gets a confirmation, you get the lead "
    "instantly",
    "SSL security",
    "Full ownership. Your domain, your site, your content",
]

FOUNDATION = [
    "1 to 3 pages",
    "Custom design on our proven structure",
    "Professional copywriting from one 15-minute form",
    "One revision round",
    "Contact form with instant lead alerts",
    "Launches in about 2 weeks",
]
STOREFRONT = [
    "4 to 6 pages, one for each core service",
    "Deeper custom design",
    "Professional copywriting from one 15-minute form",
    "Two revision rounds",
    "Review display section",
    "Articles section, ready for future use",
    "Launches in about 3 weeks",
]
FLAGSHIP = [
    "7 to 12 pages",
    "Full custom design",
    "Professional copywriting with conversion strategy for every page",
    "Integrations: booking, menus, galleries",
    "Content moved over from your old site",
    "Extended tracking where your setup calls for it",
    "Two weeks of post-launch support",
]
CARE = [
    "Hosting on our infrastructure",
    "Security and technical upkeep",
    "Content edits when you ask (up to 30 minutes a month; bigger jobs quoted "
    "fairly)",
    "Every lead saved to your contact list, with your own login to view it",
    "Every customer review answered, usually within a day",
    "Support from the person who built your site",
]
PRESENCE = [
    "Google Business Profile optimized and managed",
    "One Google post every month",
    "One new page on your site every month, about your services and your area",
    "Review monitoring across platforms",
    "A quarterly check-in report, in plain language, showing how people are "
    "finding and using your site",
]

BODY = f"""
<section class="hero hero--simple" aria-labelledby="hero-heading">
  <div class="container">
    <div class="section-head">
      {eyebrow("Pricing")}
      <h1 id="hero-heading">Straight prices. No surprises.</h1>
      <p class="hero__lede">One price to build your website. One monthly plan
      to keep it working. Everything is listed below, including what happens if
      you ever leave.</p>
    </div>
  </div>
</section>

<section class="section--white section--quiet" aria-label="How pricing works">
  <div class="container grid grid-3 reveal">
    <div>
      <h3>1. You pay once for the build.</h3>
      <p class="text-muted">The website is yours.</p>
    </div>
    <div>
      <h3>2. You join a monthly plan.</h3>
      <p class="text-muted">So it stays hosted, maintained, and working. Most
      clients choose this. It\u2019s optional.</p>
    </div>
    <div>
      <h3>3. That\u2019s it.</h3>
      <p class="text-muted">No contracts, no custom haggling, no hidden fees.</p>
    </div>
  </div>
</section>

<section class="section" id="builds" aria-labelledby="builds-heading">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("Website builds")}
      <h2 id="builds-heading">The build. One-time, and it\u2019s yours.</h2>
    </div>
    <div class="grid grid-3">
      <article class="card reveal">
        <div class="price-line"><h3>Foundation</h3><p class="price">$1,000</p></div>
        <p class="lede">For businesses that need to look professional and get
        calls, fast.</p>
        {check_list(FOUNDATION, extra_class="mt-3")}
      </article>
      <article class="card card--featured reveal">
        <span class="card__flag">Most chosen</span>
        <div class="price-line"><h3>Storefront</h3><p class="price">$1,500</p></div>
        <p class="lede">For established businesses with multiple services to
        showcase.</p>
        {check_list(STOREFRONT, extra_class="mt-3")}
      </article>
      <article class="card reveal">
        <div class="price-line"><h3>Flagship</h3><p class="price">$2,500</p></div>
        <p class="lede">For competitive markets, and owners who want the
        website doing the selling.</p>
        {check_list(FLAGSHIP, extra_class="mt-3")}
      </article>
    </div>
  </div>
</section>

<div class="divider-band" aria-labelledby="every-build-heading">
  <div class="container reveal">
    <h4 id="every-build-heading">Every Torpie Digital website, at every price, includes:</h4>
    {check_list(EVERY_BUILD, inline=True)}
  </div>
</div>

<section class="section section--sage" id="plans" aria-labelledby="plans-heading" data-billing="monthly">
  <div class="container">
    <div class="section-head reveal">
      {eyebrow("Monthly plans")}
      <h2 id="plans-heading">After launch, we take care of it.</h2>
      <div class="toggle mt-3" role="group" aria-label="Billing period">
        <button type="button" data-billing-choice="monthly" aria-pressed="true">Monthly</button>
        <button type="button" data-billing-choice="annual" aria-pressed="false">Annual: two months on us</button>
      </div>
    </div>
    <div class="grid grid-2">
      <article class="card reveal">
        <div class="price-line">
          <h3>Care</h3>
          <p class="price">
            <span class="monthly-price">$79<small>/mo</small></span>
            <span class="annual-price">$790<small>/yr</small></span>
          </p>
        </div>
        <p class="lede">Your website, handled.</p>
        {check_list(CARE, extra_class="mt-3")}
      </article>
      <article class="card card--featured reveal">
        <span class="card__flag">Most popular</span>
        <div class="price-line">
          <h3>Presence</h3>
          <p class="price">
            <span class="monthly-price">$149<small>/mo</small></span>
            <span class="annual-price">$1,490<small>/yr</small></span>
          </p>
        </div>
        <p class="lede">Handled, and actively visible. Everything in Care, plus:</p>
        {check_list(PRESENCE, extra_class="mt-3")}
      </article>
    </div>
    <p class="small text-muted mt-3 reveal">No contracts. Upgrade, downgrade,
    or cancel anytime.</p>
  </div>
</section>

<section class="section" aria-labelledby="founding-heading">
  <div class="container">
    <div class="founding-block reveal">
      <h2 id="founding-heading" class="h-sm">These are founding client rates.</h2>
      <p>Care and Presence are priced for our first group of clients. When that
      group is full, rates go up for new clients only. Whatever rate you join
      at is yours for as long as you stay. No countdown clocks, no pressure.
      Just an honest advantage for joining early.</p>
    </div>
  </div>
</section>

<section class="section section--white" aria-labelledby="fine-print-heading">
  <div class="container">
    <div class="section-head reveal">
      <h2 id="fine-print-heading">The fine print, in plain English</h2>
    </div>
    <div class="grid grid-2">
      <div class="reveal">
        <h3>You own everything.</h3>
        <p class="text-muted">Your domain is registered in your name. Your
        website, content, and contact list are yours. We manage them for you
        while you\u2019re on a plan.</p>
      </div>
      <div class="reveal">
        <h3>If you cancel:</h3>
        <p class="text-muted">You keep your website files, your domain, and a
        full export of your contact list, free. Hosting, form handling, edits,
        and review responses end, because those run on our systems. We\u2019ll
        hand everything over cleanly. No hostages, ever.</p>
      </div>
      <div class="reveal">
        <h3>No custom discounts.</h3>
        <p class="text-muted">Everyone pays the same fair price. The annual
        option, two months on us, is the only deal we offer, and it\u2019s
        available to everyone.</p>
      </div>
      <div class="reveal">
        <h3>Upgrades are easy.</h3>
        <p class="text-muted">Care to Presence anytime, prorated. Need more
        pages later? Quoted at fair rates, built by the same hands.</p>
      </div>
    </div>
  </div>
</section>

{faq_section("Pricing FAQ", FAQ_ITEMS)}

{dark_cta("Know what you need? Get your quote.",
          "Not sure which build fits? That\u2019s what the first call is for.")}
"""
