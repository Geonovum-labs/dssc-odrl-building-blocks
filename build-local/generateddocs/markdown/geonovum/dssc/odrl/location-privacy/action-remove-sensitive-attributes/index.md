
# Location Privacy Remove Sensitive Attributes Action (Schema)

`nl.geonovum.dssc.odrl.location-privacy.action-remove-sensitive-attributes` *v0.1.0*

Action indicating that sensitive non-spatial attributes must be removed or degraded while keeping the original spatial reference.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Location Privacy Remove Sensitive Attributes Action
#### json
```json
"lp:removeSensitiveAttributes"

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/location-privacy/action-remove-sensitive-attributes/schema.json
title: Location Privacy Remove Sensitive Attributes Action
oneOf:
- const: lp:removeSensitiveAttributes
- type: object
  required:
  - '@id'
  properties:
    '@id':
      const: lp:removeSensitiveAttributes
  additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/action-remove-sensitive-attributes/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/action-remove-sensitive-attributes/schema.yaml)

## Sources

* [Using Sensitive Location Data to its Full Potential - wetransform](https://wetransform.to/news-and-events/sensitive-location-data-full-potential/)
* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL V2.2 Implementation Best Practices](https://w3c.github.io/odrl/bp/)
* [SAGE WP2 Meeting - Location Data Policies in the EDC](urn:local:SAGE-WP2-Meeting-Location-Data-Policies-in-the-EDC.pdf)
