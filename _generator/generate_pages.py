#!/usr/bin/env python3
"""Generates all top-level (non-calculator) pages."""
from build import page, breadcrumb, write

# ---------------------------------------------------------------- HOMEPAGE
def build_homepage():
    popular_ids = ["age", "percentage", "discount", "gst", "emi", "cgpa", "datediff", "unit"]
    body = f"""  <section class="hero">
    <div class="container">
      <h1>Everyday calculations made <span class="accent">simple.</span></h1>
      <p class="subhead">Free, fast and easy-to-use calculators and converters for everyday life.</p>
      <form class="hero-search" id="heroSearchForm" role="search">
        <div class="search-wrap">
          <svg class="icon-search" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
          <input type="text" id="heroSearchInput" placeholder="Search for a calculator..." aria-label="Search for a calculator" autocomplete="off">
          <button type="submit" class="search-btn">Search</button>
        </div>
        <div class="search-results" id="heroSearchResults"></div>
      </form>
      <div class="hero-tags">
        <a href="gst-calculator.html">GST Calculator</a>
        <a href="emi-calculator.html">EMI Calculator</a>
        <a href="age-calculator.html">Age Calculator</a>
        <a href="unit-converter.html">Unit Converter</a>
        <a href="percentage-calculator.html">Percentage Calculator</a>
      </div>
    </div>
  </section>

  <section class="section" id="popular">
    <div class="container">
      <div class="section-head">
        <div>
          <h2>Popular tools</h2>
          <p>The calculators people use the most.</p>
        </div>
        <a class="section-link" href="all-tools.html">View all calculators →</a>
      </div>
      <div class="tool-grid" id="popularGrid"></div>
    </div>
  </section>

  <section class="section alt" id="categories">
    <div class="container">
      <div class="section-head">
        <div>
          <h2>Browse by category</h2>
          <p>Find the right tool faster.</p>
        </div>
      </div>
      <div class="category-grid" id="categoryGrid"></div>
    </div>
  </section>

  <section class="section text-center">
    <div class="container" style="max-width:700px;">
      <h2>Built for everyday use in India</h2>
      <p>India Everyday Tools is a free collection of calculators and converters for money, education, dates and everyday life. Every calculation happens instantly in your browser — nothing is uploaded, stored or shared. No sign-up, no app to install, just open a tool and get your answer.</p>
    </div>
  </section>"""
    script = """<script>
  document.getElementById('popularGrid').innerHTML = %s.map(id => toolCardHTML(TOOLS.find(t => t.id === id))).join('');
  document.getElementById('categoryGrid').innerHTML = CATEGORIES.map(cat => {
    const items = TOOLS.filter(t => t.cat === cat);
    return `<div class="category-card">
      <div class="cat-head"><span class="cat-icon">${ICONS[CATEGORY_ICON[cat]]}</span><h3>${cat}</h3></div>
      <ul>${items.map(t => `<li><a href="${t.url}">${t.name}</a></li>`).join('')}</ul>
    </div>`;
  }).join('');
</script>""" % popular_ids
    html = page(
        title="India Everyday Tools — Free Calculators & Converters for India",
        description="Free, fast calculators and converters for everyday life in India: age, GST, EMI, percentage, discount, CGPA, unit conversion and more. No sign-up required.",
        slug="index.html",
        body=body,
        extra_scripts=script,
    )
    write("index.html", html)


# ---------------------------------------------------------------- ALL TOOLS
def build_all_tools():
    body = """  <section class="calc-page-head">
    <div class="container">
      <h1>All Calculators</h1>
      <p class="intro">Every free tool on India Everyday Tools, grouped by category. All calculations run instantly in your browser.</p>
    </div>
  </section>
  <section class="section" id="categories">
    <div class="container">
      <div class="filter-bar" id="filterBar"></div>
      <div class="tool-grid" id="allToolsGrid"></div>
    </div>
  </section>"""
    script = """<script>
  const filterBar = document.getElementById('filterBar');
  const grid = document.getElementById('allToolsGrid');
  let active = 'All';

  function render() {
    const list = active === 'All' ? TOOLS : TOOLS.filter(t => t.cat === active);
    grid.innerHTML = list.map(toolCardHTML).join('');
  }
  function renderFilters() {
    const cats = ['All', ...CATEGORIES];
    filterBar.innerHTML = cats.map(c => `<button data-cat="${c}" class="${c===active?'selected':''}">${c}</button>`).join('');
    filterBar.querySelectorAll('button').forEach(btn => {
      btn.addEventListener('click', () => {
        active = btn.dataset.cat;
        renderFilters();
        render();
      });
    });
  }
  renderFilters();
  render();

  // Deep-link support: #categories just scrolls here (already in view)
</script>"""
    html = page(
        title="All Calculators — India Everyday Tools",
        description="Browse every free calculator and converter on India Everyday Tools by category: money & finance, education, date & time, math, unit conversion and everyday life.",
        slug="all-tools.html",
        body=body,
        extra_scripts=script,
    )
    write("all-tools.html", html)


