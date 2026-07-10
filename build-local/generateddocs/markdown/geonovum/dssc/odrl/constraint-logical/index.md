
# ODRL Logical Constraint (Schema)

`nl.geonovum.dssc.odrl.constraint-logical` *v0.1.0*

A logical composition of ODRL constraints using and, or or xone.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Purpose and role logical constraint
#### json
```json
{
  "and": [
    {
      "leftOperand": "ex:purpose",
      "operator": "eq",
      "rightOperand": "ex:Research"
    },
    {
      "leftOperand": "ex:recipientRole",
      "operator": "eq",
      "rightOperand": "ex:PublicAuthority"
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/constraint-logical/schema.json
title: ODRL Logical Constraint
type: object
oneOf:
- required:
  - and
- required:
  - or
- required:
  - xone
properties:
  and:
    type: array
    minItems: 1
    items:
      oneOf:
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.yaml
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-logical/schema.yaml
  or:
    type: array
    minItems: 1
    items:
      oneOf:
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.yaml
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-logical/schema.yaml
  xone:
    type: array
    minItems: 1
    items:
      oneOf:
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.yaml
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-logical/schema.yaml
additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-logical/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-logical/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
