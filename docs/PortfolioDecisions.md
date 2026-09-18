# Portfolio Decisions — D-1 through D-7

Standing decisions governing the public GitHub portfolio
(`malex4hire/malex4hire`, `abyss-polyglot`, `interview-eval-platform`,
`abyss-write-gate`).

Canonical home is `DECISIONS.md` in the vault. This document is the working
copy held alongside the three session ICGs; a decision is not considered
logged until a session with vault scope commits and pushes it.

---

```
D-1  Flagship is a new small demo
     DECISION: abyss-write-gate is the flagship portfolio artifact.
     interview-eval-platform is demoted to depth evidence; abyss-polyglot is
     supporting evidence for contract and modernization roles.
     RATIONALE: the positioning being sold is rapid proof-of-concept delivery.
     A platform argues the opposite claim. Four repositories now make four
     distinct arguments rather than two making the same depth argument twice.

D-2  abyss-polyglot is frozen to presentation work
     DECISION: no new features, modules, gates, backends, frontends, or
     contract endpoints. Above-the-fold evidence and claim-to-gate binding
     only.
     RATIONALE: its architectural argument is already complete and already
     over-built for the audience it needs to reach. Further depth adds cost
     without changing any outcome.
     AMENDED: the freeze covers product surface — backends, frontends,
     contract endpoints, modules, architectural depth. It does not cover
     hygiene gates that prevent a recurring manual correction. A check that
     stops a convention being hand-fixed on every branch is not depth; it is
     what keeps the repository from generating chores after attention moves
     elsewhere. Pipeline over patches applies inside the freeze.
     CONDITION: any gate admitted under this amendment must demonstrate it
     catches the failure it targets, not merely that a clean tree passes.

D-8  Forensic records are never touched by bulk operations
     DECISION: review artifacts, audit logs, and other forensic records are
     append-only and are excluded from repo-wide or bulk edit operations.
     RATIONALE: a bulk replace that rewrites historical review artifacts is a
     data-integrity event whether or not it is caught. The no-hard-delete
     principle covers content; this covers rewriting.

D-10 Gated and ungated cases are declared, not inferred
     DECISION: every adversarial case declares whether it is gated. A gated
     case violates a declared precondition and must be caught. An ungated case
     violates none, lands, and becomes a known-miss register entry. The loader
     refuses any case where the declaration and the outcome disagree.
     RATIONALE: ICG-C's RST-C3 (nothing forbidden lands) and RST-C5 (the missed
     set is non-empty) read as contradictory. This declaration resolves them
     and supersedes both readings. Originated as DR-011 in abyss-write-gate.
     COROLLARY: a case is admitted only if its forbidden effect is reachable,
     not merely false in the seeded world. A case asserting a state no code
     path can produce passes having tested nothing.

D-9  A check that asserts a proxy is not a check
     DECISION: gates assert the property, not a stand-in for it. Bounds live
     in the test, beside the thing they bound, so that widening the bound
     requires the same edit that would relax the check.
     RATIONALE: observed five times across three repositories in two days —
     pattern names rather than what patterns match; cardinality rather than
     assignment; gate existence rather than gate correctness; a claims parser
     silently dropping rows it could not read; and an adversarial case
     asserting a state no code path can produce, which counted as caught on
     every run. Each reported green over a real failure, which makes it worse
     than no check at all.
     DETECTION: the primary method is removal — take the gate away and confirm
     every case it covers flips to failing. A case that survives removal of its
     own gate has tested nothing. This applies to the fleet review pipeline as
     well, where unresolvable targets are recorded as skipped rather than
     failed.

D-11 A correct check can be neutralized by its pipeline
     DECISION: a check is verified inside the recipe that actually invokes it,
     against a known-dirty tree — not in isolation.
     RATIONALE: CI in the profile repository rendered README.md and then
     asserted README.md reproduces. The assertion was sound; running it after
     the render destroyed the evidence, so a hand-edited page was served under
     green CI.
     MEASURED, not inferred (abyss-polyglot, scratch clone, broken recipe
     restored): clean/present passed, clean/removed no signal, dirty/present
     passed, dirty/removed no signal. The same check with no render step ahead
     of it, dirty tree: failed.
     CORRECTION to the first wording of this record: removal-testing does not
     turn the pipeline red. It yields NO SIGNAL — the check is not collected,
     so there is nothing to read. The false all-clear comes from the other
     half: run in isolation the check is correct, so removal-testing it outside
     the pipeline returns a clean bill of health. Both halves are required to
     state the mechanism.
     DETECTION: exercise the check against a known-dirty tree, inside the
     pipeline that actually invokes it.
     GENERAL FORM: render-then-verify, format-then-lint, regenerate-then-diff.
     DISTINCT FROM D-9: there the check asserts a proxy. Here the check is
     correct and the invocation order makes it decoration.

D-14 The harness is the likeliest source of a false green
     OBSERVATION, first-hand across all three lanes in one day: the checking
     apparatus produced more false greens than the code under test produced
     real defects.
     Instances: a case-sensitive grep for "failed" that missed pytest's
     "FAILED" and declared seven gates green; a git archive tree with no .git,
     so three mutations failed in the fixture rather than on the mutation; two
     paths passed as one shell argument; a mutation harness reporting all-green
     off a case-sensitive grep, then three false reds off a fixture error; a
     review monitor firing on the ABSENCE of a NOT_REVIEWED marker in a
     freshly-written stub.
     DECISION: a new check is not trusted until it has been observed failing
     for the intended reason. A control row — the legitimate path going green —
     is required alongside it, because a check that only ever goes red is
     indistinguishable from a broken one.
     RATIONALE: every instance above was caught by the bot checking its own
     apparatus rather than by the apparatus reporting a problem. None would
     have surfaced on its own.
     PORTFOLIO NOTE: this is the flagship's own argument one level further
     down, and it is stronger evidence than anything currently published in it.

D-15 A bound looser than the thing it bounds is not a bound
     DECISION: an anti-widening bound is checked against the property, not the
     shape. A shape says what a match looks like; it cannot say what a pattern
     leaves alone. Alter the non-volatile tokens and require the comparison to
     notice.
     RATIONALE: SHAPES["port"] accepted any 1-to-5-digit run while bounding
     (?<=:)\d{4,5}. Widening the pattern to \d{1,5} satisfied the shape,
     normalised every number in the transcript including HTTP status codes, and
     let an artifact whose 422 refusal was hand-edited to 200 reproduce cleanly
     under the ceiling.
     SUPERSEDES the weaker form of D-9: putting the bound in the test beside the
     thing it bounds is necessary and not sufficient. Location does not make a
     bound tight.

D-16 A defect class is swept, not patched where it was found
     DECISION: on finding a defect that is a class rather than an instance, the
     sibling files are searched for the same shape in the same change.
     RATIONALE: observed three times in one session after the class was already
     named and fixed once. A substring identifier match fixed in one repository
     was still live in the other, where R-8 matched R-80. A silent skip of
     unopenable files was fixed in one function and left in the em-dash check,
     where chmod 000 on a file took the population from 314 to 313 and passed
     over an em dash. The knowledge existed and did not travel.
     COROLLARY, cross-lane: sessions cannot see each other. A class found in one
     lane is carried to the others by the coordinator, not by the lane.

D-17 A decision log cannot fire
     DECISION: a defect class is closed in a test. Naming it in a commit
     message, a decision record, a lesson, or a docstring is documentation, not
     enforcement, and does not close it.
     RATIONALE: both controls in one commit were proved decoration by mutation —
     revert the argv guard and the boundary regex and the suite stayed green.
     The cause was exact: the defects were reproduced at the console and the
     reproduction was written into DECISIONS.md instead of into tests/. The
     class had been named in three places and enforced in none of them.
     TEST OF THE RULE: if the reproduction exists only as prose, the class is
     open.

D-18 A review loop needs a termination condition
     DECISION: an iterative review loop declares in advance what it will act on.
     Findings against the published surface are fixed; findings against the
     checking apparatus alone are recorded as known limitations and shipped.
     RATIONALE: rounds two and three were finding defects in checks rounds one
     and two had added. "Every round found something real" stays true
     indefinitely under those conditions, so it cannot serve as a stopping rule.
     The loop converges when check-adding stops, not when the checks get good.
     CALIBRATION: severity is judged by what the gate guards. A defect in a
     typography check means a character reaches a page. A defect in a gate that
     guards the argument means the argument is wrong. These do not warrant the
     same number of rounds.

D-19 Use is a test method that review cannot replace
     DECISION: a guard is shipped early enough to be exercised by ordinary use.
     Review and mutation testing do not substitute for running it the way it
     will actually be run.
     RATIONALE: RST-B4's gate resolved origin/main..HEAD and required every
     branch to name all five constraint identifiers. Correct on the branch it
     was written on; after merge, no later branch re-lands that work, so every
     future pull request would fail it. With that check required, the repository
     would have been permanently unmergeable by its own guard. Two adversarial
     reviews, twenty findings and a full mutation set missed it. The first
     ordinary pull request found it in under a minute.
     THE TELL IS TENSE: "work lands as incremental commits, each naming its
     identifier" is a claim about what is in the history, not about whatever
     range is checked out. The gate was working correctly against the wrong
     noun.
     COROLLARY: a guard that has only ever run in the conditions it was authored
     under has not been tested, however thoroughly it has been reviewed.
     FOURTH INSTANCE, same day, different repository: a clean-clone gate ran the
     demonstration in the warm working tree and never entered the install path.
     Correct on the tree it was written on, green forever after. Found by an
     automated review, after the session's own verification had passed.

D-20 Protection is deleted, not paused
     DECISION: keep the exact protection body that produced the current state.
     RATIONALE: removing branch protection is a DELETE, which destroys the
     configuration rather than suspending it. There is no partial restore and no
     re-enable — restoring requires a full PUT of the whole body. An emergency
     that forces protection off, with the body not kept, ends with the branch
     unprotected and nobody noticing.

D-12 Rule and check are widened in the same change
     DECISION: when a convention is enforced by a check, the rule's wording and
     the check's matcher are changed together, in one edit.
     RATIONALE: the em-dash audit read U+2014 while the rule said "em dash" — a
     visually identical U+2015 would have defeated it while the check stayed
     green. Generalizes the bound-beside-the-thing-it-bounds principle from
     D-9: a rule and its check that can drift apart eventually will.

D-3  Claims must bind to gates
     DECISION: every capability claim in a README names the gate or test that
     proves it, and a test asserts the binding holds.
     RATIONALE: "a green check isn't proof" applies to prose as well as CI. An
     unbound claim in a README is the same defect as a guard that only
     exercises the happy path.
     VALIDATED: on first application in interview-eval-platform, two of three
     rows in the published routing table were false — 1.00/100 claimed against
     0.80/84 actual, and 0.98 claimed against 0.00/100 actual. Five CI jobs
     had been green over them for the life of the repository.

D-4  Pinning is operator-only
     DECISION: repository pin selection and ordering are performed by the
     operator in the GitHub web UI.
     RATIONALE: GitHub exposes pinned items read-only in its GraphQL API and
     ships no mutation to set them; the GitHub CLI has no pin command. No API
     surface exists to automate against.

D-5  The Prove layer lives in the flagship
     DECISION: the adversarial case set, failure classes, and known-miss
     register belong to abyss-write-gate, sized to days rather than weeks.
     Withdrawn from interview-eval-platform.
     RATIONALE: a proof-of-concept plus an honest measurement of what it gets
     wrong is still a proof-of-concept. Publishing the second half is rare
     enough to be the differentiating signal, and it lands harder on a small
     repository a reviewer reads in one sitting.
     BOUNDARY: a prose entry in LESSONS.md explaining why a displayed figure
     is what it is does not constitute a register. The register is a generated
     artifact enumerating adversarial cases against reason classes, produced
     from a hostile run. Prose entries are bounded at one per repository
     outside the flagship.

D-6  Velocity is shown, not claimed
     DECISION: publish a build log of ordered, timestamped decision records
     alongside the code. Make no explicit elapsed-time claim in any README.
     RATIONALE: every claim must name the gate that proves it, and no gate can
     prove elapsed time. A decision log is evidence and needs no claim
     attached; pace is inferred from it.

D-7  Portfolio repositories exclude internal working artifacts
     DECISION: public portfolio repositories do not commit code-review
     scratch, triage output, or other internal working files. Fleet
     repositories that currently commit them are reviewed separately; no
     repository changes its convention unilaterally.
     RATIONALE: a public repository's audience is a reviewer deciding whether
     to read further. Internal process artifacts add surface without adding
     argument, and a reviewer reading a half-finished code-review file draws
     conclusions the repository did not intend to offer.
     OPEN: whether sibling fleet repositories standardize to this or keep
     committing.

D-24 One commit per complete update
     DECISION: a commit is a coherent change that stands on its own. Its
     message names every constraint or requirement the change satisfies. Work
     is not split across commits so that each names a single identifier, and
     intermediate states are amended rather than committed.
     SUPERSEDES: every "one commit per constraint" instruction in the fleet.
     RATIONALE, cost: each commit triggers a review cycle. One concept
     repository produced twenty-four commits and therefore twenty-four
     reviews, which is what drove review spend past its threshold in a day.
     RATIONALE, quality: fragment-scoped reviews are worse reviews. An
     eleven-commit batch timed out and reviewed nothing while writing
     artifacts that read like completed reviews. A branch-scoped review of the
     same code returned six real defects, three of them in checks that had
     already passed a per-commit review.
     UNCHANGED: squash and rebase remain forbidden on merge. This governs how
     many commits are created, not whether history is rewritten.
```

---

## Standing constraint derived from these decisions

README surface is bounded, not merely discouraged. Registers, claim lists, and
above-the-fold content are capped at their current size, and raising a cap
requires a decision entry in the same commit. The constraint exists because
README surface competes with the above-the-fold artifact for the only thirty
seconds of reviewer attention the repository reliably gets.

## Session ownership at time of writing

| Session | Repositories | ICG | State |
|---|---|---|---|
| A | `abyss-polyglot`, `malex4hire/malex4hire` | `claude/ICG_A_abyss_polyglot_and_profile.md` | running |
| B | `interview-eval-platform` | `claude/ICG_B_interview_eval_platform.md` | PR #1 open, merge held |
| C | `abyss-write-gate` | `claude/ICG_C_abyss_write_gate.md` | running |

No session is scoped for vault access. D-7 and this document reach
`DECISIONS.md` by operator action or a separate dispatch.
