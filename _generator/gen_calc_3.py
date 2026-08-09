#!/usr/bin/env python3
from build import calc_page, write

# ============================================================ SIMPLE INTEREST
def build_simple_interest():
    calc_card = """      <div class="field-group">
        <label for="principal">Principal amount</label>
        <div class="input-prefix-wrap"><span class="prefix">₹</span><input type="number" id="principal" placeholder="e.g. 50000"></div>
        <div class="error-text" id="principalError"></div>
      </div>
      <div class="field-row">
        <div class="field-group">
          <label for="rate">Interest rate (% per year)</label>
          <input type="number" id="rate" placeholder="e.g. 8" step="0.01">
          <div class="error-text" id="rateError"></div>
        </div>
        <div class="field-group">
          <label for="time">Time period (years)</label>
          <input type="number" id="time" placeholder="e.g. 3" step="0.1">
          <div class="error-text" id="timeError"></div>
        </div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Total Amount</div>
          <div class="result-value" id="rTotal">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label">Principal</div><div class="r-value" id="rPrincipal">-</div></div>
          <div class="result-item"><div class="r-label">Interest Earned</div><div class="r-value" id="rInterest">-</div></div>
        </div>
      </div>"""

    info = """    <h2>What is simple interest?</h2>
    <p>Simple interest is calculated only on the original principal amount for the entire time period, unlike compound interest, where interest is also earned on previously accumulated interest. It's a straightforward way to estimate returns on fixed-term deposits or the cost of certain short-term loans.</p>
    <div class="formula-box">Simple Interest (SI) = (P × R × T) ÷ 100
Total Amount = P + SI

P = Principal, R = Annual rate (%), T = Time in years</div>
    <h2>How to use this calculator</h2>
    <ol>
      <li>Enter the principal amount.</li>
      <li>Enter the annual interest rate.</li>
      <li>Enter the time period in years (you can use decimals, e.g. 2.5 for two and a half years).</li>
      <li>Press <strong>Calculate</strong> to see the interest earned and total amount.</li>
    </ol>"""

    faq = [
        ("How is simple interest different from compound interest?", "Simple interest is calculated only on the original principal for the whole period, so it grows in a straight line. Compound interest adds earned interest back into the principal periodically, so it grows faster over time. See our Compound Interest Calculator to compare."),
        ("Can I use months instead of years for the time period?", "Enter the time in years — for months, divide by 12 first (for example, 6 months = 0.5 years)."),
        ("Is this useful for loans as well as deposits?", "Yes, simple interest is used for some fixed deposits, short-term loans and certain lending products, though most bank loans in India use the reducing-balance (EMI) method instead — see our EMI Calculator for that case."),
    ]

    script = """<script>
  const principal = document.getElementById('principal'), pErr = document.getElementById('principalError');
  const rate = document.getElementById('rate'), rErr = document.getElementById('rateError');
  const time = document.getElementById('time'), tErr = document.getElementById('timeError');
  const result = document.getElementById('result');

  function calculate() {
    [principal, rate, time].forEach(i => i.classList.remove('input-error'));
    [pErr, rErr, tErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    let ok = true;
    const P = parseNum(principal.value), R = parseNum(rate.value), T = parseNum(time.value);
    if (isNaN(P) || P <= 0) { showError(principal, pErr, 'Enter a principal amount greater than 0.'); ok = false; }
    if (isNaN(R) || R < 0) { showError(rate, rErr, 'Enter a valid interest rate.'); ok = false; }
    if (isNaN(T) || T <= 0) { showError(time, tErr, 'Enter a time period greater than 0.'); ok = false; }
    if (!ok) { result.classList.remove('show'); return; }

    const si = (P * R * T) / 100;
    const total = P + si;
    document.getElementById('rTotal').textContent = formatINR(total);
    document.getElementById('rPrincipal').textContent = formatINR(P);
    document.getElementById('rInterest').textContent = formatINR(si);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    principal.value=''; rate.value=''; time.value='';
    [principal, rate, time].forEach(i => i.classList.remove('input-error'));
    [pErr, rErr, tErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="simple-interest.html",
        title="Simple Interest Calculator",
        meta_desc="Calculate simple interest and total amount on any principal, rate and time period using the standard SI formula.",
        h1="Simple Interest Calculator",
        intro="Calculate simple interest earned on a principal amount over a fixed time period.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["ci", "emi", "gst"],
        extra_script=script,
    )
    write("simple-interest.html", html)


# ============================================================ COMPOUND INTEREST
def build_compound_interest():
    calc_card = """      <div class="field-group">
        <label for="principal">Principal amount</label>
        <div class="input-prefix-wrap"><span class="prefix">₹</span><input type="number" id="principal" placeholder="e.g. 100000"></div>
        <div class="error-text" id="principalError"></div>
      </div>
      <div class="field-row">
        <div class="field-group">
          <label for="rate">Interest rate (% per year)</label>
          <input type="number" id="rate" placeholder="e.g. 7.5" step="0.01">
          <div class="error-text" id="rateError"></div>
        </div>
        <div class="field-group">
          <label for="time">Time period (years)</label>
          <input type="number" id="time" placeholder="e.g. 5" step="0.1">
          <div class="error-text" id="timeError"></div>
        </div>
      </div>
      <div class="field-group">
        <label>Compounding frequency</label>
        <div class="chip-group" id="freqChips">
          <button type="button" class="chip" data-n="1">Annually</button>
          <button type="button" class="chip" data-n="2">Semi-annually</button>
          <button type="button" class="chip" data-n="4">Quarterly</button>
          <button type="button" class="chip selected" data-n="12">Monthly</button>
        </div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Final Amount</div>
          <div class="result-value" id="rTotal">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label">Principal</div><div class="r-value" id="rPrincipal">-</div></div>
          <div class="result-item"><div class="r-label">Interest Earned</div><div class="r-value" id="rInterest">-</div></div>
        </div>
      </div>"""

    info = """    <h2>What is compound interest?</h2>
    <p>Compound interest is calculated on the principal plus any interest already earned, so returns grow faster the more frequently interest is compounded. This is how most fixed deposits, recurring deposits and long-term investments actually grow.</p>
    <div class="formula-box">A = P × (1 + r/n)^(n × t)
