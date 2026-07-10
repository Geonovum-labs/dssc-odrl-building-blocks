# DSSC Dataspace ODRL Policy Building Blocks

Experimental OGC Building Blocks register for ODRL-based access and usage policies as exchanged through the Dataspace Protocol and used by connector implementations such as Eclipse EDC and TNO TSG.

## Scope

This register profiles a practical, interoperable subset of ODRL for dataspace policy exchange and validation. It supports:

- validation of ODRL JSON-LD policy payloads before publication in a catalog;
- reusable policy patterns for dataspace rulebooks;
- comparison of connector behaviour across Eclipse EDC and TNO TSG;
- generation of examples, schemas, tests and conformance notes.

The register does **not** attempt to cover the full ODRL information model.

## Important OGC Building Blocks conventions used here

- Every building block directory contains an `examples.yaml` file so examples are included in the generated documentation UI and validated by the tooling.
- Test resources are placed in each block's `tests/` directory.
- Negative test cases are named with the `-fail` suffix before the extension, for example `missing-action-fail.json`.
- A `tests.yaml` file is included in selected blocks to demonstrate explicit test declarations with `require-fail: true`.

## Initial building blocks

Core policy structures:

- `odrl/policy-set`
- `odrl/offer`
- `odrl/agreement`
- `odrl/permission`
- `odrl/prohibition`
- `odrl/obligation`
- `odrl/constraint-atomic`
- `odrl/constraint-logical`

Action blocks:

- `odrl/action-use`
- `odrl/action-access`

Reusable policy patterns:

- `odrl/patterns/access-by-participant-credential`
- `odrl/patterns/purpose-limitation`
- `odrl/patterns/time-limited-use`
- `odrl/patterns/no-redistribution`

## Build

This repository follows the common OGC Building Blocks layout with source blocks under `_sources/` and generated assets under `build/`.

```bash
./build.sh
```

The included `build.sh` is a placeholder. Replace it with the OGC Building Blocks CLI command or GitHub Action used in your environment.


## Location privacy extension

Additional experimental building blocks have been added for location-data policies derived from the SAGE/Wetransform work on Location Data Policies in the EDC.

Specification inputs:

- Wetransform article: Using Sensitive Location Data to its Full Potential.
- SAGE WP2 Meeting slide deck: Location Data Policies in the EDC, 25 June 2026.
- W3C ODRL Information Model 2.2 and ODRL implementation best practices.

The extension includes action blocks, constraint blocks, a participant geofence credential reference, and LDP1-LDP6 policy-pattern blocks.
