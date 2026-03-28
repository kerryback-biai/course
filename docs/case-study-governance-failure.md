# Case Study: Air Canada — When the Chatbot Makes a Promise the Company Can't Keep

*For use in Session 6: "Can You Trust It?" — Reliability, Verification, and Governance*

---

## The Story

In November 2022, Jake Moffatt visited the Air Canada website to book a last-minute flight from Vancouver to Toronto after the death of a close family member. Like many airlines, Air Canada offers reduced bereavement fares — but the rules about how and when to apply for them were buried across multiple pages of the airline's website. Rather than hunt through the site, Moffatt did what an increasing number of customers do: he asked the chatbot.

The chatbot responded clearly and confidently. It told Moffatt that if he needed to travel immediately, he could book a full-price ticket and then submit it for a reduced bereavement rate within 90 days by completing a Ticket Refund Application form. It even provided a link. Moffatt booked a round-trip ticket for C$1,640.36 and, after returning home, filed for the bereavement discount as the chatbot had instructed. Air Canada denied his claim. The reason: the airline's actual bereavement policy, stated on a separate page of the same website, explicitly prohibited retroactive applications. The chatbot had fabricated a policy that did not exist.

Moffatt filed a complaint with British Columbia's Civil Resolution Tribunal. Air Canada's defense was remarkable in its candor about the state of enterprise AI governance: the airline argued it could not be held liable for information provided by its chatbot because the chatbot was "a separate legal entity that is responsible for its own actions." The tribunal rejected this outright. Member Christopher Rivers wrote: "While a chatbot has an interactive component, it is still just a part of Air Canada's website. It should be obvious to Air Canada that it is responsible for all the information on its website. It makes no difference whether the information comes from a static page or a chatbot."

In February 2024, the tribunal ordered Air Canada to pay C$812.02 — the fare difference of C$650.88, plus interest and tribunal fees. The dollar amount was small. The precedent was not. The ruling established that companies are legally responsible for the outputs of their AI systems, whether those outputs are accurate or not.

---

## What Went Wrong

**Failure mode: Hallucination in a customer-facing AI system.** The chatbot generated a plausible but entirely fabricated refund policy. It did not retrieve the correct bereavement policy from Air Canada's own documentation — it constructed an answer that sounded reasonable but contradicted the airline's actual rules.

**Why the error was not caught:** Air Canada deployed the chatbot without a verification layer between the AI's responses and the customer. There was no maker/checker process. No one reviewed what the chatbot was telling customers about specific policies. No one tested it against the actual bereavement fare rules. The chatbot operated autonomously on high-stakes topics — refund eligibility, fare policies, passenger rights — with no human in the loop and no automated policy-checking guardrail.

**Contributing factor: Over-trust in AI output.** Air Canada appears to have treated the chatbot as a deflection tool (reduce call center volume) rather than as a system that could create binding commitments. The company did not anticipate that a customer would reasonably rely on chatbot statements the same way they would rely on a human agent's statements — even though, from the customer's perspective, both are representatives of the airline.

---

## The Governance Lesson

The Air Canada case is a textbook example of deploying AI as a "maker" with no "checker." The chatbot produced answers. No system or person verified them before they reached the customer. And the company learned — via a legal ruling — that AI-generated output carries the same weight as any other official company communication.

For enterprise data agents, the lesson generalizes directly. When an AI agent generates a financial report, a customer analysis, or a supply chain recommendation, the output is not a draft until someone treats it as one. Without an explicit verification step — whether that is a human reviewer, an automated cross-check against source data, or a second AI system validating the first — the organization is accepting AI output as ground truth. The Air Canada tribunal ruling makes clear that "the AI said it" is not a defense. The organization owns the output.

The governance minimum for any customer-facing or decision-driving AI system is straightforward: define which topics require verification before the output reaches a human decision-maker or customer, assign accountability for that verification to a specific role, and log both the AI output and the verification decision for audit purposes.

---

## Discussion Questions

1. **Accountability mapping.** Air Canada argued the chatbot was "a separate legal entity." Who in your organization would be accountable if an AI system gave a customer or a regulator wrong information? Is that accountability currently documented, or would you discover the answer only after an incident?

2. **The verification cost tradeoff.** Adding a human verification layer to Air Canada's chatbot would have slowed response times and increased costs — exactly the metrics the chatbot was deployed to improve. How do you decide which AI outputs require human verification and which can be delivered directly? What criteria would you use to draw that line?

3. **Testing for failure modes.** Air Canada apparently never tested the chatbot against its own bereavement policy. For the AI agent you are scoping in your capstone project, what are the three most likely ways it could produce a confidently wrong answer — and how would you test for each before deployment?

---

## Sources

- Moffatt v. Air Canada, 2024 BCCRT 149, British Columbia Civil Resolution Tribunal, February 14, 2024.
- "Air Canada chatbot promised a discount. Now the airline has to pay it." *The Washington Post*, February 18, 2024. [Link](https://www.washingtonpost.com/travel/2024/02/18/air-canada-airline-chatbot-ruling/)
- "How can I mislead you? Air Canada found liable for chatbot's bad advice on bereavement rates." *CBC News*, February 2024. [Link](https://www.cbc.ca/news/canada/british-columbia/air-canada-chatbot-lawsuit-1.7116416)
- "BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot." *American Bar Association — Business Law Today*, February 2024. [Link](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- "Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot." *McCarthy Tetrault — TechLex*, 2024. [Link](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)
- "The Risks of Relying on AI: Lessons from Air Canada's Chatbot Debacle." *Cloud Security Alliance*, June 2024. [Link](https://cloudsecurityalliance.org/blog/2024/06/05/the-risks-of-relying-on-ai-lessons-from-air-canada-s-chatbot-debacle)
