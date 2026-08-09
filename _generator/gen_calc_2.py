#!/usr/bin/env python3
from build import calc_page, write

# ============================================================ EMI CALCULATOR
def build_emi():
    calc_card = """      <div class="field-group">
        <label for="loanAmt">Loan amount</label>
        <div class="input-prefix-wrap"><span class="prefix">₹</span><input type="number" id="loanAmt" placeholder="e.g. 1000000"></div>
        <div class="error-text" id="loanAmtError"></div>
      </div>
      <div class="field-row">
        <div class="field-group">
          <label for="rate">Annual interest rate (%)</label>
          <input type="number" id="rate" placeholder="e.g. 9.5" step="0.01">
          <div class="error-text" id="rateError"></div>
        </div>
        <div class="field-group">
          <label for="tenure">Loan tenure</label>
          <input type="number" id="tenure" placeholder="e.g. 20">
          <div class="error-text" id="tenureError"></div>
        </div>
      </div>
      <div class="field-group">
        <div class="toggle-group" id="tenureUnit">
          <button data-unit="years" class="selected">Years</button>
          <button data-unit="months">Months</button>
        </div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate EMI</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Monthly EMI</div>
          <div class="result-value" id="rEmi">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label">Total Interest</div><div class="r-value" id="rInterest">-</div></div>
          <div class="result-item"><div class="r-label">Total Payment</div><div class="r-value" id="rTotal">-</div></div>
        </div>
      </div>"""

    info = """    <h2>What is EMI?</h2>
    <p>EMI (Equated Monthly Instalment) is the fixed amount you pay every month towards a loan, covering both principal repayment and interest, until the loan is fully repaid. Lenders in India calculate EMI using the reducing-balance method, where interest is charged only on the outstanding principal each month.</p>
    <h2>The EMI formula</h2>
    <div class="formula-box">EMI = P × r × (1 + r)^n ÷ ((1 + r)^n − 1)

P = Loan amount (Principal)
r = Monthly interest rate (Annual rate ÷ 12 ÷ 100)
n = Loan tenure in months</div>
    <p>Total interest is the total of all EMI payments minus the original loan amount, and total payment is simply the EMI multiplied by the number of months.</p>
    <h2>How to use the EMI Calculator</h2>
    <ol>
      <li>Enter the loan amount you plan to borrow.</li>
      <li>Enter the annual interest rate offered by your lender.</li>
      <li>Enter the tenure and choose whether it's in years or months.</li>
      <li>Press <strong>Calculate EMI</strong> to see your monthly instalment, total interest, and total repayment.</li>
    </ol>"""

    faq = [
        ("Does this include processing fees or other charges?", "No, this calculator computes the standard EMI based on principal, rate and tenure only. Banks may add processing fees, insurance, or other charges that aren't reflected here — check your loan offer for the full cost."),
        ("What happens if the interest rate is 0%?", "If the rate is 0%, the EMI is simply the loan amount divided evenly by the number of months, with no interest component."),
        ("Is this the same formula banks use?", "Most Indian banks and NBFCs use the reducing-balance EMI formula shown above for home loans, car loans and personal loans, though exact terms can vary by lender."),
    ]

    script = """<script>
  const loanAmt = document.getElementById('loanAmt'), loanErr = document.getElementById('loanAmtError');
  const rate = document.getElementById('rate'), rateErr = document.getElementById('rateError');
  const tenure = document.getElementById('tenure'), tenureErr = document.getElementById('tenureError');
  const result = document.getElementById('result');
  let unit = 'years';

  document.getElementById('tenureUnit').addEventListener('click', (e) => {
    const btn = e.target.closest('button'); if (!btn) return;
    document.querySelectorAll('#tenureUnit button').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    unit = btn.dataset.unit;
  });

  function calculate() {
    [loanAmt, rate, tenure].forEach(i => i.classList.remove('input-error'));
    [loanErr, rateErr, tenureErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    let ok = true;
    const P = parseNum(loanAmt.value);
    const annualRate = parseNum(rate.value);
    const t = parseNum(tenure.value);

    if (isNaN(P) || P <= 0) { showError(loanAmt, loanErr, 'Enter a loan amount greater than 0.'); ok = false; }
    if (isNaN(annualRate) || annualRate < 0) { showError(rate, rateErr, 'Enter a valid interest rate.'); ok = false; }
    if (isNaN(t) || t <= 0) { showError(tenure, tenureErr, 'Enter a tenure greater than 0.'); ok = false; }
    if (!ok) { result.classList.remove('show'); return; }

    const n = unit === 'years' ? t * 12 : t;
    const r = annualRate / 12 / 100;
    let emi;
    if (r === 0) { emi = P / n; } else { emi = (P * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1); }
    const totalPayment = emi * n;
    const totalInterest = totalPayment - P;

    document.getElementById('rEmi').textContent = formatINR(emi);
    document.getElementById('rInterest').textContent = formatINR(totalInterest);
    document.getElementById('rTotal').textContent = formatINR(totalPayment);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    loanAmt.value=''; rate.value=''; tenure.value='';
    [loanAmt, rate, tenure].forEach(i => i.classList.remove('input-error'));
    [loanErr, rateErr, tenureErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="emi-calculator.html",
        title="EMI Calculator - Calculate Monthly Loan EMI",
        meta_desc="Calculate your monthly EMI, total interest and total payment for any home, car or personal loan using the standard reducing-balance formula.",
        h1="EMI Calculator",
        intro="Calculate your monthly loan EMI, total interest and total repayment amount instantly.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["si", "ci", "gst"],
        extra_script=script,
    )
    write("emi-calculator.html", html)


# ============================================================ CGPA TO PERCENTAGE
def build_cgpa():
    calc_card = """      <div class="field-group">
        <label for="cgpa">CGPA (out of 10)</label>
        <input type="number" id="cgpa" placeholder="e.g. 8.2" step="0.01">
        <div class="error-text" id="cgpaError"></div>
      </div>
      <div class="field-group">
        <label for="multiplier">Conversion multiplier</label>
        <input type="number" id="multiplier" value="9.5" step="0.1">
        <div class="hint">9.5 is a commonly used multiplier (used by CBSE and several universities). Change this if your institution specifies a different one.</div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Convert to Percentage</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Estimated Percentage</div>
          <div class="result-value" id="rMain">—</div>
        </div>
      </div>
      <div class="disclaimer-box">CGPA-to-percentage conversion rules may vary by university or institution. Check your institution's official formula before submitting a converted percentage anywhere official.</div>"""

    info = """    <h2>How CGPA is converted to a percentage</h2>
    <p>Many Indian universities and boards, including CBSE, use a simple multiplier to convert CGPA (Cumulative Grade Point Average, typically on a 10-point scale) into an equivalent percentage. The most commonly referenced multiplier is 9.5, though this is only an approximation and not a universal rule.</p>
    <div class="formula-box">Percentage = CGPA × 9.5</div>
    <h2>Why the multiplier can change</h2>
    <p>Different universities, especially at the postgraduate or engineering level, sometimes use a different multiplier or a completely different formula (for example, "(CGPA − 0.75) × 10"). This calculator lets you edit the multiplier field so you can match your own institution's official method if it's different from the common 9.5 default.</p>"""

    faq = [
        ("Is 9.5 the correct multiplier for every university?", "No. 9.5 is a widely used approximation, notably associated with CBSE, but many universities publish their own formula. Always check your institution's official conversion method for anything submitted officially."),
        ("Can CGPA be above 10?", "Most Indian grading systems use a 10-point CGPA scale, so this calculator expects a value between 0 and 10."),
        ("Why does my university's percentage differ slightly from this estimate?", "Because conversion formulas vary — some universities use a different multiplier, some subtract a constant first. This tool gives a commonly used estimate, not an official transcript value."),
    ]

    script = """<script>
  const cgpa = document.getElementById('cgpa'), cgpaErr = document.getElementById('cgpaError');
  const multiplier = document.getElementById('multiplier');
  const result = document.getElementById('result');

  function calculate() {
    clearError(cgpa, cgpaErr);
    const c = parseNum(cgpa.value);
    const m = parseNum(multiplier.value);
    if (isNaN(c) || c < 0 || c > 10) { showError(cgpa, cgpaErr, 'Enter a CGPA between 0 and 10.'); result.classList.remove('show'); return; }
    if (isNaN(m) || m <= 0) { cgpa.classList.add('input-error'); result.classList.remove('show'); return; }
    const pct = c * m;
    document.getElementById('rMain').textContent = formatNumber(pct) + '%';
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    cgpa.value=''; multiplier.value='9.5';
    clearError(cgpa, cgpaErr);
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="cgpa-to-percentage.html",
        title="CGPA to Percentage Calculator",
        meta_desc="Convert your CGPA to an estimated percentage using the commonly used 9.5 multiplier, or your own institution's formula.",
        h1="CGPA to Percentage Calculator",
        intro="Convert your CGPA into an estimated percentage using a standard or custom conversion multiplier.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["attendance", "average", "percentage"],
        extra_script=script,
    )
    write("cgpa-to-percentage.html", html)


# ============================================================ DATE DIFFERENCE
def build_datediff():
    calc_card = """      <div class="field-row">
        <div class="field-group">
          <label for="startDate">Start date</label>
          <input type="date" id="startDate">
        </div>
        <div class="field-group">
          <label for="endDate">End date</label>
          <input type="date" id="endDate">
        </div>
      </div>
      <div class="error-text" id="ddError"></div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate Difference</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Difference</div>
          <div class="result-value" id="rMain">—</div>
        </div>
        <div class="result-grid">
          <div class="result-item"><div class="r-label">Years</div><div class="r-value" id="rYears">-</div></div>
          <div class="result-item"><div class="r-label">Months</div><div class="r-value" id="rMonths">-</div></div>
          <div class="result-item"><div class="r-label">Days</div><div class="r-value" id="rDays">-</div></div>
        </div>
        <div class="result-note" id="rTotal"></div>
      </div>"""

    info = """    <h2>How the date difference is calculated</h2>
    <p>This calculator finds the calendar-accurate difference between two dates, broken down into complete years, complete months, and remaining days — as well as the total number of days between them, which is useful for calculating durations, notice periods, or project timelines.</p>
    <h2>How to use it</h2>
    <ol>
      <li>Select a start date.</li>
      <li>Select an end date.</li>
      <li>Press <strong>Calculate Difference</strong> to see the breakdown and the total number of days.</li>
    </ol>"""

    faq = [
        ("Can the end date be before the start date?", "The calculator expects the end date to be on or after the start date. If you enter them the other way round, you'll see a validation message."),
        ("Does this count the start and end day both?", "The total days figure is the number of full days between the two dates (end minus start), which matches how most duration calculations, notice periods, and interest-period calculations are done."),
        ("Can I use this for age calculation too?", "For a person's exact age from their date of birth to today, our dedicated Age Calculator is a more convenient option, though the underlying calculation is the same."),
    ]

    script = """<script>
  const startDate = document.getElementById('startDate');
  const endDate = document.getElementById('endDate');
  const ddError = document.getElementById('ddError');
  const result = document.getElementById('result');
  const today = new Date().toISOString().slice(0,10);
  endDate.value = today;

  function daysInMonth(y, m) { return new Date(y, m + 1, 0).getDate(); }

  function calculate() {
    ddError.textContent=''; ddError.classList.remove('show');
    if (!startDate.value || !endDate.value) { ddError.textContent='Please select both dates.'; ddError.classList.add('show'); result.classList.remove('show'); return; }
    const d1 = new Date(startDate.value + 'T00:00:00');
    const d2 = new Date(endDate.value + 'T00:00:00');
    if (d1 > d2) { ddError.textContent='End date must be on or after the start date.'; ddError.classList.add('show'); result.classList.remove('show'); return; }

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
    document.getElementById('rTotal').textContent = `That's a total of ${formatNumber(totalDays,0)} days.`;
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    startDate.value=''; endDate.value=today;
    ddError.textContent=''; ddError.classList.remove('show');
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="date-difference.html",
        title="Date Difference Calculator - Days Between Two Dates",
        meta_desc="Find the exact number of years, months and days between any two dates, plus the total number of days.",
        h1="Date Difference Calculator",
        intro="Find the number of years, months and days between any two dates.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["age", "countdown", "attendance"],
        extra_script=script,
    )
    write("date-difference.html", html)


