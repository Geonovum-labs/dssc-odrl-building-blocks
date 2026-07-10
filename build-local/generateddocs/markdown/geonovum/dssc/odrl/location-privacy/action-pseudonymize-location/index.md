
# Location Privacy Pseudonymize Location Action (Schema)

`nl.geonovum.dssc.odrl.location-privacy.action-pseudonymize-location` *v0.1.0*

Action indicating that the spatial reference must be pseudonymized before transfer.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Location Privacy Pseudonymize Location Action
#### json
```json
"lp:pseudonymizeLocation"

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://example.org/building-blocks/odrl/location-privacy/action-pseudonymize-location/schema.json
title: Location Privacy Pseudonymize Location Action
oneOf:
- const: lp:pseudonymizeLocation
- type: object
  required:
  - '@id'
  properties:
    '@id':
      const: lp:pseudonymizeLocation
  additionalProperties: true

```

Links to the schema:

* YAML version: [schema.yaml](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/action-pseudonymize-location/schema.json)
* JSON version: [schema.json](http://localhost:9090/register/build-local/annotated/geonovum/dssc/odrl/location-privacy/action-pseudonymize-location/schema.yaml)

## Sources

* [Using Sensitive Location Data to its Full Potential - wetransform](https://wetransform.to/news-and-events/sensitive-location-data-full-potential/)
* [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [ODRL V2.2 Implementation Best Practices](https://w3c.github.io/odrl/bp/)
* [SAGE WP2 Meeting - Location Data Policies in the EDC](urn:local:SAGE-WP2-Meeting-Location-Data-Policies-in-the-EDC.pdf)
