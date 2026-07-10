
# Dataspace Access Action (Schema)

`nl.geonovum.dssc.odrl.action-access` *v0.1.0*

The access action pattern for access policies and offer visibility.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Dataspace Access Action
#### json
```json
"access"

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/action-access/schema.json
title: Dataspace Access Action
oneOf:
- const: access
- type: object
  required:
  - '@id'
  properties:
    '@id':
      const: access
  additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/action-access/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/action-access/schema.yaml)

## Sources

* [DSSC Blueprint - Access & Usage Policies Enforcement](https://toolbox.dssc.eu/?pane=technical&technical=access-usage-policies-enforcement)
* [Eclipse Tractus-X Connector Kit - Working with Policies](https://eclipse-tractusx.github.io/docs-kits/kits/connector-kit/adoption-view/working-with-policies/)
* [TNO Security Gateway - Policy Enforcement Framework](https://tno-tsg.gitlab.io/docs/core-container/pef/)
