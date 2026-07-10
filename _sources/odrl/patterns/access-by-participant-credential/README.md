# Access by Participant Credential

Allows use only when the requesting participant has a required verifiable credential or claim.

## Intent

This pattern is a reusable starting point. Adapt the `leftOperand`, vocabulary IRIs and connector-specific bindings to the rulebook of the dataspace.

## Connector compatibility notes

- Eclipse EDC: requires an implementation/binding for custom left operands unless using built-in operands.
- TNO TSG: align operands and evaluation with configured policy rule templates and policy enforcement components.

## Validation notes

Examples are declared in `examples.yaml`. Negative tests use filenames ending in `-fail`.
