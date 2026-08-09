#!/usr/bin/env python3
from build import calc_page, write

# ============================================================ SALARY HIKE
def build_salary_hike():
    calc_card = """      <div class="toggle-group" id="salaryUnit">
        <button data-unit="monthly" class="selected">Monthly Salary</button>
        <button data-unit="annual">Annual Salary (CTC)</button>
      </div>
      <div class="field-group" style="margin-top:20px;">
        <label for="currentSalary" id="salaryLabel">Current monthly salary</label>
        <div class="input-prefix-wrap"><span class="prefix">₹</span><input type="number" id="currentSalary" placeholder="e.g. 60000"></div>
        <div class="error-text" id="salaryError"></div>
      </div>
      <div class="field-group">
        <label for="hikePct">Hike percentage</label>
        <input type="number" id="hikePct" placeholder="e.g. 15">
        <div class="error-text" id="hikeError"></div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate New Salary</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label" id="rLabel">New Monthly Salary</div>
          <div class="result-value" id="rMain">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label">Hike Amount</div><div class="r-value" id="rHike">-</div></div>
          <div class="result-item"><div class="r-label" id="rOtherLabel">New Annual Salary</div><div class="r-value" id="rOther">-</div></div>
        </div>
      </div>"""

    info = """    <h2>How salary hike is calculated</h2>
    <p>A salary hike percentage is applied to your current salary to work out the hike amount, which is then added to get your new salary. This calculator also shows the equivalent annual or monthly figure so you can see both views at once.</p>
    <div class="formula-box">Hike Amount = Current Salary × (Hike % ÷ 100)
New Salary = Current Salary + Hike Amount</div>
    <h2>How to use it</h2>
    <ol>
      <li>Choose whether you're entering a monthly salary or an annual CTC.</li>
      <li>Enter your current salary figure.</li>
      <li>Enter the hike percentage you've been offered or are expecting.</li>
      <li>Press <strong>Calculate New Salary</strong> to see your new salary, the hike amount, and the equivalent monthly or annual figure.</li>
    </ol>"""

    faq = [
        ("Does this account for tax deductions?", "No, this calculator shows the gross hike on the salary figure you enter. Actual take-home pay depends on tax slabs, deductions and your CTC structure, which vary per individual."),
        ("What's the difference between monthly salary and CTC?", "Monthly salary is generally your in-hand or gross monthly pay, while annual CTC (Cost to Company) often includes benefits, bonuses and employer contributions beyond your monthly cash salary. Choose whichever figure matches what you're entering."),
        ("Can I use this for a salary decrease?", "This calculator is designed for positive hikes. For a pay cut, you can still get an estimate by treating the percentage as a decrease and interpreting the \"hike amount\" as the reduction — though the exact wording is aimed at raises."),
    ]

    script = """<script>
  const currentSalary = document.getElementById('currentSalary'), sErr = document.getElementById('salaryError');
  const hikePct = document.getElementById('hikePct'), hErr = document.getElementById('hikeError');
  const result = document.getElementById('result');
  let unit = 'monthly';

  document.getElementById('salaryUnit').addEventListener('click', (e) => {
    const btn = e.target.closest('button'); if (!btn) return;
    document.querySelectorAll('#salaryUnit button').forEach(b => b.classList.remove('selected'));
    btn.classList.add('selected');
    unit = btn.dataset.unit;
    document.getElementById('salaryLabel').textContent = unit === 'monthly' ? 'Current monthly salary' : 'Current annual salary (CTC)';
    document.getElementById('rLabel').textContent = unit === 'monthly' ? 'New Monthly Salary' : 'New Annual Salary';
    document.getElementById('rOtherLabel').textContent = unit === 'monthly' ? 'New Annual Salary' : 'New Monthly Salary';
    result.classList.remove('show');
  });

  function calculate() {
    [currentSalary, hikePct].forEach(i => i.classList.remove('input-error'));
    [sErr, hErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    let ok = true;
    const s = parseNum(currentSalary.value), h = parseNum(hikePct.value);
    if (isNaN(s) || s <= 0) { showError(currentSalary, sErr, 'Enter a salary greater than 0.'); ok = false; }
    if (isNaN(h)) { showError(hikePct, hErr, 'Enter a valid hike percentage.'); ok = false; }
    if (!ok) { result.classList.remove('show'); return; }

    const hikeAmt = s * (h / 100);
    const newSalary = s + hikeAmt;
    const otherView = unit === 'monthly' ? newSalary * 12 : newSalary / 12;

    document.getElementById('rMain').textContent = formatINR(newSalary);
    document.getElementById('rHike').textContent = formatINR(hikeAmt);
    document.getElementById('rOther').textContent = formatINR(otherView);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    currentSalary.value=''; hikePct.value='';
    [currentSalary, hikePct].forEach(i => i.classList.remove('input-error'));
    [sErr, hErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="salary-hike-calculator.html",
        title="Salary Hike Calculator",
        meta_desc="Calculate your new salary after a percentage hike, with both monthly and annual figures.",
        h1="Salary Hike Calculator",
        intro="Calculate your new salary and hike amount after a percentage increase.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["ci", "percentage", "emi"],
        extra_script=script,
    )
    write("salary-hike-calculator.html", html)


# ============================================================ TIP CALCULATOR
def build_tip():
    calc_card = """      <div class="field-group">
        <label for="billAmount">Bill amount</label>
        <div class="input-prefix-wrap"><span class="prefix">₹</span><input type="number" id="billAmount" placeholder="e.g. 1200"></div>
        <div class="error-text" id="billError"></div>
      </div>
      <div class="field-group">
        <label>Tip percentage</label>
        <div class="chip-group" id="tipChips">
          <button type="button" class="chip" data-rate="5">5%</button>
          <button type="button" class="chip selected" data-rate="10">10%</button>
          <button type="button" class="chip" data-rate="15">15%</button>
          <button type="button" class="chip" data-rate="20">20%</button>
        </div>
        <input type="number" id="tipCustom" placeholder="Custom tip %" style="margin-top:10px;">
      </div>
      <div class="field-group">
        <label for="peopleCount">Number of people</label>
        <input type="number" id="peopleCount" value="1" min="1">
        <div class="error-text" id="peopleError"></div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate Tip</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label">Total Bill</div>
          <div class="result-value" id="rTotal">—</div>
        </div>
        <div class="result-grid" style="grid-template-columns:repeat(2,1fr);">
          <div class="result-item"><div class="r-label">Tip Amount</div><div class="r-value" id="rTip">-</div></div>
          <div class="result-item"><div class="r-label">Per Person</div><div class="r-value" id="rPerPerson">-</div></div>
        </div>
      </div>"""

    info = """    <h2>How the tip is calculated</h2>
    <p>The tip amount is a percentage of your bill, and the total bill is your original amount plus that tip. If you're splitting the bill across a group, the per-person amount divides the total evenly.</p>
    <div class="formula-box">Tip Amount = Bill × (Tip % ÷ 100)
