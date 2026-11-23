# Gaps & blockers
- BLOCKED: no network in authoring environment (github.com DNS fails) -> nothing cloned or verified.
- BLOCKED(legal): recompilation needs lawfully owned game binaries; none included.
- Open: licence compatibility, console key/exploit dependencies, hardware availability (Xbox/PS5, AMD/NVIDIA/Intel, ARM64), awesome-list triage.


## Update 2026-11-23
- Open: full GTA VI startup on Xbox2Windows is unverified (reported by team).
- Open: ReCity's additions over Leonida unknown; licence inheritance unchecked.
- Open: licences, SHAs, OS/GPU/arch support, deps for all five verified-exist repos not yet supplied.
- Open: awesome-list linked repos untriaged.
- Open: the 10 other assignment repos are unverified even remotely.
- Blocked: local GitHub access (still down); mirrors and arbitrary downloads deliberately not used.

## Update 2026-11-23
- Resolved (second-hand only): licences, platform claims, requirements for the four core repos are now documented, still unverified locally.
- Open: exact SHAs/dates/releases/owners for all repos; LICENSE texts and per-file headers; AnyPS5 licence source; vendored deps and their licences.
- Open: ReCity requirements and Linux/macOS status; GPU vendor support for all repos (not stated); ARM64 status beyond macOS test tools; AnyPS5 Apple Silicon native-vs-Rosetta.
- Blocked: licence-isolation of AnyPS5 (GPL-2.0-only) from GPL-3 lineage prevents any combined build; needs legal review if interaction is ever wanted.
- Blocked: no upstream boots GTA VI (Leonida, ReCity) or demonstrates startup (Xbox2Windows).

## Update 2026-11-23 (relay 3)
- Open: LICENSE and third-party notices unread for all 12 licence-reported/unknown projects; SixNG GPL-3.0 variant; AnyPS5 licence source.
- Open: provenance: TomBox, "rage9", rpf9-explorer pinned SHA/licence, ReCity and Leonida submodules.
- Open: SixNG's actual BCPack limitations; bcpack-rs scope and relation to SixNG.
- Open: hardware/driver details behind ReCity and Xbox2Windows GPU claims (still E1, none E3).
- Open: platforms/requirements/approach for OpenScarlett, xbox-emulator, SixNG and the rpf9 tools; Percy6Stars purpose and exact terms.
- Blocked: no network, so no inspection was possible; no code copied; nothing built or tested.
- Blocked (legal): Percy6Stars link-only; AnyPS5 isolated from GPL-3 projects (incl. SixNG).

## Update (Leonida-PC rc1)
Blocked since no GitHub access: cloning Leonida (SHA, branch, submodules, LICENSE, build/test instructions), source inspection, any upstream build. Original contribution this round is tooling only (tests, CI, 3 fixed defects), not engine work.
