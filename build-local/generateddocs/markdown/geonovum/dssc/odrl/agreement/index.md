
# ODRL Agreement for Dataspace Protocol (Schema)

`nl.geonovum.dssc.odrl.agreement` *v0.1.0*

An ODRL Agreement profile for negotiated dataspace contracts.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### ODRL Agreement for Dataspace Protocol
#### json
```json
{
  "@context": [
    "https://www.w3.org/ns/odrl.jsonld",
    {
      "ex": "https://example.org/policy/"
    }
  ],
  "@type": "Agreement",
  "permission": [
    {
      "action": "use",
      "constraint": {
        "leftOperand": "ex:purpose",
        "operator": "eq",
        "rightOperand": "ex:Research"
      }
    }
  ],
  "target": "urn:example:dataset:1"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/agreement/schema.json
title: ODRL Agreement for Dataspace Protocol
type: object
required:
- '@type'
properties:
  '@context':
    oneOf:
    - type: string
    - type: object
    - type: array
      items:
        oneOf:
        - type: string
        - type: object
  '@id':
    type: string
  '@type':
    oneOf:
    - const: Agreement
    - const: odrl:Agreement
  profile:
    type: string
  target:
    oneOf:
    - type: string
    - type: array
      items:
        type: string
  assigner:
    type: string
  assignee:
    type: string
  permission:
    type: array
    items:
      $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/permission/schema.yaml
  prohibition:
    type: array
    items:
      $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/prohibition/schema.yaml
  obligation:
    type: array
    items:
      $ref: http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/obligation/schema.yaml
anyOf:
- required:
  - permission
- required:
  - prohibition
- required:
  - obligation
additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/agreement/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/agreement/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
