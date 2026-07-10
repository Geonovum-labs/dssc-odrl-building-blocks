
# ODRL Use Action (Schema)

`nl.geonovum.dssc.odrl.action-use` *v0.1.0*

The ODRL use action for usage policies.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### ODRL Use Action
#### json
```json
"use"

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/action-use/schema.json
title: ODRL Use Action
oneOf:
- const: use
- type: object
  required:
  - '@id'
  properties:
    '@id':
      const: use
  additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/action-use/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/action-use/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
