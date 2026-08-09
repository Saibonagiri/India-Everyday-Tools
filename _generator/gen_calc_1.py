#!/usr/bin/env python3
from build import calc_page, write

# ============================================================ AGE CALCULATOR
def build_age():
    calc_card = """      <div class="field-group">
        <label for="dob">Date of birth</label>
        <input type="date" id="dob">
        <div class="error-text" id="dobError"></div>
      </div>
      <div class="field-group">
        <label for="asOf">Calculate age as of</label>
        <input type="date" id="asOf">
        <div class="hint">Defaults to today. Change this to find your age on any date.</div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate Age</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Your Age</div>
          <div class="result-value" id="rMain">—</div>
        </div>
        <div class="result-grid">
          <div class="result-item"><div class="r-label">Years</div><div class="r-value" id="rYears">-</div></div>
          <div class="result-item"><div class="r-label">Months</div><div class="r-value" id="rMonths">-</div></div>
          <div class="result-item"><div class="r-label">Days</div><div class="r-value" id="rDays">-</div></div>
        </div>
        <div class="result-note" id="rTotal"></div>
      </div>"""

    info = """    <h2>How age is calculated</h2>
    <p>This calculator finds the exact time between your date of birth and the target date (today, by default) and breaks it down into complete years, complete months, and remaining days — the same way you'd count it on a calendar. It also works out the total number of days you've been alive, which is useful for milestones or official forms that ask for age in days.</p>
    <h2>How to use the Age Calculator</h2>
    <ol>
      <li>Enter your date of birth using the date picker.</li>
      <li>Optionally change "Calculate age as of" if you want your age on a specific date rather than today.</li>
      <li>Press <strong>Calculate Age</strong> to see your age in years, months, days and total days.</li>
      <li>Use <strong>Reset</strong> to clear the form and start again.</li>
    </ol>"""

    faq = [
        ("Why does the day count sometimes look different from a simple subtraction?", "Months have different numbers of days, so the calculator borrows days from the previous month when the day-of-month of your birth date is later than the day-of-month of the target date, similar to how you'd count age by hand on a calendar."),
        ("Can I find my age on a future or past date?", "Yes. Change the \"Calculate age as of\" field to any date, past or future, and the calculator will show your age as of that date."),
        ("Does this calculator store my date of birth?", "No. The calculation happens entirely in your browser and nothing you enter is sent to a server or saved."),
    ]

    script = """<script>
  const dob = document.getElementById('dob');
  const asOf = document.getElementById('asOf');
  const dobError = document.getElementById('dobError');
  const result = document.getElementById('result');

  const today = new Date();
  asOf.value = today.toISOString().slice(0,10);
  dob.max = today.toISOString().slice(0,10);

  function daysInMonth(y, m) { return new Date(y, m + 1, 0).getDate(); }

  function calculate() {
    clearErr();
    if (!dob.value) { showErr('Please enter your date of birth.'); return; }
    const d1 = new Date(dob.value + 'T00:00:00');
    const d2 = new Date((asOf.value || today.toISOString().slice(0,10)) + 'T00:00:00');
    if (isNaN(d1.getTime())) { showErr('Please enter a valid date.'); return; }
    if (d1 > d2) { showErr('Date of birth must be before the "as of" date.'); return; }

    let years = d2.getFullYear() - d1.getFullYear();
    let months = d2.getMonth() - d1.getMonth();
    let days = d2.getDate() - d1.getDate();

    if (days < 0) {
      months -= 1;
      const prevMonth = d2.getMonth() === 0 ? 11 : d2.getMonth() - 1;
      const prevYear = d2.getMonth() === 0 ? d2.getFullYear() - 1 : d2.getFullYear();
      days += daysInMonth(prevYear, prevMonth);
    }
    if (months < 0) { months += 12; years -= 1; }

    const totalDays = Math.round((d2 - d1) / 86400000);

    document.getElementById('rMain').textContent = `${years} yrs, ${months} mo, ${days} days`;
    document.getElementById('rYears').textContent = years;
    document.getElementById('rMonths').textContent = months;
    document.getElementById('rDays').textContent = days;
    document.getElementById('rTotal').textContent = `That's a total of ${formatNumber(totalDays,0)} days lived.`;
    result.classList.add('show');
  }

  function showErr(msg) { showError(dob, dobError, msg); result.classList.remove('show'); }
  function clearErr() { clearError(dob, dobError); }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    dob.value = ''; asOf.value = today.toISOString().slice(0,10);
    clearErr(); result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="age-calculator.html",
        title="Age Calculator - Calculate Your Exact Age",
        meta_desc="Calculate your exact age in years, months and days using your date of birth. Free, instant and works entirely in your browser.",
        h1="Age Calculator",
        intro="Find your exact age in years, months and days using your date of birth.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["datediff", "countdown", "attendance"],
        extra_script=script,
    )
    write("age-calculator.html", html)


# ============================================================ PERCENTAGE CALCULATOR
def build_percentage():
    calc_card = """      <div class="toggle-group" id="modeToggle" role="tablist" aria-label="Calculation type">
        <button data-mode="of" class="selected">% of a number</button>
        <button data-mode="what">Is what %</button>
        <button data-mode="change">% Change</button>
      </div>

      <div id="modeOf" class="calc-mode">
        <div class="field-row" style="margin-top:20px;">
          <div class="field-group">
            <label for="ofX">Percentage (%)</label>
            <input type="number" id="ofX" placeholder="e.g. 20">
          </div>
          <div class="field-group">
            <label for="ofY">Of value</label>
            <input type="number" id="ofY" placeholder="e.g. 500">
          </div>
        </div>
      </div>

      <div id="modeWhat" class="calc-mode" style="display:none;">
        <div class="field-row" style="margin-top:20px;">
          <div class="field-group">
            <label for="whatX">This value</label>
            <input type="number" id="whatX" placeholder="e.g. 40">
          </div>
          <div class="field-group">
            <label for="whatY">Out of</label>
            <input type="number" id="whatY" placeholder="e.g. 200">
          </div>
        </div>
      </div>

      <div id="modeChange" class="calc-mode" style="display:none;">
        <div class="field-row" style="margin-top:20px;">
          <div class="field-group">
            <label for="chgX">From value</label>
            <input type="number" id="chgX" placeholder="e.g. 250">
          </div>
          <div class="field-group">
            <label for="chgY">To value</label>
            <input type="number" id="chgY" placeholder="e.g. 300">
          </div>
        </div>
      </div>

      <div class="error-text" id="pctError"></div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label" id="rLabel">Result</div>
          <div class="result-value" id="rMain">—</div>
        </div>
      </div>"""

    info = """    <h2>The three percentage calculations explained</h2>
    <p><strong>% of a number</strong> answers questions like "What is 20% of 500?" by multiplying the value by the percentage divided by 100.</p>
    <p><strong>Is what %</strong> answers "40 is what percentage of 200?" by dividing the first value by the second and multiplying by 100.</p>
    <p><strong>% Change</strong> answers "What is the percentage increase or decrease from 250 to 300?" by finding the difference between the two values relative to the starting value.</p>
    <h2>Formulas used</h2>
    <div class="formula-box">% of a number:  (X ÷ 100) × Y