# ---------------------------------------------------------------- STATIC PAGES
def build_about():
    body = """<section class="content-page">
    <h1>About India Everyday Tools</h1>
    <p class="updated">A small, focused project built for everyday calculations.</p>
    <p>India Everyday Tools is a free collection of calculators and converters built for the small, everyday calculations people in India actually need — working out a GST amount, checking an EMI before taking a loan, converting a CGPA for a job application, or splitting a restaurant bill.</p>
    <p>The idea behind this website is simple: calculations like these shouldn't require downloading an app, creating an account, or digging through a cluttered page full of unrelated content. Every tool here is designed to load quickly, explain itself clearly, and give you a straight answer.</p>
    <h2>How the calculators work</h2>
    <p>Every calculator on this site runs entirely in your web browser using standard, well-known formulas (such as the reducing-balance EMI formula, or the standard simple and compound interest formulas). Nothing you type is sent to a server, stored in a database, or shared with anyone — the maths happens on your device, instantly.</p>
    <h2>Why we built this</h2>
    <p>Many existing calculator sites are cluttered, slow, or filled with confusing pop-ups. We wanted something faster and more straightforward: open a calculator, enter your numbers, get your answer, and move on with your day.</p>
    <h2>Accuracy and limitations</h2>
    <p>We take care to use correct, standard formulas and test each calculator with real examples. That said, rules like GST rates, CGPA conversion formulas, and tax slabs can change or vary by institution or authority. Please treat results as a helpful estimate and confirm anything important with an official source. See our <a class="inline-link" href="disclaimer.html">Disclaimer</a> for details.</p>
    <h2>Get in touch</h2>
    <p>Have feedback, found an error, or want a new calculator added? Visit our <a class="inline-link" href="contact.html">Contact page</a> — we'd genuinely like to hear from you.</p>
  </section>"""
    write("about.html", page(title="About Us — India Everyday Tools", description="Learn about India Everyday Tools, a free collection of everyday calculators and converters built for accuracy, speed and privacy.", slug="about.html", body=body))


def build_contact():
    body = """<section class="content-page">
    <h1>Contact Us</h1>
    <p class="updated">We'd like to hear from you.</p>
    <p>India Everyday Tools is an independently run project. If you've spotted an incorrect calculation, have a suggestion for a new calculator, or just want to share feedback, please reach out.</p>
    <h2>Email</h2>
    <p>You can reach us at <strong>hello@indiaeverydaytools.com</strong> (replace with your real support email address before publishing).</p>
    <h2>What to include</h2>
    <ul>
      <li>The name of the calculator you're writing about, if applicable.</li>
      <li>The values you entered and the result you received, if you're reporting a calculation issue.</li>
      <li>Any calculator you'd like to see added to the site.</li>
    </ul>
    <p>We read every message, though as a small project it may take us a little time to respond. This website does not collect your email address or any personal details automatically — we only see what you choose to send us directly.</p>
  </section>"""
    write("contact.html", page(title="Contact Us — India Everyday Tools", description="Get in touch with India Everyday Tools for feedback, corrections, or calculator suggestions.", slug="contact.html", body=body))


def build_privacy():
    body = """<section class="content-page">
    <h1>Privacy Policy</h1>
    <p class="updated">Last updated: [add date before publishing]</p>
    <p>This Privacy Policy explains how India Everyday Tools ("we", "this website") handles information when you use our calculators and converters.</p>
    <h2>Calculations happen in your browser</h2>
    <p>Every calculator on this website performs its calculations locally, using JavaScript that runs on your own device. The numbers and dates you enter into a calculator — such as a salary, loan amount, date of birth or CGPA — are not transmitted to our servers, stored in a database, or seen by us. When you close or refresh the page, that data is gone.</p>
    <h2>Information we do not collect</h2>
    <p>We do not ask for or knowingly collect your name, email address, phone number, financial account details, or any other personal profile information through the calculators on this site. There is no account creation, login, or sign-up required to use any tool.</p>
    <h2>Cookies and analytics</h2>
    <p>This website does not currently use tracking cookies. If we introduce privacy-friendly analytics or advertising in the future (for example, to keep this website free to use), this policy will be updated in advance to describe what is collected, such as general usage statistics or advertising identifiers, and how you can control it. Third-party services we may use in the future, including advertising providers, may set their own cookies and collect data according to their own privacy policies.</p>
    <h2>Third-party links</h2>
    <p>Some pages may link to external resources for further reading. We are not responsible for the privacy practices or content of external websites.</p>
    <h2>Children's privacy</h2>
    <p>This website is a general-purpose utility tool and is not directed at children. We do not knowingly collect personal information from children.</p>
    <h2>Changes to this policy</h2>
    <p>We may update this Privacy Policy from time to time, for example if we introduce new features such as advertising. Any changes will be posted on this page with an updated date.</p>
    <h2>A note on accuracy of this statement</h2>
    <p>We aim to describe our practices accurately and avoid absolute claims. No website can guarantee complete security or privacy under all circumstances, and this policy should not be read as such a guarantee.</p>
    <h2>Contact</h2>
    <p>Questions about this policy can be sent through our <a class="inline-link" href="contact.html">Contact page</a>.</p>
  </section>"""
    write("privacy-policy.html", page(title="Privacy Policy — India Everyday Tools", description="Read how India Everyday Tools handles your information. All calculations run locally in your browser and no personal data is collected.", slug="privacy-policy.html", body=body))


