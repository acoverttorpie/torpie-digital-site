from build import browser_frame, dark_cta, eyebrow

TITLE = "Real Work, Real Results | Torpie Digital"
DESCRIPTION = ("Real businesses, real results, real timeframes. Case studies "
               "in local visibility, search growth, and lead follow-up for "
               "local service businesses.")

BODY = f"""
<section class="hero hero--simple" aria-labelledby="hero-heading">
  <div class="container">
    <div class="section-head">
      {eyebrow("Real work")}
      <h1 id="hero-heading">Proof, with numbers attached.</h1>
      <p class="hero__lede">Real businesses, real results, real timeframes. No
      vague promises, no stock claims. Here\u2019s what this work looks like
      when it\u2019s done right.</p>
    </div>
  </div>
</section>

<section class="section section--white" aria-label="Case studies">
  <div class="container">

    <article class="case" aria-labelledby="case-1-heading">
      <div class="reveal">
        <div class="case__tag">
          <span class="tag">Local visibility &middot; Landscaping</span>
          <span class="case__source">(Delivered by our founder)</span>
        </div>
        <h2 id="case-1-heading">From \u201cpermanently closed\u201d on Google to 3 jobs a month.</h2>
        <p>A family-owned landscaping business had no website, zero online
        reviews, and a Google Business Profile marked permanently closed. The
        internet was sending them nothing, and the family felt it.</p>
        <p>We built their website, fixed and rebuilt their Google presence, and
        put review collection in motion.</p>
        <div class="case__results">
          <h3>The results</h3>
          <p>Full local search visibility restored &middot; 5+ quote requests a
          month from organic traffic alone &middot; an average of 3 jobs a
          month closed from website leads.</p>
        </div>
      </div>
      <div class="case__media">
        {browser_frame("familylandscaping.com",
                       "[SCREENSHOT: landscaping site in browser frame. Replace before launch.]")}
      </div>
    </article>

    <article class="case case--flip" aria-labelledby="case-2-heading">
      <div class="reveal">
        <div class="case__tag">
          <span class="tag">Search growth &middot; Caf&eacute;</span>
          <span class="case__source">(Delivered by our founder)</span>
        </div>
        <h2 id="case-2-heading">A caf&eacute; that Google learned to love.</h2>
        <p>A local Colombian caf&eacute; had a web presence that only showed up
        when people searched their name. Nobody discovering coffee in their
        area was finding them.</p>
        <p>We built their site and grew it with consistent, local content over
        time.</p>
        <div class="case__results">
          <h3>The results, over 16 months</h3>
          <p>3,160 total clicks and 223,000 search impressions &middot;
          quarterly clicks up from 197 to 435 &middot; average search position
          improved from 27.2 to 5.7.</p>
        </div>
        <p class="text-muted">This is what \u201csearch-ready, then grown over
        time\u201d actually looks like. It isn\u2019t fast. It compounds.</p>
      </div>
      <div class="case__media">
        {browser_frame("frytangacafe.com", "",
                       image="/assets/img/frytanga.jpg",
                       alt="Frytanga Cafe website: Colombian cafe hero section with menu navigation and call button")}
      </div>
    </article>

    <article class="case" aria-labelledby="case-3-heading">
      <div class="reveal">
        <div class="case__tag">
          <span class="tag">Lead follow-up &middot; Pest control</span>
          <span class="case__source">(Delivered by our founder)</span>
        </div>
        <h2 id="case-3-heading">Same leads. Three times the customers.</h2>
        <p>A pest control company was generating 15 leads a day but closing
        only around 30 a month. Leads waited 1 to 2 days for a callback and
        went cold.</p>
        <p>We built a system that responded to every lead instantly and kept
        them warm until a rep could call.</p>
        <div class="case__results">
          <h3>The results</h3>
          <p>Closes grew from 30 a month to over 100, a 233% increase &middot;
          roughly $4,100 a month in new recurring revenue &middot; $49,000+ a
          year added.</p>
        </div>
        <p class="text-muted">Speed to lead is the whole game. It\u2019s why
        every website we build acknowledges every inquiry in under a minute.</p>
      </div>
      <div class="case__media">
        {browser_frame("pestcontrolco.com",
                       "[SCREENSHOT OR SYSTEM DIAGRAM. Replace before launch.]")}
      </div>
    </article>

  </div>
</section>


<section class="section section--white" aria-labelledby="builds-heading">
  <div class="container">
    <div class="section-head section-head--center reveal">
      {eyebrow("Recent builds", center=True)}
      <h2 id="builds-heading">Live sites, built by Torpie Digital.</h2>
    </div>
    <div class="grid grid-3 build-gallery">
      <a class="build-tile reveal" href="https://frytangacafe.com" target="_blank" rel="noopener">
        {browser_frame("frytangacafe.com", "",
                       image="/assets/img/frytanga.jpg",
                       alt="Frytanga Cafe website hero with hand-folded empanadas")}
        <h3>Frytanga Caf&eacute;</h3>
        <p class="text-muted small">Colombian caf&eacute; &middot; Ossining, NY</p>
      </a>
      <a class="build-tile reveal" href="https://lucazpainting.com" target="_blank" rel="noopener">
        {browser_frame("lucazpainting.com", "",
                       image="/assets/img/lucaz.jpg",
                       alt="Lucaz Painting and Carpentry website hero with booking buttons and Google reviews")}
        <h3>Lucaz Painting &amp; Carpentry</h3>
        <p class="text-muted small">Painting &amp; carpentry &middot; Westchester County, NY</p>
      </a>
      <a class="build-tile reveal" href="https://deluxeautospa.co" target="_blank" rel="noopener">
        {browser_frame("deluxeautospa.co", "",
                       image="/assets/img/deluxe.jpg",
                       alt="Deluxe Auto Spa website hero for mobile car detailing with booking button")}
        <h3>Deluxe Auto Spa</h3>
        <p class="text-muted small">Mobile detailing &middot; Croton, NY</p>
      </a>
    </div>
  </div>
</section>

<section class="section--quiet section" aria-label="A note on these results">
  <div class="container">
    <p class="text-muted small reveal">These projects
    were delivered by our founder before Torpie Digital took its current form.
    Same hands, same standard. Torpie Digital client results will be added as
    they\u2019re earned, with the same honesty: real numbers, real
    timeframes.</p>
  </div>
</section>

{dark_cta("Want to be the next one on this page?", "")}
"""