Is what %:      (X ÷ Y) × 100
% Change:       ((New − Old) ÷ Old) × 100</div>"""

    faq = [
        ("What's the difference between percentage increase and decrease?", "An increase means the new value is higher than the old one and shows a positive percentage; a decrease means the new value is lower and shows a negative percentage. This calculator labels the result as an increase or decrease automatically."),
        ("Can I use negative numbers?", "The \"% of a number\" and \"Is what %\" calculations work with positive values. For \"% Change\", the starting value should not be zero, since percentage change from zero is undefined."),
        ("Is this useful for exam marks or discounts?", "Yes — \"Is what %\" is commonly used for marks (e.g. 40 out of 200), and \"% of a number\" is useful for tips, discounts, and GST-style calculations."),
    ]

    script = """<script>
  const modes = { of: document.getElementById('modeOf'), what: document.getElementById('modeWhat'), change: document.getElementById('modeChange') };
  let currentMode = 'of';
  const pctError = document.getElementById('pctError');
  const result = document.getElementById('result');

  document.querySelectorAll('#modeToggle button').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('#modeToggle button').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      currentMode = btn.dataset.mode;
      Object.values(modes).forEach(m => m.style.display = 'none');
      modes[currentMode].style.display = 'block';
      result.classList.remove('show');
      clearError(null, pctError);
    });
  });

  function calculate() {
    clearError(null, pctError);
    let label = 'Result', value = null;

    if (currentMode === 'of') {
      const x = parseNum(document.getElementById('ofX').value);
      const y = parseNum(document.getElementById('ofY').value);
      if (isNaN(x) || isNaN(y)) { pctError.textContent = 'Please enter both values.'; pctError.classList.add('show'); return; }
      value = (x / 100) * y;
      label = `${formatNumber(x)}% of ${formatNumber(y)}`;
      document.getElementById('rMain').textContent = formatNumber(value);
    } else if (currentMode === 'what') {
      const x = parseNum(document.getElementById('whatX').value);
      const y = parseNum(document.getElementById('whatY').value);
      if (isNaN(x) || isNaN(y)) { pctError.textContent = 'Please enter both values.'; pctError.classList.add('show'); return; }
      if (y === 0) { pctError.textContent = 'The "out of" value cannot be zero.'; pctError.classList.add('show'); return; }
      value = (x / y) * 100;
      label = `${formatNumber(x)} is what % of ${formatNumber(y)}`;
      document.getElementById('rMain').textContent = formatNumber(value) + '%';
    } else {
      const x = parseNum(document.getElementById('chgX').value);
      const y = parseNum(document.getElementById('chgY').value);
      if (isNaN(x) || isNaN(y)) { pctError.textContent = 'Please enter both values.'; pctError.classList.add('show'); return; }
      if (x === 0) { pctError.textContent = 'The "from" value cannot be zero.'; pctError.classList.add('show'); return; }
      value = ((y - x) / Math.abs(x)) * 100;
      label = value >= 0 ? 'Percentage increase' : 'Percentage decrease';
      document.getElementById('rMain').textContent = formatNumber(Math.abs(value)) + '%';
    }
    document.getElementById('rLabel').textContent = label;
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    document.querySelectorAll('#modeOf input, #modeWhat input, #modeChange input').forEach(i => i.value = '');
    result.classList.remove('show');
    clearError(null, pctError);
  });
