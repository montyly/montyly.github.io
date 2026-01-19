---
title: Getting Rounding Right in DeFi
permalink: /blog/rounding-in-defi
---

<style>
.nav-tabs {
  display: flex;
  margin-bottom: 1.5rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-family: inherit;
  font-size: 0.95em;
  overflow: hidden;
  width: fit-content;
}

.nav-tabs a {
  padding: 8px 16px;
  text-decoration: none;
  color: #0366d6;
  background: #f8f8f8;
  border-right: 1px solid #ccc;
  flex: 1;
  text-align: center;
}

.nav-tabs a:last-child {
  border-right: none;
}

.nav-tabs a.active {
  background: white;
  font-weight: bold;
}
</style>

<div class="nav-tabs">
  <a href="/">Home</a>
  <a href="/blog" class="active">Blog</a>
  <a href="/talks/">Talks</a>
  <a href="/portfolio/">Portfolio</a>
  <a href="/about/">About</a>
</div>


# Getting Rounding Right in DeFi

---

*January 2026*

Rounding bugs are having a moment, and not in a good way. Bunny, Balancer (twice), Yield V2, the Solana Program Library... the list of protocols hit by rounding exploits keeps growing. This isn't coincidence. When the same bug class shows up this frequently, it's a sign that attackers have developed systematic methodologies and tooling to find and exploit these issues efficiently.

Most guidance on rounding boils down to one rule: "round in favor of the protocol." But as we'll see, that advice is necessary but nowhere near sufficient. Real protocols have complex formulas, intermediate values that get reused, and edge cases where determining the correct rounding direction is far from obvious.

This post covers why rounding goes wrong, walks through a real attack, and offers a framework for actually getting it right.

---

## Why Rounding Is a Security Problem

If you've worked with Solidity, you know the EVM doesn't do decimals. Everything is integers. When you divide, the remainder disappears:

```solidity
uint a = 8;
uint b = 12;
uint c = 5;

uint v0 = (a * b) / c;  // 19
uint v1 = a * (b / c);  // 16
```

Same inputs, different order, different results. **Algebraic equivalence is not semantic equivalence on-chain.**

DeFi protocols work around this using fixed-point arithmetic, scaling numbers up by a factor (usually 10^18) to simulate decimals. But every multiplication and division still loses precision. The question isn't *if* you lose precision, it's *how you handle the loss*.

Libraries like PRBMath and Solmate provide functions like `mulWadDown` and `mulWadUp` that let you choose your rounding directio: whether the result should be slightly smaller or larger when precision is lost.

---

## Case Study: The Balancer Rounding Bug (2021)

Let's look at a simplified version of a vulnerability found during an [audit of Balancer in 2021](https://github.com/trailofbits/publications/blob/master/reviews/2021-04-balancer-balancerv2-securityreview.pdf). This is not the recent Balancer hack, but it perfectly illustrates how rounding can go wrong. The swap formula calculates how many tokens you receive (tokenOut) based on how many you deposit (tokenIn):

```
tokenOut = balanceOut * (1 - balanceIn / (balanceIn + tokenIn))
```

The ratio `balanceIn / (balanceIn + tokenIn)` is always less than 1. As you send more tokens in, this ratio shrinks, and you get more tokens out.

Here's the problem: **what if that ratio rounds to zero?**

If the division truncates to 0, the formula becomes:

```
tokenOut = balanceOut * (1 - 0)
tokenOut = balanceOut
```

You get *everything*.

### The Attack

An attacker can abuse this scenario:

1. **Flash mint** a massive amount of Token A (say, 10^38)
2. **Unbalance the pool** by swapping all that Token A for nearly all of Token B, leaving just 1 wei of Token B in the pool
3. **Exploit the rounding**: Swap 2 * 10^18 Token B back. With `balanceIn = 1` wei, the ratio rounds to zero, and the attacker receives the entire Token A balance
4. **Repay and profit**: Pay back the flash loan. The attacker started with nothing and ends up with all the token A and most of the token B

