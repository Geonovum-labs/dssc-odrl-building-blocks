
# ODRL Prohibition Rule (Schema)

`nl.geonovum.dssc.odrl.prohibition` *v0.1.0*

A prohibition rule disallowing an action under optional constraints.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### ODRL Prohibition Rule
#### json
```json
{
  "action": "use",
  "constraint": {
    "leftOperand": "ex:purpose",
    "operator": "eq",
    "rightOperand": "ex:Research"
  }
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/prohibition/schema.json
title: ODRL Prohibition Rule
type: object
required:
- action
properties:
  '@id':
    type: string
  target:
    oneOf:
    - type: string
    - type: array
      items:
        type: string
  action:
    oneOf:
    - type: string
    - type: object
      required:
      - '@id'
      properties:
        '@id':
          type: string
      additionalProperties: true
  constraint:
    oneOf:
    - oneOf:
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.yaml
      - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-logical/schema.yaml
    - type: array
      items:
        oneOf:
        - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-atomic/schema.yaml
        - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/constraint-logical/schema.yaml
  duty:
    oneOf:
    - $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/obligation/schema.yaml
    - type: array
      items:
        $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/obligation/schema.yaml
additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/prohibition/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/prohibition/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