</script>"""

    html = calc_page(
        slug="percentage-calculator.html",
        title="Percentage Calculator - Find Percentages Instantly",
        meta_desc="Calculate what X% of a number is, what percentage one number is of another, or the percentage increase or decrease between two values.",
        h1="Percentage Calculator",
        intro="Work out percentages, reverse percentages, and percentage increase or decrease — all in one tool.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["discount", "gst", "average"],
        extra_script=script,
    )
    write("percentage-calculator.html", html)


# ============================================================ DISCOUNT CALCULATOR
def build_discount():
    calc_card = """      <div class="field-group">
        <label for="price">Original price</label>
        <div class="input-prefix-wrap"><span class="prefix">₹</span><input type="number" id="price" placeholder="e.g. 2000"></div>
        <div class="error-text" id="priceError"></div>
      </div>
      <div class="field-group">
        <label for="discount">Discount percentage</label>
        <input type="number" id="discount" placeholder="e.g. 25">
        <div class="error-text" id="discountError"></div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate Discount</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Final Price</div>
          <div class="result-value" id="rFinal">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label">Discount Amount</div><div class="r-value" id="rDiscount">-</div></div>
          <div class="result-item"><div class="r-label">You Save</div><div class="r-value" id="rSave">-</div></div>
        </div>
      </div>"""

    info = """    <h2>How the discount is calculated</h2>
    <p>This calculator applies a straightforward percentage discount to the price you enter. The discount amount is the original price multiplied by the discount percentage, and the final price is what remains after subtracting that discount.</p>
    <div class="formula-box">Discount Amount = Original Price × (Discount % ÷ 100)
