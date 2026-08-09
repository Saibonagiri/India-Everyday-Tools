/* ============================================================
   India Everyday Tools — shared site behaviour
   Tool registry, search, mobile menu, formatting helpers.
   Everything here runs 100% client-side. No network calls.
   ============================================================ */

/* ---------- Tool registry (used by search, homepage, all-tools) ---------- */
const TOOLS = [
  { id: "age", name: "Age Calculator", url: "age-calculator.html", desc: "Find your exact age in years, months and days.", cat: "Date & Time", keywords: "age birthday dob date of birth years old" },
  { id: "percentage", name: "Percentage Calculator", url: "percentage-calculator.html", desc: "Work out percentages, increases and decreases.", cat: "Math", keywords: "percentage percent of increase decrease" },
  { id: "discount", name: "Discount Calculator", url: "discount-calculator.html", desc: "Find the final price and savings on a sale.", cat: "Everyday Life", keywords: "discount sale off price save" },
  { id: "gst", name: "GST Calculator", url: "gst-calculator.html", desc: "Add or remove GST from any amount.", cat: "Money & Finance", keywords: "gst tax goods services add remove" },
  { id: "emi", name: "EMI Calculator", url: "emi-calculator.html", desc: "Calculate your monthly loan EMI instantly.", cat: "Money & Finance", keywords: "emi loan interest monthly installment home car" },
  { id: "cgpa", name: "CGPA to Percentage", url: "cgpa-to-percentage.html", desc: "Convert your CGPA into an estimated percentage.", cat: "Education", keywords: "cgpa gpa percentage college university marks" },
  { id: "datediff", name: "Date Difference Calculator", url: "date-difference.html", desc: "Find the days, months and years between two dates.", cat: "Date & Time", keywords: "date difference between days months years" },
  { id: "unit", name: "Unit Converter", url: "unit-converter.html", desc: "Convert length, weight, temperature and more.", cat: "Unit Conversion", keywords: "unit convert length weight mass temperature area volume speed data" },
  { id: "si", name: "Simple Interest Calculator", url: "simple-interest.html", desc: "Calculate simple interest on any principal.", cat: "Money & Finance", keywords: "simple interest principal rate time" },
  { id: "ci", name: "Compound Interest Calculator", url: "compound-interest.html", desc: "See how your investment grows with compounding.", cat: "Money & Finance", keywords: "compound interest investment growth returns" },
  { id: "average", name: "Average Calculator", url: "average-calculator.html", desc: "Find the average, sum and count of numbers.", cat: "Math", keywords: "average mean sum numbers" },
  { id: "attendance", name: "Attendance Calculator", url: "attendance-calculator.html", desc: "Check your attendance percentage and safe leaves.", cat: "Education", keywords: "attendance percentage classes college school bunk" },
  { id: "salary", name: "Salary Hike Calculator", url: "salary-hike-calculator.html", desc: "Calculate your new salary after a hike.", cat: "Money & Finance", keywords: "salary hike increment appraisal raise" },
  { id: "tip", name: "Tip Calculator", url: "tip-calculator.html", desc: "Split the bill and calculate tips for a group.", cat: "Everyday Life", keywords: "tip bill split restaurant per person" },
  { id: "countdown", name: "Date Countdown", url: "countdown.html", desc: "Count down the days to any future date.", cat: "Date & Time", keywords: "countdown days remaining future event" },
];

const CATEGORIES = ["Money & Finance", "Education", "Date & Time", "Math", "Unit Conversion", "Everyday Life"];

/* ---------- Icon set (inline SVG strings, stroke-based) ---------- */
const ICONS = {
  age: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="M12 14v3l2 1"/></svg>',
  percentage: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>',
  discount: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41 12 22l-9-9V3h10z"/><circle cx="7.5" cy="7.5" r="1.5"/></svg>',
  gst: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z"/><path d="M9 9h6M9 13h6M9 17h3"/></svg>',
  emi: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="13" rx="2"/><path d="M2 10h20M6 15h4"/></svg>',
  cgpa: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/></svg>',
  datediff: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m9 16 2 2 4-4"/></svg>',
  unit: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3 4 7l4 4"/><path d="M4 7h11a5 5 0 0 1 5 5"/><path d="m16 21 4-4-4-4"/><path d="M20 17H9a5 5 0 0 1-5-5"/></svg>',
  si: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 14l4-4 3 3 5-6"/></svg>',
  ci: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 16c1-4 2-6 3.5-6s1.5 3 3 3 2-5 3.5-5 1.5 4 3 4"/></svg>',
  average: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h18"/><rect x="5" y="10" width="3" height="10"/><rect x="10.5" y="6" width="3" height="14"/><rect x="16" y="13" width="3" height="7"/></svg>',
  attendance: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
  salary: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 6l-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/></svg>',
  tip: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
  countdown: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6M12 2v3"/></svg>',
  search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>',
  arrow: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  money: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/></svg>',
  edu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/></svg>',
  date: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
  math: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="5" x2="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/></svg>',
  convert: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3 4 7l4 4"/><path d="M4 7h11a5 5 0 0 1 5 5"/><path d="m16 21 4-4-4-4"/><path d="M20 17H9a5 5 0 0 1-5-5"/></svg>',
  life: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.6a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78L12 21.23l8.84-8.84a5.5 5.5 0 0 0 0-7.78Z"/></svg>',
};

const CATEGORY_ICON = { "Money & Finance": "money", "Education": "edu", "Date & Time": "date", "Math": "math", "Unit Conversion": "convert", "Everyday Life": "life" };