You can see more details about the attack path in my [WonderCon slides](https://github.com/montyly/publications/blob/main/industrial/presentations/2025/wondercon/2025-11-16_rounding.pdf).

**The fix?** Round that ratio *up* instead of down. If it doesn't round to zero, the attacker won't receive the full Token A balance in step 3. The leftover makes the attack unprofitable.

---

## "Just Round in Favor of the Protocol"

The standard advice is simple: always round in favor of the protocol.

- When calculating amounts **paid out** to users → round **down**
- When calculating amounts **paid in** by users → round **up**

This ensures precision loss hurts the user, not the protocol. Simple, right?

Not quite.

### The Complexity Problem

Real formulas get complicated. Consider this made-up example that illustrates the kind of complexity you might encounter:

```
tokenOut = (a^(c/d)) * (1 - (e / (e + f + g))^(h*k/j))
```

To round the final result down, you need to trace through every intermediate step:

- `a^(c/d)` needs to round down
- But if `a < 1`, then `c/d` needs to round *up* to make `a^(c/d)` smaller
- If `a >= 1`, then `c/d` needs to round *down*

**The correct rounding direction can depend on runtime values.** If you find yourself in this situation, it's a sign you should rethink how the formula is composed.

### The Reuse Problem

Sometimes an intermediate value feeds into multiple calculations with conflicting requirements:

```solidity
uint256 a = computeA(...);  // Should this round up or down?
uint256 b = formulaB(a);    // Needs 'a' rounded down
uint256 c = formulaC(a);    // Needs 'a' rounded up
```

There's no single right answer. You might need to compute `a` twice with different rounding, adding complexity and gas costs.

### The Trapping Problem

Rounding in favor of the protocol can backfire. Consider a liquidation that calculates collateral to seize, rounded up to be conservative. If that rounded-up amount exceeds the user's actual balance, the transaction reverts.

An attacker could exploit this to make themselves unliquidatable, keeping a risky position open indefinitely. The "safe" rounding direction created a denial-of-service vulnerability.

### The Integration Problem

When your protocol integrates with external contracts, their rounding decisions become yours. Errors propagate and compound.

This vector is underexplored today, but as DeFi composability increases, I expect it to grow.

---

## A Framework for Getting Rounding Right

To decrease the likelihood of rounding error, there is no magic bullet. You need to consider rounding risk from the start and be disciplined about them:

### 1. Paradigm Shift: Every Incorrect Rounding Is a Bug

There's an important distinction in security:

- **Bug**: An error in the code
- **Vulnerability**: A bug with a potential security risk
- **Exploit**: One or multiple vulnerabilities with a demonstrated attack path

Security researchers focus on exploits because they need to demonstrate profit. But here's the key insight: **all incorrect roundings are bugs, some of those bugs are vulnerabilities, and some of those vulnerabilities can lead to exploits.**

Demonstrating exploitability is hard. It might require specific market conditions, depend on the behavior of external protocols, or require chaining multiple vulnerabilities together. In most cases, fixing a rounding bug is much easier than proving it can be exploited.

Developers should treat *every* incorrect rounding as a bug, whether exploitable today or not. A rounding error that seems harmless now might become exploitable later on. Don't wait for a proof of exploitability for an incorrect rounding, fix it anyway.

### 2. Design-Level Thinking

This is where the real wins happen. Before writing code:

**Analyze and restructure your formulas.** Understanding the bounds of your variables unlocks simplifications. If you can prove `a >= 1` always holds in your system, you eliminate the conditional rounding logic for `a^(c/d)`. These constraints come from your protocol's invariants, so document and enforce them. Algebraic rearrangement can eliminate problematic divisions entirely or combine multiple divisions into one.

**Precision Loss Cancellation.** Sometimes you can rewrite a formula so that precision losses cancel each other out across multiple steps. Instead of fighting rounding at every operation, you design the math so errors offset naturally.

Here's a simplified example inspired by lending protocols. Imagine code that calculates collateral to seize during liquidation:

```
collateral_to_seize = (amount * index) / index
```

For the sake of argument, consider that you cannot simply discard `index / index` due to how the operations are structured across different functions.

If you want `collateral_to_seize` to round up (to favor the protocol: more collateral is seized from the underwater position), the naive approach says: round the multiplication up, and round the division up too. But look what happens if you round up then down instead:

| Rounding Strategy | Result | Error (wei) |
|-------------------|--------|-------------|
| UP then DOWN | 2.111... | 0 |
| DOWN then DOWN | 2.111... - 1 wei | -1 |
| UP then UP | 2.111... + 1 wei | +1 |

*(Example: amount = 2.111..., index = 1.111...)*

The UP then DOWN approach gives zero error because the rounding errors cancel. The multiplication overshoots slightly, then the division undershoots by the same amount. By understanding the mathematical structure, you get exact results without needing to round "correctly" at each step.

Here's a pseudo formal proof to give a better intuition. Consider fixed-point arithmetic with scale S (e.g., 10^18). We assume `index > S` (i.e., index represents a value > 1.0). If `index < S`, that's outside typical protocol invariants for a lending index. If `index == S`, rounding isn't a concern.

For the operation:

```
result = divDown(mulUp(amount, index), index)
```

**Step 1: mulUp**

```
step1 = mulUp(amount, index) = ceil(amount × index / S)
```

Let's define the exact value as `exact = amount × index / S`. Then:

```
step1 = exact + ε₁
```

where `ε₁ ∈ {0, 1}` (the rounding error from ceiling, in wei).

**Step 2: divDown**

```
result = divDown(step1, index) = floor(step1 × S / index)
```

Substituting step1:

```
result = floor((exact + ε₁) × S / index)
       = floor((amount × index / S + ε₁) × S / index)
       = floor(amount × index × S / (S × index) + ε₁ × S / index)
       = floor(amount + ε₁ × S / index)
```

**Step 3: Cancellation condition**

Since `index > S`, we have `ε₁ × S / index < ε₁`. Given that `ε₁ ∈ {0, 1}`, this means `ε₁ × S / index` is either 0 (when `ε₁ = 0`) or a fraction less than 1 (when `ε₁ = 1`). In both cases, `floor(amount + ε₁ × S / index) = amount`. The rounding errors cancel.

Precision Loss Cancellation is not something I've seen discussed much, but I believe this type of analysis will become more common as DeFi codebases mature and become robust against precision loss.

**Create a rounding decision table.** Some rounding choices are subjective. Is rounding down on protocol fees acceptable if it simplifies logic? Should the sender or receiver bear the loss during a transfer? Decide explicitly and document it. This table becomes a reference for developers, auditors, and bug bounty hunters.

**Watch for trapping paths.** Any rounding that could cause a revert needs a cap or fallback. If you round up the collateral to seize in a liquidation, make sure it can't exceed the user's actual balance.

### 3. Implementation Discipline

Good design gets you most of the way there. These practices help you stay consistent:

- **Make the code modular**: Math that is easy to isolate is easier to review and test. Keep your arithmetic logic in dedicated functions rather than buried in complex business logic.
- **Use explicit naming**: `mulDown(...)` or `mul(..., Rounding.DOWN)`. Never leave rounding direction ambiguous.
- **Document every decision**: An inline code comment explaining *why* you chose that direction will help reviewing and maintaining the code.
- **Test edge cases**: Unit tests should verify behavior at the boundaries where rounding matters most.
- **Use fuzzing and formal verification**: Tools like Foundry, Echidna, or Medusa can stress test your maths to find edge cases. For critical math, tools like Certora, Halmos, or the K framework can prove properties hold for all inputs.

---

## Key Takeaways

1. **All incorrect roundings are bugs.** Some become vulnerabilities, some become exploits. Don't wait for an exploitability demonstration to fix it.

2. **Know the rounding direction of every operation before writing code.** Designing this in advance will help structure the code and make implementation straightforward.

3. **"Round in favor of the protocol" is necessary but not sufficient.** Complex formulas, intermediate value reuse, and trapping paths all create scenarios where determining the correct direction is harder than it sounds.

4. **Algebraic rearrangement and Precision Loss Cancellation are the hidden heroes.** Sometimes you can structure formulas so rounding errors offset naturally, giving you exact results without fighting each operation.

Rounding is hard. It's subtle, context-dependent, and easy to get wrong. But it's also tractable if you take it seriously from day one.

---

*If you need help with your DeFi protocol, [reach out](mailto:josselin@seceureka.com).*