Final Price = Original Price − Discount Amount</div>
    <h2>How to use the Discount Calculator</h2>
    <ol>
      <li>Enter the original price of the item.</li>
      <li>Enter the discount percentage being offered.</li>
      <li>Press <strong>Calculate Discount</strong> to see the final price and how much you save.</li>
    </ol>"""

    faq = [
        ("Does this handle multiple discounts stacked together?", "This calculator applies a single discount percentage. For two discounts applied one after another (for example 20% then an extra 10%), calculate the first discount, then run the result through the calculator again with the second percentage."),
        ("Can the discount percentage be more than 100%?", "No — a discount above 100% would mean a negative price, so the calculator will ask you to enter a value between 0 and 100."),
        ("Does this include GST or other taxes?", "No, this calculator only applies the discount. If you also need to add GST to a price, use our GST Calculator."),
    ]

    script = """<script>
  const price = document.getElementById('price'), priceErr = document.getElementById('priceError');
  const discount = document.getElementById('discount'), discErr = document.getElementById('discountError');
  const result = document.getElementById('result');

  function calculate() {
    clearError(price, priceErr); clearError(discount, discErr);
    let ok = true;
    const p = parseNum(price.value), d = parseNum(discount.value);
    if (isNaN(p) || p < 0) { showError(price, priceErr, 'Enter a valid price of 0 or more.'); ok = false; }
    if (isNaN(d) || d < 0 || d > 100) { showError(discount, discErr, 'Enter a discount between 0 and 100.'); ok = false; }
    if (!ok) { result.classList.remove('show'); return; }

    const discAmt = p * (d / 100);
    const final = p - discAmt;
    document.getElementById('rFinal').textContent = formatINR(final);
    document.getElementById('rDiscount').textContent = formatINR(discAmt);
    document.getElementById('rSave').textContent = formatINR(discAmt);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    price.value = ''; discount.value = '';
    clearError(price, priceErr); clearError(discount, discErr);
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="discount-calculator.html",
        title="Discount Calculator - Find Final Price & Savings",
        meta_desc="Calculate the final price and amount saved after applying a discount percentage to any price.",
        h1="Discount Calculator",
        intro="Find the final price and how much you save after a percentage discount.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["gst", "percentage", "tip"],
        extra_script=script,
    )
    write("discount-calculator.html", html)