def build_terms():
    body = """<section class="content-page">
    <h1>Terms of Use</h1>
    <p class="updated">Last updated: [add date before publishing]</p>
    <p>By using India Everyday Tools, you agree to the following terms. Please read them before using the calculators on this website.</p>
    <h2>Use of the website</h2>
    <p>India Everyday Tools provides free calculators and converters for general informational purposes. You may use these tools for personal or professional reference, free of charge, without creating an account.</p>
    <h2>No professional advice</h2>
    <p>The results provided by any calculator on this website — including but not limited to EMI, GST, interest, CGPA, salary and attendance calculators — are estimates based on standard, publicly known formulas. They do not constitute financial, tax, legal, educational or other professional advice, and should not be relied upon as the sole basis for any decision. See our <a class="inline-link" href="disclaimer.html">Disclaimer</a> for more detail.</p>
    <h2>Accuracy of results</h2>
    <p>We test our calculators carefully and aim for correct results based on the formulas described on each page. However, we do not guarantee that results will be error-free, complete, or applicable to your specific situation, particularly where official rates, rules or institutional formulas change over time.</p>
    <h2>Acceptable use</h2>
    <p>You agree not to misuse this website, including attempting to disrupt its normal operation, copy its content for republishing without permission, or use it in any way that violates applicable law.</p>
    <h2>Intellectual property</h2>
    <p>The design, layout, original text and branding of India Everyday Tools belong to its operator. The underlying mathematical formulas used in the calculators are standard, publicly available methods and are not owned by us.</p>
    <h2>Limitation of liability</h2>
    <p>India Everyday Tools is provided "as is" without warranties of any kind. To the fullest extent permitted by law, we are not liable for any loss or damage arising from your use of, or reliance on, this website or its calculators.</p>
    <h2>Changes to these terms</h2>
    <p>We may update these Terms of Use from time to time. Continued use of the website after changes are posted means you accept the updated terms.</p>
    <h2>Contact</h2>
    <p>Questions about these terms can be sent through our <a class="inline-link" href="contact.html">Contact page</a>.</p>
  </section>"""
    write("terms-of-use.html", page(title="Terms of Use — India Everyday Tools", description="Terms of Use for India Everyday Tools, a free calculator and converter website.", slug="terms-of-use.html", body=body))


def build_disclaimer():
    body = """<section class="content-page">
    <h1>Disclaimer</h1>
    <p class="updated">Last updated: [add date before publishing]</p>
    <p>The calculators and converters on India Everyday Tools are provided for informational and general-purpose use. Results may vary depending on the applicable rules, formulas, institutions, or assumptions used at the time of calculation.</p>
    <p>For financial, tax, legal, educational, or other important decisions, please verify the result with the relevant official source or a qualified professional before acting on it.</p>
    <h2>Financial calculators</h2>
    <p>Tools such as the EMI, GST, Simple Interest, Compound Interest and Salary Hike calculators use standard formulas widely used across the finance industry. They do not account for bank-specific processing fees, prepayment charges, changing interest rates, or GST rate changes over time. Always confirm final figures with your bank, lender, or tax advisor.</p>
    <h2>Education calculators</h2>
    <p>The CGPA to Percentage and Attendance calculators use commonly referenced formulas. CGPA-to-percentage conversion in particular varies by university or institution — always check your institution's official formula before submitting a converted percentage anywhere official.</p>
    <h2>No professional relationship</h2>
    <p>Use of this website does not create any advisory, financial, legal or professional relationship between you and India Everyday Tools.</p>
    <h2>Contact</h2>
    <p>If you believe a calculator is producing an incorrect result, please let us know via our <a class="inline-link" href="contact.html">Contact page</a> so we can review it.</p>
  </section>"""
    write("disclaimer.html", page(title="Disclaimer — India Everyday Tools", description="Important disclaimer about the accuracy and use of calculators on India Everyday Tools.", slug="disclaimer.html", body=body))


if __name__ == "__main__":
    build_homepage()
    build_all_tools()
    build_about()
    build_contact()
    build_privacy()
    build_terms()
    build_disclaimer()
    print("Static + homepage pages generated.")