Compound Interest = A − P

P = Principal, r = Annual rate (as a decimal), n = Compounding frequency per year, t = Time in years</div>
    <h2>How to use this calculator</h2>
    <ol>
      <li>Enter your principal (starting) amount.</li>
      <li>Enter the annual interest rate.</li>
      <li>Enter the time period in years.</li>
      <li>Choose how often interest is compounded — annually, semi-annually, quarterly or monthly.</li>
      <li>Press <strong>Calculate</strong> to see the final amount and total interest earned.</li>
    </ol>"""

    faq = [
        ("Why does compounding frequency matter?", "The more often interest is added back to the principal, the sooner it starts earning interest itself. Monthly compounding will produce a slightly higher return than annual compounding at the same stated rate."),
        ("What's a realistic compounding frequency for Indian bank deposits?", "This varies by bank and product — many fixed deposits compound quarterly, while some recurring deposits and savings accounts compound monthly or annually. Check your specific product's terms."),
        ("How is this different from simple interest?", "Simple interest is calculated only on the original principal throughout, while compound interest is calculated on a growing balance that includes previously earned interest — see our Simple Interest Calculator for a direct comparison."),
    ]

    script = """<script>
  const principal = document.getElementById('principal'), pErr = document.getElementById('principalError');
  const rate = document.getElementById('rate'), rErr = document.getElementById('rateError');
  const time = document.getElementById('time'), tErr = document.getElementById('timeError');
  const result = document.getElementById('result');
  let n = 12;

  document.getElementById('freqChips').addEventListener('click', (e) => {
    const chip = e.target.closest('.chip'); if (!chip) return;
    document.querySelectorAll('#freqChips .chip').forEach(c => c.classList.remove('selected'));
    chip.classList.add('selected');
    n = parseInt(chip.dataset.n, 10);
  });

  function calculate() {
    [principal, rate, time].forEach(i => i.classList.remove('input-error'));
    [pErr, rErr, tErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    let ok = true;
    const P = parseNum(principal.value), R = parseNum(rate.value), T = parseNum(time.value);
    if (isNaN(P) || P <= 0) { showError(principal, pErr, 'Enter a principal amount greater than 0.'); ok = false; }
    if (isNaN(R) || R < 0) { showError(rate, rErr, 'Enter a valid interest rate.'); ok = false; }
    if (isNaN(T) || T <= 0) { showError(time, tErr, 'Enter a time period greater than 0.'); ok = false; }
    if (!ok) { result.classList.remove('show'); return; }

    const r = R / 100;
    const A = P * Math.pow(1 + r / n, n * T);
    const ci = A - P;
    document.getElementById('rTotal').textContent = formatINR(A);
    document.getElementById('rPrincipal').textContent = formatINR(P);
    document.getElementById('rInterest').textContent = formatINR(ci);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    principal.value=''; rate.value=''; time.value='';
    document.querySelectorAll('#freqChips .chip').forEach(c => c.classList.remove('selected'));
    document.querySelector('#freqChips .chip[data-n="12"]').classList.add('selected');
    n = 12;
    [principal, rate, time].forEach(i => i.classList.remove('input-error'));
    [pErr, rErr, tErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="compound-interest.html",
        title="Compound Interest Calculator",
        meta_desc="Calculate compound interest and final amount for any principal, rate, time and compounding frequency.",
        h1="Compound Interest Calculator",
        intro="See how your money grows over time with compound interest, at any compounding frequency.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["si", "emi", "salary"],
        extra_script=script,
    )
    write("compound-interest.html", html)


# ============================================================ AVERAGE CALCULATOR
def build_average():
    calc_card = """      <div class="field-group">
        <label for="numbers">Enter numbers</label>
        <textarea id="numbers" rows="5" placeholder="Enter numbers separated by commas, spaces or new lines&#10;e.g. 45, 67, 89, 23, 90"></textarea>
        <div class="error-text" id="numError"></div>
        <div class="hint">Separate numbers with commas, spaces, or one per line.</div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate Average</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Average</div>
          <div class="result-value" id="rAvg">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label">Sum</div><div class="r-value" id="rSum">-</div></div>
          <div class="result-item"><div class="r-label">Count</div><div class="r-value" id="rCount">-</div></div>
        </div>
      </div>"""

    info = """    <h2>How the average is calculated</h2>
    <p>This calculator finds the arithmetic mean of any list of numbers you enter — the sum of all values divided by how many values there are. It also shows the total sum and the number of values, which is handy for checking your data was entered correctly.</p>
    <div class="formula-box">Average = Sum of all numbers ÷ Count of numbers</div>
    <h2>How to use it</h2>
    <ol>
      <li>Type or paste your numbers into the box, separated by commas, spaces or new lines.</li>
      <li>Press <strong>Calculate Average</strong> to see the average, sum and count.</li>
    </ol>"""

    faq = [
        ("What formats can I use to enter numbers?", "You can separate numbers with commas, spaces, tabs, or put each number on its own line — the calculator recognises all of these."),
        ("Does it handle decimals and negative numbers?", "Yes, both decimals (like 4.5) and negative numbers (like -12) are supported."),
        ("Is there a limit to how many numbers I can enter?", "There's no fixed limit — you can paste in a large list, and the calculation still happens instantly in your browser."),
    ]

    script = """<script>
  const numbers = document.getElementById('numbers'), numErr = document.getElementById('numError');
  const result = document.getElementById('result');

  function calculate() {
    clearError(numbers, numErr);
    const raw = numbers.value.split(/[\\s,]+/).map(s => s.trim()).filter(Boolean);
    const vals = raw.map(Number).filter(n => !isNaN(n));
    if (vals.length === 0) { showError(numbers, numErr, 'Enter at least one valid number.'); result.classList.remove('show'); return; }
    const sum = vals.reduce((a, b) => a + b, 0);
    const avg = sum / vals.length;
    document.getElementById('rAvg').textContent = formatNumber(avg, 4);
    document.getElementById('rSum').textContent = formatNumber(sum, 4);
    document.getElementById('rCount').textContent = vals.length;
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    numbers.value = ''; clearError(numbers, numErr); result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="average-calculator.html",
        title="Average Calculator - Mean, Sum & Count",
        meta_desc="Calculate the average, sum and count of any list of numbers instantly.",
        h1="Average Calculator",
        intro="Find the average, sum and total count of a list of numbers.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["percentage", "cgpa", "attendance"],
        extra_script=script,
    )
    write("average-calculator.html", html)


# ============================================================ ATTENDANCE CALCULATOR
def build_attendance():
    calc_card = """      <div class="field-row">
        <div class="field-group">
          <label for="totalClasses">Total classes held</label>
          <input type="number" id="totalClasses" placeholder="e.g. 80">
          <div class="error-text" id="totalError"></div>
        </div>
        <div class="field-group">
          <label for="attendedClasses">Classes attended</label>
          <input type="number" id="attendedClasses" placeholder="e.g. 65">
          <div class="error-text" id="attendedError"></div>
        </div>
      </div>
      <div class="field-group">
        <label for="targetPct">Required attendance (%)</label>
        <input type="number" id="targetPct" value="75">
        <div class="hint">Most institutions require 75%. Change this to match your college's rule.</div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate Attendance</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Current Attendance</div>
          <div class="result-value" id="rMain">—</div>
        </div>
        <div class="result-note" id="rNote"></div>
      </div>"""

    info = """    <h2>How attendance percentage works</h2>
    <p>Your attendance percentage is simply the number of classes you've attended divided by the total number of classes held so far. Most colleges and schools set a minimum required percentage (commonly 75%) that you need to maintain to be eligible for exams.</p>
    <div class="formula-box">Attendance % = (Classes Attended ÷ Total Classes) × 100</div>
    <h2>Classes you can safely miss, or need to attend</h2>
    <p>If you're above the required percentage, this calculator estimates how many upcoming classes you could miss while still staying at or above the target — assuming those future classes are simply not attended and still count towards the total. If you're below the required percentage, it estimates how many upcoming classes you'd need to attend (assuming you attend every one of them) to reach the target.</p>"""

    faq = [
        ("Why 75% by default?", "75% is a commonly used minimum attendance requirement at many Indian colleges and universities, but it varies by institution — change the \"Required attendance\" field to match your own college's rule."),
        ("How is \"classes you can miss\" calculated?", "It assumes every additional class held is also a class you skip, and finds the maximum number of such classes you can miss before your attendance percentage would drop below your target."),
        ("What if reaching the target isn't mathematically possible?", "If your target is 100% and you've already missed any classes, or if there simply aren't enough remaining classes information to reach the target, the calculator will let you know it isn't achievable with the numbers given."),
    ]

    script = """<script>
  const totalClasses = document.getElementById('totalClasses'), totalErr = document.getElementById('totalError');
  const attendedClasses = document.getElementById('attendedClasses'), attErr = document.getElementById('attendedError');
  const targetPct = document.getElementById('targetPct');
  const result = document.getElementById('result');

  function calculate() {
    [totalClasses, attendedClasses].forEach(i => i.classList.remove('input-error'));
    [totalErr, attErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    let ok = true;
    const total = parseNum(totalClasses.value);
    const attended = parseNum(attendedClasses.value);
    const target = parseNum(targetPct.value);

    if (isNaN(total) || total <= 0) { showError(totalClasses, totalErr, 'Enter total classes greater than 0.'); ok = false; }
    if (isNaN(attended) || attended < 0) { showError(attendedClasses, attErr, 'Enter a valid number of attended classes.'); ok = false; }
    if (ok && attended > total) { showError(attendedClasses, attErr, 'Attended classes cannot exceed total classes.'); ok = false; }
    if (!ok) { result.classList.remove('show'); return; }

    const pct = (attended / total) * 100;
    document.getElementById('rMain').textContent = formatNumber(pct) + '%';

    let note = '';
    const t = isNaN(target) || target <= 0 ? 75 : target;
    if (pct >= t) {
      if (t < 100) {
        const maxMiss = Math.floor((attended * 100 / t) - total);
        note = maxMiss > 0
          ? `You can miss up to ${maxMiss} more class${maxMiss === 1 ? '' : 'es'} and still stay at or above ${formatNumber(t,0)}% attendance.`
          : `You're right at the edge of ${formatNumber(t,0)}% — missing another class now would drop you below target.`;
      } else {
        note = `You're meeting the ${formatNumber(t,0)}% target. At 100% required attendance, you cannot miss any further classes.`;
      }
    } else {
      if (t >= 100) {
        note = `A 100% target can no longer be reached since you've already missed classes.`;
      } else {
        const needed = Math.ceil((t * total - 100 * attended) / (100 - t));
        note = needed > 0
          ? `You need to attend the next ${needed} class${needed === 1 ? '' : 'es'} in a row to reach ${formatNumber(t,0)}% attendance.`
          : `You're below target — please review the numbers entered.`;
      }
    }
    document.getElementById('rNote').textContent = note;
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    totalClasses.value=''; attendedClasses.value=''; targetPct.value='75';
    [totalClasses, attendedClasses].forEach(i => i.classList.remove('input-error'));
    [totalErr, attErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="attendance-calculator.html",
        title="Attendance Calculator - Track Your Attendance %",
        meta_desc="Calculate your attendance percentage, how many classes you can safely miss, or how many you need to attend to reach your target.",
        h1="Attendance Calculator",
        intro="Check your current attendance percentage and how many classes you can miss or need to attend.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["cgpa", "average", "datediff"],
        extra_script=script,
    )
    write("attendance-calculator.html", html)


if __name__ == "__main__":
    build_simple_interest()
    build_compound_interest()
    build_average()
    build_attendance()
    print("Batch 3 (simple-interest, compound-interest, average, attendance) generated.")
