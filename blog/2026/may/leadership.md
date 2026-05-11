---
title: Security is a leadership problem
permalink: /blog/leadership
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

# Security is a leadership problem

Security is often treated as the problem of finding unknown vulnerabilities. But after a hack, you hear the same explanation from many affected teams:

> “We knew it was a weak point, but we thought it was ok.”

The problem was not that nobody understood the risk existed. The problem was that the organization accepted it.

Most blockchain teams do not ignore security, but they often treat it as a phase instead of an intrinsic characteristic of their product. When asked if they take it seriously, many founders answer: “yes, we got audited by X”, but have little strategy beyond that. Security becomes a question of how many bugs were found, or whether the audit was considered “good enough” to ship. That framing misses the point.

Security decisions are made under incomplete information, release pressure, and competing incentives. No audit or process can fully prove that a complex system is safe. At some point, someone decides what level of risk is acceptable.

In practice, many of the decisions that determine security outcomes sit above the code. Security is a leadership problem.

## Temporary assumptions become permanent

Sometimes timelines force decisions before risks are fully evaluated. A release needs to happen, so the risk “needs” to be low. In other cases, concerns are deprioritized because no one clearly owns the evaluation process. Teams rarely revisit the assumptions behind the accepted risks.

Over time, protocols evolve. There are new integrations, new assets, or changes in dependencies. A centralization assumption was accepted because of low TVL, but later became a critical point of failure. A rounding edge case was judged acceptable because it lived in an unused component, but later became part of a critical code path. What was once considered a minor or isolated risk quietly becomes a systemic risk.

Most of the time, these assumptions only exist in one engineer’s head and are never tracked. Once that engineer leaves the team, the context disappears with them.

This pattern appears repeatedly in incidents. The original trade-off is often not the problem. The problem is that nobody revisits it once the system changes. 

And sometimes systems change the fastest precisely when their exposure is growing.

## Exposure often scales faster than confidence

Early-stage teams frequently say they do not yet have the budget for security. But security is not only about paying for audits. It is also about controlling exposure while confidence in the system is still limited.

A small team cannot always afford multiple reviews, formal verification, internal security teams, or months of assessment. But it can decide not to expose an immature system to unlimited losses.

Protocols sometimes gain traction much faster than anticipated. What started as a small experiment suddenly becomes a high-value target for attackers. Exposure often scales much faster than the organization’s ability to evaluate and manage risk.

There are many levers that early-stage protocols can use to limit the consequences of incidents:

- **Reduce scope.** Cut non-essential features, avoid risky integrations, reduce cross-protocol dependencies.
- **Limit exposure.** Add TVL caps, liquidity limits, or rate limits.
- **Use centralization deliberately.** Keep systems upgradeable or migratable, add pause mechanisms, and tightly control admin access.
    

These trade-offs are uncomfortable because they compete directly with growth, speed, and competitiveness. But that is precisely why they are leadership decisions.

Security is not about eliminating all risk. That is impossible in complex systems. It is about making sure exposure grows at a pace the organization can still understand and control. 

The problem becomes harder once no one clearly owns decisions about exposure, timelines, and acceptable risk internally.

## Organizations lack security ownership

As teams grow, another problem appears: the lack of security ownership.

Traditional financial institutions usually have internal security teams, CISOs, and reporting structures designed around risk ownership. In contrast, many DeFi organizations still externalize security almost entirely to third-party providers. After an audit, security is “done”.

This model made sense while the industry was scaling quickly and expertise was scarce. It is increasingly insufficient today.

Blockchain teams need internal security ownership. 

But ownership without authority is mostly cosmetic. In some organizations, engineers are made “responsible” for security while having no authority over timelines. They may identify risks, but have little ability to delay a launch, reduce scope, or change priorities once deadlines approach. Ownership exists on paper, not in reality.

A useful model is that security is owned by a founder early on, and becomes more explicit and formalized as the team grows. As time becomes constrained, this forces founders to define how it is delegated. Many teams with a strong security posture evolved this way, sometimes without realizing it.

But formal ownership alone is not enough. Leadership determines whether risks are discussed openly or quietly minimized inside the organization.

## How leadership changes security discussions

Leadership tone impacts how engineers prioritize security, and leaders rarely realize it.

If audit findings are consistently challenged by leadership for optics, engineers become less likely to raise concerns. If delays caused by security work are treated as failures, teams will aim to avoid them even when they are needed. If leadership publicly mocks competitors after incidents, people become less willing internally to say they are not confident in something.

Eventually, discussions shift from understanding issues to managing how they are perceived.

The strongest teams behave very differently. Leads want assumptions challenged. During audits, engineers actively seek feedback instead of defending the current implementation. Engineers are comfortable raising uncertainty, and refactoring proposals are taken seriously even when they delay releases.

In rare cases, I have seen engineers push to increase the severity of findings because they believed the actual risk was understated. That only happens when people feel safe surfacing problems instead of minimizing them.

Leadership sets the tone for whether risks are discussed early or quietly minimized.

## Security has to be part of decision-making

Risk evaluation, exposure scaling, ownership, leadership tone: all of this ultimately comes down to whether security influences decisions early, or is only considered near the end.

Founders are rarely trained to think about security this way. It is often treated as validation of the product rather than part of the strategy.

A useful comparison is profitability. Founders remain responsible for profitability even if execution is delegated. Profit is not something evaluated at the very end of the process. It shapes what gets built, how aggressively the company scales, and what constraints exist around growth.

Security should work similarly.

The security budget should influence what can responsibly be built in the first place. A common failure is to design a highly complex system and only later realize that the organization lacks the resources to properly assess it.

The important questions are often straightforward:

- **If our TVL moves from $1m to $10m, what additional security measures do we need?** This means treating TVL as risk, not just as success.
- **With our current security budget, what level of complexity can we responsibly support?**
- After an audit, **what catastrophic scenarios still remain possible?**
- **Which assumptions are we currently relying on, and when do they stop being true?**
    

These questions are not separate from product strategy. They are product strategy.

Security should not be treated as a final validation step. It should influence architecture, complexity, and exposure decisions long before the audits begin.

***

The most visible parts of security are often not what determine the outcome. Audits, findings, and fixes matter, but many failures start much earlier: with decisions about scope, exposure, timelines, and which risks are considered acceptable.

Strong organizations do not necessarily avoid every mistake. But they tend to revisit assumptions as systems evolve, limit exposure while confidence is still low, and create environments where engineers can raise concerns instead of minimizing them.

Audits find bugs. Leadership determines whether the system that produced them gets fixed, delayed, or shipped anyway.
