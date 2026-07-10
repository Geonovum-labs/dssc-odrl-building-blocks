
# ODRL Atomic Constraint (Schema)

`nl.geonovum.dssc.odrl.constraint-atomic` *v0.1.0*

A basic ODRL constraint with left operand, operator and right operand.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Atomic purpose constraint
#### json
```json
{
  "leftOperand": "ex:purpose",
  "operator": "eq",
  "rightOperand": "ex:Research"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/constraint-atomic/schema.json
title: ODRL Atomic Constraint
type: object
required:
- leftOperand
- operator
properties:
  leftOperand:
    type: string
  operator:
    type: string
    enum:
    - eq
    - neq
    - gt
    - gteq
    - lt
    - lteq
    - isAnyOf
    - isAllOf
    - isNoneOf
    - gte
    - lte
    - isPartOf
  rightOperand: {}
  rightOperandReference:
    type: string
  unit:
    type: string
  dataType:
    type: string
oneOf:
- required:
  - rightOperand
- required:
  - rightOperandReference
additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
