# Relationship & dependency map
Basis: facts reported by the research team (see reports/VERIFICATION_STATUS.md). Edges marked *inferred* are planning assumptions to confirm by reading code.

```
                         awesome-gta6-reverse-engineering  (directory; links to be triaged)
                                      |  (lists)
        +-----------------------------+---------------------------+
        |                             |                           |
   [GTA VI RE / recomp line]    [Xbox recomp line]          [PS5 portability line]
   Leonida ──derived──> ProjectReCity   Xbox2Windows           AnyPS5 (boykopovar)
   (ReCity is a derivative,      (CPU + shader experiments;    (separate research project;
    NOT independent)              full GTA VI startup           NOT an Xbox GTA VI port)
                                  unverified)
                                                                
   [GTA VI asset tools - category gta6-assets, all UNVERIFIED]
   rpf9, rpf9-extract, GTA6-Asset-Info   (no verified link to the lines above)
```

## Rules this map implies
- **Leonida ↔ ProjectReCity:** one lineage. Do not count them as two implementations or as mutual corroboration. Compare ReCity against Leonida's history to isolate what ReCity adds; evaluate their licences together (derivative must honour the parent's terms).
- **Xbox2Windows:** independent of the Leonida line unless code inspection shows shared code (*unknown*). Evidence status: experiments documented, end-to-end startup unverified.
- **AnyPS5:** different target platform (PS5) and different purpose. Do not merge its capabilities into the Xbox/GTA VI matrix. Treat as a separate research track; any reusable ideas (loader, syscall layer) are *inferred* possibilities only.
- **Asset tools:** separate category; they need game archives the project will not hold. Usable only as source to read/lint, not run against game data here.
- **Directory:** a source of leads, not evidence. Each linked repo needs its own verification and triage before entering the manifest.