# ============================================================ UNIT CONVERTER
def build_unit_converter():
    calc_card = """      <div class="field-group">
        <label for="unitCategory">Category</label>
        <select id="unitCategory">
          <option value="length">Length</option>
          <option value="weight">Weight / Mass</option>
          <option value="temperature">Temperature</option>
          <option value="area">Area</option>
          <option value="volume">Volume</option>
          <option value="speed">Speed</option>
          <option value="data">Data / Storage</option>
        </select>
      </div>
      <div class="field-row">
        <div class="field-group">
          <label for="unitFrom">From</label>
          <select id="unitFrom"></select>
        </div>
        <div class="field-group">
          <label for="unitTo">To</label>
          <select id="unitTo"></select>
        </div>
      </div>
      <div class="field-group">
        <label for="unitValue">Value</label>
        <input type="number" id="unitValue" placeholder="Enter a value" value="1">
        <div class="error-text" id="unitError"></div>
      </div>
      <div class="result-card show" id="result">
        <div class="result-main">
          <div class="result-label" id="rLabel">Result</div>
          <div class="result-value" id="rMain">—</div>
        </div>
      </div>"""

    info = """    <h2>Supported conversions</h2>
    <p>This converter supports length, weight/mass, temperature, area, volume, speed, and digital storage. Choose a category, pick your "from" and "to" units, and enter a value — the result updates instantly as you type.</p>
    <h2>How conversions work</h2>
    <p>For most categories, each unit is converted to a common base unit (such as metres for length, or kilograms for weight) and then converted from that base unit into your target unit. Temperature is handled separately since Celsius, Fahrenheit and Kelvin use different formulas rather than a simple multiplier.</p>"""

    faq = [
        ("Why is temperature handled differently?", "Celsius, Fahrenheit and Kelvin scales don't share a common zero point or proportional scale, so converting between them uses specific formulas (like °F = °C × 9/5 + 32) rather than a simple multiplication factor used for length or weight."),
        ("Are data storage units calculated in 1000s or 1024s?", "This calculator uses the binary convention (1 KB = 1024 bytes, 1 MB = 1024 KB, and so on), which matches how operating systems typically report file and storage sizes."),
        ("Can I convert in both directions?", "Yes — simply swap the \"From\" and \"To\" units, or enter a value in either field's unit and read the equivalent result."),
    ]

    script = """<script>
  const UNIT_DATA = {
    length: { base: 'm', units: {
      mm: 0.001, cm: 0.01, m: 1, km: 1000, inch: 0.0254, foot: 0.3048, yard: 0.9144, mile: 1609.344
    }, labels: { mm:'Millimetre (mm)', cm:'Centimetre (cm)', m:'Metre (m)', km:'Kilometre (km)', inch:'Inch (in)', foot:'Foot (ft)', yard:'Yard (yd)', mile:'Mile (mi)' } },
    weight: { base: 'kg', units: {
      mg: 0.000001, g: 0.001, kg: 1, tonne: 1000, ounce: 0.0283495, pound: 0.453592
    }, labels: { mg:'Milligram (mg)', g:'Gram (g)', kg:'Kilogram (kg)', tonne:'Tonne (t)', ounce:'Ounce (oz)', pound:'Pound (lb)' } },
    area: { base: 'sqm', units: {
      sqmm: 0.000001, sqcm: 0.0001, sqm: 1, hectare: 10000, sqkm: 1000000, acre: 4046.8564224, sqft: 0.09290304, sqyard: 0.83612736, sqmile: 2589988.110336
    }, labels: { sqmm:'Sq. Millimetre', sqcm:'Sq. Centimetre', sqm:'Sq. Metre', hectare:'Hectare', sqkm:'Sq. Kilometre', acre:'Acre', sqft:'Sq. Foot', sqyard:'Sq. Yard', sqmile:'Sq. Mile' } },
    volume: { base: 'l', units: {
      ml: 0.001, l: 1, cubicm: 1000, gallon: 3.785411784, quart: 0.946352946, pint: 0.473176473, cup: 0.236588236, cubicft: 28.316846592
    }, labels: { ml:'Millilitre (ml)', l:'Litre (l)', cubicm:'Cubic Metre', gallon:'Gallon (US)', quart:'Quart (US)', pint:'Pint (US)', cup:'Cup (US)', cubicft:'Cubic Foot' } },
    speed: { base: 'mps', units: {
      mps: 1, kmph: 0.277778, mph: 0.44704, knot: 0.514444
    }, labels: { mps:'Metres/second', kmph:'Km/hour', mph:'Miles/hour', knot:'Knot' } },
    data: { base: 'byte', units: {
      bit: 0.125, byte: 1, kb: 1024, mb: 1048576, gb: 1073741824, tb: 1099511627776
    }, labels: { bit:'Bit', byte:'Byte', kb:'Kilobyte (KB)', mb:'Megabyte (MB)', gb:'Gigabyte (GB)', tb:'Terabyte (TB)' } },
  };
  const TEMP_LABELS = { celsius: 'Celsius (°C)', fahrenheit: 'Fahrenheit (°F)', kelvin: 'Kelvin (K)' };

  const category = document.getElementById('unitCategory');
  const fromSel = document.getElementById('unitFrom');
  const toSel = document.getElementById('unitTo');
  const valueInput = document.getElementById('unitValue');
  const unitError = document.getElementById('unitError');
  const result = document.getElementById('result');

  function populateUnits() {
    const cat = category.value;
    fromSel.innerHTML = ''; toSel.innerHTML = '';
    if (cat === 'temperature') {
      Object.keys(TEMP_LABELS).forEach(key => {
        fromSel.add(new Option(TEMP_LABELS[key], key));
        toSel.add(new Option(TEMP_LABELS[key], key));
      });
      fromSel.value = 'celsius'; toSel.value = 'fahrenheit';
    } else {
      const data = UNIT_DATA[cat];
      Object.keys(data.units).forEach(key => {
        fromSel.add(new Option(data.labels[key], key));
        toSel.add(new Option(data.labels[key], key));
      });
      const keys = Object.keys(data.units);
      fromSel.value = keys[0]; toSel.value = keys[Math.min(2, keys.length - 1)];
    }
    convert();
  }

  function toCelsius(v, unit) {
    if (unit === 'celsius') return v;
    if (unit === 'fahrenheit') return (v - 32) * 5/9;
    if (unit === 'kelvin') return v - 273.15;
  }
  function fromCelsius(v, unit) {
    if (unit === 'celsius') return v;
    if (unit === 'fahrenheit') return v * 9/5 + 32;
    if (unit === 'kelvin') return v + 273.15;
  }

  function convert() {
    unitError.textContent=''; unitError.classList.remove('show');
    const v = parseNum(valueInput.value);
    if (isNaN(v)) { document.getElementById('rMain').textContent = '—'; return; }
    const cat = category.value;
    let out;
    if (cat === 'temperature') {
      out = fromCelsius(toCelsius(v, fromSel.value), toSel.value);
    } else {
      const data = UNIT_DATA[cat];
      const baseVal = v * data.units[fromSel.value];
      out = baseVal / data.units[toSel.value];
    }
    const fromLabel = cat === 'temperature' ? TEMP_LABELS[fromSel.value] : UNIT_DATA[cat].labels[fromSel.value];
    const toLabel = cat === 'temperature' ? TEMP_LABELS[toSel.value] : UNIT_DATA[cat].labels[toSel.value];
    document.getElementById('rLabel').textContent = `${formatNumber(v)} ${fromLabel} =`;
    document.getElementById('rMain').textContent = `${formatNumber(out, 6)} ${toLabel}`;
  }

  category.addEventListener('change', populateUnits);
  fromSel.addEventListener('change', convert);
  toSel.addEventListener('change', convert);
  valueInput.addEventListener('input', convert);

  populateUnits();
</script>"""

    html = calc_page(
        slug="unit-converter.html",
        title="Unit Converter - Length, Weight, Temperature & More",
        meta_desc="Convert length, weight, temperature, area, volume, speed and data storage units instantly, free and entirely in your browser.",
        h1="Unit Converter",
        intro="Convert between length, weight, temperature, area, volume, speed and data storage units.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["percentage", "average", "gst"],
        extra_script=script,
    )
    write("unit-converter.html", html)


if __name__ == "__main__":
    build_emi()
    build_cgpa()
    build_datediff()
    build_unit_converter()
    print("Batch 2 (emi, cgpa, date-difference, unit-converter) generated.")