function toolIcon(id) { return ICONS[id] || ICONS.math; }

/* ---------- Root-relative path helper (site is a flat folder of .html pages) ---------- */
function toolCardHTML(tool) {
  return `<a class="tool-card" href="${tool.url}">
    <div class="tool-icon">${toolIcon(tool.id)}</div>
    <h3>${tool.name}</h3>
    <p class="desc">${tool.desc}</p>
    <span class="tool-open">Open Calculator ${ICONS.arrow}</span>
  </a>`;
}

/* ---------- Mobile menu ---------- */
function initMobileMenu() {
  const toggle = document.querySelector(".menu-toggle");
  const panel = document.querySelector(".mobile-panel");
  if (!toggle || !panel) return;
  toggle.addEventListener("click", () => {
    const open = panel.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });
}

/* ---------- Search (client-side, matches name/keywords) ---------- */
function searchTools(query) {
  const q = query.trim().toLowerCase();
  if (!q) return [];
  return TOOLS
    .map((t) => {
      const hay = (t.name + " " + t.keywords + " " + t.desc).toLowerCase();
      let score = 0;
      if (t.name.toLowerCase().startsWith(q)) score += 10;
      if (t.name.toLowerCase().includes(q)) score += 5;
      if (t.keywords.includes(q)) score += 4;
      if (hay.includes(q)) score += 1;
      return { tool: t, score };
    })
    .filter((r) => r.score > 0)
    .sort((a, b) => b.score - a.score)
    .map((r) => r.tool);
}

function renderSearchResults(container, results) {
  if (!results.length) {
    container.innerHTML = `<div class="search-empty">No calculators found. Try "age", "gst" or "loan".</div>`;
    container.classList.add("open");
    return;
  }
  container.innerHTML = results
    .slice(0, 8)
    .map(
      (t) => `<a href="${t.url}">
        <span class="sr-icon">${toolIcon(t.id)}</span>
        <span>
          <span class="sr-title">${t.name}</span><br>
          <span class="sr-desc">${t.desc}</span>
        </span>
      </a>`
    )
    .join("");
  container.classList.add("open");
}

function initSearchBox(inputSel, resultsSel, formSel) {
  const input = document.querySelector(inputSel);
  const results = document.querySelector(resultsSel);
  if (!input || !results) return;

  input.addEventListener("input", () => {
    const r = searchTools(input.value);
    if (input.value.trim()) renderSearchResults(results, r);
    else results.classList.remove("open");
  });

  input.addEventListener("focus", () => {
    if (input.value.trim()) renderSearchResults(results, searchTools(input.value));
  });

  document.addEventListener("click", (e) => {
    if (!results.contains(e.target) && e.target !== input) results.classList.remove("open");
  });

  const form = formSel ? document.querySelector(formSel) : null;
  if (form) {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const r = searchTools(input.value);
      if (r.length) window.location.href = r[0].url;
    });
  }
}

/* ---------- Formatting helpers used by calculator pages ---------- */
function formatINR(amount, opts) {
  opts = opts || {};
  if (amount === null || amount === undefined || isNaN(amount)) return "₹0";
  const decimals = opts.decimals === undefined ? 2 : opts.decimals;
  const neg = amount < 0;
  amount = Math.abs(amount);
  const fixed = amount.toFixed(decimals);
  let [intPart, decPart] = fixed.split(".");
  let lastThree = intPart.slice(-3);
  let other = intPart.slice(0, -3);
  if (other) lastThree = "," + lastThree;
  const formattedInt = other.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + lastThree;
  const out = "₹" + formattedInt + (decimals > 0 ? "." + decPart : "");
  return neg ? "-" + out : out;
}

function formatNumber(num, decimals) {
  if (num === null || num === undefined || isNaN(num)) return "0";
  decimals = decimals === undefined ? 2 : decimals;
  return Number(num).toLocaleString("en-IN", { maximumFractionDigits: decimals, minimumFractionDigits: 0 });
}

function showError(inputEl, errorEl, message) {
  if (inputEl) inputEl.classList.add("input-error");
  if (errorEl) {
    errorEl.textContent = message;
    errorEl.classList.add("show");
  }
}
function clearError(inputEl, errorEl) {
  if (inputEl) inputEl.classList.remove("input-error");
  if (errorEl) {
    errorEl.textContent = "";
    errorEl.classList.remove("show");
  }
}

function parseNum(val) {
  if (val === "" || val === null || val === undefined) return NaN;
  const n = parseFloat(val);
  return isNaN(n) ? NaN : n;
}

/* ---------- Related tools renderer ---------- */
function renderRelated(containerSel, ids) {
  const el = document.querySelector(containerSel);
  if (!el) return;
  el.innerHTML = ids
    .map((id) => {
      const t = TOOLS.find((x) => x.id === id);
      if (!t) return "";
      return `<a href="${t.url}"><span class="ri">${toolIcon(t.id)}</span> ${t.name}</a>`;
    })
    .join("");
}

/* ---------- Init on load ---------- */
document.addEventListener("DOMContentLoaded", () => {
  initMobileMenu();
  initSearchBox("#headerSearchInput", "#headerSearchResults", "#headerSearchForm");
  initSearchBox("#heroSearchInput", "#heroSearchResults", "#heroSearchForm");

  // Highlight nav active link
  const path = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".main-nav a, .mobile-panel nav a").forEach((a) => {
    const href = a.getAttribute("href");
    if (href === path || (path === "" && href === "index.html")) a.classList.add("active");
  });
});