Total Bill = Bill + Tip Amount
Per Person = Total Bill ÷ Number of People</div>
    <h2>How to use it</h2>
    <ol>
      <li>Enter the bill amount.</li>
      <li>Choose a tip percentage, or enter a custom one.</li>
      <li>Enter how many people are splitting the bill.</li>
      <li>Press <strong>Calculate Tip</strong> to see the total and per-person amount.</li>
    </ol>"""

    faq = [
        ("What's a typical tip percentage in India?", "There's no fixed rule — many people tip around 5–10% at restaurants where service isn't already included, though this varies widely by city, establishment and personal preference."),
        ("Does this account for service charge already on the bill?", "No — if your bill already includes a service charge, you may not need to add an additional tip. Check your bill before adding one on top."),
        ("Can I split the bill unevenly?", "This calculator splits the total evenly across the number of people you enter. For uneven splits, you'd need to divide individual portions manually."),
    ]

    script = """<script>
  const billAmount = document.getElementById('billAmount'), billErr = document.getElementById('billError');
  const tipCustom = document.getElementById('tipCustom');
  const peopleCount = document.getElementById('peopleCount'), peopleErr = document.getElementById('peopleError');
  const result = document.getElementById('result');
  let selectedTip = 10;

  document.getElementById('tipChips').addEventListener('click', (e) => {
    const chip = e.target.closest('.chip'); if (!chip) return;
    document.querySelectorAll('#tipChips .chip').forEach(c => c.classList.remove('selected'));
    chip.classList.add('selected');
    selectedTip = parseFloat(chip.dataset.rate);
    tipCustom.value = '';
  });
  tipCustom.addEventListener('input', () => {
    if (tipCustom.value !== '') document.querySelectorAll('#tipChips .chip').forEach(c => c.classList.remove('selected'));
  });

  function calculate() {
    [billAmount, peopleCount].forEach(i => i.classList.remove('input-error'));
    [billErr, peopleErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    let ok = true;
    const bill = parseNum(billAmount.value);
    const people = parseNum(peopleCount.value);
    const tipRate = tipCustom.value !== '' ? parseNum(tipCustom.value) : selectedTip;
    if (isNaN(bill) || bill <= 0) { showError(billAmount, billErr, 'Enter a bill amount greater than 0.'); ok = false; }
    if (isNaN(people) || people < 1) { showError(peopleCount, peopleErr, 'Enter at least 1 person.'); ok = false; }
    if (!ok) { result.classList.remove('show'); return; }

    const tipAmt = bill * (tipRate / 100);
    const total = bill + tipAmt;
    const perPerson = total / people;

    document.getElementById('rTotal').textContent = formatINR(total);
    document.getElementById('rTip').textContent = formatINR(tipAmt);
    document.getElementById('rPerPerson').textContent = formatINR(perPerson);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    billAmount.value=''; tipCustom.value=''; peopleCount.value='1';
    document.querySelectorAll('#tipChips .chip').forEach(c => c.classList.remove('selected'));
    document.querySelector('#tipChips .chip[data-rate="10"]').classList.add('selected');
    selectedTip = 10;
    [billAmount, peopleCount].forEach(i => i.classList.remove('input-error'));
    [billErr, peopleErr].forEach(e => { e.textContent=''; e.classList.remove('show'); });
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="tip-calculator.html",
        title="Tip Calculator - Split the Bill Instantly",
        meta_desc="Calculate the tip amount, total bill, and amount per person for any bill and group size.",
        h1="Tip Calculator",
        intro="Calculate the tip, total bill, and how much each person owes.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["discount", "percentage", "average"],
        extra_script=script,
    )
    write("tip-calculator.html", html)


# ============================================================ COUNTDOWN
def build_countdown():
    calc_card = """      <div class="field-group">
        <label for="targetDate">Target date</label>
        <input type="date" id="targetDate">
        <div class="error-text" id="targetError"></div>
      </div>
      <div class="btn-row">
        <button class="btn btn-primary" id="calcBtn">Calculate Countdown</button>
        <button class="btn btn-secondary" id="resetBtn">Reset</button>
      </div>
      <div class="result-card" id="result">
        <div class="result-main">
          <div class="result-label" id="rLabel">Days Remaining</div>
          <div class="result-value" id="rMain">—</div>
        </div>
        <div class="result-grid">
          <div class="result-item"><div class="r-label">Months</div><div class="r-value" id="rMonths">-</div></div>
          <div class="result-item"><div class="r-label">Days</div><div class="r-value" id="rDays">-</div></div>
          <div class="result-item"><div class="r-label">Total Days</div><div class="r-value" id="rTotalDays">-</div></div>
        </div>
      </div>"""

    info = """    <h2>How the countdown works</h2>
    <p>This tool calculates exactly how many days remain between today and any future date you choose — useful for counting down to a birthday, anniversary, exam, trip, or deadline. It also breaks the remaining time down into an approximate number of months and days.</p>
    <h2>How to use it</h2>
    <ol>
      <li>Select a future date.</li>
      <li>Press <strong>Calculate Countdown</strong> to see the days remaining.</li>
    </ol>"""

    faq = [
        ("What happens if I choose a past date?", "The calculator is designed for future dates. If you select a date that has already passed, it will let you know instead of showing a countdown."),
        ("Does today count as day zero or day one?", "The total days figure is the number of full days between today and the target date, so if the target date is tomorrow, it will show 1 day remaining."),
        ("Can I use this to count down to an exam or event?", "Yes — this works for any future date, whether it's a personal milestone, a deadline, or an event you're planning for."),
    ]

    script = """<script>
  const targetDate = document.getElementById('targetDate');
  const targetError = document.getElementById('targetError');
  const result = document.getElementById('result');
  const today = new Date(); today.setHours(0,0,0,0);
  const tomorrow = new Date(today); tomorrow.setDate(tomorrow.getDate() + 1);
  targetDate.value = tomorrow.toISOString().slice(0,10);
  targetDate.min = today.toISOString().slice(0,10);

  function daysInMonth(y, m) { return new Date(y, m + 1, 0).getDate(); }

  function calculate() {
    targetError.textContent=''; targetError.classList.remove('show');
    if (!targetDate.value) { targetError.textContent = 'Please select a target date.'; targetError.classList.add('show'); result.classList.remove('show'); return; }
    const target = new Date(targetDate.value + 'T00:00:00');
    if (target < today) { targetError.textContent = 'That date has already passed. Choose a future date.'; targetError.classList.add('show'); result.classList.remove('show'); return; }

    const totalDays = Math.round((target - today) / 86400000);
    let months = target.getMonth() - today.getMonth() + (target.getFullYear() - today.getFullYear()) * 12;
    let days = target.getDate() - today.getDate();
    if (days < 0) {
      months -= 1;
      const prevMonth = target.getMonth() === 0 ? 11 : target.getMonth() - 1;
      const prevYear = target.getMonth() === 0 ? target.getFullYear() - 1 : target.getFullYear();
      days += daysInMonth(prevYear, prevMonth);
    }

    document.getElementById('rMain').textContent = `${formatNumber(totalDays,0)} day${totalDays === 1 ? '' : 's'}`;
    document.getElementById('rMonths').textContent = months;
    document.getElementById('rDays').textContent = days;
    document.getElementById('rTotalDays').textContent = formatNumber(totalDays,0);
    result.classList.add('show');
  }

  document.getElementById('calcBtn').addEventListener('click', calculate);
  document.getElementById('resetBtn').addEventListener('click', () => {
    targetDate.value = tomorrow.toISOString().slice(0,10);
    targetError.textContent=''; targetError.classList.remove('show');
    result.classList.remove('show');
  });
</script>"""

    html = calc_page(
        slug="countdown.html",
        title="Date Countdown Calculator - Days Remaining",
        meta_desc="Count down the days, months and days remaining to any future date, event or deadline.",
        h1="Date Countdown",
        intro="Count down the days remaining to any future date, birthday, event or deadline.",
        calc_card_inner=calc_card,
        info_sections=info,
        faq_items=faq,
        related_ids=["age", "datediff", "attendance"],
        extra_script=script,
    )
    write("countdown.html", html)


if __name__ == "__main__":
    build_salary_hike()
    build_tip()
    build_countdown()
    print("Batch 4 (salary-hike, tip, countdown) generated.")