# ============================================================ GST CALCULATOR
def build_gst():
    calc_card = """      <div class="toggle-group" id="gstToggle">
        <button data-mode="add" class="selected">Add GST</button>
        <button data-mode="remove">Remove GST</button>
      </div>
      <div class="field-group" style="margin-top:20px;">
        <label for="gstAmount" id="gstAmountLabel">Amount (excluding GST)</label>
        <div class="input-prefix-wrap"><span class="prefix">₹</span><input type="number" id="gstAmount" placeholder="e.g. 1000"></div>
        <div class="error-text" id="gstAmountError"></div>
      </div>
      <div class="field-group">
        <label>GST Rate</label>
        <div class="chip-group" id="gstChips">
          <button type="button" class="chip selected" data-rate="5">5%</button>
          <button type="button" class="chip" data-rate="12">12%</button>
          <button type="button" class="chip" data-rate="18">18%</button>
          <button type="button" class="chip" data-rate="28">28%</button>
        </div>
        <div class="hint">Or enter a custom rate below.</div>
        <input type="number" id="gstCustomRate" placeholder="Custom GST %" style="margin-top:10px;">
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate GST</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label" id="rFinalLabel">Final Amount</div>
          <div class="result-value" id="rFinal">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label" id="rOrigLabel">Original Amount</div><div class="r-value" id="rOrig">-</div></div>
          <div class="result-item"><div class="r-label">GST Amount</div><div class="r-value" id="rGst">-</div></div>
        </div>
      </div>
      <div class="disclaimer-box">GST rates can change and may vary by product or service category. Please verify the applicable rate for your specific transaction before relying on this result.</div>"""

    info = """    <h2>Adding vs removing GST</h2>
    <p><strong>Add GST</strong> takes an amount that does not yet include GST and adds the tax on top — useful when pricing a product or service. <strong>Remove GST</strong> does the opposite: it takes a final, GST-inclusive amount and works out how much of it was the original price versus the tax, which is useful when reading a bill that already includes GST.</p>
    <div class="formula-box">Add GST:     GST Amount = Amount × (Rate ÷ 100)
             Final Amount = Amount + GST Amount

Remove GST:  Original Amount = Final Amount ÷ (1 + Rate ÷ 100)
             GST Amount = Final Amount − Original Amount</div>
    <h2>Common GST rates in India</h2>
    <p>GST in India is commonly applied at 5%, 12%, 18% and 28%, depending on the category of goods or services. This calculator includes quick-select buttons for these common rates, plus a custom rate field for anything else.</p>"""

    faq = [
        ("Which GST rate should I select?", "The applicable GST rate depends on the specific goods or service category and current government notifications. Check your invoice, the GST portal, or a tax professional if you're unsure."),
        ("What does \"Remove GST\" actually calculate?", "It takes a price that already includes GST (like a restaurant bill total) and splits it back into the pre-tax amount and the GST portion, using the rate you select."),
        ("Do GST rates ever change?", "Yes, GST rates are set by the government and can change over time or vary by category. Always verify the current rate for your transaction before making financial decisions."),
    ]

    script = """<script>
  const amount = document.getElementById('gstAmount'), amtErr = document.getElementById('gstAmountError');
  const customRate = document.getElementById('gstCustomRate');
  const result = document.getElementById('result');
  let mode = 'add';
  let selectedRate = 5;

  document.getElementById('gstToggle').addEventListener('click', (e) => {
    const btn = e.target.closest('button'); if (!btn) return;
    document.querySelectorAll('#gstToggle button').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    mode = btn.dataset.mode;
    document.getElementById('gstAmountLabel').textContent = mode === 'add' ? 'Amount (excluding GST)' : 'Amount (including GST)';
    document.getElementById('rFinalLabel').textContent = mode === 'add' ? 'Final Amount (incl. GST)' : 'Original Amount (excl. GST)';
    document.getElementById('rOrigLabel').textContent = mode === 'add' ? 'Original Amount' : 'Final Amount';
    result.classList.remove('show');
  });

  document.getElementById('gstChips').addEventListener('click', (e) => {
    const chip = e.target.closest('.chip'); if (!chip) return;
    document.querySelectorAll('#gstChips .chip').forEach(c => c.classList.remove('selected'));
    chip.classList.add('selected');
    selectedRate = parseFloat(chip.dataset.rate);
    customRate.value = '';
  });

  customRate.addEventListener('input', () => {
    if (customRate.value !== '') {
      document.querySelectorAll('#gstChips .chip').forEach(c => c.classList.remove('selected'));
    }
  });

  function calculate() {
    clearError(amount, amtErr);
    const amt = parseNum(amount.value);
    const rate = customRate.value !== '' ? parseNum(customRate.value) : selectedRate;
    if (isNaN(amt) || amt < 0) { showError(amount, amtErr, 'Enter a valid amount of 0 or more.'); result.classList.remove('show'); return; }
    if (isNaN(rate) || rate < 0) { showError(amount, amtErr, 'Enter a valid GST rate.'); result.classList.remove('show'); return; }

    let orig, gstAmt, final;
    if (mode === 'add') {
      orig = amt; gstAmt = amt * (rate / 100); final = orig + gstAmt;
    } else {
      final = amt; orig = amt / (1 + rate / 100); gstAmt = final - orig;
    }
    document.getElementById('rFinal').textContent = formatINR(mode === 'add' ? final : orig);
    document.getElementById('rOrig').textContent = formatINR(mode === 'add' ? orig : final);
    document.getElementById('rGst').textContent = formatINR(gstAmt);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    amount.value = ''; customRate.value = '';
    document.querySelectorAll('#gstChips .chip').forEach(c => c.classList.remove('selected'));
    document.querySelector('#gstChips .chip').classList.add('selected');
    selectedRate = 5;
    clearError(amount, amtErr);
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="gst-calculator.html",
        title="GST Calculator - Add or Remove GST Instantly",
        meta_desc="Add or remove GST from any amount using common Indian GST rates (5%, 12%, 18%, 28%) or a custom rate.",
        h1="GST Calculator",
        intro="Add GST to a price, or remove GST from a final amount, using standard Indian GST rates.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["discount", "percentage", "emi"],
        extra_script=script,
    )
    write("gst-calculator.html", html)


if __name__ == "__main__":
    build_age()
    build_percentage()
    build_discount()
    build_gst()
    print("Batch 1 (age, percentage, discount, gst) generated.")
