# India Everyday Tools

Free, client-side calculators and converters for everyday life in India. Pure HTML, CSS and JavaScript — **no backend, no database, no build step, no framework.** Open it, edit it, host it anywhere.

## 1. Opening the site in VS Code

1. Unzip the project and open the folder in VS Code.
2. Install the **Live Server** extension (by Ritwick Dey) — search for it in the Extensions panel.
3. Right-click `index.html` → **Open with Live Server**.
4. The site opens in your browser at `http://127.0.0.1:5500` (or similar) and reloads automatically as you edit files.

You don't need Node.js, npm, or any build tools — every page is a plain `.html` file that works by itself.

## 2. Project structure

```
index.html                  Homepage
all-tools.html               All calculators + category filter
age-calculator.html          } 
percentage-calculator.html   }
discount-calculator.html     }
gst-calculator.html          }
emi-calculator.html          }
cgpa-to-percentage.html      }  15 calculator pages
date-difference.html         }  (each is fully self-contained)
unit-converter.html          }
simple-interest.html         }
compound-interest.html       }
average-calculator.html      }
attendance-calculator.html   }
salary-hike-calculator.html  }
tip-calculator.html          }
countdown.html               }
about.html                   Static content page
contact.html                 Static content page
privacy-policy.html          Static content page
terms-of-use.html            Static content page
disclaimer.html              Static content page
robots.txt                   Search engine crawling rules
sitemap.xml                  List of all pages, for SEO
assets/css/style.css         All styling (single shared stylesheet)
assets/js/main.js            Shared logic: tool list, search, mobile menu, formatting helpers
_generator/                  Optional Python scripts used to originally generate the HTML.
                              You do NOT need these to run or edit the site — they're only
                              useful if you want to regenerate every page from a template
                              after a big structural change. Safe to delete.
```

Every calculator page follows the same structure: breadcrumb → title & intro → calculator card →
explanation/formula → how-to → FAQ → related tools. The calculation logic for each tool lives in
a `<script>` tag at the bottom of that page's own `.html` file, so you can find and edit any single
calculator without touching the others.

## 3. Making edits

- **Colours / fonts / spacing:** edit `assets/css/style.css`. The primary accent colour is defined once,
  at the top, as `--red-500: #E34234;` — change it there to re-theme the whole site.
- **Site-wide text (footer, nav):** edit the `header_html()` / `footer_html()` functions in
  `_generator/build.py` and re-run the generator, **or** just find/replace the same block of HTML
  across each page manually (it's identical in every file).
- **A single calculator's text, formula or fields:** open that calculator's `.html` file directly and edit
  the HTML/JS in place — no build step required.
- **Add a brand-new calculator:** easiest is to duplicate the structure of a similar existing page,
  add an entry to the `TOOLS` array in `assets/js/main.js` (so it shows up in search, the homepage
  and All Tools), and add its icon to the `ICONS` object.

## 4. Regenerating pages from the Python templates (optional)

If you'd rather make structural changes once and regenerate every page, edit the relevant file in
`_generator/` and run:

```bash
cd _generator
python3 generate_pages.py   # homepage, all-tools, about/contact/privacy/terms/disclaimer
python3 gen_calc_1.py       # age, percentage, discount, gst
python3 gen_calc_2.py       # emi, cgpa, date-difference, unit-converter
python3 gen_calc_3.py       # simple-interest, compound-interest, average, attendance
python3 gen_calc_4.py       # salary-hike, tip, countdown
```

Each script writes its `.html` files into the project root (one directory up from `_generator/`).
This step needs Python 3 — it's not needed to simply run or host the site.

## 5. Deploying the site

Since this is a static site, you can host it for free on any of these:

- **Netlify / Vercel:** drag-and-drop the whole folder (minus `_generator/`) in their dashboard, or connect a GitHub repo.
- **GitHub Pages:** push the folder to a repo and enable Pages in the repo settings.
- **Any regular web host / shared hosting / cPanel:** upload the files via FTP — there's nothing to install or configure.

Before going live:
- Update the placeholder domain `https://www.india-everyday-tools.onrender.com` in `sitemap.xml`, `robots.txt`
  and inside `_generator/build.py` (`SITE_URL`) to your real domain.
- Update the placeholder email address in `contact.html`.
- Add real "Last updated" dates to `privacy-policy.html`, `terms-of-use.html` and `disclaimer.html`.

## 6. Getting ready for Google AdSense

This site was built with AdSense's content policies in mind:

- Every calculator page has substantial original explanatory content (what the calculator does, the
  formula it uses, how to use it, and an FAQ) — not just a bare input box, which AdSense typically rejects.
- There's no duplicate or keyword-stuffed content between pages.
- `about.html`, `contact.html`, `privacy-policy.html`, `terms-of-use.html` and `disclaimer.html` are
  real, useful pages rather than empty placeholders.
- No fake or misleading buttons, no auto-refreshing pages, no pop-ups.

**Before applying:**
1. Give the site some real traffic history and a bit of time live — Google generally wants to see an
   established, functioning site, not one submitted on day one.
2. Fill in the placeholder details in `about.html`, `contact.html` and the legal pages with your real
   information.
3. Consider adding a couple more original paragraphs of content to any page you feel is thin.
4. When you're approved, add your AdSense script to a shared location — for example, right after the
   opening `<head>` tag in every page, or better, only on pages where ads make sense (avoid placing ads
   inside the calculator card itself). Because every page shares the same header/footer structure, this
   is a small, repeatable edit.

No ad code, ad network script, or ad placeholder is included in this build — that's intentional, so the
site can be reviewed and approved on its own merits first.

## 7. What this site intentionally does NOT include

- No backend server, API, or database of any kind.
- No login, sign-up, or user accounts.
- No payment processing.
- No AI API calls.
- No tracking or analytics scripts (add your own privacy-friendly analytics later if you want usage data).
- No collection or storage of personal information — every calculation happens locally in the visitor's
  browser using plain JavaScript.
